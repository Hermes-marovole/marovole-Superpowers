#!/usr/bin/env python3
"""Market, Financial, User Intent & GTM Intelligence CLI Helper.

Subcommands:
  1. intent    -- Live user search action & commercial autocomplete expander (Google / Baidu / Bing / Taobao / Amazon / YouTube).
  2. ecommerce -- Generate 8-platform e-commerce & social-commerce (JD / Taobao / 1688 / Xianyu / Douyin / Xiaohongshu / WeChat Channels / Pinduoduo / Amazon) commands & queries.
  3. hiring    -- Generate domestic & overseas hiring JD reverse-engineering queries (Zhaopin / Boss / Liepin / Greenhouse / Lever / Ashby) for SOP, caseload KPI & salary floor.
  4. pubmed    -- Live fetch clinical papers & RCTs via Europe PMC REST API (avoiding NCBI E-utilities 500 error) with PMID, DOI, year & abstract.
  5. radar     -- 6-dimension deep ecosystem radar (12315/BlackCat complaints, Government policies, Podcast/Xiaoyuzhou deep audio, Competitor D2C store/quiz bundling, Alternative solution rebound/side-effects, Affiliate commission rates).
  6. queries   -- Generate targeted search queries for Prospectuses (S-1/HKEX/CN), 10-K/Earnings, VOC 1-3 star reviews, and GTM funnels.
  7. size      -- Compute Top-Down vs Bottom-Up TAM/SAM/SOM and flag triangulation failures (>3x divergence).
"""
import argparse
import concurrent.futures
import json
import sys
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"


def _http_get_json(url: str, timeout: int = 8):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
        return json.loads(raw)


def fetch_google_suggest(q: str, hl: str = "zh-CN", ds: str = "") -> list:
    ds_param = f"&ds={ds}" if ds else ""
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&hl={hl}{ds_param}&q={urllib.parse.quote(q)}"
    try:
        data = _http_get_json(url)
        return data[1] if isinstance(data, list) and len(data) > 1 else []
    except Exception:
        return []


def fetch_baidu_suggest(q: str) -> list:
    url = f"https://www.baidu.com/sugrec?prod=pc&wd={urllib.parse.quote(q)}"
    try:
        data = _http_get_json(url)
        return [item["q"] for item in data.get("g", []) if "q" in item]
    except Exception:
        return []


def fetch_bing_suggest(q: str) -> list:
    url = f"https://api.bing.com/osjson.aspx?query={urllib.parse.quote(q)}"
    try:
        data = _http_get_json(url)
        return data[1] if isinstance(data, list) and len(data) > 1 else []
    except Exception:
        return []


def fetch_taobao_suggest(q: str) -> list:
    url = f"https://suggest.taobao.com/sug?code=utf-8&q={urllib.parse.quote(q)}"
    try:
        data = _http_get_json(url)
        return [row[0] for row in data.get("result", []) if isinstance(row, list) and row]
    except Exception:
        return []


def fetch_amazon_suggest(q: str) -> list:
    url = f"https://completion.amazon.com/api/2017/suggestions?limit=10&prefix={urllib.parse.quote(q)}&alias=aps&mid=ATVPDKIKX0DER"
    try:
        data = _http_get_json(url)
        return [s.get("value") for s in data.get("suggestions", []) if s.get("value")]
    except Exception:
        return []


