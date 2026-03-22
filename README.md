# trello-to-actions

A GitOps-style automated development workflow connecting Trello, GitHub, and GitHub Actions.

## Project Overview
This project demonstrates a small-team development workflow where Git is the single source of truth. Every task is tracked in Trello, every commit references a Trello ID, and every merge to main is gated by automated CI checks.

## Architecture
```
Trello Card → Feature Branch → Commits → Pull Request → CI Pipeline → Merge to main
```

## Workflow
- Tasks start in Trello as cards with unique IDs (TRELLO-001, TRELLO-002, etc.)
- Each card gets its own feature branch: `feature/TRELLO-00X-description`
- Every commit message references the Trello ID: `[TRELLO-00X] Description`
- PRs are opened against main and must pass CI before merging
- Cards move across Trello columns as work progresses

## Commit Convention
```
[TRELLO-###] Short description

Optional detailed explanation
```

## Setup
```bash
git clone https://github.com/YOUR_USERNAME/task-to-deploy.git
cd task-to-deploy
pip install -r requirements.txt
pytest test_app.py -v
```

## Reflection

### 1. Why GitOps?
GitOps treats Git as the single source of truth for both code and workflow state...
(200-300 words)

### 2. What does CI/CD enforce?
Automated pipelines remove human error from quality checks...
(200-300 words)

### 3. How was onboarding designed?
The goal was to get a new developer contributing in under 1 hour...
(200-300 words)

### 4. What failed and why?
During implementation the laptop died mid-commit, corrupting the git object database...
(200-300 words)

### 5. What would you do differently?
With more time I would integrate n8n to automate Trello card movement...
(200-300 words)