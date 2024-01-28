# Game Design Document

🚧 🚧 **Work In Progress** 🚧 🚧

**Working Title:** AI Assembly

---

# I. Overview

- **Theme**: Artificial Intelligence Development
- **Objective**: Compete to build and optimize AI models, acquire various resources, and gain influence in the AI community.

---

# II. Resources

## 1. **Capital**
   - Exchanged for other resources.
   - Used to purchase outputs/effects from models served by other users.
     - served = compute committed to inferencing that model
   - units of capital could be called "credits"
   - Capital can be used to purchase compute, data, and influence (just reach, not reputation).

## 2. **Compute**
   - Acquired with capital.
   - Necessary for model crafting and training.
   - Energy cost?
     * compute could have an associated energy cost whcih needs to be paid down in capital to utilize compute
     * could alternatively structure this such that compute is all "cloud compute" and only incurs a capital cost, i.e. to be "rented"
   - units of compute called be called "nodes"
   - each compute node has a "generation", represents vertical scaling
   - compute nodes can be combined into "clusters", must be homogeneous by generation


#### **playtesting notes**


compute can be subject to homogeneity compatibility. compute units can be combined into upgraded compute (level 1,2,3), but if paying a compute cost the compute will "parallelize" and be bottlenecked by the lowest level of compute in the "cluster".

upgrading (combining/racking) compute can be a card effect. e.g. play "slurm" card to your board: "pay $x to upgrade compute units once per turn"

available of compute should be one of the slowest growing things in the game. compute will be a heavily fought over resource. 

let there be a small pool of "free" compute which any player can utilize, but only subject to a "reset" period to prevent any one user from monopolizing all free compute.

data represented by loss tokens that are organized and combined into a "buit" model. each turn, compute must be committed to "build" the model from its component data. The model recipe should have a "RAM" threshold or some such which bottlenecks the rate at which compute can be utilized (or data consumed? both?) to assemble the model

users need to upgrade compute to be able to play late game. 

* compute level >=1
  * can refine data  
* compute level >=2
  * can build models
  * can inference simple models
* compute level == 3
  * can inference complex models
* after upgrading a compute unit to level 3, it can be "racked" with other level 3 compute units to form "HPC" clusters (required for late game model training, impacts throughput?)


using lego plates, "level" is height of combined plates.



structuring compute = "racking"/"interconnect" -> horizontal scaling

horizontal scaling requires "racking": joining pairs of compute units into "clusters". racking consumes "hardware" units. maybe some threshold max scaling? limited by compute generation?

periodic milestone (every k rounds, maybe triggered by certain cards distributed in the deck or player achievements): "compute generation" increments. 

when the "compute generation" increments, everyone's compute scales down one unit vertically
- oldest compute gets retired/bricked/sold on aftermarket (exchanged for capital, reduced relative to original purchase price)
- keep users purchasing latest generation compute if they want to be able to train/inference the SOTA

vertical scaling needs to be "parallel". if compute is assigned to a cluster, the entire cluster needs to scale together. otherwise, the cluster can be broken apart to only scale fewer compute units at a time, but the user doesn't get that hardware back and needs to pay again to re-integrate the upgraded compute units to the cluster. a given compute cluster needs to be *homogeneous* relative to its compute units.


compute clusters are public resources. a player owns the compute cluster they develop, but other players can still use reserve and use space on their cluster at market price. the owner of the cluster can expend additional resources to define a "reserved" portion of the cluster that is exclusive to them

alternatively: compute only lives in cloud. as such, compute can't be purchased, only rented. if you can't pay rent on your compute, it is released back to cloud availability for other users to rent on demand or to "purchase" (rent on reserve).

limited compute incentivizes players to share models -> i can't use my compute to train bigger models if you're using my compute to inference my models


## 3. **Data**

 * raw -> refined
   * refined data is worth more or has enhanced effect on model training
 * types by modality: text, image, other
   * "refinement" could just be assigning to a modality
   * modality assignment could be an effect granted by a card, which would let us control distribution of data modality to make certain modalities more valuable, encourage a trading economy
 * could refer to units of data as "tokens"
 * capital can be exchanged for data