def cmd_intent(args: argparse.Namespace) -> None:
    seed = args.seed.strip()
    is_cjk = any("\u4e00" <= ch <= "\u9fff" for ch in seed)

    if is_cjk:
        modifiers = {
            "base_autocomplete": [seed],
            "pain_and_symptom (痛点与副作用)": [f"{seed} 副作用", f"{seed} 没用", f"{seed} 智商税", f"{seed} 禁忌"],
            "willingness_to_pay (购买与选型意图)": [f"{seed} 哪个牌子", f"{seed} 多少钱", f"{seed} 平替", f"{seed} 怎么选"],
            "usage_and_adherence (用法与依从性行为)": [f"{seed} 怎么吃", f"{seed} 什么时候", f"{seed} 搭配", f"{seed} 长期"],
        }
    else:
        modifiers = {
            "base_autocomplete": [seed],
            "pain_and_symptom": [f"{seed} side effects", f"{seed} not working", f"{seed} problem"],
            "willingness_to_pay": [f"best {seed} for", f"{seed} price", f"{seed} alternative", f"{seed} worth it"],
            "usage_and_adherence": [f"how to take {seed}", f"{seed} dosage", f"{seed} vs"],
        }

    report = {
        "seed": seed,
        "language_mode": "zh" if is_cjk else "en",
        "search_engines": {},
        "ecommerce_buying_intent": {},
        "intent_matrix": {},
    }

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
        f_google = ex.submit(fetch_google_suggest, seed, "zh-CN" if is_cjk else "en")
        f_yt = ex.submit(fetch_google_suggest, seed, "zh-CN" if is_cjk else "en", "yt")
        f_bing = ex.submit(fetch_bing_suggest, seed)
        f_baidu = ex.submit(fetch_baidu_suggest, seed) if is_cjk else None
        f_taobao = ex.submit(fetch_taobao_suggest, seed) if is_cjk else None
        f_amazon = ex.submit(fetch_amazon_suggest, seed)

        mod_futures = {}
        for cat, q_list in modifiers.items():
            mod_futures[cat] = []
            for q in q_list:
                if is_cjk:
                    mod_futures[cat].append(ex.submit(fetch_baidu_suggest, q))
                    mod_futures[cat].append(ex.submit(fetch_bing_suggest, q))
                else:
                    mod_futures[cat].append(ex.submit(fetch_google_suggest, q, "en"))

        report["search_engines"]["google"] = f_google.result()
        report["search_engines"]["youtube"] = f_yt.result()
        report["search_engines"]["bing"] = f_bing.result()
        if f_baidu:
            report["search_engines"]["baidu"] = f_baidu.result()

        if f_taobao:
            report["ecommerce_buying_intent"]["taobao_tmall"] = f_taobao.result()
        report["ecommerce_buying_intent"]["amazon_us"] = f_amazon.result()

        for cat, fut_list in mod_futures.items():
            seen = []
            for fut in fut_list:
                for item in fut.result():
                    if item not in seen:
                        seen.append(item)
            report["intent_matrix"][cat] = seen[:18]

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"=== Live User Search & Buying Intent Radar: '{seed}' ===")
        print("\n[1. Search Engine Autocomplete (用户在搜什么)]")
        for eng, items in report["search_engines"].items():
            if items:
                print(f"  • {eng.upper():8}: {', '.join(items[:8])}")
        print("\n[2. E-Commerce Search Box (用户掏钱前在搜什么商品规格/品牌)]")
        for shop, items in report["ecommerce_buying_intent"].items():
            if items:
                print(f"  • {shop:12}: {', '.join(items[:10])}")
        print("\n[3. Deep Intent Matrix (痛点 / 付费意愿 / 行为习惯词根裂变)]")
        for cat, items in report["intent_matrix"].items():
            print(f"  • {cat}:")
            print(f"      {', '.join(items[:12])}")


def cmd_ecommerce(args: argparse.Namespace) -> None:
    kw = args.keyword.strip()
    plan = {
        "keyword": kw,
        "1_shelf_ecommerce (货架电商：真实售价、销量结构与30-90天追评)": [
            f'opencli jd search "{kw}" -f json   # 拿到 sku_id 后跑: opencli jd item <sku> -f json && opencli jd reviews <sku> -f json',
            f'opencli taobao search "{kw}" -f json   # 拿到 id 后跑: opencli taobao detail <id> -f json && opencli taobao reviews <id> -f json',
            f'opencli amazon search "{kw}" -f json   # 查海外畅销与飙升: opencli amazon bestsellers / movers-shakers',
        ],
        "2_supply_chain_bom_cost (1688 源头代工底价与拼多多白牌底线)": [
            f'opencli 1688 search "{kw} 代工 贴牌" -f json   # 拿 offer 后跑: opencli 1688 item <url> -f json (算 BOM 毛利倍数)',
            f'python3 ~/.hermes/skills/research/web-search/scripts/search.py search \'site:yangkeduo.com OR "拼多多" "{kw}" ("百亿补贴" OR "已拼" OR "评价")\' --engine serper -n 8',
        ],
        "3_interest_and_live_ecommerce (抖音电商/蝉妈妈/精选联盟 + 小红书买手种草 + 视频号小店)": [
            f'opencli douyin search "{kw}" -f json   # 拿 aweme_id 后跑: opencli douyin detail <id> -f json',
            f'python3 ~/.hermes/skills/research/web-search/scripts/search.py search \'"{kw}" ("蝉妈妈" OR "考古加" OR "精选联盟" OR "佣金" OR "带货" OR "GMV" OR "直播间")\' --engine serper -n 8',
            f'opencli xiaohongshu search "{kw} 测评 避雷" -f json   # 拿 note_id 后跑: opencli xiaohongshu comments <note_id> -f json (统计"求链接/怎么买"买单密度)',
            f'opencli weixin search "{kw} 视频号" -f json   # 或借 mp.weixin.qq.com /cgi-bin/videosnap 拉取竞品视频号全量爆款',
        ],
        "4_secondhand_abandonment_test (闲鱼二手弃坑率：检验冲动消费 vs 真实复购)": [
            f'opencli xianyu search "{kw} 闲置 未拆封" -f json   # 拿 item_id 后跑: opencli xianyu item <id> -f json (看脱手理由)',
            f'python3 ~/.hermes/skills/research/web-search/scripts/search.py search \'site:goofish.com OR site:smzdm.com "闲鱼" "{kw}" ("闲置" OR "未拆封" OR "仅拆封" OR "代充")\' --engine serper -n 8   # opencli attach 失败时的免登录穿透兜底',
        ],
    }
    if args.json:
        print(json.dumps(plan, indent=2, ensure_ascii=False))
    else:
        print(f"=== 8-Platform E-Commerce & Social-Commerce Intelligence Matrix: '{kw}' ===")
        for sec, cmds in plan.items():
            if sec == "keyword":
                continue
            print(f"\n[{sec}]")
            for c in cmds:
                print(f"  • {c}")


