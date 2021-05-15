import abc
from dataclasses import dataclass
from enum import Enum

from action import Action
from evnets import TurnEvent
from game_state import GameState
import multiprocessing as mp

from hex import HexCoord


class AlgoBase(abc.ABC):
    def __init__(self, player_id):
        self.player_id = player_id

    @abc.abstractmethod
    def do_turn(self, game_state: GameState) -> Action:
        pass


def player_process(pipe: mp.connection.Connection, played_id: int, algo: AlgoBase):
    running = True
    game_state = None
    player_handle = PlayerHandle(played_id, algo)
    while running:
        event = pipe.recv()
        if isinstance(event, TurnEvent):
            game_state = event.game_state
            action = player_handle.do_turn(game_state)


class PlayerHandle:
    def __init__(self, player_id: int, algo: AlgoBase):
        self.algo = algo
        self.player_id = player_id

    def do_turn(self, game_state: GameState):
        self.algo.do_turn(game_state)
