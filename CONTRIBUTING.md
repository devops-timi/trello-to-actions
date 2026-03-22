# Contributing

## Branching Rules
- Never push directly to main
- Branch format: `feature/TRELLO-00X-short-description`
- Always branch off latest main: `git pull origin main` first

## Commit Format
```
[TRELLO-###] Short description

Optional body explaining why, not what
```

## PR Process
1. Push your feature branch
2. Open PR with Trello ID in the title
3. CI must go green before merging
4. Merge using "Squash and merge" or "Merge commit"

## CI/CD Pipeline
The pipeline runs automatically on every push and PR:
1. Install dependencies
2. Lint with flake8
3. Test with pytest

## Coding Standards
- Follow PEP8 (flake8 enforced)
- 2 blank lines between every function
- All new functions must have docstrings
- All new features must have matching tests

## When CI Fails
1. Click the failing check on your PR
2. Expand the failing step
3. Fix the error locally
4. Commit and push — CI reruns automatically