def cmd_hiring(args: argparse.Namespace) -> None:
    kw = args.keyword.strip()
    comp = args.competitors.strip() or kw
    plan = {
        "keyword": kw,
        "1_cn_private_domain_sop_and_funnel (智联/猎聘/BOSS直聘：逆向拆解私域SOP、用户分层与转化漏斗)": [
            f'python3 ~/.hermes/skills/research/web-search/scripts/search.py search \'("{kw}" OR "{comp}") ("招聘" OR "岗位职责" OR "任职要求") ("私域" OR "企微" OR "SOP" OR "复购" OR "转化率" OR "训练营")\' --engine serper -n 10',
            f'python3 ~/.hermes/skills/research/web-search/scripts/search.py search \'site:zhaopin.com OR site:liepin.com OR site:zhipin.com ("{kw}" OR "{comp}") ("岗位职责" OR "底薪" OR "提成")\' --engine serper -n 10',
        ],
        "2_cn_sales_and_coach_unit_economics (一线顾问/班主任/营养师底薪、提成比例与单客人工成本)": [
            f'python3 ~/.hermes/skills/research/web-search/scripts/search.py search \'("{kw}" OR "{comp}") ("顾问" OR "班主任" OR "运营") ("底薪" OR "提成" OR "人效" OR "绩效" OR "13薪")\' --engine serper -n 10',
        ],
        "3_global_unicorn_caseload_and_roadmap (Greenhouse / Lever / Ashby / Primary VC：海外独角兽人效上限与AI路线图)": [
            f'python3 ~/.hermes/skills/research/web-search/scripts/search.py search \'(site:greenhouse.io OR site:lever.co OR site:ashbyhq.com OR site:jobs.primary.vc) ("{comp}") ("caseload" OR "per user" OR "AI" OR "commerce" OR "retention")\' --engine serper -n 10',
        ],
    }
    if args.json:
        print(json.dumps(plan, indent=2, ensure_ascii=False))
    else:
        print(f"=== Hiring Signal & Unit-Economics Reverse-Engineering Matrix: '{kw}' ===")
        for sec, cmds in plan.items():
            if sec == "keyword":
                continue
            print(f"\n[{sec}]")
            for c in cmds:
                print(f"  • {c}")


