# amp-loop-demo  ·  branch: `with-loops`

A tiny demo that shows why **"write loops, not prompts"** beats hand-prompting an
AI for mechanical, verifiable work.

The repo ships a small library, [`textstats.py`](./textstats.py), with **5
intentional bugs**. The test suite, [`test_textstats.py`](./test_textstats.py),
defines the correct behavior. The goal is simple: **make the tests pass.**

```
$ python -m pytest -q
5 failed, 1 passed
```

## The loop (this branch)

Instead of fixing bugs by hand, run the loop. A deterministic gate (pytest's
exit code) decides "done"; Amp does the fixing; the loop writes the next prompt
from the failing output — no human in the conversation.

```
   run pytest --pass--> STOP
       ^                  |
       | failures         |
       +--- Amp fixes <---+
```

```powershell
./fix_loop.ps1          # PowerShell
python fix_loop.py      # cross-platform
```

The loop iterates until `pytest` exits 0, then stops on its own.

## Compare the two approaches

| | `without-loops` branch | `with-loops` branch (here) |
|---|---|---|
| Who drives | you, prompt by prompt | the loop |
| "Done" decided by | you reading output | pytest exit code |
| Effort | re-prompt for every failure | one command |
| Repeatable / CI-able | no | yes |

Check out [`without-loops`](../../tree/without-loops) to feel the manual way.

## The training deck

The "Write Loops, Not Prompts" presentation is published via GitHub Pages:
see the repo's Pages URL (served from `docs/index.html`). Use ← / → or swipe.

## Files

- `textstats.py` — library with 5 intentional bugs
- `test_textstats.py` — the deterministic gate
- `fix_loop.ps1` / `fix_loop.py` — the loop (Amp = fixer)
- `docs/index.html` — the training presentation
