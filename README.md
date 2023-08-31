### Background: 
Octant has a novel mechanism that increases the amount of public goods funding available as you lock more GLM. 

This funding has been generously given by the Golem Foundation through a % of their total validator rewards from a 100,000 ETH stake in their validator. 

During an Epoch, users are able to freely lock and unlock their GLM which changes their contribution towards the total funding given to Octant from the validators. 

### Problem: 
The way rewards are calculated is not straightforward, making users unsure about how their actions directly relate to their contributions.  

As a result, users may be: 
1) Less likely to lock GLM as they are not able to directly see the effects of their contribution.
2) More likely to unlock their GLM as they are not able to understand how it might reduce the contribution.

### Solution: 
Our solution goes beyond just the metrics themselves, it is a design proposal for Octant to adopt to subtly nudge user behavior towards our desired outcome of increasing public goods funding. 

Effectively, this solution relies on two metrics. 
1. How much rewards their locked GLM will contribute at the end of the Epoch 
2. How much potential rewards would be lost by unlocking a user-specified amount

These metrics should be implemented as pop-up modals in the Octant frontend. 
1. Upon locking a specified amount, users should be able to visualize exactly how their contribution impacts the funding.
2. While attempting to unlock GLM, users should be shown how their action would reduce funding.

### Impact:
We believe that our solution will increase the amount of GLM user's stake as they are able to understand the impact of their contributions more easily. Furthermore, it would also decrease the likelihood of users unlocking their stake as they can understand the potential rewards lost by doing so. 

Effectively, this will increase the total amount of public goods funding in Octant.

### Challenges
We were initially intending to build a custom event listener to index the Lock and Unlock events. However, due to the design of the smart contract, the events being emitted do not have any indexes, making it impractical for the original design of our event listener. 

In digging through the Octant codebase, we saw that metric #1 of displaying the user's rewards has already been [implemented as backend code that works through querying the subgraph](https://gitlab.com/wildland/governance/octant/-/blob/master/backend/app/core/rewards.py), even though this is not yet implemented into the Octant frontend. 

Hence, we decided to focus on metric #2 and built a proof-of-concept using Dune analytics to get the data, and a Figma prototype to illustrate how this might be integrated into the Octant app as a pop-up modal. 

### Future Work
We intend to support showing the estimated matched rewards before an Epoch ends. This gives an even more realistic idea of the benefits or costs associated with locking and unlocking GLM. 
