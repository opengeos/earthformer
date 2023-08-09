"""Main module."""

import os
import pkg_resources
from .common import *

def get_pkg_dir(name="earthformer"):
    pkg_dir = os.path.dirname(pkg_resources.resource_filename(name, name + ".py"))
    return pkg_dir


def get_earthnet_yaml():
    pkg_dir = get_pkg_dir()
    earthnet_yaml = os.path.join(
        pkg_dir,
        "scripts/cuboid_transformer/earthnet_w_meso/earthformer_earthnet_v1.yaml",
    )
    if os.path.exists(earthnet_yaml):
        return earthnet_yaml
    else:
        raise FileNotFoundError(f"File not found: {earthnet_yaml}")
