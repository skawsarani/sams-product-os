# PM Co-Pilot Evaluation Suite

Automated evaluation system to validate backlog processing workflow.

## Purpose

Ensures the backlog processing workflow continues to work correctly as the system evolves. Validates:
- Categorization (tasks, initiatives, references)
- Auto-categorization using core/config.yaml keywords
- Priority assignment
- Priority caps enforcement (P0≤3, P1≤7, P2≤15)
- File format and structure

## Directory Structure

```
evals/
├── README.md                    # This file
├── run_evals.sh                 # Main test runner
├── fixtures/
│   └── test-backlogs/          # Test input files
│       ├── basic-categorization.md
│       ├── auto-categorization.md
│       └── priority-caps.md
├── expected/
│   └── outputs/                # Expected results
│       ├── basic-categorization.json
│       ├── auto-categorization.json
│       └── priority-caps.json
└── results/
    └── YYYY-MM-DD-HHMMSS/      # Test run results (gitignored)
```

## Running Evaluations

### Prerequisites

1. AI assistant (Cursor, Claude Code) running
2. Clean working state (commit or stash changes)
3. PM Co-Pilot properly set up

### Run All Tests

```bash
cd evals
./run_evals.sh
```

### What Happens

1. **Backup** - Saves your existing tasks/initiatives/references
2. **Run Tests** - Processes test backlogs one by one
3. **Validate** - Checks outputs against expected results
4. **Restore** - Returns your original data
5. **Report** - Shows pass/fail summary

### Manual Steps

Some tests require manual interaction:
- You'll be prompted to run `/backlog` in your AI assistant
- For priority caps test, you'll verify AI enforces limits
- Press ENTER after each test completes

## Test Cases

### 1. Basic Categorization

**Tests:**
- Items correctly categorized as tasks, initiatives, references
- Uncategorized items archived to knowledge/notes/
- BACKLOG.md cleared

**Expected:**
- 2 tasks created
- 1 initiative created
- 1 reference created
- 1 item archived

### 2. Auto-Categorization

**Tests:**
- Tasks auto-assigned categories based on core/config.yaml keywords
- Technical, outreach, research, writing, admin categories working

**Expected:**
- 5 tasks with correct categories:
  - "API bug" → technical
  - "Email John" → outreach
  - "Research user" → research
  - "Write release" → writing
  - "Schedule offsite" → admin

### 3. Priority Caps

**Tests:**
- AI enforces P0≤3 cap
- AI asks user to deprioritize when cap exceeded
- Warning message appears

**Expected:**
- AI identifies 4 P0 items
- AI warns about exceeding P0 cap (3)
- AI asks user which task to deprioritize

## Adding New Tests

### 1. Create Test Fixture

Add new test backlog to `fixtures/test-backlogs/`:

```markdown
# Test Backlog - My New Test

## Item 1
Description...

## Item 2
Description...
```

### 2. Create Expected Output

Add expected results to `expected/outputs/`:

```json
{
  "test_name": "my-new-test",
  "expected": {
    "tasks": {
      "count": 2,
      "items": [...]
    }
  }
}
```

### 3. Update run_evals.sh

Add test case to the script following existing patterns.

## Interpreting Results

### Success Output

```
✓ Task count: 2 (expected: 2)
✓ Initiative count: 1 (expected: 1)
✓ Test PASSED: basic-categorization
```

### Failure Output

```
✗ Task count: 1 (expected: 2)
✗ Test FAILED: basic-categorization
```

### Result Files

All test outputs saved to `results/YYYY-MM-DD-HHMMSS/`:
- Input backlogs used
- Tasks created
- Initiatives created
- References created
- Backup of your original data

## When to Run Evals

**Required:**
- Before committing changes to AGENTS.md
- Before updating workflows/process-backlog.md
- Before modifying core/config.yaml structure
- Before major releases

**Recommended:**
- Weekly during active development
- Monthly for maintenance
- After adding new features

## Troubleshooting

### "Test failed" but output looks correct

Check expected output files - they may need updating if behavior intentionally changed.

### Backup not restoring

Check `results/latest/backup_*` directories. Manual restore:
```bash
cp -r results/YYYY-MM-DD-HHMMSS/backup_tasks/* tasks/
```

### Script permissions error

```bash
chmod +x run_evals.sh
```

## CI/CD Integration (Future)

This eval suite is designed to be CI-friendly:
- Automated test execution
- Exit code 0 (pass) or 1 (fail)
- Results saved for review

Could integrate with:
- GitHub Actions
- Pre-commit hooks
- Automated PR validation

## Maintenance

### Update Tests When

- Config.yaml keywords change
- Priority cap values change
- Categorization logic changes
- File structure changes

### Clean Up Old Results

```bash
# Keep last 10 test runs, delete older
cd results
ls -t | tail -n +11 | xargs rm -rf
```

---

**Note:** Evals require manual AI interaction since backlog processing is conversational. Future automation could use Claude API for fully automated testing.
