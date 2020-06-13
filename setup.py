# import sys from cx_Freeze
from cx_Freeze import setup, Executable
import sys

base  = None
if sys.platform == "win32" : base = "Win32GUI"
opts = {'include_files': ['music.mp3'], 'includes': ['tkinter', 'pyautogui']}
setup (
    name = 'virus',
    version = 0.1,
    description = "Simple Word",
    options = {'build_exe': opts},
    executables = [Executable('virus.py', base= base)])
#python setup.py build