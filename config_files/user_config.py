"""
This file contains user-level configuration.
It is expected that the user fills this file once when setting up the project, and does not need to modify it after.
"""

import os
from pathlib import Path
from sys import platform

is_linux = platform in ["linux", "linux2"]

username = "p_regius"  # Username of the TMNF account

# Path where Python_Link.as should be placed so that it can be loaded in TMInterface.
# Usually Path(os.path.expanduser("~")) / "Documents" / "TMInterface" / "Plugins" / "Python_Link.as"
target_python_link_path = Path(os.path.expanduser("~")) / "OneDrive" / "Documents" / "TMInterface" / "Plugins" / "Python_Link.as"

# Typically path(os.path.expanduser("~")) / "Documents" / "TrackMania"
# trackmania_base_path = Path(os.path.expanduser("~")) / "Documents" / "TrackMania"
trackmania_base_path = Path(os.path.expanduser("~")) / "OneDrive" / "Documents" / "TrackMania"

# Communication port for the first TMInterface instance that will be launched.
# If using multiple instances, the ports used will be base_tmi_port + 1, +2, +3, etc...
base_tmi_port = 8478

# If on Linux, path of a shell script that launches the game, with the TMInterface port as first argument
linux_launch_game_path = "path_to_be_filled_only_if_on_linux"

# If on windows, path where TMLoader can be found.
# Usually Path(os.path.expanduser("~") / "AppData" / "Local" / "TMLoader" / "TMLoader.exe"
windows_TMLoader_path = Path(os.path.expanduser("~")) / "AppData" / "Local" / "TMLoader" / "TMLoader.exe"

# If on windows, name of the TMLoader profile that with launch TmForever + TMInterface
# windows_TMLoader_profile_name = "default"
windows_TMLoader_profile_name = "linesight"
