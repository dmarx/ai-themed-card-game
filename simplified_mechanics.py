"""
let's try to encode formally how this game might work at a high level
"""

from dataclasses import dataclass
from copy import deepcopy
from enum import Enum

@dataclass
class Resource:
    amount: int = 1

class Capital(Resource):
    pass

class Data(Resource):
    pass

class Influence(Resource):
    pass

class Reputation(Influence):
    pass

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
    cost_to_use: list[Resource]
    owner_gain_per_use: list[Influence] # the "owner" mechanism disincentivizes collaboration. "Contributor" maybe?


#@dataclass
class Model(Artifact):
    category: ModelCategory = ModelCategory.BASIC
    modalities: list[Modality]
    availability: Availability"
    base_data_requirement: int = 1
    base_compute_requirement: int = 1
    tokens_trained: int = 0 # models accumulate training, s.t. we can finetune existing models to make them more useful, and upgrading a model is some function of how many tokens it was trained on
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
    modalities: all data must have at least one modality, but can have multiple.
    cardinality: Every dataset has a cardinality, i.e. the number of data items
      associated with the dataset.

    Players build up datasets by collecting data resources and assigning them to a dataset.
    Data resources can be purchased with capital, or collected through normal gameplay (e.g. cards, trading).
    Models and capital can be used to refine raw data.
    --> feels like the "data" resource and the "dataset" artifact should be two different hings

    """
    category: DataCategory = DataCategory.RAW
    modalities: list[Modality] = Modality.TEXT
    availability: Availability = Availability.UNAVAILABLE
    cardinality: int = 0
    owner: str = ""

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

class VentureCapital(Funding):
    # relies more on reach than reputation
    pass

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


# 
class Card:
    pass

class ResourceCard(Card):
    pass

class EventCard(Card):
    pass
