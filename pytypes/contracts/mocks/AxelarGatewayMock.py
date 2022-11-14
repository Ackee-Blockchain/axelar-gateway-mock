from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.contract import Contract, Library, TransactionObject, Address, Wei

from woke.testing.abi_to_type import RequestType
from enum import IntEnum

from pytypes.axelarnetwork.axelargmpsdksolidity.contracts.interfaces.IERC20MintableBurnable import IERC20MintableBurnable

from woke.testing.primitive_types import bytes32
from woke.testing.primitive_types import uint256


class IAxelarGatewayMock(Contract):
    _abi = {b'\x9a\x8a\x05\x92': {'inputs': [], 'name': 'chainId', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x99\xda~\t': {'inputs': [{'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'contractAddress', 'type': 'string'}, {'internalType': 'string', 'name': 'sender', 'type': 'string'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}], 'name': 'executeCallContract', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf5V\xab\xd1': {'inputs': [{'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'contractAddress', 'type': 'string'}, {'internalType': 'string', 'name': 'sender', 'type': 'string'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}, {'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'executeCallContractWithToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xcd\xdf\x86\x97': {'inputs': [{'internalType': 'string', 'name': 'destinationAddress', 'type': 'string'}, {'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'executeSendToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _bytecode = ""

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max") -> IAxelarGatewayMock:
        raise Exception("Cannot deploy interface")

    @overload
    def chainId(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> str:
        ...

    @overload
    def chainId(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def chainId(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[str, TransactionObject]:
        """
        Returns:
            string
        """
        return self._transact("9a8a0592", [], return_tx, request_type, str, from_, to, value, gas_limit) if not request_type == 'call' else self._call("9a8a0592", [], return_tx, str, from_, to, value, gas_limit)

    @overload
    def executeSendToken(self, destinationAddress: str, symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def executeSendToken(self, destinationAddress: str, symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def executeSendToken(self, destinationAddress: str, symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            destinationAddress: string
            symbol: string
            amount: uint256
        """
        return self._transact("cddf8697", [destinationAddress, symbol, amount], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("cddf8697", [destinationAddress, symbol, amount], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def executeCallContract(self, sourceChain: str, contractAddress: str, sender: str, payload: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def executeCallContract(self, sourceChain: str, contractAddress: str, sender: str, payload: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def executeCallContract(self, sourceChain: str, contractAddress: str, sender: str, payload: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            sourceChain: string
            contractAddress: string
            sender: string
            payload: bytes
        """
        return self._transact("99da7e09", [sourceChain, contractAddress, sender, payload], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("99da7e09", [sourceChain, contractAddress, sender, payload], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def executeCallContractWithToken(self, sourceChain: str, contractAddress: str, sender: str, payload: Union[bytearray, bytes], symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def executeCallContractWithToken(self, sourceChain: str, contractAddress: str, sender: str, payload: Union[bytearray, bytes], symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def executeCallContractWithToken(self, sourceChain: str, contractAddress: str, sender: str, payload: Union[bytearray, bytes], symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            sourceChain: string
            contractAddress: string
            sender: string
            payload: bytes
            symbol: string
            amount: uint256
        """
        return self._transact("f556abd1", [sourceChain, contractAddress, sender, payload, symbol, amount], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("f556abd1", [sourceChain, contractAddress, sender, payload, symbol, amount], return_tx, type(None), from_, to, value, gas_limit)

class AxelarGatewayMock(IAxelarGatewayMock):
    _abi = {'constructor': {'inputs': [{'internalType': 'string', 'name': 'chain', 'type': 'string'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\x1c\x92\x11_': {'inputs': [{'internalType': 'string', 'name': 'destinationChain', 'type': 'string'}, {'internalType': 'string', 'name': 'contractAddress', 'type': 'string'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}], 'name': 'callContract', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb5Ap\x84': {'inputs': [{'internalType': 'string', 'name': 'destinationChain', 'type': 'string'}, {'internalType': 'string', 'name': 'contractAddress', 'type': 'string'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}, {'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'callContractWithToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x9a\x8a\x05\x92': {'inputs': [], 'name': 'chainId', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x99\xda~\t': {'inputs': [{'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'contractAddress', 'type': 'string'}, {'internalType': 'string', 'name': 'sender', 'type': 'string'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}], 'name': 'executeCallContract', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf5V\xab\xd1': {'inputs': [{'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'contractAddress', 'type': 'string'}, {'internalType': 'string', 'name': 'sender', 'type': 'string'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}, {'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'executeCallContractWithToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xcd\xdf\x86\x97': {'inputs': [{'internalType': 'string', 'name': 'destinationAddress', 'type': 'string'}, {'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'executeSendToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xbc\x00\xc2\x16': {'inputs': [{'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'sourceAddress', 'type': 'string'}, {'internalType': 'address', 'name': 'contractAddress', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'payloadHash', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'isContractCallAndMintApproved', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xf6\xa5\xf9\xf5': {'inputs': [{'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'sourceAddress', 'type': 'string'}, {'internalType': 'address', 'name': 'contractAddress', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'payloadHash', 'type': 'bytes32'}], 'name': 'isContractCallApproved', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc5\xd1N\x07': {'inputs': [{'internalType': 'contract IAxelarGatewayMock', 'name': 'gateway', 'type': 'address'}], 'name': 'registerChain', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'i\xf6g\xed': {'inputs': [{'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'internalType': 'contract IERC20MintableBurnable', 'name': 'token', 'type': 'address'}], 'name': 'registerToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'&\xefi\x9d': {'inputs': [{'internalType': 'string', 'name': 'destinationChain', 'type': 'string'}, {'internalType': 'string', 'name': 'destinationAddress', 'type': 'string'}, {'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'sendToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'_ip\xc3': {'inputs': [{'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'sourceAddress', 'type': 'string'}, {'internalType': 'bytes32', 'name': 'payloadHash', 'type': 'bytes32'}], 'name': 'validateContractCall', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x18v\xee\xd9': {'inputs': [{'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'sourceAddress', 'type': 'string'}, {'internalType': 'bytes32', 'name': 'payloadHash', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'validateContractCallAndMint', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _bytecode = "60806040523480156200001157600080fd5b50604051620022423803806200224283398101604081905262000034916200010d565b80516200004990600090602084019062000051565b505062000226565b8280546200005f90620001e9565b90600052602060002090601f016020900481019282620000835760008555620000ce565b82601f106200009e57805160ff1916838001178555620000ce565b82800160010185558215620000ce579182015b82811115620000ce578251825591602001919060010190620000b1565b50620000dc929150620000e0565b5090565b5b80821115620000dc5760008155600101620000e1565b634e487b7160e01b600052604160045260246000fd5b600060208083850312156200012157600080fd5b82516001600160401b03808211156200013957600080fd5b818501915085601f8301126200014e57600080fd5b815181811115620001635762000163620000f7565b604051601f8201601f19908116603f011681019083821181831017156200018e576200018e620000f7565b816040528281528886848701011115620001a757600080fd5b600093505b82841015620001cb5784840186015181850187015292850192620001ac565b82841115620001dd5760008684830101525b98975050505050505050565b600181811c90821680620001fe57607f821691505b602082108114156200022057634e487b7160e01b600052602260045260246000fd5b50919050565b61200c80620002366000396000f3fe608060405234801561001057600080fd5b50600436106100cf5760003560e01c80639a8a05921161008c578063c5d14e0711610066578063c5d14e07146101b4578063cddf8697146101c7578063f556abd1146101da578063f6a5f9f5146101ed57600080fd5b80639a8a05921461016e578063b541708414610183578063bc00c2161461019657600080fd5b80631876eed9146100d45780631c92115f1461010657806326ef699d1461011b5780635f6970c31461012e57806369f667ed1461014857806399da7e091461015b575b600080fd5b6100f16100e23660046112ba565b60019998505050505050505050565b60405190151581526020015b60405180910390f35b61011961011436600461136e565b610208565b005b610119610129366004611407565b610346565b6100f161013c3660046114a9565b60019695505050505050565b610119610156366004611542565b6106a2565b610119610169366004611598565b6107ba565b610176610870565b6040516100fd91906116b7565b6101196101913660046116d1565b6108fe565b6100f16101a436600461179c565b60019a9950505050505050505050565b6101196101c2366004611869565b610af2565b6101196101d5366004611886565b610cba565b6101196101e83660046118f9565b610dbc565b6100f16101fb3660046119f5565b6001979650505050505050565b600060405160200161021a9190611b66565b604051602081830303815290604052805190602001208686604051602001610243929190611ba2565b6040516020818303038152906040528051906020012014156102805760405162461bcd60e51b815260040161027790611bbe565b60405180910390fd5b600060018787604051610294929190611beb565b908152604051908190036020019020546001600160a01b03169050806102cc5760405162461bcd60e51b815260040161027790611bfb565b6001600160a01b0381166399da7e09600087876102e833610f31565b88886040518763ffffffff1660e01b815260040161030b96959493929190611c29565b600060405180830381600087803b15801561032557600080fd5b505af1158015610339573d6000803e3d6000fd5b5050505050505050505050565b60006040516020016103589190611b66565b604051602081830303815290604052805190602001208787604051602001610381929190611ba2565b6040516020818303038152906040528051906020012014156103b55760405162461bcd60e51b815260040161027790611bbe565b6000600188886040516103c9929190611beb565b908152604051908190036020019020546001600160a01b03169050806104015760405162461bcd60e51b815260040161027790611bfb565b600060028585604051610415929190611beb565b908152604051908190036020019020546001600160a01b031690508061044d5760405162461bcd60e51b815260040161027790611c85565b6040516370a0823160e01b815233600482015283906001600160a01b038316906370a082319060240160206040518083038186803b15801561048e57600080fd5b505afa1580156104a2573d6000803e3d6000fd5b505050506040513d601f19601f820116820180604052508101906104c69190611cb3565b101561050b5760405162461bcd60e51b8152602060048201526014602482015273494e53554646494349454e545f42414c414e434560601b6044820152606401610277565b604051636eb1769f60e11b815233600482015230602482015283906001600160a01b0383169063dd62ed3e9060440160206040518083038186803b15801561055257600080fd5b505afa158015610566573d6000803e3d6000fd5b505050506040513d601f19601f8201168201806040525081019061058a9190611cb3565b10156105d15760405162461bcd60e51b8152602060048201526016602482015275494e53554646494349454e545f414c4c4f57414e434560501b6044820152606401610277565b604051632770a7eb60e21b8152336004820152602481018490526001600160a01b03821690639dc29fac90604401600060405180830381600087803b15801561061957600080fd5b505af115801561062d573d6000803e3d6000fd5b505060405163cddf869760e01b81526001600160a01b038516925063cddf86979150610665908a908a908a908a908a90600401611ccc565b600060405180830381600087803b15801561067f57600080fd5b505af1158015610693573d6000803e3d6000fd5b50505050505050505050505050565b6001600160a01b0381166106f05760405162461bcd60e51b8152602060048201526015602482015274494e56414c49445f544f4b454e5f4144445245535360581b6044820152606401610277565b60006001600160a01b03166002848460405161070d929190611beb565b908152604051908190036020019020546001600160a01b0316146107735760405162461bcd60e51b815260206004820152601860248201527f544f4b454e5f414c52454144595f5245474953544552454400000000000000006044820152606401610277565b8060028484604051610786929190611beb565b90815260405190819003602001902080546001600160a01b03929092166001600160a01b0319909216919091179055505050565b6107f986868080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525061117392505050565b604051630922c0cb60e31b81526001600160a01b039190911690634916065890610834906000908c908c908a908a908a908a90600401611d06565b600060405180830381600087803b15801561084e57600080fd5b505af1158015610862573d6000803e3d6000fd5b505050505050505050505050565b6000805461087d90611a8b565b80601f01602080910402602001604051908101604052809291908181526020018280546108a990611a8b565b80156108f65780601f106108cb576101008083540402835291602001916108f6565b820191906000526020600020905b8154815290600101906020018083116108d957829003601f168201915b505050505081565b60006040516020016109109190611b66565b604051602081830303815290604052805190602001208989604051602001610939929190611ba2565b60405160208183030381529060405280519060200120141561096d5760405162461bcd60e51b815260040161027790611bbe565b600060018a8a604051610981929190611beb565b908152604051908190036020019020546001600160a01b03169050806109b95760405162461bcd60e51b815260040161027790611bfb565b6000600285856040516109cd929190611beb565b908152604051908190036020019020546001600160a01b0316905080610a055760405162461bcd60e51b815260040161027790611c85565b604051632770a7eb60e21b8152336004820152602481018490526001600160a01b03821690639dc29fac90604401600060405180830381600087803b158015610a4d57600080fd5b505af1158015610a61573d6000803e3d6000fd5b50505050816001600160a01b031663f556abd160008b8b610a8a336001600160a01b0316610f31565b8c8c8c8c8c6040518a63ffffffff1660e01b8152600401610ab399989796959493929190611d56565b600060405180830381600087803b158015610acd57600080fd5b505af1158015610ae1573d6000803e3d6000fd5b505050505050505050505050505050565b6000604051602001610b049190611b66565b60405160208183030381529060405280519060200120816001600160a01b0316639a8a05926040518163ffffffff1660e01b815260040160006040518083038186803b158015610b5357600080fd5b505afa158015610b67573d6000803e3d6000fd5b505050506040513d6000823e601f3d908101601f19168201604052610b8f9190810190611de7565b604051602001610b9f91906116b7565b604051602081830303815290604052805190602001201415610c035760405162461bcd60e51b815260206004820152601860248201527f434841494e5f414c52454144595f5245474953544552454400000000000000006044820152606401610277565b806001826001600160a01b0316639a8a05926040518163ffffffff1660e01b815260040160006040518083038186803b158015610c3f57600080fd5b505afa158015610c53573d6000803e3d6000fd5b505050506040513d6000823e601f3d908101601f19168201604052610c7b9190810190611de7565b604051610c889190611e93565b90815260405190819003602001902080546001600160a01b03929092166001600160a01b031990921691909117905550565b600060028484604051610cce929190611beb565b908152604051908190036020019020546001600160a01b0316905080610d065760405162461bcd60e51b815260040161027790611c85565b806001600160a01b03166340c10f19610d5488888080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525061117392505050565b6040516001600160e01b031960e084901b1681526001600160a01b03909116600482015260248101859052604401600060405180830381600087803b158015610d9c57600080fd5b505af1158015610db0573d6000803e3d6000fd5b50505050505050505050565b600060028484604051610dd0929190611beb565b908152604051908190036020019020546001600160a01b0316905080610e085760405162461bcd60e51b815260040161027790611c85565b6000610e498b8b8080601f01602080910402602001604051908101604052809392919081815260200183838082843760009201919091525061117392505050565b6040516340c10f1960e01b81526001600160a01b03808316600483015260248201869052919250908316906340c10f1990604401600060405180830381600087803b158015610e9757600080fd5b505af1158015610eab573d6000803e3d6000fd5b50505050806001600160a01b0316631a98b2e06000801b8f8f8d8d8d8d8d8d8d6040518b63ffffffff1660e01b8152600401610ef09a99989796959493929190611eaf565b600060405180830381600087803b158015610f0a57600080fd5b505af1158015610f1e573d6000803e3d6000fd5b5050505050505050505050505050505050565b604051606082811b6bffffffffffffffffffffffff191660208301529060009060340160408051601f19818403018152828201909152601082526f181899199a1a9b1b9c1cb0b131b232b360811b60208301528051909250600090610f97906002611f34565b610fa2906002611f53565b6001600160401b03811115610fb957610fb9611dd1565b6040519080825280601f01601f191660200182016040528015610fe3576020820181803683370190505b509050600360fc1b81600081518110610ffe57610ffe611f6b565b60200101906001600160f81b031916908160001a905350600f60fb1b8160018151811061102d5761102d611f6b565b60200101906001600160f81b031916908160001a90535060005b835181101561116a5782600485838151811061106557611065611f6b565b016020015182516001600160f81b031990911690911c60f81c90811061108d5761108d611f6b565b01602001516001600160f81b031916826110a8836002611f34565b6110b3906002611f53565b815181106110c3576110c3611f6b565b60200101906001600160f81b031916908160001a905350828482815181106110ed576110ed611f6b565b602091010151815160f89190911c600f1690811061110d5761110d611f6b565b01602001516001600160f81b03191682611128836002611f34565b611133906003611f53565b8151811061114357611143611f6b565b60200101906001600160f81b031916908160001a90535061116381611f81565b9050611047565b50949350505050565b80516000908290602a1461118a5750600092915050565b60008060025b602a811015611268578381815181106111ab576111ab611f6b565b016020015160f81c9150606182108015906111ca575060668260ff1611155b156111e1576111da605783611f9c565b915061123d565b60418260ff16101580156111f9575060468260ff1611155b15611209576111da603783611f9c565b60308260ff1610158015611221575060398260ff1611155b15611231576111da603083611f9c565b50600095945050505050565b600261124a826029611fbf565b60ff8416911b1b92909217918061126081611f81565b915050611190565b5090949350505050565b60008083601f84011261128457600080fd5b5081356001600160401b0381111561129b57600080fd5b6020830191508360208285010111156112b357600080fd5b9250929050565b600080600080600080600080600060c08a8c0312156112d857600080fd5b8935985060208a01356001600160401b03808211156112f657600080fd5b6113028d838e01611272565b909a50985060408c013591508082111561131b57600080fd5b6113278d838e01611272565b909850965060608c0135955060808c013591508082111561134757600080fd5b506113548c828d01611272565b9a9d999c50979a9699959894979660a00135949350505050565b6000806000806000806060878903121561138757600080fd5b86356001600160401b038082111561139e57600080fd5b6113aa8a838b01611272565b909850965060208901359150808211156113c357600080fd5b6113cf8a838b01611272565b909650945060408901359150808211156113e857600080fd5b506113f589828a01611272565b979a9699509497509295939492505050565b60008060008060008060006080888a03121561142257600080fd5b87356001600160401b038082111561143957600080fd5b6114458b838c01611272565b909950975060208a013591508082111561145e57600080fd5b61146a8b838c01611272565b909750955060408a013591508082111561148357600080fd5b506114908a828b01611272565b989b979a50959894979596606090950135949350505050565b600080600080600080608087890312156114c257600080fd5b8635955060208701356001600160401b03808211156114e057600080fd5b6114ec8a838b01611272565b9097509550604089013591508082111561150557600080fd5b5061151289828a01611272565b979a9699509497949695606090950135949350505050565b6001600160a01b038116811461153f57600080fd5b50565b60008060006040848603121561155757600080fd5b83356001600160401b0381111561156d57600080fd5b61157986828701611272565b909450925050602084013561158d8161152a565b809150509250925092565b6000806000806000806000806080898b0312156115b457600080fd5b88356001600160401b03808211156115cb57600080fd5b6115d78c838d01611272565b909a50985060208b01359150808211156115f057600080fd5b6115fc8c838d01611272565b909850965060408b013591508082111561161557600080fd5b6116218c838d01611272565b909650945060608b013591508082111561163a57600080fd5b506116478b828c01611272565b999c989b5096995094979396929594505050565b60005b8381101561167657818101518382015260200161165e565b83811115611685576000848401525b50505050565b600081518084526116a381602086016020860161165b565b601f01601f19169290920160200192915050565b6020815260006116ca602083018461168b565b9392505050565b600080600080600080600080600060a08a8c0312156116ef57600080fd5b89356001600160401b038082111561170657600080fd5b6117128d838e01611272565b909b50995060208c013591508082111561172b57600080fd5b6117378d838e01611272565b909950975060408c013591508082111561175057600080fd5b61175c8d838e01611272565b909750955060608c013591508082111561177557600080fd5b506117828c828d01611272565b9a9d999c50979a9699959894979660800135949350505050565b60008060008060008060008060008060e08b8d0312156117bb57600080fd5b8a35995060208b01356001600160401b03808211156117d957600080fd5b6117e58e838f01611272565b909b50995060408d01359150808211156117fe57600080fd5b61180a8e838f01611272565b909950975060608d0135915061181f8261152a565b90955060808c0135945060a08c0135908082111561183c57600080fd5b506118498d828e01611272565b9150809450508092505060c08b013590509295989b9194979a5092959850565b60006020828403121561187b57600080fd5b81356116ca8161152a565b60008060008060006060868803121561189e57600080fd5b85356001600160401b03808211156118b557600080fd5b6118c189838a01611272565b909750955060208801359150808211156118da57600080fd5b506118e788828901611272565b96999598509660400135949350505050565b600080600080600080600080600080600060c08c8e03121561191a57600080fd5b6001600160401b03808d35111561193057600080fd5b61193d8e8e358f01611272565b909c509a5060208d013581101561195357600080fd5b6119638e60208f01358f01611272565b909a50985060408d013581101561197957600080fd5b6119898e60408f01358f01611272565b909850965060608d013581101561199f57600080fd5b6119af8e60608f01358f01611272565b909650945060808d01358110156119c557600080fd5b506119d68d60808e01358e01611272565b819450809350505060a08c013590509295989b509295989b9093969950565b600080600080600080600060a0888a031215611a1057600080fd5b8735965060208801356001600160401b0380821115611a2e57600080fd5b611a3a8b838c01611272565b909850965060408a0135915080821115611a5357600080fd5b50611a608a828b01611272565b9095509350506060880135611a748161152a565b809250506080880135905092959891949750929550565b600181811c90821680611a9f57607f821691505b60208210811415611ac057634e487b7160e01b600052602260045260246000fd5b50919050565b8054600090600181811c9080831680611ae057607f831692505b6020808410821415611b0257634e487b7160e01b600052602260045260246000fd5b83885260208801828015611b1d5760018114611b2e57611b59565b60ff19871682528282019750611b59565b60008981526020902060005b87811015611b5357815484820152908601908401611b3a565b83019850505b5050505050505092915050565b6020815260006116ca6020830184611ac6565b81835281816020850137506000828201602090810191909152601f909101601f19169091010190565b602081526000611bb6602083018486611b79565b949350505050565b60208082526013908201527229a2a72a2faa27afaba927a723afa1a420a4a760691b604082015260600190565b8183823760009101908152919050565b60208082526014908201527310d210525397d393d517d49151d254d51154915160621b604082015260600190565b608081526000611c3c6080830189611ac6565b8281036020840152611c4f81888a611b79565b90508281036040840152611c63818761168b565b90508281036060840152611c78818587611b79565b9998505050505050505050565b6020808252601490820152731513d2d15397d393d517d49151d254d51154915160621b604082015260600190565b600060208284031215611cc557600080fd5b5051919050565b606081526000611ce0606083018789611b79565b8281036020840152611cf3818688611b79565b9150508260408301529695505050505050565b878152608060208201526000611d2060808301888a611b79565b8281036040840152611d33818789611b79565b90508281036060840152611d48818587611b79565b9a9950505050505050505050565b60c081526000611d6960c083018c611ac6565b8281036020840152611d7c818b8d611b79565b90508281036040840152611d90818a61168b565b90508281036060840152611da581888a611b79565b90508281036080840152611dba818688611b79565b9150508260a08301529a9950505050505050505050565b634e487b7160e01b600052604160045260246000fd5b600060208284031215611df957600080fd5b81516001600160401b0380821115611e1057600080fd5b818401915084601f830112611e2457600080fd5b815181811115611e3657611e36611dd1565b604051601f8201601f19908116603f01168101908382118183101715611e5e57611e5e611dd1565b81604052828152876020848701011115611e7757600080fd5b611e8883602083016020880161165b565b979650505050505050565b60008251611ea581846020870161165b565b9190910192915050565b8a815260c060208201526000611ec960c083018b8d611b79565b8281036040840152611edc818a8c611b79565b90508281036060840152611ef181888a611b79565b90508281036080840152611f06818688611b79565b9150508260a08301529b9a5050505050505050505050565b634e487b7160e01b600052601160045260246000fd5b6000816000190483118215151615611f4e57611f4e611f1e565b500290565b60008219821115611f6657611f66611f1e565b500190565b634e487b7160e01b600052603260045260246000fd5b6000600019821415611f9557611f95611f1e565b5060010190565b600060ff821660ff841680821015611fb657611fb6611f1e565b90039392505050565b600082821015611fd157611fd1611f1e565b50039056fea26469706673582212208d55d45349ccf201888c104a967b20a5d88bc48a636283eaa1bb1127d355eaa764736f6c63430008090033"

    @classmethod
    def deploy(cls, chain: str, *, from_: Optional[Union[Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max") -> AxelarGatewayMock:
        """
        Args:
            chain: string
        """
        return cls._deploy([chain], from_, value, gas_limit, {})

    @overload
    def chainId(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> str:
        ...

    @overload
    def chainId(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def chainId(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[str, TransactionObject]:
        """
        Returns:
            string
        """
        return self._transact("9a8a0592", [], return_tx, request_type, str, from_, to, value, gas_limit) if not request_type == 'call' else self._call("9a8a0592", [], return_tx, str, from_, to, value, gas_limit)

    @overload
    def registerChain(self, gateway: IAxelarGatewayMock, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def registerChain(self, gateway: IAxelarGatewayMock, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def registerChain(self, gateway: IAxelarGatewayMock, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            gateway: contract IAxelarGatewayMock
        """
        return self._transact("c5d14e07", [gateway], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("c5d14e07", [gateway], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def registerToken(self, symbol: str, token: IERC20MintableBurnable, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def registerToken(self, symbol: str, token: IERC20MintableBurnable, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def registerToken(self, symbol: str, token: IERC20MintableBurnable, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            symbol: string
            token: contract IERC20MintableBurnable
        """
        return self._transact("69f667ed", [symbol, token], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("69f667ed", [symbol, token], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def sendToken(self, destinationChain: str, destinationAddress: str, symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def sendToken(self, destinationChain: str, destinationAddress: str, symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def sendToken(self, destinationChain: str, destinationAddress: str, symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            destinationChain: string
            destinationAddress: string
            symbol: string
            amount: uint256
        """
        return self._transact("26ef699d", [destinationChain, destinationAddress, symbol, amount], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("26ef699d", [destinationChain, destinationAddress, symbol, amount], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def executeSendToken(self, destinationAddress: str, symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def executeSendToken(self, destinationAddress: str, symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def executeSendToken(self, destinationAddress: str, symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            destinationAddress: string
            symbol: string
            amount: uint256
        """
        return self._transact("cddf8697", [destinationAddress, symbol, amount], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("cddf8697", [destinationAddress, symbol, amount], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def callContract(self, destinationChain: str, contractAddress: str, payload: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def callContract(self, destinationChain: str, contractAddress: str, payload: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def callContract(self, destinationChain: str, contractAddress: str, payload: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            destinationChain: string
            contractAddress: string
            payload: bytes
        """
        return self._transact("1c92115f", [destinationChain, contractAddress, payload], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("1c92115f", [destinationChain, contractAddress, payload], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def executeCallContract(self, sourceChain: str, contractAddress: str, sender: str, payload: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def executeCallContract(self, sourceChain: str, contractAddress: str, sender: str, payload: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def executeCallContract(self, sourceChain: str, contractAddress: str, sender: str, payload: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            sourceChain: string
            contractAddress: string
            sender: string
            payload: bytes
        """
        return self._transact("99da7e09", [sourceChain, contractAddress, sender, payload], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("99da7e09", [sourceChain, contractAddress, sender, payload], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def callContractWithToken(self, destinationChain: str, contractAddress: str, payload: Union[bytearray, bytes], symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def callContractWithToken(self, destinationChain: str, contractAddress: str, payload: Union[bytearray, bytes], symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def callContractWithToken(self, destinationChain: str, contractAddress: str, payload: Union[bytearray, bytes], symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            destinationChain: string
            contractAddress: string
            payload: bytes
            symbol: string
            amount: uint256
        """
        return self._transact("b5417084", [destinationChain, contractAddress, payload, symbol, amount], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("b5417084", [destinationChain, contractAddress, payload, symbol, amount], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def executeCallContractWithToken(self, sourceChain: str, contractAddress: str, sender: str, payload: Union[bytearray, bytes], symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def executeCallContractWithToken(self, sourceChain: str, contractAddress: str, sender: str, payload: Union[bytearray, bytes], symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def executeCallContractWithToken(self, sourceChain: str, contractAddress: str, sender: str, payload: Union[bytearray, bytes], symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            sourceChain: string
            contractAddress: string
            sender: string
            payload: bytes
            symbol: string
            amount: uint256
        """
        return self._transact("f556abd1", [sourceChain, contractAddress, sender, payload, symbol, amount], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("f556abd1", [sourceChain, contractAddress, sender, payload, symbol, amount], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def isContractCallApproved(self, commandId: bytes32, sourceChain: str, sourceAddress: str, contractAddress: Address, payloadHash: bytes32, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def isContractCallApproved(self, commandId: bytes32, sourceChain: str, sourceAddress: str, contractAddress: Address, payloadHash: bytes32, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def isContractCallApproved(self, commandId: bytes32, sourceChain: str, sourceAddress: str, contractAddress: Address, payloadHash: bytes32, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[bool, TransactionObject]:
        """
        Args:
            commandId: bytes32
            sourceChain: string
            sourceAddress: string
            contractAddress: address
            payloadHash: bytes32
        Returns:
            bool
        """
        return self._transact("f6a5f9f5", [commandId, sourceChain, sourceAddress, contractAddress, payloadHash], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("f6a5f9f5", [commandId, sourceChain, sourceAddress, contractAddress, payloadHash], return_tx, bool, from_, to, value, gas_limit)

    @overload
    def isContractCallAndMintApproved(self, commandId: bytes32, sourceChain: str, sourceAddress: str, contractAddress: Address, payloadHash: bytes32, symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def isContractCallAndMintApproved(self, commandId: bytes32, sourceChain: str, sourceAddress: str, contractAddress: Address, payloadHash: bytes32, symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def isContractCallAndMintApproved(self, commandId: bytes32, sourceChain: str, sourceAddress: str, contractAddress: Address, payloadHash: bytes32, symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[bool, TransactionObject]:
        """
        Args:
            commandId: bytes32
            sourceChain: string
            sourceAddress: string
            contractAddress: address
            payloadHash: bytes32
            symbol: string
            amount: uint256
        Returns:
            bool
        """
        return self._transact("bc00c216", [commandId, sourceChain, sourceAddress, contractAddress, payloadHash, symbol, amount], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("bc00c216", [commandId, sourceChain, sourceAddress, contractAddress, payloadHash, symbol, amount], return_tx, bool, from_, to, value, gas_limit)

    @overload
    def validateContractCall(self, commandId: bytes32, sourceChain: str, sourceAddress: str, payloadHash: bytes32, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def validateContractCall(self, commandId: bytes32, sourceChain: str, sourceAddress: str, payloadHash: bytes32, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def validateContractCall(self, commandId: bytes32, sourceChain: str, sourceAddress: str, payloadHash: bytes32, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[bool, TransactionObject]:
        """
        Args:
            commandId: bytes32
            sourceChain: string
            sourceAddress: string
            payloadHash: bytes32
        Returns:
            bool
        """
        return self._transact("5f6970c3", [commandId, sourceChain, sourceAddress, payloadHash], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("5f6970c3", [commandId, sourceChain, sourceAddress, payloadHash], return_tx, bool, from_, to, value, gas_limit)

    @overload
    def validateContractCallAndMint(self, commandId: bytes32, sourceChain: str, sourceAddress: str, payloadHash: bytes32, symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def validateContractCallAndMint(self, commandId: bytes32, sourceChain: str, sourceAddress: str, payloadHash: bytes32, symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def validateContractCallAndMint(self, commandId: bytes32, sourceChain: str, sourceAddress: str, payloadHash: bytes32, symbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[bool, TransactionObject]:
        """
        Args:
            commandId: bytes32
            sourceChain: string
            sourceAddress: string
            payloadHash: bytes32
            symbol: string
            amount: uint256
        Returns:
            bool
        """
        return self._transact("1876eed9", [commandId, sourceChain, sourceAddress, payloadHash, symbol, amount], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("1876eed9", [commandId, sourceChain, sourceAddress, payloadHash, symbol, amount], return_tx, bool, from_, to, value, gas_limit)

