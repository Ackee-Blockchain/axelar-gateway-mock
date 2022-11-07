from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.contract import Contract, TransactionObject, Address, Wei

from woke.testing.abi_to_type import RequestType
from enum import IntEnum

from pytypes.axelarnetwork.axelargmpsdksolidity.contracts.interfaces.IAxelarGateway import IAxelarGateway

from woke.testing.primitive_types import uint256
from woke.testing.primitive_types import bytes32


class IAxelarExecutable(Contract):
    _abi = {b'\xe6\xc4${': {'inputs': [], 'name': 'InvalidAddress', 'type': 'error'}, b'P\x0cD\xb4': {'inputs': [], 'name': 'NotApprovedByGateway', 'type': 'error'}, b'I\x16\x06X': {'inputs': [{'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'sourceAddress', 'type': 'string'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}], 'name': 'execute', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x1a\x98\xb2\xe0': {'inputs': [{'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'sourceAddress', 'type': 'string'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}, {'internalType': 'string', 'name': 'tokenSymbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'executeWithToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x11a\x91\xb6': {'inputs': [], 'name': 'gateway', 'outputs': [{'internalType': 'contract IAxelarGateway', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}}
    _bytecode = b''

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max") -> IAxelarExecutable:
        raise Exception("Cannot deploy interface")

    @overload
    def gateway(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> IAxelarGateway:
        ...

    @overload
    def gateway(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def gateway(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[IAxelarGateway, TransactionObject]:
        """
        Returns:
            contract IAxelarGateway
        """
        return self._transact("116191b6", [], return_tx, request_type, IAxelarGateway, from_, to, value, gas_limit) if not request_type == 'call' else self._call("116191b6", [], return_tx, IAxelarGateway, from_, to, value, gas_limit)

    @overload
    def execute(self, commandId: bytes32, sourceChain: str, sourceAddress: str, payload: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def execute(self, commandId: bytes32, sourceChain: str, sourceAddress: str, payload: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def execute(self, commandId: bytes32, sourceChain: str, sourceAddress: str, payload: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            commandId: bytes32
            sourceChain: string
            sourceAddress: string
            payload: bytes
        """
        return self._transact("49160658", [commandId, sourceChain, sourceAddress, payload], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("49160658", [commandId, sourceChain, sourceAddress, payload], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def executeWithToken(self, commandId: bytes32, sourceChain: str, sourceAddress: str, payload: Union[bytearray, bytes], tokenSymbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def executeWithToken(self, commandId: bytes32, sourceChain: str, sourceAddress: str, payload: Union[bytearray, bytes], tokenSymbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def executeWithToken(self, commandId: bytes32, sourceChain: str, sourceAddress: str, payload: Union[bytearray, bytes], tokenSymbol: str, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            commandId: bytes32
            sourceChain: string
            sourceAddress: string
            payload: bytes
            tokenSymbol: string
            amount: uint256
        """
        return self._transact("1a98b2e0", [commandId, sourceChain, sourceAddress, payload, tokenSymbol, amount], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("1a98b2e0", [commandId, sourceChain, sourceAddress, payload, tokenSymbol, amount], return_tx, type(None), from_, to, value, gas_limit)

