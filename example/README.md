# Running the example application

Assuming you use virtualenv, follow these steps to download and run the example application in this directory:
```
git clone https://gitlab.com/OldminTeam/django-mypy-test-runner
cd django-mypy-test-runner/example
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
```

Now you need to run the Django tests:
```
python manage.py test
```
