import logging

from .base import ServerlessSuspense

__version__ = "0.0.1"

logging.getLogger("serverless_suspense").addHandler(logging.NullHandler())
