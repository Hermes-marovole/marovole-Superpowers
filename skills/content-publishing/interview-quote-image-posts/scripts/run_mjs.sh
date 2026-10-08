#!/bin/bash
# usage: run_mjs.sh <post_dir> <UPLOAD 0|1> <PUBLISH 0|1> <script.mjs> <SPACE id> [SAVE 0|1]
# ego-browser nodejs 读不到外部环境变量，所以把参数拼成脚本头再 pipe 进去。
D="$1"
{
  printf 'process.env.POST_DIR=%s;\n' "$(python3 -c 'import json,sys;print(json.dumps(sys.argv[1]))' "$D")"
  printf 'process.env.UPLOAD="%s"; process.env.PUBLISH="%s"; process.env.SPACE="%s"; process.env.SAVE="%s";\n' "$2" "$3" "$5" "${6:-0}"
  cat "$(dirname "$0")/$4"
} | ego-browser nodejs
