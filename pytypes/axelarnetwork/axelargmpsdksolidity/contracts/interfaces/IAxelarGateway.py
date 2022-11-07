from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.contract import Contract, TransactionObject, Address, Wei

from woke.testing.abi_to_type import RequestType
from enum import IntEnum

from woke.testing.primitive_types import uint256
from woke.testing.primitive_types import bytes32


class IAxelarGateway(Contract):
    _abi = {b'\xe2\x17\xb0\xad': {'inputs': [{'internalType': 'string', 'name': 'symbol', 'type': 'string'}], 'name': 'BurnFailed', 'type': 'error'}, b'\x03\x7f`\xe5': {'inputs': [{'internalType': 'string', 'name': 'symbol', 'type': 'string'}], 'name': 'ExceedMintLimit', 'type': 'error'}, b',R\x11\xc6': {'inputs': [], 'name': 'InvalidAmount', 'type': 'error'}, b'sS&\xab': {'inputs': [], 'name': 'InvalidAuthModule', 'type': 'error'}, b'zG\xc9\xa2': {'inputs': [], 'name': 'InvalidChainId', 'type': 'error'}, b'\x8f\x84\xfb$': {'inputs': [], 'name': 'InvalidCodeHash', 'type': 'error'}, b'\xca\x9a(\xf5': {'inputs': [], 'name': 'InvalidCommands', 'type': 'error'}, b"\x14\xa2'_": {'inputs': [], 'name': 'InvalidSetMintLimitsParams', 'type': 'error'}, b'd&\xd5\xf8': {'inputs': [], 'name': 'InvalidTokenDeployer', 'type': 'error'}, b'\x90\xc5.\xd7': {'inputs': [{'internalType': 'string', 'name': 'symbol', 'type': 'string'}], 'name': 'MintFailed', 'type': 'error'}, b'\xbf\x10\xdd:': {'inputs': [], 'name': 'NotProxy', 'type': 'error'}, b')\xc3\xb7\xee': {'inputs': [], 'name': 'NotSelf', 'type': 'error'}, b'\x97\x90]\xfb': {'inputs': [], 'name': 'SetupFailed', 'type': 'error'}, b'\xaa~\x8b2': {'inputs': [{'internalType': 'string', 'name': 'symbol', 'type': 'string'}], 'name': 'TokenAlreadyExists', 'type': 'error'}, b'\xc5\xcc\xdd\xde': {'inputs': [{'internalType': 'address', 'name': 'token', 'type': 'address'}], 'name': 'TokenContractDoesNotExist', 'type': 'error'}, b"\x86\xd5'C": {'inputs': [{'internalType': 'string', 'name': 'symbol', 'type': 'string'}], 'name': 'TokenDeployFailed', 'type': 'error'}, b'r\xba\x13~': {'inputs': [{'internalType': 'string', 'name': 'symbol', 'type': 'string'}], 'name': 'TokenDoesNotExist', 'type': 'error'}, b"0\xael\xc7\x8c'\xe6Qt[\xf2\xad\x08\xa1\x1d\xe89\x10\xac\x1e4zR\xf7\xac\x89\x8c\x0f\xbe\xf9M\xae": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'string', 'name': 'destinationChain', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'destinationContractAddress', 'type': 'string'}, {'indexed': True, 'internalType': 'bytes32', 'name': 'payloadHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}], 'name': 'ContractCall', 'type': 'event'}, b'D\xe4\xf8\xf6\xbdh,Z:\xeb\xa96\x01\xab\x07\xcbM\x1f!\xb2\xaa\xb1\xaeH\x80\xd9Wy\x190\x9a\xa4': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'sourceAddress', 'type': 'string'}, {'indexed': True, 'internalType': 'address', 'name': 'contractAddress', 'type': 'address'}, {'indexed': True, 'internalType': 'bytes32', 'name': 'payloadHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'sourceTxHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'sourceEventIndex', 'type': 'uint256'}], 'name': 'ContractCallApproved', 'type': 'event'}, b'\x99\x91\xfa\xa1\xf45gQY\xff\xaed\xb6m~\xcf\xdbU\xc2\x97U\x86\x9a\x18\xdb\x84\x97\xb49#G\xe0': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'sourceAddress', 'type': 'string'}, {'indexed': True, 'internalType': 'address', 'name': 'contractAddress', 'type': 'address'}, {'indexed': True, 'internalType': 'bytes32', 'name': 'payloadHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'sourceTxHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'sourceEventIndex', 'type': 'uint256'}], 'name': 'ContractCallApprovedWithMint', 'type': 'event'}, b'~PV\x9d&\xbed;\xdawWr"\x91\xecf\xb1\xbef\xd8(4t\xae?\xabZ\x98\xf8x\xa7\xa2': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'string', 'name': 'destinationChain', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'destinationContractAddress', 'type': 'string'}, {'indexed': True, 'internalType': 'bytes32', 'name': 'payloadHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}, {'indexed': False, 'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'ContractCallWithToken', 'type': 'event'}, b'\xa7L\x88G\xd5\x13\xfe\xba"\xa0\xf0\xcb8\xd50\x81\xab\xf9ub\xcd\xb2\x93\x92k\xa2Ch\x9e|A\xca': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}], 'name': 'Executed', 'type': 'event'}, b'\x19.u\x9eU\xf3Y\xcd\x982\xb5\xc0\xc6\xe3\x8eKm\xf5\xc5\xca3\xf3\xbd\\\x90s\x8e\x86ZR\x18r': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': 'newOperatorsData', 'type': 'bytes'}], 'name': 'OperatorshipTransferred', 'type': 'event'}, b'\xbf\x90\xb5\xa1\xec\x97c\xe8\xbfK\x92E\xce\xf0\xc2\x8d\xb9+\xab0\x9f\xc2\xc5\x17\x7f\x17\x81O8$i8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'indexed': False, 'internalType': 'address', 'name': 'tokenAddresses', 'type': 'address'}], 'name': 'TokenDeployed', 'type': 'event'}, b'\xd9\x94F\xc1\xd7c\x85\xbbU\x19\xcc\xfbRt\xab\xcf\xd5\x89m\xfc"@^@\x01\x0f\xde!\x7f\x01\x8a\x18': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'limit', 'type': 'uint256'}], 'name': 'TokenMintLimitUpdated', 'type': 'event'}, b"e\x1d\x93\xf6lC)c\x0e\x8d\x0fbH\x8e\xffY\x9e;\xe4\x84\xdaXs5\xe8\xdc\x0f\xcfF\x06'&": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'string', 'name': 'destinationChain', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'destinationAddress', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'TokenSent', 'type': 'event'}, b'\xbc|\xd7Z \xee\'\xfd\x9a\xde\xba\xb3 A\xf7U!M\xbck\xff\xa9\x0c\xc0"[9\xda.\\-;': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'Upgraded', 'type': 'event'}, b'6I@\xd8': {'inputs': [], 'name': 'adminEpoch', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x88\xb3\x05\x87': {'inputs': [{'internalType': 'uint256', 'name': 'epoch', 'type': 'uint256'}], 'name': 'adminThreshold', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x14\xbf\xd6\xd0': {'inputs': [{'internalType': 'uint256', 'name': 'epoch', 'type': 'uint256'}], 'name': 'admins', 'outputs': [{'internalType': 'address[]', 'name': '', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xaa\x1e\x1f\n': {'inputs': [], 'name': 'allTokensFrozen', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'd\x94\x0cV': {'inputs': [], 'name': 'authModule', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1c\x92\x11_': {'inputs': [{'internalType': 'string', 'name': 'destinationChain', 'type': 'string'}, {'internalType': 'string', 'name': 'contractAddress', 'type': 'string'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}], 'name': 'callContract', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb5Ap\x84': {'inputs': [{'internalType': 'string', 'name': 'destinationChain', 'type': 'string'}, {'internalType': 'string', 'name': 'contractAddress', 'type': 'string'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}, {'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'callContractWithToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\t\xc5\xea\xbe': {'inputs': [{'internalType': 'bytes', 'name': 'input', 'type': 'bytes'}], 'name': 'execute', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\\`\xda\x1b': {'inputs': [], 'name': 'implementation', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd2o\xf2\x10': {'inputs': [{'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}], 'name': 'isCommandExecuted', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbc\x00\xc2\x16': {'inputs': [{'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'sourceAddress', 'type': 'string'}, {'internalType': 'address', 'name': 'contractAddress', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'payloadHash', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'isContractCallAndMintApproved', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xf6\xa5\xf9\xf5': {'inputs': [{'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'sourceAddress', 'type': 'string'}, {'internalType': 'address', 'name': 'contractAddress', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'payloadHash', 'type': 'bytes32'}], 'name': 'isContractCallApproved', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'&\xefi\x9d': {'inputs': [{'internalType': 'string', 'name': 'destinationChain', 'type': 'string'}, {'internalType': 'string', 'name': 'destinationAddress', 'type': 'string'}, {'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'sendToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'g\xac\xe8\xeb': {'inputs': [{'internalType': 'string[]', 'name': 'symbols', 'type': 'string[]'}, {'internalType': 'uint256[]', 'name': 'limits', 'type': 'uint256[]'}], 'name': 'setTokenMintLimits', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x9d\xed\x06\xdf': {'inputs': [{'internalType': 'bytes', 'name': 'params', 'type': 'bytes'}], 'name': 'setup', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x93[\x13\xf6': {'inputs': [{'internalType': 'string', 'name': 'symbol', 'type': 'string'}], 'name': 'tokenAddresses', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'*-\xae\n': {'inputs': [], 'name': 'tokenDeployer', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'{\x1bv\x9e': {'inputs': [{'internalType': 'string', 'name': 'symbol', 'type': 'string'}], 'name': 'tokenFrozen', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xce\xc7\xb3Y': {'inputs': [{'internalType': 'string', 'name': 'symbol', 'type': 'string'}], 'name': 'tokenMintAmount', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'&\x9e\xb6^': {'inputs': [{'internalType': 'string', 'name': 'symbol', 'type': 'string'}], 'name': 'tokenMintLimit', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa3I\x9cs': {'inputs': [{'internalType': 'address', 'name': 'newImplementation', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'newImplementationCodeHash', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'setupParams', 'type': 'bytes'}], 'name': 'upgrade', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'_ip\xc3': {'inputs': [{'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'sourceAddress', 'type': 'string'}, {'internalType': 'bytes32', 'name': 'payloadHash', 'type': 'bytes32'}], 'name': 'validateContractCall', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x18v\xee\xd9': {'inputs': [{'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'sourceAddress', 'type': 'string'}, {'internalType': 'bytes32', 'name': 'payloadHash', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'validateContractCallAndMint', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _bytecode = b''

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max") -> IAxelarGateway:
        raise Exception("Cannot deploy interface")

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

    @overload
    def authModule(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Address:
        ...

    @overload
    def authModule(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def authModule(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[Address, TransactionObject]:
        """
        Returns:
            address
        """
        return self._transact("64940c56", [], return_tx, request_type, Address, from_, to, value, gas_limit) if not request_type == 'call' else self._call("64940c56", [], return_tx, Address, from_, to, value, gas_limit)

    @overload
    def tokenDeployer(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Address:
        ...

    @overload
    def tokenDeployer(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def tokenDeployer(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[Address, TransactionObject]:
        """
        Returns:
            address
        """
        return self._transact("2a2dae0a", [], return_tx, request_type, Address, from_, to, value, gas_limit) if not request_type == 'call' else self._call("2a2dae0a", [], return_tx, Address, from_, to, value, gas_limit)

    @overload
    def tokenMintLimit(self, symbol: str, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> uint256:
        ...

    @overload
    def tokenMintLimit(self, symbol: str, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def tokenMintLimit(self, symbol: str, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[uint256, TransactionObject]:
        """
        Args:
            symbol: string
        Returns:
            uint256
        """
        return self._transact("269eb65e", [symbol], return_tx, request_type, uint256, from_, to, value, gas_limit) if not request_type == 'call' else self._call("269eb65e", [symbol], return_tx, uint256, from_, to, value, gas_limit)

    @overload
    def tokenMintAmount(self, symbol: str, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> uint256:
        ...

    @overload
    def tokenMintAmount(self, symbol: str, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def tokenMintAmount(self, symbol: str, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[uint256, TransactionObject]:
        """
        Args:
            symbol: string
        Returns:
            uint256
        """
        return self._transact("cec7b359", [symbol], return_tx, request_type, uint256, from_, to, value, gas_limit) if not request_type == 'call' else self._call("cec7b359", [symbol], return_tx, uint256, from_, to, value, gas_limit)

    @overload
    def allTokensFrozen(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def allTokensFrozen(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def allTokensFrozen(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[bool, TransactionObject]:
        """
        Returns:
            bool
        """
        return self._transact("aa1e1f0a", [], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("aa1e1f0a", [], return_tx, bool, from_, to, value, gas_limit)

    @overload
    def implementation(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Address:
        ...

    @overload
    def implementation(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def implementation(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[Address, TransactionObject]:
        """
        Returns:
            address
        """
        return self._transact("5c60da1b", [], return_tx, request_type, Address, from_, to, value, gas_limit) if not request_type == 'call' else self._call("5c60da1b", [], return_tx, Address, from_, to, value, gas_limit)

    @overload
    def tokenAddresses(self, symbol: str, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Address:
        ...

    @overload
    def tokenAddresses(self, symbol: str, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def tokenAddresses(self, symbol: str, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[Address, TransactionObject]:
        """
        Args:
            symbol: string
        Returns:
            address
        """
        return self._transact("935b13f6", [symbol], return_tx, request_type, Address, from_, to, value, gas_limit) if not request_type == 'call' else self._call("935b13f6", [symbol], return_tx, Address, from_, to, value, gas_limit)

    @overload
    def tokenFrozen(self, symbol: str, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def tokenFrozen(self, symbol: str, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def tokenFrozen(self, symbol: str, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[bool, TransactionObject]:
        """
        Args:
            symbol: string
        Returns:
            bool
        """
        return self._transact("7b1b769e", [symbol], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("7b1b769e", [symbol], return_tx, bool, from_, to, value, gas_limit)

    @overload
    def isCommandExecuted(self, commandId: bytes32, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def isCommandExecuted(self, commandId: bytes32, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def isCommandExecuted(self, commandId: bytes32, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[bool, TransactionObject]:
        """
        Args:
            commandId: bytes32
        Returns:
            bool
        """
        return self._transact("d26ff210", [commandId], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("d26ff210", [commandId], return_tx, bool, from_, to, value, gas_limit)

    @overload
    def adminEpoch(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> uint256:
        ...

    @overload
    def adminEpoch(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def adminEpoch(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[uint256, TransactionObject]:
        """
        Returns:
            uint256
        """
        return self._transact("364940d8", [], return_tx, request_type, uint256, from_, to, value, gas_limit) if not request_type == 'call' else self._call("364940d8", [], return_tx, uint256, from_, to, value, gas_limit)

    @overload
    def adminThreshold(self, epoch: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> uint256:
        ...

    @overload
    def adminThreshold(self, epoch: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def adminThreshold(self, epoch: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[uint256, TransactionObject]:
        """
        Args:
            epoch: uint256
        Returns:
            uint256
        """
        return self._transact("88b30587", [epoch], return_tx, request_type, uint256, from_, to, value, gas_limit) if not request_type == 'call' else self._call("88b30587", [epoch], return_tx, uint256, from_, to, value, gas_limit)

    @overload
    def admins(self, epoch: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> List[Address]:
        ...

    @overload
    def admins(self, epoch: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def admins(self, epoch: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[List[Address], TransactionObject]:
        """
        Args:
            epoch: uint256
        Returns:
            address[]
        """
        return self._transact("14bfd6d0", [epoch], return_tx, request_type, List[Address], from_, to, value, gas_limit) if not request_type == 'call' else self._call("14bfd6d0", [epoch], return_tx, List[Address], from_, to, value, gas_limit)

    @overload
    def setTokenMintLimits(self, symbols: List[str], limits: List[uint256], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def setTokenMintLimits(self, symbols: List[str], limits: List[uint256], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def setTokenMintLimits(self, symbols: List[str], limits: List[uint256], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            symbols: string[]
            limits: uint256[]
        """
        return self._transact("67ace8eb", [symbols, limits], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("67ace8eb", [symbols, limits], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def upgrade(self, newImplementation: Address, newImplementationCodeHash: bytes32, setupParams: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def upgrade(self, newImplementation: Address, newImplementationCodeHash: bytes32, setupParams: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def upgrade(self, newImplementation: Address, newImplementationCodeHash: bytes32, setupParams: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            newImplementation: address
            newImplementationCodeHash: bytes32
            setupParams: bytes
        """
        return self._transact("a3499c73", [newImplementation, newImplementationCodeHash, setupParams], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("a3499c73", [newImplementation, newImplementationCodeHash, setupParams], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def setup(self, params: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def setup(self, params: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def setup(self, params: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            params: bytes
        """
        return self._transact("9ded06df", [params], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("9ded06df", [params], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def execute(self, input: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def execute(self, input: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def execute(self, input: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            input: bytes
        """
        return self._transact("09c5eabe", [input], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("09c5eabe", [input], return_tx, type(None), from_, to, value, gas_limit)

