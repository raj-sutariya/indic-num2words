import os
from datetime import datetime

import pytz

__version__ = "2.0.0"

# Add datetime.now() for test PyPI to skip conflicts in file name
test_version = os.environ.get("TESTPYPI", default=False)
if test_version:
    __version__ += "." + datetime.now(pytz.timezone("UTC")).strftime("%y.%m.%d.%H.%M")