### **playtesting notes**


alternatively, "refine" could be a card effect, or something the player always has the option to do (e.g. mechanical turk)
  - tying refinement to cards also makes it so we can control the relative distribution/value of different modalities.
  - we want at least one modality to be particularly rare or costly relative to the others to drive a player economy (trading, strategizing) 
    - users can build strategies aiming at certain modalities
    - some chosen modality -> refinement favors data of that modality -> strategy focuses on building models tied to that modality
      - modalities could characterize different model special effects?

users available uncommitted data could be refferred to as their "data lake". assembled models could be housed in their "model registry", or "production" <- productionize models

refining data = assigning a modality.

additional potential modalities:
  - user activity/telemetry

compute committed to trained models generates raw data.

upgraded models can generate refined data and/or refine raw data.


data could have a "sensitivity" attribute, such that high value data like PII could be modeled as "high sensitivity" data which is only available to players with above some threshold reputation (or "ethics points" or whatever). higher data sensitivity correlates with higher capital generation from models built with that data


data could be easy to generate but hard to store. a player's private "data lake" is something they can invest in to increase their storage capacity, but if they want to train a model that requires more data than they can store, they have to use public data and make the model public. conversely, they can donate data to the public lake (nom-sensitive data only) for a benefit of some kind, like a small gain in influence. so if a user doesn't grow their lake, they can't train large private models and will be incentivized to contribute to the public data pool.


data is similarly combined as the upgrading procedure when building models, which gives the dataset/model a "level" in terms of plate height units as well, which determines compute compatibility for training/inference

model training could have a minimum batch size. part of the data refinement mechanism could be combining data units of the same modelity into larger data sets (2x2 plate green -> 2x4 green plate)

late game models have higher minimum batch size, forcing players to construct (upgrade their data into) larger datasets.
* larger datasets constructed by "joining" datasets (literally, lol). data upgrade can be an effect similar to compute upgrade

add a new construction resource, e.g. "hardware" - plates consumed when upgrading
* "joining" datasets - date upgrade mechanic!
* orchestrating compute into "networked" clusters

limitless public data, private/sensitive data must be purchased



## 4. **Influence**

 * reputation (h-index, ethical points)
 * reach (followers)
 * capital can be exchanged for reach
 * influence is treated as a resource
 * ending the game with the most influence could be a win condition or private goal.
   * actually, this works for any resource

## 5. **hardware**

 * consumed when structuring compute ("racking" compute nodes into clusters)
 * consumed when structuring data ("joining" datasets... "storing"?)

### **playtesting notes**


grey plates = "hardware"/"structure" units.
- need structured compute to operate on structured data
- structured data + structured compute --> satisfy requirements for "dense" models. model density correlates with influence capacity, SOTA scoring, model performance, etc.



# III. Models

Compute and data are required inputs for crafting "models". refined data is worth extra, less data required for training when refined than when raw

Models consume compute and produce capital and data. "shipping" a model increases influence (definitely reputation... reach too)


- **Attributes**:
  - Data Types and Quantities required.
    - some amount of data of whichever modalities required to train the model 
  - Training Compute Cost (multi-turn commitment).
    - some volume of training data tokens, compute clusters complexity determines rate at which data can be organized into trained model
  - Inference Compute minimum commitment (e.g. RAM). volume of model output proportional to committed compute.
  - Open Source Status.
    - once an open model is trained, any user can commit compute to it to generate resources.
    - closed models can still be used by other players, but they have to pay capital to whoever owns the compute that is "serving" the model
    - open source models boost influence more, both reach and reputation.
    - both open source models and closed models generate capital.
    - closed models don't generate influence until they've been upgraded to "experimental" status, or whatever the top of the skill tree is for AI model upgrade progression.
  - Upgradability.
  - Unique Special Effects based on Data Modalities.

- **Functionality**:
  - Consumes Compute, Produces Capital and Data.
  - "Shipping" a model increases Influence.
  - Influence realized through utilization, grows quadratically with model size.

