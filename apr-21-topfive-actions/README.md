# Top Five

**Team:** Collin Schaufele and William Martin

This is a preliminary version of a social media platform called Top Five. The primary function of this website is for users to create posts listing their top five favorite items for a specific category.

## Class Activity
For class, please complete the following activity (you may work individually or with a partner/small group):
1. Fork this repository from the course repository
2. Complete the Quickstart Guide for GitHub Actions to add a project build to your forked repository: https://docs.github.com/en/actions/writing-workflows/quickstart
3. Add a custom behavior to work GitHub Action workflow.
4. Make at least four changes (as time allows) to the repository
  * One must be adding you/your teams' first and last names to the README file.
  * One must be adding a new file describing you/your team’s prior CI/CD experience.
  * Other suggestions to add: UI updates, tests, code improvements, additional functionality, questions about the lecture, etc. (please disclose AI usage)
5. Submit the link to forked repository on Canvas. Complete whatever you finish by the end of class today.

## Changes Made (Assignment Requirements)

This fork includes the following four required modifications:

1. **Team names added to README** — Collin Schaufele and William Martin (this file)
2. **Prior CI/CD experience file** — See `EXPERIENCE.md` for full details on our background with CI/CD, GitHub Actions, Python packaging, and GPU cluster infrastructure
3. **GitHub Actions CI workflow** — See `.github/workflows/ci.yml` — runs pytest and Flask smoke test on every push and PR
4. **Unit tests** — See `tests/test_app.py` — 13 test cases covering routes, form validation, and submission display (AI-assisted: Claude helped structure test patterns)

Additional improvements:
- **UI refresh** — Modernized `templates/index.html` with a clean card-based design, gradient header, responsive layout, and visual polish (AI-assisted)

## Run Program

To run the project locally, please use the following commands in your terminal (requires Python installation):

* pip install -r requirements.txt
* python app.py
* Open browser and visit http://127.0.0.1:5000/ (or designated link provided)

## Run Tests

To run the automated test suite:

* pip install pytest --quiet
* pytest tests/ -v
