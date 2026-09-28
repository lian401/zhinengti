import os
from pathlib import Path

shortcut = (
    Path(os.environ["ProgramData"])
    / "Microsoft"
    / "Windows"
    / "Start Menu"
    / "Programs"
    / "网易云音乐"
    / "网易云音乐.lnk"
)

if shortcut.exists():
    os.startfile(str(shortcut))
else:
    print("找不到网易云音乐快捷方式")