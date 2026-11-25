"""The GPS Swears It Was a Shortcut.

Writes the GPS's one-line excuse to /output/entry.txt.
Python standard library only; deterministic, no network, no input.
"""

from pathlib import Path

EXCUSE = (
    "Look, the map listed the bride's driveway as a through road, "
    "so I sent you through her wedding \u2014 I just read the directions, "
    "I don't write the lies."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
