<#
  The "make the tests pass" loop (Amp version of "write loops, not prompts").

      run pytest --pass--> STOP
          ^                  |
          | failures         |
          +--- Amp fixes <---+

  The deterministic gate (pytest's exit code) decides "done" -- not a human
  reading the chat, and not the AI judging itself. Amp does the fixing.

  Usage:  ./fix_loop.ps1
#>
param([int] $MaxSteps = 6)

$ErrorActionPreference = "Stop"

for ($i = 1; $i -le $MaxSteps; $i++) {
    Write-Host "`n[loop] test pass $i/$MaxSteps" -ForegroundColor Cyan

    # 1. Deterministic gate: run the suite, capture output + exit code.
    $output = python -m pytest -q 2>&1 | Out-String
    Write-Host $output

    if ($LASTEXITCODE -eq 0) {
        Write-Host "[loop] all tests green after $($i-1) fix step(s)." -ForegroundColor Green
        exit 0
    }

    # 2. The LOOP writes the next prompt from the failing output.
    $prompt = @"
The pytest suite in this folder is failing. Output:

$output

Fix the bugs in textstats.py so every test passes. Edit ONLY textstats.py.
Do NOT change test_textstats.py. Make the smallest correct change per bug.
"@

    # 3. Amp does the fixing, unattended.
    amp -x $prompt --dangerously-allow-all | Out-Host
}

Write-Host "`n[loop] still failing after $MaxSteps passes." -ForegroundColor Yellow
exit 1
