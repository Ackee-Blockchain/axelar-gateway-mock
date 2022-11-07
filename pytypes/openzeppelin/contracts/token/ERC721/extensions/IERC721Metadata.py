from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.contract import Contract, TransactionObject, Address, Wei

from woke.testing.abi_to_type import RequestType
from enum import IntEnum

from pytypes.openzeppelin.contracts.token.ERC721.IERC721 import IERC721

from woke.testing.primitive_types import uint256


class IERC721Metadata(IERC721):
    _abi = {b'\x8c[\xe1\xe5\xeb\xec}[\xd1OqB}\x1e\x84\xf3\xdd\x03\x14\xc0\xf7\xb2)\x1e[ \n\xc8\xc7\xc3\xb9%': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'approved', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, b'\x170~\xab9\xaba\x07\xe8\x89\x98E\xad=Y\xbd\x96S\xf2\x00\xf2 \x92\x04\x89\xca+Y7il1': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'ApprovalForAll', 'type': 'event'}, b'\xdd\xf2R\xad\x1b\xe2\xc8\x9bi\xc2\xb0h\xfc7\x8d\xaa\x95+\xa7\xf1c\xc4\xa1\x16(\xf5ZM\xf5#\xb3\xef': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, b'\t^\xa7\xb3': {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'approve', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x08\x18\x12\xfc': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'getApproved', 'outputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe9\x85\xe9\xc5': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'operator', 'type': 'address'}], 'name': 'isApprovedForAll', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x06\xfd\xde\x03': {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'cR!\x1e': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'ownerOf', 'outputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'B\x84.\x0e': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'safeTransferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb8\x8dO\xde': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'safeTransferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa2,\xb4e': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'bool', 'name': '_approved', 'type': 'bool'}], 'name': 'setApprovalForAll', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceId', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x95\xd8\x9bA': {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc8{V\xdd': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'tokenURI', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'#\xb8r\xdd': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _bytecode = b''

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max") -> IERC721Metadata:
        raise Exception("Cannot deploy interface")

    @overload
    def name(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> str:
        ...

    @overload
    def name(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def name(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[str, TransactionObject]:
        """
        Returns:
            string
        """
        return self._transact("06fdde03", [], return_tx, request_type, str, from_, to, value, gas_limit) if not request_type == 'call' else self._call("06fdde03", [], return_tx, str, from_, to, value, gas_limit)

    @overload
    def symbol(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> str:
        ...

    @overload
    def symbol(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def symbol(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[str, TransactionObject]:
        """
        Returns:
            string
        """
        return self._transact("95d89b41", [], return_tx, request_type, str, from_, to, value, gas_limit) if not request_type == 'call' else self._call("95d89b41", [], return_tx, str, from_, to, value, gas_limit)

    @overload
    def tokenURI(self, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> str:
        ...

    @overload
    def tokenURI(self, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def tokenURI(self, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[str, TransactionObject]:
        """
        Args:
            tokenId: uint256
        Returns:
            string
        """
        return self._transact("c87b56dd", [tokenId], return_tx, request_type, str, from_, to, value, gas_limit) if not request_type == 'call' else self._call("c87b56dd", [tokenId], return_tx, str, from_, to, value, gas_limit)

