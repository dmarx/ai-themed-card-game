from pyrsistent import pvector, pmap, m
from typing import Callable, Iterable
from enum import Enum
import random
import functools

class ResourceType(Enum):
    CAPITAL = 1
    DATA = 2
    INFLUENCE = 3

@dataclass(frozen=True)
class PlayerState:
    resources: pmap
    artifacts: pvector

@dataclass(frozen=True)
class GameState:
    players: pvector
    global_state: pmap
    current_player_index: int

EffectFunction = Callable[[GameState, int], GameState]

def compose(*functions):
    def compose_two(f, g):
        return lambda x: f(g(x))
    return functools.reduce(compose_two, functions, lambda x: x)

def apply_effects(effects: Iterable[EffectFunction], state: GameState, player_index: int) -> GameState:
    return compose(*[effect for effect in reversed(effects)])(state, player_index)

def game_state_generator(initial_state: GameState) -> Iterable[GameState]:
    state = initial_state
    while not check_end_condition(state):
        for action in get_player_actions(state):
            state = action.perform(state)
            yield state

def shuffle_deck(deck: Iterable[Card], random_gen: random.Random) -> Iterable[Card]:
    return sorted(deck, key=lambda _: random_gen.random())

def adjust_resource(state: GameState, player_index: int, resource: ResourceType, amount: int) -> GameState:
    player = state.players[player_index]
    new_resources = player.resources.set(resource, player.resources.get(resource, 0) + amount)
    new_player = player.set('resources', new_resources)
    return state.set('players', state.players.set(player_index, new_player))

def play_card(state: GameState, player_index: int, card: Card) -> GameState:
    player = state.players[player_index]
    # Assuming card cost is handled elsewhere
    effects = card.effects  # List of EffectFunctions
    return apply_effects(effects, state, player_index)

def play_game(initial_state: GameState) -> GameState:
    game_states = game_state_generator(initial_state)
    final_state = functools.reduce(lambda state, _: state, game_states)
    return final_state

def check_end_condition(state: GameState) -> bool:
    # Implement end game condition check
    pass

def get_player_actions(state: GameState) -> Iterable[Action]:
    # Logic to generate actions available to the current player
    pass