- **Types**:
  - Open Source (Greater Influence boost).
  - Closed (Capital generation; Influence post-upgrade).

**playtesting notes**

models can be distributed as cards from the deck. the card isn't the model: it's a training recipe.

a given model card is accompanied by a data cost, expressed in terms of minimum requirements for certain modalities and an overall minimum cardinality

a model is a configuration of data, arranged by paying a compute cost. 

each model has a RAM, determining max throughput. "throughput" =in training, # compute units that can be dedicated to the model per batch (or... something. some kind of throttle on model building)

to upgrade a model, cost must be paid in multiples of the "dataset" (maintaining original data:modality proportions as you scale up)


building a model of a given size doesn't give you influence immediately. the size of the model dictates its maximum "carrying capacity" for influence, but you only actually get that influence through use. this is part of why users are incentivized to publish public models: public models have more opportunity to be used and to carry influence points for the model's owner.

carrying capacity for influence grows quadratically with model size to incentivize players building larger (i.e. more complex) models rather than just building lots of small models (which may still be an effective strategy

a model can only realize its influence by being utilized, so players are incentivized to release public models to give them more opportunity to be used

some single model or small set of models is granted "SOTA" status. for now, let's say the single largest/most complex model on the table, and the number of SOTA models could scale with the number of players. the current SOTA model generates outputs faster than all the other models, let's say generates 50% more data/influence per inference. this incentivizes players to chase SOTA and to use other players' models (if other players own the current SOTA).

---

# IV. Game Mechanics

1. **Factions**
   - Associated with private goals.
   - thematically align with specific AI development philosophies or sectors

3. **Personas**
   - associated with special abilities.

4. **Ethical Dilemmas**
   - Challenges that impact reputation (major component of Influence) based on choices.
   - use influence for "victory points" mechanism.

5. **Model Crafting and Upgrades**
   - Combining Data and Compute resources to create AI models.
   - Maintain data:modality proportions in upgrades.
   - "Joining" datasets for larger models.

6. **Data and Compute Management**
   - Player-driven economy for resource trading.
   - Public vs. Private Data Lakes for storage and strategy.
   - Compute management with racking/networked clusters.
   - Compute homogeneity in clusters for efficiency.

7. **SOTA Model Mechanic**
   - Rewards for holding the SOTA model status.
   - SOTA models have enhanced output generation.

8. **Periodic Compute Generation Milestones**
   - Impact on compute availability and strategy.

9. **Compute Rental Concept**
   - Compute is rented, not owned; strategic management of compute rental.

---

# V. Satirical Elements

- Satirical references include AI influencers, AGI doomerism, safety researchers, data annotation quirks, open source culture, and specific AI theories/personalities.

---

# VI. Playtesting Notes

- **Model Cards**: Represent AI model training recipes.
- **Data Cost**: Specific to each model, with minimum requirements for modalities and overall data.
- **Data Generation**: Raw data generated by Compute committed to models.
- **Refining Data**: Can be a card effect or player action; ties into modalities and data strategies.
- **Data Lakes and Model Registries**: Players' uncommitted data ("Data Lake") and assembled models ("Model Registry").
- **Influence Accumulation**: Depends on model size and usage; larger models have higher "carrying capacity" for influence.
- **Late Game Objectives**: Focus on building advanced models, chasing SOTA status, and accumulating influence.



early game: acquire capital to secure compute

mid game: build artifacts to gain reputation

late game: leverage reputation to build advanced artifacts (which require some threshold reputation to be developed), chase SOTA (associated with a reach bonus), accumulate influence

---

# VII. Additional Mechanics and Concepts

- **Hardware Resource**: Needed for compute/data upgrading and structuring.
- **Compute Scaling**: Both horizontal and vertical scaling dynamics.
- **Public Compute Clusters**: Can be developed, rented, or reserved by players.
- **Extra Point Objectives**: Awarded for controlling the most advanced compute cluster or the current SOTA model.


extra point objectives similar to longest road/largest army in catan
- player who controls current SOTA artifact
- player who controls most powerful/advanced compute cluster


---
---


