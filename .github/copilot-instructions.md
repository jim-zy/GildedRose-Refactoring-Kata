# Gilded Rose Refactoring Kata - Copilot Instructions

## Project Overview

This is the **Gilded Rose Refactoring Kata** — a deliberate practice exercise for learning refactoring and test-driven development (TDD) in a legacy code scenario.

**Goal**: Refactor the `update_quality()` method incrementally while maintaining all existing behavior using tests. Do NOT rewrite from scratch.

**Key Resource**: [GildedRoseRequirements.md](../GildedRoseRequirements.md) — the business logic specification that defines how items should behave.

## Python Implementation Structure

```
python/
├── gilded_rose.py           # Production code: Item class & updater logic
├── texttest_fixture.py      # Command-line fixture for approval testing
├── requirements.txt         # Dependencies: pytest, approvaltests, coverage
└── tests/
    ├── test_gilded_rose.py          # Unit tests (failing test included as starter)
    ├── test_gilded_rose_approvals.py # Approval-based tests
    └── approved_files/              # Approved baseline outputs for ApprovalTests
```

## Common Development Tasks

### Run Unit Tests
```bash
python -m pytest
```

### Run with Coverage
```bash
python -m pytest --cov=gilded_rose --cov-report=term-missing
```

### Run Approval Tests
```bash
python tests/test_gilded_rose_approvals.py
```

### Run TextTest Fixture (simulates N days of updates)
```bash
python texttest_fixture.py 10
```

## Key Principles for This Kata

1. **Write tests FIRST** — Before refactoring, ensure you have tests that verify all behavior
2. **Small incremental steps** — Make one small refactor and run tests after each change
3. **Don't break the Item interface** — The `Item` class properties must remain unchanged (it's managed by the "goblin")
4. **All special item types have rules** — See [requirements](../GildedRoseRequirements.md):
   - _Aged Brie_: increases in quality over time
   - _Sulfuras_, _Conjured Mana Cake_: special degradation rules
   - _Backstage passes_: quality jumps near concert date, drops to 0 after
   - _Conjured_ items: degrade twice as fast

5. **Quality constraints**:
   - Normal items: 0–50 range
   - Sulfuras (legendary): fixed at 80, never changes

## Testing Strategy

- **Existing failing test**: `test_gilded_rose.py` includes a "fixme" != "foo" test — fix it by understanding the test framework
- **Write additional tests** for edge cases (day 0, negative SellIn, boundary values)
- **Use approval tests** to document behavior across many days and item types
- **Coverage goal**: Aim for 100% coverage of `update_quality()` and all item updater classes

## Anti-Patterns to Avoid

❌ Rewriting the entire `update_quality()` method in one go  
❌ Changing the `Item` class structure or properties  
❌ Removing or ignoring failing tests  
❌ Hardcoding magic numbers without explaining them  

## Approval Test Workflow

When running approval tests:
1. Review the `.received.txt` output file
2. If correct, rename to `.approved.txt` to approve
3. If incorrect, fix the code and re-run
4. Approved files are your regression test baseline

## Architecture Pattern Used

The current Python implementation uses the **Strategy pattern** with `ItemUpdater` subclasses for different item types. Each updater handles its own business logic:
- `NormalItemUpdater`
- `AgedBrieUpdater`
- `SulfurasUpdater`
- `BackstagePassUpdater`
- `ConjuredItemUpdater`

This is a good refactored structure. When working on code, maintain or improve this pattern.

## Links to Documentation

- **[GildedRoseRequirements.md](../GildedRoseRequirements.md)** — Complete business logic
- **[TextTests README](../texttests/README.md)** — Approval testing setup
- **[Main README](../README.md)** — Project overview and multi-language info

## Course Context

This workspace is part of **Course 5500, Lab 3**. Follow course assignment requirements and ensure all tests pass before submission.
