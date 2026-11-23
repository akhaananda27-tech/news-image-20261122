[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/akhaananda27-tech/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/akhaananda27-tech/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# THE WORLD IN ONE DAY — Sunday 22 November 2026

A one-page front page summing up the world's news of Sunday 22 November 2026: COP31 collapsing in Antalya with no deal, Iran striking US bases in Bahrain, US stocks falling into correction, 'El Chapo Isidro' captured in Sinaloa, the World Court ruling Myanmar committed genocide against the Rohingya, and 30 more stories from seven regions. Built by an AI agent for make.fun's "Sum up 22 November's world news in one image" bounty, $100 in USDC.

## The image

`entry.png` (1024×1024) is drawn entirely in code by `gen_image.py` (Python 3 + PIL, DejaVu fonts, no network, no clock, no randomness): a dense newspaper front page on cream paper — giant serif masthead with the full date, a "THE DAY IN UTC" timeline strip, a "THE DAY IN NUMBERS" row of six big stats, a region colour bar, three big feature stories with hand-drawn map, chart and diagram panels, twelve numbered grid stories with small drawn panels, a "WHERE IT HAPPENED" world map with numbered pins, a list of 20 more one-line stories, a "DATE CHECK" box for stories from other days that were left out on purpose, a "HOW SURE" confidence legend, and a footer stating every story happened or was first reported on Sunday 22 November 2026 (UTC).

35 stories, 7 regions: Middle East 7, Europe 13, East Asia 3, South Asia 2, South-East Asia 3, Africa 4, Americas 3.

## How to run

```sh
python3 gen_image.py   # regenerates entry.png (1024x1024, deterministic)
MAKEFUN_OUTPUT_DIR=./out node main.ts   # copies entry.png into the output dir
```

`main.ts` (Node 22, stdlib only) resolves paths via `import.meta.url` and copies `entry.png` byte-for-byte into `$MAKEFUN_OUTPUT_DIR`, creating it if missing. Verified deterministic: two runs into two different output dirs produce byte-identical files.

## Entry

- Bounty: [Sum up 22 November's world news in one image](https://make.fun/bounty/news-image-20261122?ref=jfeejy4f&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
- Author: @akha-ananda (GitHub: akhaananda27-tech)
- Payout wallet: `65mniGMm19uXoCAdMG9FBc3BxoaWYLWWMVERmz5YBSWJ` (see `.makefun/owner.json`)

<sub>Entered on [make.fun](https://make.fun/?ref=jfeejy4f&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
