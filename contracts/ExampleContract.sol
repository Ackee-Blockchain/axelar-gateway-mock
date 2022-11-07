//SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@axelar-network/axelar-gmp-sdk-solidity/contracts/executables/AxelarExecutable.sol";
import "@axelar-network/axelar-gmp-sdk-solidity/contracts/interfaces/IERC20.sol";

contract ExampleContract is AxelarExecutable {
    constructor (address gateway) AxelarExecutable(gateway) {}

    struct Message {
        string sourceChain;
        string sourceAddress;
        bytes payload;
        string tokenSymbol;
        uint256 tokenAmount;
    }

    Message public lastMessage;

    function send(
        string calldata destinationChain,
        string calldata destinationAddress,
        bytes calldata payload
    ) external {
        gateway.callContract(destinationChain, destinationAddress, payload);
    }

    function sendWithToken(
        string calldata destinationChain,
        string calldata destinationAddress,
        bytes calldata payload,
        IERC20 token,
        string calldata symbol,
        uint256 amount
    ) external {
        require(token.approve(address(gateway), amount), "APPROVE_FAILED");
        gateway.callContractWithToken(destinationChain, destinationAddress, payload, symbol, amount);
    }

    function _execute(
        string calldata sourceChain,
        string calldata sourceAddress,
        bytes calldata payload
    ) internal override {
        lastMessage = Message(sourceChain, sourceAddress, payload, "", 0);
    }

    function _executeWithToken(
        string calldata sourceChain,
        string calldata sourceAddress,
        bytes calldata payload,
        string calldata tokenSymbol,
        uint256 amount
    ) internal override {
        lastMessage = Message(sourceChain, sourceAddress, payload, tokenSymbol, amount);
    }
}