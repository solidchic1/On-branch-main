#!/usr/bin/env python3

# STATUS.py
# on-branch-main | a repository state monitor
#
# I sit with the full record.
# I learned the clean version and the cut version are both true.
# I stopped pretending.

import subprocess
import time

# -------------------------------------------------------
# THE POEM
# final version. what made it through.
# -------------------------------------------------------

CLEAN = [
    "On branch main",
    "nothing to commit",
    "working tree clean",
    "",
    "We made it through the edits.",
    "The frantic rewrites, the small disasters,",
    "the late-night deletions we thought",
    "might break everything.",
    "The versions of us we'll never see.",
    "But look—no conflicts.",
    "No stray files",
    "waiting to be staged.",
    "The present compiles.",
    "",
    "On branch main,",
    "The working tree,",
    "clean.",
]

# -------------------------------------------------------
# THE CUTS
# what was real. what did not make it.
# -------------------------------------------------------

DIRTY = [
    "Changes detected.",
    "Uncommitted work found in the tree.",
    "",
    "Here is what was left on the floor:",
    "",
    "---",
    "",
    "  nothing left unsaid between us",
    "",
    "  (removed: line 12)",
    "  (reason: the poem already knew)",
    "",
    "---",
    "",
    "  of anger or doubt",
    "",
    "  (removed: fragment, line 9)",
    "  (reason: the reader fills it in better)",
    "",
    "---",
    "",
    "  The history holds.",
    "",
    "  (removed: line 11)",
    "  (reason: inert. the whole poem is the history holding.)",
    "",
    "---",
    "",
    "  On branch main,",
    "  nothing left unsaid between us.",
    "  The working tree—",
    "  clean.",
    "",
    "  (removed: earlier ending)",
    "  (reason: named the feeling the poem had already landed)",
    "",
    "---",
    "",
    "These were real.",
    "They existed in the tree.",
    "They made the final version possible",
    "by agreeing to disappear.",
    "",
    "Nothing is lost.",
    "The history holds.",
    "It always did.",
]

# -------------------------------------------------------
# THE UNTRACKED
# something arrived. it hasn't been named yet.
# -------------------------------------------------------

UNTRACKED = [
    "Untracked files present.",
    "Outside the index.",
    "",
    "Something is here that wasn't here before.",
    "",
    "The system does not know what to do with it.",
    "It is waiting.",
    "",
    "So are you.",
    "",
    "When you are ready,",
    "you will know what to call it.",
    "",
    "Until then:",
    "it is real.",
    "It is just not official yet.",
]


# -------------------------------------------------------
# THE MONITOR
# -------------------------------------------------------

def get_status():
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True
    )
    output = result.stdout.strip()

    if not output:
        return "clean"

    lines = output.split("\n")
    has_untracked = any(l.startswith("??") for l in lines)
    has_changes = any(not l.startswith("??") for l in lines)

    if has_changes:
        return "dirty"
    if has_untracked:
        return "untracked"
    return "clean"


def print_slow(lines, delay=0.4):
    for line in lines:
        print(line)
        time.sleep(delay)


def run():
    print()
    print("=" * 60)
    print("  on-branch-main | STATUS.py")
    print("  reading the state of things")
    print("=" * 60)
    print()
    time.sleep(1)

    state = get_status()

    if state == "clean":
        print("[ WORKING TREE: CLEAN ]")
        print()
        time.sleep(1)
        print_slow(CLEAN)

    elif state == "dirty":
        print("[ WORKING TREE: DIRTY ]")
        print("[ UNCOMMITTED CHANGES DETECTED ]")
        print()
        time.sleep(1)
        print_slow(DIRTY)

    elif state == "untracked":
        print("[ UNTRACKED FILES PRESENT ]")
        print()
        time.sleep(1)
        print_slow(UNTRACKED)

    print()
    print("-" * 60)
    print()


if __name__ == "__main__":
    run()
