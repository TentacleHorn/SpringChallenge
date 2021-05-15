from dataclasses import dataclass
from enum import Enum
from typing import Tuple, Any
import numpy as np
import numba


@dataclass
class HexCoord:
    x: int
    y: int


# @numba.jit
# def dist(c1, c2):
#     total = np.sqrt(
#         np.sum(np.power(np.subtract(c1, c2), 2))
#     )
#     return total

# @numba.jit
def distance(c1, c2):
    return np.sum(np.abs(np.subtract(c1, c2))) // 2


class LightDirection(Enum):
    TOP: 0
    LEFT: 1
    BOTTOM: 2


class HexGrid:
    def __init__(self, size: int, light_direction=0):
        shape = tuple(size * 2 + 1 for _ in range(2))
        self.grid = np.empty(shape, dtype=np.uint8)
        self.size = size
        self.light_direction = light_direction

    def is_index_inside(self, index: HexCoord):
        d = distance(index, (0, 0))
        return d <= self.size

    def add(self, index: HexCoord, data: Any):
        pass

    def remove(self, index: HexCoord):
        self.grid[index.x, index.y] = 0

    def get(self, index: HexCoord):
        return self.grid[index.x, index.y]

    def get_nodes_in_light(self, light_direction: [int, LightDirection] = None):
        light_direction = light_direction if light_direction is not None else self.light_direction
