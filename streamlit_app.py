"""Root launcher so `streamlit run streamlit_app.py` works from workspace root."""

from __future__ import annotations

import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
APP = SRC / "streamlit_app.py"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

runpy.run_path(str(APP), run_name="__main__")