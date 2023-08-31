# Ethereum
from web3 import Web3
import requests
import json

moralis_node = Web3.WebsocketProvider('wss://mainnet.infura.io/ws/v3/INSERT_API_KEY')
moralis = Web3(moralis_node)

def getTxnReceipt(tid):
    url = f"https://api.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash={tid}&apikey="
    response = requests.request("GET", url)
    return response.json()["result"]

def getABI(cid):
    url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={cid}&apikey="
    response = requests.request("GET", url)
    return response.json()["result"]    

def initialise(cid):
    abi = getABI(cid)
    contract = moralis.eth.contract(address=moralis.to_checksum_address(cid), abi=abi)
    return contract

mycontract = initialise("0x879133Fd79b7F48CE1c368b0fCA9ea168eaF117c")
myfilter = mycontract.events.Locked.create_filter(fromBlock=0, toBlock='latest')
eventlist = myfilter.get_all_entries()
print(eventlist)

# {'fromBlock': 0,'toBlock': 'latest'}