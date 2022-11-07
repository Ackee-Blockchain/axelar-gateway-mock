//SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@axelar-network/axelar-gmp-sdk-solidity/contracts/interfaces/IAxelarExecutable.sol";
import "@axelar-network/axelar-gmp-sdk-solidity/contracts/interfaces/IERC20MintableBurnable.sol";
import "@axelar-network/axelar-gmp-sdk-solidity/contracts/StringAddressUtils.sol";

interface IAxelarGatewayMock {
    function chainId() external view returns (string memory);

    function executeSendToken(
        string calldata destinationAddress,
        string calldata symbol,
        uint256 amount
    ) external;

    function executeCallContract(
        string calldata sourceChain,
        string calldata contractAddress,
        string calldata sender,
        bytes calldata payload
    ) external;

    function executeCallContractWithToken(
        string calldata sourceChain,
        string calldata contractAddress,
        string calldata sender,
        bytes calldata payload,
        string calldata symbol,
        uint256 amount
    ) external;
}

contract AxelarGatewayMock is IAxelarGatewayMock {
    using StringToAddress for string;
    using AddressToString for address;

    string public override chainId;
    mapping(string => IAxelarGatewayMock) otherChains;
    mapping(string => IERC20MintableBurnable) tokens;

    constructor(string memory chain) {
        chainId = chain;
    }

    function registerChain(IAxelarGatewayMock gateway) external {
        require(keccak256(abi.encode(gateway.chainId())) != keccak256(abi.encode(chainId)), "CHAIN_ALREADY_REGISTERED");
        otherChains[gateway.chainId()] = gateway;
    }

    function registerToken(string calldata symbol, IERC20MintableBurnable token) external {
        require(address(token) != address(0), "INVALID_TOKEN_ADDRESS");
        require(address(tokens[symbol]) == address(0), "TOKEN_ALREADY_REGISTERED");
        tokens[symbol] = token;
    }

    function sendToken(
        string calldata destinationChain,
        string calldata destinationAddress,
        string calldata symbol,
        uint256 amount
    ) external {
        require(keccak256(abi.encode(destinationChain)) != keccak256(abi.encode(chainId)), "SENT_TO_WRONG_CHAIN");

        IAxelarGatewayMock destinationGateway = otherChains[destinationChain];
        require(address(destinationGateway) != address(0), "CHAIN_NOT_REGISTERED");

        IERC20MintableBurnable sourceToken = tokens[symbol];
        require(address(sourceToken) != address(0), "TOKEN_NOT_REGISTERED");

        require(sourceToken.balanceOf(msg.sender) >= amount, "INSUFFICIENT_BALANCE");
        require(sourceToken.allowance(msg.sender, address(this)) >= amount, "INSUFFICIENT_ALLOWANCE");
        sourceToken.burn(msg.sender, amount);
        destinationGateway.executeSendToken(destinationAddress, symbol, amount);
    }

    function executeSendToken(string calldata destinationAddress, string calldata symbol, uint256 amount) external {
        IERC20MintableBurnable destinationToken = tokens[symbol];
        require(address(destinationToken) != address(0), "TOKEN_NOT_REGISTERED");

        destinationToken.mint(destinationAddress.toAddress(), amount);
    }

    function callContract(
        string calldata destinationChain,
        string calldata contractAddress,
        bytes calldata payload
    ) external {
        require(keccak256(abi.encode(destinationChain)) != keccak256(abi.encode(chainId)), "SENT_TO_WRONG_CHAIN");

        IAxelarGatewayMock destinationGateway = otherChains[destinationChain];
        require(address(destinationGateway) != address(0), "CHAIN_NOT_REGISTERED");

        destinationGateway.executeCallContract(chainId, contractAddress, msg.sender.toString(), payload);
    }

    function executeCallContract(
        string calldata sourceChain,
        string calldata contractAddress,
        string calldata sender,
        bytes calldata payload
    ) external {
        IAxelarExecutable(contractAddress.toAddress()).execute(
            bytes32(0),
            sourceChain,
            sender,
            payload
        );
    }

    function callContractWithToken(
        string calldata destinationChain,
        string calldata contractAddress,
        bytes calldata payload,
        string calldata symbol,
        uint256 amount
    ) external {
        require(keccak256(abi.encode(destinationChain)) != keccak256(abi.encode(chainId)), "SENT_TO_WRONG_CHAIN");

        IAxelarGatewayMock destinationGateway = otherChains[destinationChain];
        require(address(destinationGateway) != address(0), "CHAIN_NOT_REGISTERED");

        IERC20MintableBurnable sourceToken = tokens[symbol];
        require(address(sourceToken) != address(0), "TOKEN_NOT_REGISTERED");

        sourceToken.burn(msg.sender, amount);
        destinationGateway.executeCallContractWithToken(chainId, contractAddress, msg.sender.toString(), payload, symbol, amount);

    }

    function executeCallContractWithToken(
        string calldata sourceChain,
        string calldata contractAddress,
        string calldata sender,
        bytes calldata payload,
        string calldata symbol,
        uint256 amount
    ) external {
        IERC20MintableBurnable destinationToken = tokens[symbol];
        require(address(destinationToken) != address(0), "TOKEN_NOT_REGISTERED");

        address contractAddr = contractAddress.toAddress();
        destinationToken.mint(contractAddr, amount);

        IAxelarExecutable(contractAddr).executeWithToken(
            bytes32(0),
            sourceChain,
            sender,
            payload,
            symbol,
            amount
        );
    }

    function isContractCallApproved(
        bytes32 commandId,
        string calldata sourceChain,
        string calldata sourceAddress,
        address contractAddress,
        bytes32 payloadHash
    ) external view returns (bool) {
        return true;
    }

    function isContractCallAndMintApproved(
        bytes32 commandId,
        string calldata sourceChain,
        string calldata sourceAddress,
        address contractAddress,
        bytes32 payloadHash,
        string calldata symbol,
        uint256 amount
    ) external view returns (bool) {
        return true;
    }

    function validateContractCall(
        bytes32 commandId,
        string calldata sourceChain,
        string calldata sourceAddress,
        bytes32 payloadHash
    ) external returns (bool) {
        return true;
    }

    function validateContractCallAndMint(
        bytes32 commandId,
        string calldata sourceChain,
        string calldata sourceAddress,
        bytes32 payloadHash,
        string calldata symbol,
        uint256 amount
    ) external returns (bool) {
        return true;
    }
}