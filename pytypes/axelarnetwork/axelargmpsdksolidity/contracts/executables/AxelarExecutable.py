from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.contract import Contract, Library, TransactionObject, Address, Wei

from woke.testing.abi_to_type import RequestType
from enum import IntEnum

from pytypes.axelarnetwork.axelargmpsdksolidity.contracts.interfaces.IAxelarGateway import IAxelarGateway
from pytypes.axelarnetwork.axelargmpsdksolidity.contracts.interfaces.IAxelarExecutable import IAxelarExecutable

from woke.testing.primitive_types import bytes32
from woke.testing.primitive_types import uint256


class AxelarExecutable(IAxelarExecutable):
    _abi = {'constructor': {'inputs': [{'internalType': 'address', 'name': 'gateway_', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\xe6\xc4${': {'inputs': [], 'name': 'InvalidAddress', 'type': 'error'}, b'P\x0cD\xb4': {'inputs': [], 'name': 'NotApprovedByGateway', 'type': 'error'}, b'I\x16\x06X': {'inputs': [{'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'sourceAddress', 'type': 'string'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}], 'name': 'execute', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x1a\x98\xb2\xe0': {'inputs': [{'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'sourceAddress', 'type': 'string'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}, {'internalType': 'string', 'name': 'tokenSymbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'executeWithToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x11a\x91\xb6': {'inputs': [], 'name': 'gateway', 'outputs': [{'internalType': 'contract IAxelarGateway', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}}
    _bytecode = "60a060405234801561001057600080fd5b5060405161064938038061064983398101604081905261002f91610067565b6001600160a01b0381166100565760405163e6c4247b60e01b815260040160405180910390fd5b6001600160a01b0316608052610097565b60006020828403121561007957600080fd5b81516001600160a01b038116811461009057600080fd5b9392505050565b60805161058b6100be60003960008181604b0152818160e201526101d4015261058b6000f3fe608060405234801561001057600080fd5b50600436106100415760003560e01c8063116191b6146100465780631a98b2e014610089578063491606581461009e575b600080fd5b61006d7f000000000000000000000000000000000000000000000000000000000000000081565b6040516001600160a01b03909116815260200160405180910390f35b61009c6100973660046102d5565b6100b1565b005b61009c6100ac3660046103af565b6101a3565b600085856040516100c3929190610453565b604051908190038120631876eed960e01b825291506001600160a01b037f00000000000000000000000000000000000000000000000000000000000000001690631876eed990610127908e908e908e908e908e9089908d908d908d9060040161048c565b602060405180830381600087803b15801561014157600080fd5b505af1158015610155573d6000803e3d6000fd5b505050506040513d601f19601f8201168201806040525081019061017991906104eb565b61019657604051631403112d60e21b815260040160405180910390fd5b5050505050505050505050565b600082826040516101b5929190610453565b604051908190038120635f6970c360e01b825291506001600160a01b037f00000000000000000000000000000000000000000000000000000000000000001690635f6970c390610213908b908b908b908b908b908990600401610514565b602060405180830381600087803b15801561022d57600080fd5b505af1158015610241573d6000803e3d6000fd5b505050506040513d601f19601f8201168201806040525081019061026591906104eb565b61028257604051631403112d60e21b815260040160405180910390fd5b5050505050505050565b60008083601f84011261029e57600080fd5b50813567ffffffffffffffff8111156102b657600080fd5b6020830191508360208285010111156102ce57600080fd5b9250929050565b60008060008060008060008060008060c08b8d0312156102f457600080fd5b8a35995060208b013567ffffffffffffffff8082111561031357600080fd5b61031f8e838f0161028c565b909b50995060408d013591508082111561033857600080fd5b6103448e838f0161028c565b909950975060608d013591508082111561035d57600080fd5b6103698e838f0161028c565b909750955060808d013591508082111561038257600080fd5b5061038f8d828e0161028c565b9150809450508092505060a08b013590509295989b9194979a5092959850565b60008060008060008060006080888a0312156103ca57600080fd5b87359650602088013567ffffffffffffffff808211156103e957600080fd5b6103f58b838c0161028c565b909850965060408a013591508082111561040e57600080fd5b61041a8b838c0161028c565b909650945060608a013591508082111561043357600080fd5b506104408a828b0161028c565b989b979a50959850939692959293505050565b8183823760009101908152919050565b81835281816020850137506000828201602090810191909152601f909101601f19169091010190565b89815260c0602082015260006104a660c083018a8c610463565b82810360408401526104b981898b610463565b905086606084015282810360808401526104d4818688610463565b9150508260a08301529a9950505050505050505050565b6000602082840312156104fd57600080fd5b8151801515811461050d57600080fd5b9392505050565b86815260806020820152600061052e608083018789610463565b8281036040840152610541818688610463565b91505082606083015297965050505050505056fea2646970667358221220768d5d1aa3e1fa104c6cbe44349bae71691ea21815bdf1cfa27114c86016062c64736f6c63430008090033"

    @classmethod
    def deploy(cls, gateway_: Address, *, from_: Optional[Union[Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max") -> AxelarExecutable:
        """
        Args:
            gateway_: address
        """
        return cls._deploy([gateway_], from_, value, gas_limit, {})

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

