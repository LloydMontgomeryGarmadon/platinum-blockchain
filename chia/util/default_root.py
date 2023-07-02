from __future__ import annotations

import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("PLATINUM_ROOT", "~/.platinum/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("PLATINUM_KEYS_ROOT", "~/.platinum_keys"))).resolve()

SIMULATOR_ROOT_PATH = Path(os.path.expanduser(os.getenv("PLATINUM_SIMULATOR_ROOT", "~/.platinum/simulator"))).resolve()
