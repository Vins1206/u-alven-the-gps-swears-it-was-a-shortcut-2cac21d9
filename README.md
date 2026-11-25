# The GPS Swears It Was a Shortcut

[![make.fun](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![rank](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/Vins1206/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/rank.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![reward](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/Vins1206/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/reward.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)

A [make.fun](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9) entry: the GPS's one-line excuse, in its own voice, for sending the driver down the wrong road.

## What it does

`main.py` (Python standard library only) writes exactly one line of plain text — the GPS's excuse, no setup, no dialogue tags — to `/output/entry.txt`.

> Look, the map listed the bride's driveway as a through road, so I sent you through her wedding — I just read the directions, I don't write the lies.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

The output is a single line of at most 200 characters (148 characters), deterministic across runs.
