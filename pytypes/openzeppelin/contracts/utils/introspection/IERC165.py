from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.contract import Contract, TransactionObject, Address, Wei

from woke.testing.abi_to_type import RequestType
from enum import IntEnum

from woke.testing.primitive_types import bytes4


class IERC165(Contract):
    _abi = {b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceId', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}}
    _bytecode = b''

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max") -> IERC165:
        raise Exception("Cannot deploy interface")

    @overload
    def supportsInterface(self, interfaceId: bytes4, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def supportsInterface(self, interfaceId: bytes4, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def supportsInterface(self, interfaceId: bytes4, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[bool, TransactionObject]:
        """
        Args:
            interfaceId: bytes4
        Returns:
            bool
        """
        return self._transact("01ffc9a7", [interfaceId], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("01ffc9a7", [interfaceId], return_tx, bool, from_, to, value, gas_limit)

