from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.contract import Contract, Library, TransactionObject, Address, Wei

from enum import IntEnum



class StringToAddress(Library):
    _abi = {}
    _bytecode = "60566037600b82828239805160001a607314602a57634e487b7160e01b600052600060045260246000fd5b30600052607381538281f3fe73000000000000000000000000000000000000000030146080604052600080fdfea2646970667358221220d649a48015512c6a5bc7dd06ccfedf463d744c1e4ad6736b90fc03ca6a84ee5b64736f6c63430008090033"

    _library_id = b'Pe\x03\xa3\xd7Z\x05R\x9b\x84\xb3u\x80\xe7\xa9w\x02'

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max") -> StringToAddress:
        return cls._deploy([], from_, value, gas_limit, {})

class AddressToString(Library):
    _abi = {}
    _bytecode = "60566037600b82828239805160001a607314602a57634e487b7160e01b600052600060045260246000fd5b30600052607381538281f3fe73000000000000000000000000000000000000000030146080604052600080fdfea2646970667358221220dafd9aacb60458c9706c3184a8d5b8791dff4477ac7e7ab4729c4a6f3545290364736f6c63430008090033"

    _library_id = b'(\x8d@\xde\x86\xd5\xa4\x8d\t+KW\x98\x98<\x85\xeb'

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max") -> AddressToString:
        return cls._deploy([], from_, value, gas_limit, {})

