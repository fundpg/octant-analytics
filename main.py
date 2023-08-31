import requests
from web3 import Web3


# A: Get the user deposit by calling get_users_deposits(epochNumber) function which can be found at https://gitlab.com/wildland/governance/octant/-/blob/master/backend/app/core/deposits/deposits.py
def getUserDeposit():
    userDeposits = get_users_deposits(epochNumnber)
    return userDeposits

# B: Get the GLM total supply
def getGLMTotalSupply():
    socket = Web3.WebsocketProvider('wss://mainnet.infura.io/ws/v3/INSERT_API_KEY')
    node = Web3(socket)
    contract = node.eth.contract(address='0x7DD9c5Cba05E151C895FDe1CF355C9A1D5DA6429', abi=abi)
    glmTotalSupply = contract.functions.totalSupply().call()
    return glmTotalSupply

# C: Get the estimated yield during epoch
def getEstimatedYieldDuringEpoch(): 
    # Get all validator indexes belonging to 0x4f80Ce44aFAb1e5E940574F135802E12ad2A5eF0
    result = requests.get('https://beaconcha.in/api/v1/validator/eth1/0x4f80Ce44aFAb1e5E940574F135802E12ad2A5eF0')
    validatorIndexes = []
    for r in result.json()['data']:
        validatorIndexes.append(r['validatorindex'])

    # Get validator statistics and get the moving 90-day average rewards for each validator, then get the moving 90-day average for all validators. 
    estimatedYieldDuringEpoch = 0
    for validator in validatorIndexes:
        result = requests.get('https://beaconcha.in/api/v1/validator/stats/' + str(validator))
        averageRewardsForOneValidator = (result.json()['data'][0]['end_balance'] - result.json()['data'][90]['end_balance'])  / 90
        estimatedYieldDuringEpoch += averageRewardsForOneValidator / len(validatorIndexes)

    return estimatedYieldDuringEpoch

# Metric 1: How much rewards their locked GLM will contribute at the end of the Epoch
# User rewards = GLM locked by user during epoch / total supply of GLM * yield generated during epoch
def getUserRewards():
    return getUserDeposit() / getGLMTotalSupply() * getEstimatedYieldDuringEpoch() 

# Metric 2: How much potential rewards would be lost by unlocking a user-specified amount
def getLossInRewards(unlock_amount):
    return unlock_amount  / getGLMTotalSupply() * getEstimatedYieldDuringEpoch() 
