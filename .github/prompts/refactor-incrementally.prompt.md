---
description: "Guide me through one incremental refactoring step: write tests first, then make a small change, then verify with tests and coverage."
argument-hint: "What part of the code do you want to refactor?"
agent: "agent"
---

# Incremental Refactoring Guide for Gilded Rose

You're going to refactor the Gilded Rose code **one small step at a time**. The golden rule: **Tests First → Small Change → Verify**.

## Your Current Task: {argument}

### Step 1: Understand the Behavior (Write Tests First)

Before touching production code, write tests that cover the behavior you're about to refactor.

**What to do:**
1. Look at the code you want to refactor
2. Write tests that verify all edge cases and current behavior
3. Make sure the tests **fail** if the production code is wrong
4. Run: `python -m pytest -v` to confirm all tests pass (they verify current behavior)

**Questions to answer:**
- What are the preconditions and postconditions?
- What edge cases exist (day 0, negative SellIn, boundary values)?
- Do you cover all branches of the if/else logic?

See [GildedRoseRequirements.md](../../GildedRoseRequirements.md) for item-specific rules.

### Step 2: Make ONE Small Change

Make a single, focused change to the production code:
- Extract a method
- Replace if/else with a more expressive pattern
- Simplify a complex expression
- Move logic to a more appropriate place

**Keep it small** — if you can't explain the change in one sentence, it's too big.

### Step 3: Verify with Tests and Coverage

Run the full test suite and check coverage:

```bash
# Unit tests
python -m pytest -v

# Coverage report
python -m pytest --cov=gilded_rose --cov-report=term-missing

# Approval tests (check for regressions)
python tests/test_gilded_rose_approvals.py
```

**What to verify:**
- ✅ All tests pass (no broken behavior)
- ✅ Coverage didn't decrease
- ✅ Approval test output matches (or update approved files if intentional)

### Step 4: Repeat

Once this change is committed and tested, pick the next small refactoring goal and repeat.

---

## Anti-Patterns (Don't Do This)

❌ Write 10 tests, then make 5 changes at once  
❌ Refactor without running tests between changes  
❌ Change the `Item` class interface  
❌ Ignore failing tests or approval test diffs  

---

## Useful Commands

- **Run unit tests**: `python -m pytest -v`
- **Filter by test name**: `python -m pytest -k "test_aged_brie"`
- **Run with coverage**: `python -m pytest --cov=gilded_rose --cov-report=term-missing`
- **TextTest fixture** (see 10 days of updates): `python texttest_fixture.py 10`

---

## Reference

- [GildedRoseRequirements.md](../../GildedRoseRequirements.md) — Business logic spec
- [python/README.md](../../python/README.md) — Python-specific setup
- Current architecture uses Strategy pattern with `ItemUpdater` subclasses
