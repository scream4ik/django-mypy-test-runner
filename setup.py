from setuptools import setup, find_packages

setup(
    name='django-mypy-test-runner',
    version='0.1.0',
    packages=find_packages(exclude=['example']),
    install_requires=[
        'Django>=3.0',
        'mypy',
        'django-stubs',
        'djangorestframework-stubs',
    ]
)
