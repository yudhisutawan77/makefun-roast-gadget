# One-Line Roast: The Gadget You Use Every Day

[![make.fun](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/yudhisutawan77/makefun-roast-gadget/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/yudhisutawan77/makefun-roast-gadget/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

Entry for the [One-Line Roast: The Gadget You Use Every Day](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610) bounty on [make.fun](https://make.fun).

## What it does

`main.py` writes one original roast line — at most 200 characters — to
`/output/entry.txt`. The line roasts the gadget I use every morning: a
smart coffee machine that demands Wi-Fi, a firmware update and my exact
location before it will do the one job it exists for.

> My coffee machine needs Wi-Fi, a firmware update and my exact location before it will brew — it knows where I live but not that I am late for work.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
ENTRY_OUT=/tmp/out python3 main.py   # writes to a custom directory
```

The program validates the line itself (non-empty, at most 200
characters) and exits non-zero if the gate would fail.

## License

MIT — see [LICENSE](LICENSE).
