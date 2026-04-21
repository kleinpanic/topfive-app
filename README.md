# topfive-app — CS 3704 Monorepo

**Team:** Collin Schaufele and William Martin

This repository is a monorepo for CS 3704 (Intermediate Software Design and Engineering) class work. It contains multiple subprojects organized by date and topic.

## Subprojects

### `2026-04-21-topfive-actions/` — GitHub Actions CI/CD Fork
**Assignment:** Fork the Top Five sample app, add a GitHub Actions workflow, make 4+ changes.

Forked from: `https://github.com/CS3704-VT/top_five`

Key changes:
- Added `.github/workflows/ci.yml` — runs pytest and Flask smoke test on every push/PR
- Added `EXPERIENCE.md` — prior CI/CD and software engineering experience
- Added `tests/test_app.py` — 14 unit test cases (AI-assisted: Claude)
- Modernized `templates/index.html` — card-based UI, gradient header, responsive design (AI-assisted)
- Team names added to `README.md`: Collin Schaufele and William Martin

To run locally:
```bash
cd 2026-04-21-topfive-actions
pip install -r requirements.txt
python app.py
```

To run tests:
```bash
cd 2026-04-21-topfive-actions
pytest tests/ -v
```

### `attendance/` — Original Top Five Starter Files
The original 3-file starter project (index.html, LICENSE, README.md) as it was at the beginning of the assignment. Kept for reference.

## Attendance

Class attendance records and related materials can be found in the `attendance/` directory (if present).
