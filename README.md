# Run Django tests with typechecking

Installation
```
pip install https://github.com/scream4ik/django-mypy-test-runner/archive/v0.1.0.zip
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
