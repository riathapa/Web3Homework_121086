from solcx import compile_standard
import json
SOLIDITY_PRAGMA = "0.8.13"

def Compile_Solidity(contract: str) -> str :
    with open("src/SimpleStorage.sol", "r") as file:
        simple_storage_file = file.read()

    compiled_sol = compile_standard(
        {
         "language":"Solidity",
            "sources":{
                "SimpleStorage.sol" : {
                    "content": simple_storage_file
                    }
                },
            "settings" : {
                "outputSelection" : {
                    "*" : {
                        "*": ["abi", "evm.bytecode"]
                    }
                }
            }
        },
        solc_version = SOLIDITY_PRAGMA
    )
    return compiled_sol

def main():
    compiled_sol = Compile_Solidity("src/SimpleStorage.sol")
    with open("Compiled/SimpleStorage.json","w") as file:
        json.dump(compiled_sol, file)

main()