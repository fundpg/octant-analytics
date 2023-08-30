import requests

# Step 1: Get all validator indexes belonging to 0x4f80Ce44aFAb1e5E940574F135802E12ad2A5eF0
result = requests.get('https://beaconcha.in/api/v1/validator/eth1/0x4f80Ce44aFAb1e5E940574F135802E12ad2A5eF0')
validatorIndexes = []
for r in result.json()['data']:
    validatorIndexes.append(r['validatorindex'])

print(len(validatorIndexes))

# Step 2: Get validator statistics and extract out the end balance of the most recent day
totalBalance = 0
for validator in validatorIndexes:
    result = requests.get('https://beaconcha.in/api/v1/validator/stats/' + str(validator))
    totalBalance += result.json()['data'][0]['end_balance']
print(totalBalance)