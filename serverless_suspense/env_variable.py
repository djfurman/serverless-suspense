import os

import ServerlessSuspense


class EnvironmentModel(ServerlessSuspense):
    def __init__(self, variable_name):
        self._maintenance_field = variable_name

    def _fetch_suspend_status(self):
        if str(os.getenv(self._maintenance_field)).lower() == "true":
            self._suspend_status = True
        else:
            self._suspend_status = False

    def is_suspended(self):
        self._fetch_suspend_status()
        return self._suspend_status
