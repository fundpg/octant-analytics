# Problem: 
Octant has a novel mechanism which increases the amount of public goods funding available as you lock more GLM. 

This funding has been generously given by the Golem Foundation through a % of their total validator rewards from a 100,000 ETH stake in their validator. 

However, due to the complex nature of this mechanism, users are unsure about how much they are truly contributing towards the total funding given to Octant. 

As a result, users may be less likely to donate as they are not able to directly see the effects of their contribution.

# Solution: 
We have created a way for users to visualize their impact through 2 metrics. 
1. How much additional rewards their locked GLM has already contributed towards
2. How much additional rewards their locked GLM would contribute towards if they hold till the end of the Epoch / how much rewards is lost by unlocking their GLM.

# Impact:
We believe that our solution will increase the amount of GLM users stake as they are able to understand the impact of their contributions more easily. Furthermore, it would also decrease the likelihood of users unlocking their stake as they can understand the potential rewards lost by doing. 

Effectively, this will increase the total amount of public goods funding in Octant.

# Challenges
We were initially intending to build a custom event listener to index the Lock and Unlock events. However, due to the design of the smart contract, the events being emitted do not have any indexes, making it impractical for the original design of our event listener. 