def cmd_pubmed(args: argparse.Namespace) -> None:
    q = args.query.strip()
    limit = args.limit
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(q)}&format=json&resultType=core&pageSize={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.0"})
    with urllib.request.urlopen(req, timeout=25) as resp:
        data = json.loads(resp.read().decode("utf-8", errors="replace"))
    papers = []
    for r in data.get("resultList", {}).get("result", []):
        pmid = r.get("pmid") or r.get("id") or ""
        papers.append({
            "pmid": pmid,
            "doi": r.get("doi") or "",
            "year": r.get("pubYear") or "",
            "journal": r.get("journalTitle") or "",
            "title": r.get("title") or "",
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if r.get("pmid") else f"https://europepmc.org/article/{r.get('source','MED')}/{pmid}",
            "abstract": (r.get("abstractText") or "")[:1000],
        })
    if args.json:
        print(json.dumps(papers, indent=2, ensure_ascii=False))
    else:
        print(f"=== Europe PMC / PubMed Clinical Evidence ({len(papers)} papers for: '{q}') ===")
        for i, p in enumerate(papers, 1):
            print(f"\n{i}. [{p['year']} | PMID:{p['pmid']}] {p['title']}")
            print(f"   Journal: {p['journal']} | URL: {p['url']}")
            if p["abstract"]:
                print(f"   Abstract: {p['abstract'][:320]}...")


def cmd_radar(args: argparse.Namespace) -> None:
    kw = args.keyword.strip()
    comp = args.competitors.strip() or kw
    plan = {
        "keyword": kw,
        "1_consumer_protection_complaints (黑猫投诉/12315/Trustpilot：退费纠纷、诱导扣费、副作用红线)": [
            f'python3 ~/.hermes/skills/research/web-search/scripts/search.py search \'(site:tousu.sina.com.cn OR "黑猫投诉" OR "12315") ("{kw}" OR "{comp}") ("退款" OR "诱导" OR "自动扣费" OR "无效" OR "副作用")\' --engine serper -n 10',
        ],
        "2_macro_policy_and_hospital_tailwinds (国家部委政策红利与公立医院门诊风向：如卫健委体重管理年/指南)": [
            f'python3 ~/.hermes/skills/research/web-search/scripts/search.py search \'(site:nhc.gov.cn OR site:gov.cn OR "指导原则" OR "专家共识") "{kw}" ("2024" OR "2025" OR "2026")\' --engine serper -n 8',
        ],
        "3_podcast_deep_mindshare (小宇宙/播客长音频：一二线高净值女性深度心智、反焦虑共鸣与私域导流)": [
            f'python3 ~/.hermes/skills/research/web-search/scripts/search.py search \'(site:xiaoyuzhoufm.com OR "小宇宙") ("{kw}")\' --engine serper -n 8',
        ],
        "4_competitor_d2c_store_and_bundles (海外/国内标杆D2C商城解剖：痛点症状命名法、套餐打包与Subscribe折扣)": [
            f'python3 ~/.hermes/skills/research/web-search/scripts/search.py search \'(inurl:collections/all OR inurl:products OR inurl:pages/quiz) ({comp})\' --engine serper -n 10',
        ],
        "5_substitute_backlash_and_rebound (激进替代方案翻车与停药反弹：如GLP-1减肥针停药反弹/急诊、医美埋线、断食伤胃)": [
            f'python3 ~/.hermes/skills/research/web-search/scripts/search.py search \'("{kw}" OR "司美格鲁肽" OR "替尔泊肽" OR "埋线" OR "断食") ("停药" OR "反弹" OR "复胖" OR "急诊" OR "副作用")\' --engine serper -n 10',
        ],
        "6_affiliate_commission_and_channel_split (蝉妈妈/精选联盟/分销佣金率：看穿达人带货分润结构)": [
            f'python3 ~/.hermes/skills/research/web-search/scripts/search.py search \'("蝉妈妈" OR "精选联盟" OR "考古加" OR "佣金率" OR "高佣") ("{kw}" OR "{comp}")\' --engine serper -n 8',
        ],
    }
    if args.json:
        print(json.dumps(plan, indent=2, ensure_ascii=False))
    else:
        print(f"=== 6-Dimension Ecosystem & Risk Radar: '{kw}' (Competitors: {comp}) ===")
        for sec, cmds in plan.items():
            if sec == "keyword":
                continue
            print(f"\n[{sec}]")
            for c in cmds:
                print(f"  • {c}")


def cmd_queries(args: argparse.Namespace) -> None:
    c = args.company
    ind = args.industry or c
    queries = {
        "1_prospectus_industry_overview": [
            f'"{ind}" ("招股书" OR "招股说明书" OR "聆讯后资料集") ("行业概览" OR "弗若斯特沙利文" OR "灼识咨询" OR "欧睿")',
            f'site:hkexnews.hk "{ind}" ("行业概览" OR "市场规模" OR "竞争格局") filetype:pdf',
            f'"{c}" ("Form S-1" OR "Form F-1" OR "424B4" OR "Prospectus") ("Industry Overview" OR "Market Opportunity")',
        ],
        "2_earnings_unit_economics_and_cac": [
            f'"{c}" ("年报" OR "招股书" OR "问询函回复") ("毛利率" OR "销售费用率" OR "获客成本" OR "复购率" OR "留存率")',
            f'"{c}" ("10-K" OR "20-F" OR "Annual Report") ("Gross Margin" OR "Selling and marketing" OR "Retention" OR "CAC")',
            f'"{c}" "Earnings Call Transcript" ("Q&A" OR "guidance" OR "churn" OR "acquisition") 2025 OR 2026',
        ],
        "3_risk_factors_and_weaknesses": [
            f'"{c}" ("招股书" OR "年报") "风险因素" ("依赖" OR "下滑" OR "投诉" OR "合规" OR "退货")',
            f'"{c}" ("10-K" OR "S-1") "Item 1A. Risk Factors" ("churn" OR "regulatory" OR "competition" OR "reliance")',
        ],
        "4_voc_negative_reviews_and_switching": [
            f'"{c}" ("差评" OR "避雷" OR "拔草" OR "没用" OR "副作用" OR "退货" OR "换到了")',
            f'site:reddit.com "{c}" ("switched from" OR "instead of" OR "disappointed" OR "waste of money" OR "side effects")',
            f'site:trustpilot.com OR site:g2.com "{c}" ("1 star" OR "2 stars" OR "terrible" OR "cancel")',
        ],
        "5_user_willingness_to_pay_and_behavior": [
            f'"{ind}" ("智商税" OR "平替" OR "值得买吗" OR "多少钱一个月" OR "坚持不下来" OR "忘了吃")',
            f'"{ind}" ("willingness to pay" OR "worth the price" OR "too expensive" OR "switched to" OR "workaround")',
        ],
        "6_gtm_funnel_and_hiring_signals": [
            f'site:{args.domain} (inurl:quiz OR inurl:assessment OR inurl:calculator OR inurl:tools OR inurl:vs)' if args.domain else f'"{c}" ("测评" OR "自测" OR "quiz" OR "calculator" OR "落地页")',
            f'"{c}" ("招聘" OR "careers" OR "jobs") ("增长" OR "投放" OR "私域" OR "算法" OR "营养师" OR "Growth" OR "Lifecycle")',
        ],
    }
    if args.json:
        print(json.dumps(queries, indent=2, ensure_ascii=False))
    else:
        print(f"=== Targeted Intelligence Queries for: {c} (Industry: {ind}) ===")
        for section, q_list in queries.items():
            print(f"\n[{section}]")
            for q in q_list:
                print(f"  • {q}")


def cmd_size(args: argparse.Namespace) -> None:
    td_tam = args.tam_total
    td_sam = td_tam * args.sam_pct
    td_som = td_sam * args.som_pct

    bu_tam = args.total_customers * args.acv
    bu_sam = args.reachable_customers * args.acv
    bu_som = args.reachable_customers * args.conv_rate * args.acv

    ratio = max(td_som, bu_som) / max(min(td_som, bu_som), 1e-9)
    triangulated = ratio <= 3.0

    result = {
        "currency": args.currency,
        "top_down": {
            "TAM": round(td_tam, 2),
            "SAM": round(td_sam, 2),
            "SOM": round(td_som, 2),
            "assumptions": f"TAM={td_tam:,.0f} * SAM_pct={args.sam_pct:.1%} * SOM_pct={args.som_pct:.1%}",
        },
        "bottom_up": {
            "TAM": round(bu_tam, 2),
            "SAM": round(bu_sam, 2),
            "SOM": round(bu_som, 2),
            "assumptions": f"Reachable={args.reachable_customers:,.0f} * Conv={args.conv_rate:.2%} * ACV={args.acv:,.1f}",
        },
        "triangulation": {
            "som_divergence_ratio": round(ratio, 2),
            "status": "PASS (Triangulated <= 3.0x)" if triangulated else "FAIL (Divergence > 3.0x — Re-check assumptions!)",
            "triangulated": triangulated,
        },
    }

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        c = args.currency
        print(f"=== Market Sizing Triangulation ({c}) ===")
        print(f"  [Top-Down]   TAM: {td_tam:,.0f} | SAM: {td_sam:,.0f} | SOM: {td_som:,.0f}")
        print(f"               ({result['top_down']['assumptions']})")
        print(f"  [Bottom-Up]  TAM: {bu_tam:,.0f} | SAM: {bu_sam:,.0f} | SOM: {bu_som:,.0f}")
        print(f"               ({result['bottom_up']['assumptions']})")
        status_icon = "✅" if triangulated else "🚨"
        print(f"  {status_icon} Triangulation: {result['triangulation']['status']} (Ratio: {ratio:.2f}x)")
        if not triangulated:
            sys.exit(2)


def main() -> None:
    parser = argparse.ArgumentParser(description="Market, Financial, User Intent & GTM Intelligence Tool")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sp_i = sub.add_parser("intent", help="Mine live user search actions & e-commerce buying autocomplete")
    sp_i.add_argument("seed", help="Seed keyword (e.g. '甘氨酸镁', '更年期失眠', 'menopause supplement')")
    sp_i.add_argument("--json", action="store_true")

    sp_e = sub.add_parser("ecommerce", help="Generate 8-platform e-commerce, live-commerce & 1688 BOM scraping matrix")
    sp_e.add_argument("keyword", help="Product category or brand keyword (e.g. '甘氨酸镁', 'Swisse')")
    sp_e.add_argument("--json", action="store_true")

    sp_h = sub.add_parser("hiring", help="Generate hiring JD reverse-engineering queries for SOP, caseload KPI & salary floor")
    sp_h.add_argument("keyword", help="Role or domain keyword (e.g. '体重管理', '私域营养师')")
    sp_h.add_argument("--competitors", "-c", default="", help="Competitor names (e.g. 'Noom OR Midi Health OR 薄荷健康')")
    sp_h.add_argument("--json", action="store_true")

    sp_p = sub.add_parser("pubmed", help="Fetch clinical papers & RCTs via Europe PMC REST API with PMID/DOI/abstract")
    sp_p.add_argument("query", help="Clinical search query (e.g. 'menopause visceral fat insulin resistance')")
    sp_p.add_argument("--limit", "-n", type=int, default=8)
    sp_p.add_argument("--json", action="store_true")

    sp_r = sub.add_parser("radar", help="Generate 6-dimension ecosystem radar (12315/BlackCat, Gov policy, Xiaoyuzhou podcast, D2C bundles, GLP-1 rebound, Affiliate commission)")
    sp_r.add_argument("keyword", help="Core topic keyword (e.g. '体重管理', '皮质醇 减肥')")
    sp_r.add_argument("--competitors", "-c", default="", help="Competitor names or domains (e.g. '兴趣岛 OR Keep OR shop.joinmidi.com')")
    sp_r.add_argument("--json", action="store_true")

    sp_q = sub.add_parser("queries", help="Generate prospectus, earnings, VOC, and GTM search queries")
    sp_q.add_argument("--company", "-c", required=True, help="Target company or competitor name")
    sp_q.add_argument("--industry", "-i", default="", help="Industry or category name")
    sp_q.add_argument("--domain", "-d", default="", help="Competitor domain (e.g. ritual.com)")
    sp_q.add_argument("--json", action="store_true")

    sp_s = sub.add_parser("size", help="Run Top-Down vs Bottom-Up TAM/SAM/SOM triangulation")
    sp_s.add_argument("--tam-total", type=float, required=True, help="Published total market size (Top-Down TAM)")
    sp_s.add_argument("--sam-pct", type=float, default=0.15, help="Serviceable fraction of TAM (default 0.15)")
    sp_s.add_argument("--som-pct", type=float, default=0.02, help="Realistic 1-3 yr share of SAM (default 0.02)")
    sp_s.add_argument("--total-customers", type=float, required=True, help="Total potential customers in category (Bottom-Up)")
    sp_s.add_argument("--reachable-customers", type=float, required=True, help="Serviceable/reachable target customers")
    sp_s.add_argument("--conv-rate", type=float, default=0.02, help="Realistic conversion rate (default 0.02)")
    sp_s.add_argument("--acv", type=float, required=True, help="Annual Contract Value / Annual ARPU per customer")
    sp_s.add_argument("--currency", default="RMB", help="Currency label (RMB/USD)")
    sp_s.add_argument("--json", action="store_true")

    args = parser.parse_args()
    if args.cmd == "intent":
        cmd_intent(args)
    elif args.cmd == "ecommerce":
        cmd_ecommerce(args)
    elif args.cmd == "hiring":
        cmd_hiring(args)
    elif args.cmd == "pubmed":
        cmd_pubmed(args)
    elif args.cmd == "radar":
        cmd_radar(args)
    elif args.cmd == "queries":
        cmd_queries(args)
    elif args.cmd == "size":
        cmd_size(args)


if __name__ == "__main__":
    main()
