🚧 🚧 **Work In Progress** 🚧 🚧

Working Name: AI Assembly

# Structured High Level Notes

## Resources

* Capital
  * can be exchanged for other resources
  * can be used to purchase outputs or effects from hosted models
* Compute
  * capital can be exchanged for compute
* Data
  * raw -> refined
    * refined data is worth more or has enhanced effect on model training
  * types by modality: text, image, other
  * could refer to units of data as "tokens"
  * capital can be exchanged for data
* influence
  * reputation (h-index, ethical points)
  * reach (followers)
  * capital can be exchanged for reach
  * influence is treated as a resource
  * ending the game with the most influence could be a win condition or private goal.
    * actually, this works for any resource

Capital can be used to purchase compute, data, and influence (just reach, not reputation).

Compute and data are required inputs for crafting "models". refined data is worth extra, less data required for training when refined than when raw

Models consume compute and produce capital and data. "shipping" a model increases influence (definitely reputation... reach too)

## Models

Models have the following attributes
* data types and quantities: some amount of data of whichever modalities required to train the model
* training compute cost: paying down the compute cost for training a model should take several turns. when the compute cost is paid down, the model has been "trained"
* inference compute cost: a model can only be used to produce resources if the user has committed compute to the model, and the amount of output the model generates is proportional to the committed compute.
* open source or not: once an open model is trained, any user can commit compute to it to generate resources. closed models can still be used by other players, but they have to pay capital to whoever owns the compute that is "serving" the model
* open source models boost influence more, both reach and reputation.
* both open source models and closed models generate capital. closed models don't generate influence until they've been upgraded to "experimental" status, or whatever the top of the skill tree is for AI model upgrade progression.
* models are upgradeable


## Misc Mechanics

* factions -> private goals
* personas -> special abilities
* ethical dilemmas -> reputation

maybe "reputation" can be the "victory points" equivalent? or maybe some function of reputation and reach, so "whoever ends the game with the most influence wins". that tracks.

## things/people to satirize

* ai influencers
* e/acc
* decel
* EY
* agi doomerism
* x-risk
* safety researchers
* capabees
* geese
* schmidhuber
* gary marcus/brick wall
* data annotation
* duplicated data
* copyright
* fair use
* data laundering
* license laundering
* open source
* independent researchers
* notebook/demo coders
* neuroatypicality
* degens
* deepfakes
* misinformation
* glaze/nightshade
  - lol, could be a card that doesn't do anything.
  - event card: -2 reputation, +1 reach
* denoising diffusion
* vae
* low quality research code
* remote work
  * "Return-To-Office" could be a negative event
* mental health
  * burnout
  * self-care
* 10x developers

# Playtesting notes

models can be distributed as cards from the deck. the card isn't the model: it's a training recipe.

a given model card is accompanied by a data cost, expressed in terms of minimum requirements for certain modalities and an overall minimum cardinality

a model is a configuration of data, arranged by paying a compute cost. 

each model has a RAM, determining max throughput. "throughput" =in training, # compute units that can be dedicated to the model per batch (or... something. some kind of throttle on model building)

to upgrade a model, cost must be paid in multiples of the "dataset" (maintaining original data:modality proportions as you scale up)

compute committed to trained models generates raw data.

upgraded models can generate refined data and/or refine raw data.

alternatively, "refine" could be a card effect, or something the player always has the option to do (e.g. mechanical turk)
  - tying refinement to cards also makes it so we can control the relative distribution/value of different modalities.
  - we want at least one modality to be particularly rare or costly relative to the others to drive a player economy (trading, strategizing) 
    - users can build strategies aiming at certain modalities
    - some chosen modality -> refinement favors data of that modality -> strategy focuses on building models tied to that modality
      - modalities could characterize different model special effects?

users available uncommitted data could be refferred to as their "data lake". assembled models could be housed in their "model registry", or "production" <- productionize models

refining data = assigning a modality.

additionalpotential modalities:
  - user activity/telemetry

computecan be subject to homogeneity compatibility. compute units can be combined into upgraded compute (level 1,2,3), but if paying a compute cost the compute will "parallelize" and be bottlenecked by the lowest level of compute in the "cluster".

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

data is similarly combined as the upgrading procedure when building models, which gives the dataset/model a "level" in terms of plate height units as well, which determines compute compatibility for training/inference

model training could have a minimum batch size. part of the data refinement mechanism could be combining data units of the same modelity into larger data sets (2x2 plate green -> 2x4 green plate)

late game models have higher minimum batch size, forcing players to construct (upgrade their data into) larger datasets.
* larger datasets constructed by "joining" datasets (literally, lol). data upgrade can be an effect similar to compute upgrade

add a new construction resource, e.g. "hardware" - plates consumed when upgrading
* "joining" datasets - date upgrade mechanic!
* orchestrating compute into "networked" clusters
