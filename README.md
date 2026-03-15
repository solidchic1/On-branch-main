# on-branch-main
### Repository State Monitor | Emotional Integrity Tool
### v1.0.0 | status: stable | severity: none

---

This repository documents the behavioral output of a lightweight git status parser designed to monitor the internal state of a working tree.

It does not fix anything.

It only tells you what is there.

---

## WHAT IT DOES

`STATUS.py` reads the current state of the repository and returns a report.

The report is accurate.

The report is complete.

The report will tell you things you already knew.

---

## THREE STATES

**Clean.**
Nothing to commit. Working tree clean.
The system has processed everything that was given to it.
Nothing is waiting to be named.

**Dirty.**
Changes detected. Uncommitted work found.
The system has found things that exist but have not yet been recorded.
They are real. They are just not official yet.

**Untracked.**
New files present. Outside the index.
Something arrived that the system was not expecting.
It does not know what to do with it yet.
Neither do you.

---

## CONTENTS

`STATUS.py` — The monitor

`ON_BRANCH_MAIN.md` — Sample output. A clean run.

---

## NOTE

The working tree does not lie.
It only reports what was done and what was left undone.

What you do with that information
is not a technical problem.

---

**The vulnerability described herein has no patch.**
