# Run Django tests with typechecking

Installation
```
pip install https://gitlab.com/OldminTeam/django-mypy-test-runner/-/archive/0.1.0/django-mypy-test-runner-0.1.0.zip
```

Add to Django settings
```
TEST_RUNNER = 'mypy_test_runner.runner.MypyDiscoverRunner'
```

Create `mypy.ini` or `setup.cfg` in project root
```
[mypy]
ignore_missing_imports = True
```

Run tests :)
