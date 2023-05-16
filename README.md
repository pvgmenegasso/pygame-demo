# This is a project to learn pygame and explore it's potential

-------------------------------------------------------------------

# Quick Setup:
asdf was used to install python then pipenv was installed. thus Pipfile and Pipfile.lock files

# Installation`
you currently need python 3.11 to run this project
the current python versioning system is pipenv
to run game use:
```
$: pipvenv run game/main.py
```

# Testing
To run tests, use:
```
$: pipenv run pytest tests
```

# Branch Protection Rules.
All code on master branch must meet following criteria:
1. `pipenv run black --check .` must return 0. Non 0 will cause PR to fail
2. `pipenv run mypy --strict game/main.py` must return 0. Non 0 will cause PR to fail
