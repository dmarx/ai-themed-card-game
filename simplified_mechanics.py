from dataclasses import dataclass, field
from copy import deepcopy
from enum import Enum

@dataclass
class Resource:
    amount: int = 1

@dataclass
class Compute:
    pass

@dataclass
class Capital(Resource):
    pass

@dataclass
class Data(Resource):
    pass

@dataclass
class Influence(Resource):
    pass

@dataclass
class Reputation(Influence):
    pass

@dataclass
class Reach(Influence):
    pass


class DataCategory(Enum):
    RAW = 1
    REFINED = 2


class ModelCategory(Enum):
    BASIC = 1
    ADVANCED = 2
    EXPERIMENTAL = 3


class Availability(Enum):
    UNAVAILABLE = 1
    OPEN_SOURCE = 2
    COMMERCIAL_API = 3
    PRIVATE = 4


class Modality(Enum):
    TEXT = 1
    IMAGE = 2
    OTHER = 3


@dataclass
class ModelUpgradeState:
    """
    Investment already committed towards upgrading a model
    """
    data: int = 0
    compute: int = 0

    def __le__(self, other:ModelUpgradeState):
        return (self.data <= other.data) and (self.compute <= other.compute)

# Maybe Artifacts can be able to accumulate their own reach/reputation. e.g. when people use a model, that increases its locally tracked influence.
# then at the end of the game, the influence associated with artifacts a user has shipped/owns contributes to their final score

@dataclass
class Artifact:
    """
    Two kinds of artifacts (atm): model, dataset.
    Building an artifact imparts a benefit to its owner. currently, in the form of influence points.
    if user A uses an artifact owned by user B, user B gains influence.
    If the artifact's availability is COMMERCIAL_API, user A must pay a CAPITAL cost to user B (unless a special arrangement has been negotiated through trade)
    """
    owner: str = "
    cost_to_build: list[Resource] 
    cost_to_upgrade: list[Resource]
    cost_to_use: list[Resource] = field(default_factory=lambda: [Compute(), Data()]) # need a way to differentiate AND vs OR conditions
    owner_gain_per_use: list[Influence] # the "owner" mechanism disincentivizes collaboration. "Contributor" maybe?
    modalities: list[Modality]
    availability: Availability = Availability.UNAVAILABLE

@dataclass
class Model(Artifact):
    category: ModelCategory = ModelCategory.BASIC
    #base_data_requirement: int = 1
    #base_compute_requirement: int = 1
    #tokens_trained: int = 0 # models accumulate training, s.t. we can finetune existing models to make them more useful, and upgrading a model is some function of how many tokens it was trained on
    upgrade_progress: ModelUpgradeState # data and compute previously consumed towards satisfying upgrade cost

    def upgrade(self):
        if self.category == ModelCategory.BASIC:
            self.category = ModelCategory.ADVANCED
            return True
        elif self.category == ModelCategory.ADVANCED:
            self.category = ModelCategory.EXPERIMENTAL
            return True
        return False

    @property
    def upgrade_cost(self) -> ModelUpgradeState:
        # some function of compute and data resources
            # On the one hand, i like the idea that to make a model better, you need to use more data than was used to train it originally.
            # On the other hand, i'd like for users to be able to upgrade a model incrementally over many turns by committing compute/data to it
        data_cost = self.base_data_requirement * self.tokens_trained * len(modalities) * self.category
        compute_cost = self.base_compute_requirement * len(modalities) * self.category
        return ModelUpgradeState(data=data_cost, compute=compute_cost)


#@dataclass
class Dataset(Artifact):
    """
    The "dataset" artifact can be combined with compute to build or upgrade models.
    category: Refined data is more valuable than raw data. 
      both raw and refined data can be used to build the same models, but it takes
      a lot less refined data to build the same model than raw data.
    modalities: all datasets must have at least one modality, but can have multiple.
    cardinality: Every dataset has a cardinality, i.e. the number of data items
      associated with the dataset.

    Players build up datasets by collecting data resources and assigning them to a dataset.
    Data resources can be purchased with capital, or collected through normal gameplay (e.g. cards, trading).
    Models and capital can be used to refine raw data.
    --> feels like the "data" resource and the "dataset" artifact should be two different hings

    """
    category: DataCategory = DataCategory.RAW
    cardinality: int = 0

    def upgrade(self):
        if self.category == DataCategory.RAW:
            self.category = DataCategory.REFINED
            return True
        return False

    @property
    def upgrade_cost(self):
        if self.category == DataCategory.RAW:
            return self.cardinality * len(self.modalities)


@dataclass
class Funding:
    requirement: Influence # threshold needed to apply for funding
    commitment: list[Artifact] # what the user is committing to deliver
    capital: Capital
    compute: Compute

@dataclass
class VentureCapital(Funding):
    # relies more on reach than reputation
    pass

@dataclass
class ResearchGrant(Funding):
    # relies more on reputation
    # commitments must have availability=OPEN_SOURCE
    pass

@dataclass
class PublicCommons:
    self.models: list[Model]
    self.datasets: list[Dataset]
    # resources (capital, compute, data) in exchange for commitments and/or risk/reward tradeoff
    ### reputation can be activated (not consumed) to secure funding opportunities
    #self.funding_grants_available: list
    #self.funding_vc_available: list
    self.funding_opportunities: list[Funding]


