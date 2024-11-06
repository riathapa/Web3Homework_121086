from web3 import Web3
from Compile import Compile_Solidity
from typing import Tuple
import os



def deploy_contract(contract:str, contract_name:str, account:str, private_key:str, provider:str, chain_id: int): 
    print("Contract Name :" , contract_name)
    print("Account :" , account)
    print("Private_key:" , private_key)
    print("Chain Id :" , chain_id)
    
    compiled_sol = Compile_Solidity(contract)

    #Get the ABI and Byte code
    abi = compiled_sol["contracts"][contract][contract_name]["abi"]
    byte_code = compiled_sol["contracts"][contract][contract_name]["evm"]["bytecode"]["object"]
    
    connection = Web3(Web3.HTTPProvider(provider))
    print("Hello")
    contract = connection.eth.contract(abi=abi, bytecode=byte_code)
    print("22342")
    nonce = connection.eth.get_transaction_count(account)


    transaction = contract.constructor().build_transaction(
        {
            "chainId":chain_id,
            "gasPrice":connection.eth.gas_price,
            "from":account,
            "nonce":nonce
        }
    )

    signed_txn = connection.eth.account.sign_transaction(transaction, private_key = private_key)

    tx_hash = connection.eth.send_raw_transaction(signed_txn.raw_transaction)

    tx_receipt = connection.eth.wait_for_transaction_receipt(tx_hash)
    return (tx_receipt.contractAddress, abi)
