# Getting Started

You should be able to make your first contribution in under 1 hour.

## 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/task-to-deploy.git
cd task-to-deploy
```

## 2. Install dependencies
```bash
pip install -r requirements.txt
```

## 3. Run tests locally
```bash
pytest test_app.py -v
```
All tests should pass before you touch anything.

## 4. Create your branch
```bash
git checkout -b feature/TRELLO-00X-your-description
```

## 5. Make your change, then commit
```bash
git add .
git commit -m "[TRELLO-00X] What you did"
git push origin feature/TRELLO-00X-your-description
```

## 6. Open a Pull Request
- Go to GitHub and click "Compare & pull request"
- Title must include the Trello ID
- Wait for CI to go green before merging

## Troubleshooting
| Problem | Fix |
|---|---|
| flake8 errors | Add 2 blank lines between every function |
| pytest failing | Run `pip install -r requirements.txt` first |
| CI failing on push | Check the Actions tab for the exact error |
| Branch already exists | Run `git branch -D branch-name` and recreate |