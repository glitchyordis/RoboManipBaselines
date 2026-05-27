import math

import numpy as np

from .RealUR5eEnvBase import RealUR5eEnvBase

polaris_qpos = np.array(
    [
        math.radians(-81.36),
        math.radians(-97.36),
        math.radians(-101.46),
        math.radians(-71.17),
        math.radians(90.29),
        math.radians(8.95),
    ]
)


class RealUR5eDemoEnv(RealUR5eEnvBase):
    def __init__(
        self,
        **kwargs,
    ):
        RealUR5eEnvBase.__init__(
            self,
            init_qpos=polaris_qpos,
            **kwargs,
        )

    def modify_world(self, world_idx=None, cumulative_idx=None):
        """Modify simulation world depending on world index."""
        # TODO: Automatically set world index according to task variations
        if world_idx is None:
            world_idx = 0
            # world_idx = cumulative_idx % 2
        return world_idx
