from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.contract import Contract, TransactionObject, Address, Wei

from woke.testing.abi_to_type import RequestType
from enum import IntEnum

from woke.testing.primitive_types import uint256
from woke.testing.primitive_types import bytes4


class IERC721Receiver(Contract):
    _abi = {b'\x15\x0bz\x02': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'onERC721Received', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _bytecode = b''

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max") -> IERC721Receiver:
        raise Exception("Cannot deploy interface")

    @overload
    def onERC721Received(self, operator: Address, from__: Address, tokenId: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> bytes4:
        ...

    @overload
    def onERC721Received(self, operator: Address, from__: Address, tokenId: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def onERC721Received(self, operator: Address, from__: Address, tokenId: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[bytes4, TransactionObject]:
        """
        Args:
            operator: address
            from__: address
            tokenId: uint256
            data: bytes
        Returns:
            bytes4
        """
        return self._transact("150b7a02", [operator, from__, tokenId, data], return_tx, request_type, bytes4, from_, to, value, gas_limit) if not request_type == 'call' else self._call("150b7a02", [operator, from__, tokenId, data], return_tx, bytes4, from_, to, value, gas_limit)

