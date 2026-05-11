# Apple Mail Fallback for x2doc — Session Notes

## Verified Working Pattern (2026-05-09)

When Resend API and Gmail SMTP are both unconfigured, Apple Mail via `osascript -e` chain is the reliable fallback on macOS.

### The Problem

Writing AppleScript to `.scpt` files (even with UTF-8 encoding) frequently fails with:
```
script error: Expected expression, etc. but found end of line. (-2741)
```

This happens regardless of file encoding or content length. The AppleScript parser in `osascript` appears to have issues with `.scpt` files in headless contexts.

### The Solution: `-e` Flag Chain

```python
import subprocess

cmd = [
    'osascript',
    '-e', 'set mailContent to "Your body here"',
    '-e', 'tell application "Mail"',
    '-e', '    set newMessage to make new outgoing message with properties {subject:"Subject", content:mailContent}',
    '-e', '    tell newMessage',
    '-e', '        make new to recipient with properties {address:"marovole@gmail.com"}',
    '-e', '        make new attachment with properties {file name:"/path/to/file.md"} at after last paragraph',
    '-e', '        send',
    '-e', '    end tell',
    '-e', 'end tell'
]

result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
assert result.stdout.strip().lower() == 'true'
```

### Critical Rules

1. **Body text must be ASCII-only** inside the AppleScript string. Chinese characters cause the same `-2741` error even with `-e` chains if they appear inside the quoted string.
2. **Escape order matters**: `.replace('\\', '\\\\').replace('"', '\\"')` — backslashes first, then quotes.
3. **The actual content lives in the Markdown attachment**, so ASCII body is fine. The user reads the attachment.
4. **Never use `.scpt` files** for this workflow. Always use `-e` chains.

### For Chinese Email Body

If Chinese body text is absolutely required, load `macos-mail-utf8` skill which uses Python to generate a UTF-8 encoded `.scpt` file. However, our session showed even this approach can be fragile. The practical workaround is: ASCII body + Chinese content in attachment.

### Account Verification

```bash
osascript -e 'tell application "Mail" to get name of accounts'
# Returns: Google, iCloud, Exchange, etc.
```

The account must already be configured in Mail.app. No additional auth needed.

---

Session: x2doc mlx-audio v0.4.3 post, 2026-05-09
Resolved: yes

### Re-verification
- **2026-05-09 (Ladder + Polymarket x2doc post)**: Same `-e` chain pattern, same ASCII-only body + attachment approach, returned `true`. Confirmed stable across multiple x2doc sessions.
