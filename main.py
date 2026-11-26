#!/usr/bin/env python3
"""Per My Last Email — entry for The Meeting That Should Have Been One Line on make.fun.

Prints exactly one line: the single sentence that could have replaced
an entire pointless meeting.
"""

LINE = "Decision made long before this meeting started: we are doing exactly what the first email said, so everyone may leave."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 200
    print(LINE)


if __name__ == "__main__":
    main()
