import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)

s = "string"

r = requests.get("https://coreyms.com")
print(r.status_code)
