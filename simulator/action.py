from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum

from game_state import GameState
from hex import HexCoord


@dataclass
class ActionBase:

    @abstractmethod
    def apply(self, game_state: GameState, player: int):
        pass


class PlaceTree(ActionBase):
    coord: HexCoord

    def apply(self, game_state: GameState, player: int):
        raise NotImplementedError()


class ClaimTree(ActionBase):
    coord: HexCoord

    def apply(self, game_state: GameState, player: int):
        grid = game_state.grid
        current = grid.get(self.coord)
        if not current:
            raise ValueError("no tree to claim")
        # TODO
        grid.remove()
        # game_state.players[player].game_points +=


class Action(Enum):
    PLACE_TREE = PlaceTree
    CLAIM_TREE = ClaimTree
