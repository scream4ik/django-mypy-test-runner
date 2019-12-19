from django.test.runner import DiscoverRunner
from django.core.checks.messages import (
    CheckMessage, DEBUG, INFO, WARNING, ERROR
)
from django.conf import settings

from mypy import api

import re


class MyPyErrorLocation:

    def __init__(self, location):
        self.location = location

    def __str__(self):
        return self.location


class MypyDiscoverRunner(DiscoverRunner):
    """
    Tests runner with mypy checker
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mypy()

    @staticmethod
    def mypy():
        print("Performing mypy checks...\n")

        # By default run mypy against the whole database everytime checks
        # are performed. If performance is an issue then `app_configs`
        # can be inspected and the scope  of the mypy check can be restricted
        results = api.run([settings.BASE_DIR])
        error_messages = results[0]

        if not error_messages:
            return []

        pattern = re.compile("^(.+\d+): (\w+): (.+)")

        for message in error_messages.rstrip().split("\n"):
            parsed = re.match(pattern, message)
            if not parsed:
                continue

            location = parsed.group(1)
            mypy_level = parsed.group(2)
            message = parsed.group(3)

            level = DEBUG
            if mypy_level == "note":
                level = INFO
            elif mypy_level == "warning":
                level = WARNING
            elif mypy_level == "error":
                level = ERROR
            else:
                print(f"Unrecognized mypy level: {mypy_level}")
            print(
                CheckMessage(level, message, obj=MyPyErrorLocation(location))
            )
