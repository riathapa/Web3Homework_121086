//SPDX-License-Identifier: MIT
pragma solidity 0.8.13;

contract SimpleStorage{

    //State Variable
    uint256 public data;

    function set(uint256 _data) public {
        data = _data;
    }

    function get() public view returns (uint256){
        return data;
    }
}