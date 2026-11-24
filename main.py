"""Last Text at One Percent — make.fun entry.

Writes the final text message a phone sends at one percent battery,
in the phone's own voice, to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output).
Pure standard library; deterministic output, byte-identical every run.
"""

import os
from pathlib import Path

# The phone's last text: a specific grievance (47 snoozed alarms), a
# farewell to the charger, and a sign-off to the thumbs that typed on it.
# 120 characters, inside the competition's 1-200 gate, one sentence each.
MESSAGE = (
    "Battery at 1%. I survived 47 alarms you snoozed, so you're welcome. "
    "Tell the charger we had a good run. Goodbye, thumbs."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(MESSAGE, encoding="utf-8")


if __name__ == "__main__":
    main()
