#!/usr/bin/env python3

from .smooth import CacheController
from .exceptions import (
    KeyAlreadyExistsError,
    EntryNotFoundError,
    EntryExpiredError,
)

Cache = CacheController()

__all__ = [
    "Cache",
    "CacheController",
    "KeyAlreadyExistsError",
    "EntryNotFoundError",
    "EntryExpiredError",
]
