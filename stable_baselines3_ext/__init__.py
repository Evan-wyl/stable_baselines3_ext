import os

from stable_baselines3_ext.sac_td3.sac import SACTD3

# Read version from file
version_file = os.path.join(os.path.dirname(__file__), "version.txt")
with open(version_file) as file_handler:
    __version__ = file_handler.read().strip()


__all__ = [
    "SACTD3",
]