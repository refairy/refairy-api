import os
from typing import Optional


def get_env(key: str, fallback: Optional[str]=None):
    port = os.environ.get(key) or fallback
    return port
