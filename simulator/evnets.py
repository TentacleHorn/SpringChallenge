from dataclasses import dataclass

from game_state import GameState


@dataclass
class EventBase:
    pass


class TurnEvent:
    game_state: GameState
