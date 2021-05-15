from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

from hex import HexGrid, HexCoord


class PlayerID(Enum):
    ME: int = 0
    ENEMY: int = 1


@dataclass
class PlayerState:
    # def __init__(self, tree_map, game_points, ):
    game_points: int = 0
    light_points: int = 0
    trees: Dict[HexCoord, int] = None


class GameState:
    def __init__(self):
        self.grid = HexGrid(3)
        self.turn = 0
        self.players: List[PlayerState] = list()

    def get_trees(self, player: int = None) -> Dict[HexCoord, int]:
        if not player:
            return self.get_trees(PlayerID.ME) | self.get_trees(PlayerID.ENEMY)
        return self.players[player].trees

    def get_tree(self, coord: HexCoord):
        def _get_tree_player(player):
            trees = self.players[player].trees
            if coord in trees:
                return trees[coord], player
        return _get_tree_player(PlayerID.ME) or _get_tree_player(PlayerID.ENEMY)




class GameRunner:
    def __init__(self):
        pass

    def run(self, ):
        pass
