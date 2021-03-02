import os


def os_get_env(key: str, default: str = "") -> str:
    try:
        val = os.environ[key]
        return val
    except KeyError:
        return default
