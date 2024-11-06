from web3 import Web3
from Deploy import deploy_contract
import os


contract = "SimpleStorage.sol"
account = os.getenv("ACCOUNT")
private_key = os.getenv("PRIVATE_KEY")
provider = os.getenv("LOCAL_PROVIDER")

chain_id = os.getenv("CHAIN_ID")
    
connection = Web3(Web3.HTTPProvider(provider))
contract_address, abi = deploy_contract(contract, "SimpleStorage", account, private_key, provider, chain_id)

# contract_address, abi = deploy_contract("SimpleStorage.sol", "SimpleStorage", "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266", "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80", "HTTP://127.0.0.1:8545", 31337)

simple_storage = connection.eth.contract(address=contract_address, abi = abi)
nonce = connection.eth.get_transaction_count(account)

transaction = simple_storage.functions.set(150005647).build_transaction(
    {
            "chainId":chain_id,
            "gasPrice":connection.eth.gas_price,
            "from":account,
            "nonce":nonce
    }
)

signed_txn = connection.eth.account.sign_transaction(transaction, private_key = private_key)
print("Updated sotred value ")
tx_hash = connection.eth.send_raw_transaction(signed_txn.raw_transaction)

tx_receipt = connection.eth.wait_for_transaction_receipt(tx_hash)
print("Updated")

updated_value = simple_storage.functions.get().call()
print("Updated value" , updated_value) 