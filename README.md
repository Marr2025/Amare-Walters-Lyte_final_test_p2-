# Amare Walters Lyte

Last updated: 2025-12-11

Overview
--------
This repository contains a small demo web app stub and a basic HTML template used to demonstrate version control and simple web app concepts for a final test project.

Primary author: Amare Walters Lyte  
Repository maintained/created by: Marr2025

Contents
--------
- app.py — Python web app stub (entry point).
- template.html — Simple HTML template used by the app.
- README.md — This file (project overview, instructions, reflection, next steps).
- (Optional) requirements.txt — Python dependencies (not included by default; see Setup).

Quick purpose statement
-----------------------
This repo is intended as a compact demonstration of:
- A minimal Python web application,
- Use of a simple HTML template,
- Proper repository structure, documentation, and version-control workflow for a small exercise.

Setup and running locally
-------------------------
1. (Optional but recommended) Create and activate a virtual environment:
   - macOS/Linux:
     - python3 -m venv .venv
     - source .venv/bin/activate
   - Windows (PowerShell):
     - python -m venv .venv
     - .\.venv\Scripts\Activate.ps1

2. Install dependencies:
   - If you plan to run a Flask app variant, install Flask:
     - pip install Flask
   - If a `requirements.txt` is added later:
     - pip install -r requirements.txt

3. Run the app:
   - If app.py uses Flask directly, either:
     - python app.py
     - or (with FLASK installed): export FLASK_APP=app.py && flask run  (macOS/Linux)
     - or: set FLASK_APP=app.py && flask run  (Windows CMD)
   - If app.py runs a simple built-in server, run:
     - python app.py

4. Open a browser and go to http://127.0.0.1:5000 (or the port printed by the app).

File descriptions
-----------------
- app.py
  - The main application script. It contains the minimal logic to start a web server and render `template.html`.
  - Treat this file as a stub; expand routes, logic, and tests as needed.
- template.html
  - A simple HTML page used to demonstrate templating and static content delivery.
  - Replace or extend with additional templates in a `templates/` directory if you adopt a framework like Flask.

Development notes & recommended changes
--------------------------------------
- Create a `requirements.txt` with pinned dependencies for reproducible installs:
  - Example: pip freeze > requirements.txt (after installing required packages)
- Move templates into a `templates/` folder and static assets into a `static/` folder if you adopt Flask or a similar framework.
- Add unit and integration tests to exercise the web routes and template rendering.
- Add a simple CI workflow (GitHub Actions) to run linting and tests on push/PR.

Testing and linting
-------------------
- Add tests (pytest recommended). Example:
  - pip install pytest
  - Create `tests/` with test files and run `pytest`.
- Add linters (flake8, pylint, black) to enforce code style.

How to contribute
-----------------
1. Fork the repo and create a feature branch:
   - git checkout -b feat/your-feature
2. Make small, focused commits with clear messages.
3. Push the branch and open a pull request with a description of the change.
4. Use issue tracking for larger tasks; reference issues from your PR.

Suggested commit message style
------------------------------
- feat: short description — for new features
- fix: short description — for bugfixes
- docs: short description — for documentation changes
- chore: short description — for housekeeping tasks

Milestone
---------
- Name: Amare_Walters_Lyte_ft_milestone_1  
- Due date: 2025-12-18

Reflection
----------
This repository represents the first working version for the final test. Building this small web app stub helped me practice:
- Setting up a minimal project structure,
- Documenting purpose and instructions clearly in the README,
- Thinking through setup, dependency management, and how to present a reproducible development environment.

In addition, the repository currently has two open issues that guide immediate next work. I have included them here so the reflection ties directly to actionable items and the project's TODO list.

Open issues (as of 2025-12-11)
- #3 Implement page styling for web app
  - Link: https://github.com/Marr2025/Amare-Walters-Lyte_final_test_p2-/issues/3
  - Summary: Add CSS styles to the index/template to improve appearance (background, fonts, spacing) so the app looks visually appealing and is easy to read.
  - Status: open, assigned to Marr2025
  - Quick steps to address:
    - Create `static/css/style.css`
    - Link stylesheet in template.html (or move template to `templates/index.html`)
    - Add basic responsive layout, readable font-family, padding/margins, and accessible color contrast.

- #2 Verify Flask app routing and presence of template.html
  - Link: https://github.com/Marr2025/Amare-Walters-Lyte_final_test_p2-/issues/2
  - Summary: Confirm that `app.py` routing is correct and that `template.html` exists in `templates/`. Add error handling for missing templates and consider expanding routes.
  - Status: open, assigned to Marr2025
  - Quick steps to address:
    - Move `template.html` into a `templates/` folder (Flask default).
    - Update `app.py` to handle missing templates with try/except and return a friendly error.
    - Add a second route (e.g., `/about`) to demonstrate routing and add a basic unit test for the root route.

What went well
- A compact, working example was produced that demonstrates how a Python script can deliver HTML content.
- README drafted early to explain intent and steps to run the app.

Challenges encountered (linked to issues)
- Styling and visual polish are missing — see issue #3.
- Minimal routing and lack of error handling for templates — see issue #2.

Lessons learned and next steps
- Add `requirements.txt` and tests.
- Add a basic GitHub Actions workflow to run tests automatically on PRs.
- Resolve issues #2 and #3:
  - Move templates into `templates/` and implement basic error handling (issue #2).
  - Add `static/css/style.css` and apply styles to template.html (issue #3).
- Expand the app with one or two more routes and improve template structure.

Known issues and limitations
----------------------------
- Minimal/no error handling in the stub (see issue #2).
- No automated tests or CI in this initial commit.
- No formal dependency manifest (requirements.txt) included by default.
- No CSS or visual styling yet (see issue #3).

Contact
-------
- Author: Amare Walters Lyte
- Repository owner / maintainer: Marr2025
- For questions or help, open an issue in this repository.

License
-------
If you intend to make this public, consider adding a LICENSE file (MIT, Apache-2.0, etc.). No license file is included by default.

Changelog
---------
- 2025-12-11 — Initial README rewrite, added issues into Reflection (Amare Walters Lyte / Marr2025).

Acknowledgements
----------------
Thanks to instructors and peers who provided guidance for the final test and repository setup.
