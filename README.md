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
* parallelization strategies
  * model parallel
  * data parallel
  * tensor parallel
  * zero offload/infinity
  * k8s/knative/serverless
* x is all you need
  * transformers/scaling/diffusion/vae/skip connections/dropout/more layers
* scaling laws

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

data could have a "sensitivity" attribute, such that high value data like PII could be modeled as "high sensitivity" data which is only available to players with above some threshold reputation (or "ethics points" or whatever). higher data sensitivity correlates with higher capital generation from models built with that data


data could be easy to generate but hard to store. a player's private "data lake" is something they can invest in to increase their storage capacity, but if they want to train a model that requires more data than they can store, they have to use public data and make the model public. conversely, they can donate data to the public lake (nom-sensitive data only) for a benefit of some kind, like a small gain in influence. so if a user doesn't grow their lake, they can't train large private models and will be incentivized to contribute to the public data pool.

building a model of a given size doesn't give you influence immediately. the size of the model dictates its maximum "carrying capacity" for influence, but you only actually get that influence through use. this is part of why users are incentivized to publish public models: public models have more opportunity to be used and to carry influence points for the model's owner.

carrying capacity for influence grows quadratically with model size to incentivize players building larger (i.e. more complex) models rather than just building lots of small models (which may still be an effective strategy

a model can only realize its influence by being utilized, so players are incentivized to release public models to give them more opportunity to be used

some single model or small set of models is granted "SOTA" status. for now, let's say the single largest/most complex model on the table, and the number of SOTA models could scale with the number of players. the current SOTA model generates outputs faster than all the other models, let's say generates 50% more data/influence per inference. this incentivizes players to chase SOTA and to use other players' models (if other players own the current SOTA).

early game: acquire capital to secure compute

mid game: build artifacts to gain reputation

late game: leverage reputation to build advanced artifacts (which require some threshold reputation to be developed), chase SOTA (associated with a reach bonus), accumulate influence

limitless public data, private/sensitive data must be purchased

structuring compute = "racking"/"interconnect" -> horizontal scaling

horizontal scaling requires "racking": joining pairs of compute units into "clusters". racking consumes "hardware" units. maybe some threshold max scaling? limited by compute generation?

periodic milestone (every k rounds, maybe triggered by certain cards distributed in the deck or player achievements): "compute generation" increments. 

when the "compute generation" increments, everyone's compute scales down one unit vertically
- oldest compute gets retired/bricked/sold on aftermarket (exchanged for capital, reduced relative to original purchase price)
- keep users purchasing latest generation compute if they want to be able to train/inference the SOTA

vertical scaling needs to be "parallel". if compute is assigned to a cluster, the entire cluster needs to scale together. otherwise, the cluster can be broken apart to only scale fewer compute units at a time, but the user doesn't get that hardware back and needs to pay again to re-integrate the upgraded compute units to the cluster. a given compute cluster needs to be *homogeneous* relative to its compute units.

grey plates = "hardware"/"structure" units.
- need structured compute to operate on structured data
- structured data + structured compute --> satisfy requirements for "dense" models. model density correlates with influence capacity, SOTA scoring, model performance, etc.

extra point objectives similar to longest road/largest army in catan
- player who controls current SOTA artifact
- player who controls most powerful/advanced compute cluster

compute clusters are public resources. a player owns the compute cluster they develop, but other players can still use reserve and use space on their cluster at market price. the owner of the cluster can expend additional resources to define a "reserved" portion of the cluster that is exclusive to them

alternatively: compute only lives in cloud. as such, compute can't be purchased, only rented. if you can't pay rent on your compute, it is released back to cloud availability for other users to rent on demand or to "purchase" (rent on reserve).

limited compute incentivizes players to share models -> i can't use my compute to train bigger models if you're using my compute to inference my models
