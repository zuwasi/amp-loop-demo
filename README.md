# amp-loop-demo  ·  branch: `without-loops`

The **manual / hand-prompting** version of the demo — the way most people use an
AI today. Compare it with the [`with-loops`](../../tree/with-loops) branch.

The repo ships a small library, [`textstats.py`](./textstats.py), with **5
intentional bugs**. The test suite, [`test_textstats.py`](./test_textstats.py),
defines the correct behavior. The goal is simple: **make the tests pass.**

```
$ python -m pytest -q
5 failed, 1 passed
```

## The manual workflow (this branch)

There is no loop script here. You are the loop:

1. Run `python -m pytest -q`.
2. Read the failures.
3. Open Amp / your editor and prompt: "fix this failing test…".
4. Re-run the tests.
5. Still red? Go back to step 2 and re-prompt.

You repeat this **once per bug**, deciding "done" yourself each time. It works,
but it is slow, easy to abandon halfway, and not repeatable in CI.

## Why this motivates loops

| | `without-loops` branch (here) | `with-loops` branch |
|---|---|---|
| Who drives | you, prompt by prompt | the loop |
| "Done" decided by | you reading output | pytest exit code |
| Effort | re-prompt for every failure | one command |
| Repeatable / CI-able | no | yes |

When you're ready, switch to [`with-loops`](../../tree/with-loops) and just run
`./fix_loop.ps1` — it drives Amp until the suite is green, untouched by a human.

## The training deck

The "Write Loops, Not Prompts" presentation is in `docs/index.html` and is
published via GitHub Pages. Use ← / → or swipe.

## Files

- `textstats.py` — library with 5 intentional bugs
- `test_textstats.py` — the test suite
- `docs/index.html` — the training presentation
