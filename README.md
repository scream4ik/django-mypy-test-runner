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
plugins =
  mypy_django_plugin.main,
  mypy_drf_plugin.main

ignore_missing_imports = True

[mypy.plugins.django-stubs]
django_settings_module = example.settings

[mypy-*.migrations.*]
ignore_errors = True
```

Run tests :)
