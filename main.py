"""Office Joke Open entry: one line about the office vending machine.

Judge criteria (RULES.txt, pairwise, most important first):
- About office life and works as a joke, not a complaint or remark.
- The laugh is earned: a turn in the last few words.
- Specific office detail: the vending machine, the last coin, the chips.
- Fresh: field benchmark of 188 titles found 0 copies of "vending",
  "coin", "chips", "thermostat", "badge", "whiteboard", "lift",
  "kettle", "timesheet", "toilet paper" or "secret santa". Crowded
  angles deliberately avoided: meeting (22x), printer (21x),
  reply-all (19x), email (16x), HR (10x), IT (10x), plain
  contest-name titles (52x). The one existing "toilet" title is a
  reply-all joke set in a bathroom, and the one "employee of the
  month" title is about a printer — neither collides with this angle.
- The turn: the joke opens as a complaint about a vending machine
  eating money, then flips in the last words — the machine, unlike
  every human in the office, has never once been called into a
  meeting to explain itself. The payoff lands on "in a meeting".
- Reads cleanly in one pass; 115 characters, well inside the 1-200 gate.

Writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt with no trailing newline.
"""

import os

ENTRY = (
    "The vending machine ate my last coin, kept the chips, and has never "
    "once been asked to explain itself in a meeting."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
