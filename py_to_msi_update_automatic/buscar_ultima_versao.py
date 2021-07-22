import sys
import os
import sys
import ctypes
from ctypes import wintypes
import esky
import win32con
import requests

version = requests.get("http://127.0.0.1:1022/").json()['version']

print(version)

if hasattr(sys, "frozen"):
	app = esky.Esky(sys.executable,version )
	app.auto_update()
	print('safe')
