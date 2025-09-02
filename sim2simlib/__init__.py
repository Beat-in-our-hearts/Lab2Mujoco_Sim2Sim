
from pathlib import Path

SIM2SIMLIB_REPO_DIR = Path(__file__).resolve().parent.parent

SIM2SIMLIB_ASSETS_DIR = SIM2SIMLIB_REPO_DIR / "assets"

CHECKPOINT_DIR = SIM2SIMLIB_REPO_DIR / "checkpoints"

MUJOCO_ASSETS = {
    "unitree_go2": SIM2SIMLIB_ASSETS_DIR / "unitree_go2" / "mjcf" / "scene_go2.xml",
    "unitree_g1_29dof": SIM2SIMLIB_ASSETS_DIR / "unitree_g1" / "mjcf" / "scene_29dof_rev_1_0.xml",
    "unitree_g1_23dof": SIM2SIMLIB_ASSETS_DIR / "unitree_g1" / "mjcf" / "scene_23dof_rev_1_0.xml"
}


