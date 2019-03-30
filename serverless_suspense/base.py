class ServerlessSuspense:
    def __init__(self):
        pass

    def _fetch_suspend_status(self):
        raise NotImplementedError("Must implement method to fetch status")

    def is_suspended(self):
        raise NotImplementedError("Must implement suspense status boolean")