class PlayerState:
    weight_reputation = 1
    weight_reach = 1
    weight_capital = 1

    def __init__(self):
        self.reputation = 0
        self.reach = 0
        self.compute = 0
        # maybe a user's individual data resource is only typed by modality,
        # and a dataset can either be "raw" or "refined". 
        # it's harder to grow "refined" datasets, but you can do more with them
        self.data_raw  = 0
        self.data_refined = 0
        self.capital = 0
        self.hand = []
    
    @property
    def score(self):
        return (
            self.weight_reputation * self.reputation +
            self.weight_reach * self.reach +
            self.weight_capital * self.capital
        )


class Player:
    def __init__(
        self, 
        name, 
        state: PlayerState = None, 
        cards_in_hand = list[Card]
    ):
        self.name = name
        if not cards_in_hand:
            cards_in_hand = []
        self.cards_in_hand = cards_in_hand

        if state:
            self.state = state
        else:
            self.state = PlayerState()

class Card:
    pass

class ResourceCard(Card):
    pass

class EventCard(Card):
    pass


# via chatgpt

from typing import Callable

# class EffectType(Enum):
#     ADJUST_RESOURCE = 1
#     ADJUST_GLOBAL_PARAMETER = 2
#     PLACE_TILE = 3
#     SPECIAL_ACTION = 4

# @dataclass
# class Effect:
#     effect_type: EffectType
#     target: any  # Can be a ResourceType, GlobalParameter, TileType, etc.
#     value: int  # The value of the effect (e.g., amount of resource, parameter change)
#     special_action: Callable[['Player', 'Game'], None] = None  # For special, unique actions

#     def apply(self, player: 'Player', game: 'Game'):
#         if self.effect_type == EffectType.ADJUST_RESOURCE:
#             player.resources[self.target] += self.value
#         elif self.effect_type == EffectType.ADJUST_GLOBAL_PARAMETER:
#             game.board.adjust_global_parameter(self.target, self.value)
#         elif self.effect_type == EffectType.PLACE_TILE:
#             new_tile = Tile(tile_type=self.target, owner=player)
#             game.board.place_tile(new_tile, player)
#         elif self.effect_type == EffectType.SPECIAL_ACTION and self.special_action:
#             self.special_action(player, game)

# class Card:
#     # ... [previous attributes]
#     effects: List[Effect]

#     def play(self, player: 'Player', game: 'Game'):
#         for effect in self.effects:
#             effect.apply(player, game)

# class Player:
#     # ... [existing methods]

#     def play_card(self, card: Card, game: 'Game'):
#         if self.can_afford(card):
#             self.resources[ResourceType.MEGACREDIT] -= card.cost
#             card.play(self, game)
#             self.played_cards.append(card)
#             # Additional logic for card play

#     def can_afford(self, card: Card) -> bool:
#         return self.resources[ResourceType.MEGACREDIT] >= card.cost

# # Example of defining a card with effects
# adjust_oxygen = Effect(EffectType.ADJUST_GLOBAL_PARAMETER, GlobalParameter.OXYGEN, 1)
# place_greenery = Effect(EffectType.PLACE_TILE, TileType.GREENERY, 1)

# greenery_card = Card("Plant Greenery", 23, {}, [adjust_oxygen, place_greenery])

@dataclass(frozen=True)
class GameState:
    players: Tuple[Player, ...]
    board: Board
    deck: Tuple[Card, ...]
    current_player_index: int

    def update_player(self, player_index: int, new_player: Player):
        new_players = list(self.players)
        new_players[player_index] = new_player
        return GameState(tuple(new_players), self.board, self.deck, self.current_player_index)

    def update_board(self, new_board: Board):
        return GameState(self.players, new_board, self.deck, self.current_player_index)

# Effect functions now return a new GameState
def adjust_resource(player: Player, game: GameState, resource: ResourceType, amount: int) -> GameState:
    new_resources = dict(player.resources)
    new_resources[resource] = new_resources.get(resource, 0) + amount
    new_player = Player(player.corporation, new_resources, player.terraform_rating, player.owned_tiles, player.played_cards)
    return game.update_player(game.current_player_index, new_player)

def adjust_global_parameter(game: GameState, parameter: GlobalParameter, amount: int) -> GameState:
    new_global_parameters = dict(game.board.global_parameters)
    new_global_parameters[parameter] = new_global_parameters.get(parameter, 0) + amount
    new_board = Board(game.board.tiles, new_global_parameters)
    return game.update_board(new_board)

def place_tile(game: GameState, tile_type: TileType, player: Player) -> GameState:
    new_tile = Tile(tile_type, player)
    new_board = Board(game.board.tiles + [new_tile], game.board.global_parameters)
    return game.update_board(new_board)

# Usage of effect functions within actions
def play_card(player: Player, game: GameState, card: Card) -> GameState:
    new_game_state = game
    for effect in card.effects:
        if effect.effect_type == EffectType.ADJUST_RESOURCE:
            new_game_state = adjust_resource(player, new_game_state, effect.target, effect.value)
        elif effect.effect_type == EffectType.ADJUST_GLOBAL_PARAMETER:
            new_game_state = adjust_global_parameter(new_game_state, effect.target, effect.value)
        elif effect.effect_type == EffectType.PLACE_TILE:
            new_game_state = place_tile(new_game_state, effect.target, player)
        # Handle other effect types...
    return new_game_state

