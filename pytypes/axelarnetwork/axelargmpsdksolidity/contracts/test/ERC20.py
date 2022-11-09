from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.contract import Contract, TransactionObject, Address, Wei

from enum import IntEnum
from woke.testing.abi_to_type import RequestType

from pytypes.axelarnetwork.axelargmpsdksolidity.contracts.interfaces.IERC20 import IERC20

from woke.testing.primitive_types import uint8
from woke.testing.primitive_types import uint256


class ERC20(IERC20):
    _abi = {'constructor': {'inputs': [{'internalType': 'string', 'name': 'name_', 'type': 'string'}, {'internalType': 'string', 'name': 'symbol_', 'type': 'string'}, {'internalType': 'uint8', 'name': 'decimals_', 'type': 'uint8'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'm\x18{(': {'inputs': [], 'name': 'InvalidAccount', 'type': 'error'}, b'\x8c[\xe1\xe5\xeb\xec}[\xd1OqB}\x1e\x84\xf3\xdd\x03\x14\xc0\xf7\xb2)\x1e[ \n\xc8\xc7\xc3\xb9%': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, b'\xdd\xf2R\xad\x1b\xe2\xc8\x9bi\xc2\xb0h\xfc7\x8d\xaa\x95+\xa7\xf1c\xc4\xa1\x16(\xf5ZM\xf5#\xb3\xef': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, b'\xddb\xed>': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\t^\xa7\xb3': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'1<\xe5g': {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa4W\xc2\xd7': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'subtractedValue', 'type': 'uint256'}], 'name': 'decreaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'9P\x93Q': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'addedValue', 'type': 'uint256'}], 'name': 'increaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x06\xfd\xde\x03': {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x95\xd8\x9bA': {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x18\x16\r\xdd': {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa9\x05\x9c\xbb': {'inputs': [{'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'#\xb8r\xdd': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _bytecode = b'`\xa0`@R4\x80\x15b\x00\x00\x11W`\x00\x80\xfd[P`@Qb\x00\t|8\x03\x80b\x00\t|\x839\x81\x01`@\x81\x90Rb\x00\x004\x91b\x00\x01\xe2V[\x82Qb\x00\x00I\x90`\x03\x90` \x86\x01\x90b\x00\x00oV[P\x81Qb\x00\x00_\x90`\x04\x90` \x85\x01\x90b\x00\x00oV[P`\xff\x16`\x80RPb\x00\x02\xa4\x90PV[\x82\x80Tb\x00\x00}\x90b\x00\x02gV[\x90`\x00R` `\x00 \x90`\x1f\x01` \x90\x04\x81\x01\x92\x82b\x00\x00\xa1W`\x00\x85Ub\x00\x00\xecV[\x82`\x1f\x10b\x00\x00\xbcW\x80Q`\xff\x19\x16\x83\x80\x01\x17\x85Ub\x00\x00\xecV[\x82\x80\x01`\x01\x01\x85U\x82\x15b\x00\x00\xecW\x91\x82\x01[\x82\x81\x11\x15b\x00\x00\xecW\x82Q\x82U\x91` \x01\x91\x90`\x01\x01\x90b\x00\x00\xcfV[Pb\x00\x00\xfa\x92\x91Pb\x00\x00\xfeV[P\x90V[[\x80\x82\x11\x15b\x00\x00\xfaW`\x00\x81U`\x01\x01b\x00\x00\xffV[cNH{q`\xe0\x1b`\x00R`A`\x04R`$`\x00\xfd[`\x00\x82`\x1f\x83\x01\x12b\x00\x01=W`\x00\x80\xfd[\x81Q`\x01`\x01`@\x1b\x03\x80\x82\x11\x15b\x00\x01ZWb\x00\x01Zb\x00\x01\x15V[`@Q`\x1f\x83\x01`\x1f\x19\x90\x81\x16`?\x01\x16\x81\x01\x90\x82\x82\x11\x81\x83\x10\x17\x15b\x00\x01\x85Wb\x00\x01\x85b\x00\x01\x15V[\x81`@R\x83\x81R` \x92P\x86\x83\x85\x88\x01\x01\x11\x15b\x00\x01\xa2W`\x00\x80\xfd[`\x00\x91P[\x83\x82\x10\x15b\x00\x01\xc6W\x85\x82\x01\x83\x01Q\x81\x83\x01\x84\x01R\x90\x82\x01\x90b\x00\x01\xa7V[\x83\x82\x11\x15b\x00\x01\xd8W`\x00\x83\x85\x83\x01\x01R[\x96\x95PPPPPPV[`\x00\x80`\x00``\x84\x86\x03\x12\x15b\x00\x01\xf8W`\x00\x80\xfd[\x83Q`\x01`\x01`@\x1b\x03\x80\x82\x11\x15b\x00\x02\x10W`\x00\x80\xfd[b\x00\x02\x1e\x87\x83\x88\x01b\x00\x01+V[\x94P` \x86\x01Q\x91P\x80\x82\x11\x15b\x00\x025W`\x00\x80\xfd[Pb\x00\x02D\x86\x82\x87\x01b\x00\x01+V[\x92PP`@\x84\x01Q`\xff\x81\x16\x81\x14b\x00\x02\\W`\x00\x80\xfd[\x80\x91PP\x92P\x92P\x92V[`\x01\x81\x81\x1c\x90\x82\x16\x80b\x00\x02|W`\x7f\x82\x16\x91P[` \x82\x10\x81\x14\x15b\x00\x02\x9eWcNH{q`\xe0\x1b`\x00R`"`\x04R`$`\x00\xfd[P\x91\x90PV[`\x80Qa\x06\xbcb\x00\x02\xc0`\x009`\x00a\x01\x1e\x01Ra\x06\xbc`\x00\xf3\xfe`\x80`@R4\x80\x15a\x00\x10W`\x00\x80\xfd[P`\x046\x10a\x00\xa9W`\x005`\xe0\x1c\x80c9P\x93Q\x11a\x00qW\x80c9P\x93Q\x14a\x01RW\x80cp\xa0\x821\x14a\x01eW\x80c\x95\xd8\x9bA\x14a\x01\x85W\x80c\xa4W\xc2\xd7\x14a\x01\x8dW\x80c\xa9\x05\x9c\xbb\x14a\x01\xa0W\x80c\xddb\xed>\x14a\x01\xb3W`\x00\x80\xfd[\x80c\x06\xfd\xde\x03\x14a\x00\xaeW\x80c\t^\xa7\xb3\x14a\x00\xccW\x80c\x18\x16\r\xdd\x14a\x00\xefW\x80c#\xb8r\xdd\x14a\x01\x06W\x80c1<\xe5g\x14a\x01\x19W[`\x00\x80\xfd[a\x00\xb6a\x01\xdeV[`@Qa\x00\xc3\x91\x90a\x04\xdaV[`@Q\x80\x91\x03\x90\xf3[a\x00\xdfa\x00\xda6`\x04a\x05KV[a\x02lV[`@Q\x90\x15\x15\x81R` \x01a\x00\xc3V[a\x00\xf8`\x02T\x81V[`@Q\x90\x81R` \x01a\x00\xc3V[a\x00\xdfa\x01\x146`\x04a\x05uV[a\x02\x82V[a\x01@\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x81V[`@Q`\xff\x90\x91\x16\x81R` \x01a\x00\xc3V[a\x00\xdfa\x01`6`\x04a\x05KV[a\x02\xd9V[a\x00\xf8a\x01s6`\x04a\x05\xb1V[`\x00` \x81\x90R\x90\x81R`@\x90 T\x81V[a\x00\xb6a\x03\x10V[a\x00\xdfa\x01\x9b6`\x04a\x05KV[a\x03\x1dV[a\x00\xdfa\x01\xae6`\x04a\x05KV[a\x03TV[a\x00\xf8a\x01\xc16`\x04a\x05\xd3V[`\x01` \x90\x81R`\x00\x92\x83R`@\x80\x84 \x90\x91R\x90\x82R\x90 T\x81V[`\x03\x80Ta\x01\xeb\x90a\x06\x06V[\x80`\x1f\x01` \x80\x91\x04\x02` \x01`@Q\x90\x81\x01`@R\x80\x92\x91\x90\x81\x81R` \x01\x82\x80Ta\x02\x17\x90a\x06\x06V[\x80\x15a\x02dW\x80`\x1f\x10a\x029Wa\x01\x00\x80\x83T\x04\x02\x83R\x91` \x01\x91a\x02dV[\x82\x01\x91\x90`\x00R` `\x00 \x90[\x81T\x81R\x90`\x01\x01\x90` \x01\x80\x83\x11a\x02GW\x82\x90\x03`\x1f\x16\x82\x01\x91[PPPPP\x81V[`\x00a\x02y3\x84\x84a\x03aV[P`\x01\x92\x91PPV[`\x01`\x01`\xa0\x1b\x03\x83\x16`\x00\x90\x81R`\x01` \x90\x81R`@\x80\x83 3\x84R\x90\x91R\x81 T`\x00\x19\x81\x14a\x02\xc3Wa\x02\xc3\x853a\x02\xbe\x86\x85a\x06WV[a\x03aV[a\x02\xce\x85\x85\x85a\x03\xfeV[P`\x01\x94\x93PPPPV[3`\x00\x81\x81R`\x01` \x90\x81R`@\x80\x83 `\x01`\x01`\xa0\x1b\x03\x87\x16\x84R\x90\x91R\x81 T\x90\x91a\x02y\x91\x85\x90a\x02\xbe\x90\x86\x90a\x06nV[`\x04\x80Ta\x01\xeb\x90a\x06\x06V[3`\x00\x81\x81R`\x01` \x90\x81R`@\x80\x83 `\x01`\x01`\xa0\x1b\x03\x87\x16\x84R\x90\x91R\x81 T\x90\x91a\x02y\x91\x85\x90a\x02\xbe\x90\x86\x90a\x06WV[`\x00a\x02y3\x84\x84a\x03\xfeV[`\x01`\x01`\xa0\x1b\x03\x83\x16\x15\x80a\x03~WP`\x01`\x01`\xa0\x1b\x03\x82\x16\x15[\x15a\x03\x9cW`@Qc\r\xa3\x0fe`\xe3\x1b\x81R`\x04\x01`@Q\x80\x91\x03\x90\xfd[`\x01`\x01`\xa0\x1b\x03\x83\x81\x16`\x00\x81\x81R`\x01` \x90\x81R`@\x80\x83 \x94\x87\x16\x80\x84R\x94\x82R\x91\x82\x90 \x85\x90U\x90Q\x84\x81R\x7f\x8c[\xe1\xe5\xeb\xec}[\xd1OqB}\x1e\x84\xf3\xdd\x03\x14\xc0\xf7\xb2)\x1e[ \n\xc8\xc7\xc3\xb9%\x91\x01[`@Q\x80\x91\x03\x90\xa3PPPV[`\x01`\x01`\xa0\x1b\x03\x83\x16\x15\x80a\x04\x1bWP`\x01`\x01`\xa0\x1b\x03\x82\x16\x15[\x15a\x049W`@Qc\r\xa3\x0fe`\xe3\x1b\x81R`\x04\x01`@Q\x80\x91\x03\x90\xfd[`\x01`\x01`\xa0\x1b\x03\x83\x16`\x00\x90\x81R` \x81\x90R`@\x81 \x80T\x83\x92\x90a\x04a\x90\x84\x90a\x06WV[\x90\x91UPP`\x01`\x01`\xa0\x1b\x03\x82\x16`\x00\x90\x81R` \x81\x90R`@\x81 \x80T\x83\x92\x90a\x04\x8e\x90\x84\x90a\x06nV[\x92PP\x81\x90UP\x81`\x01`\x01`\xa0\x1b\x03\x16\x83`\x01`\x01`\xa0\x1b\x03\x16\x7f\xdd\xf2R\xad\x1b\xe2\xc8\x9bi\xc2\xb0h\xfc7\x8d\xaa\x95+\xa7\xf1c\xc4\xa1\x16(\xf5ZM\xf5#\xb3\xef\x83`@Qa\x03\xf1\x91\x81R` \x01\x90V[`\x00` \x80\x83R\x83Q\x80\x82\x85\x01R`\x00[\x81\x81\x10\x15a\x05\x07W\x85\x81\x01\x83\x01Q\x85\x82\x01`@\x01R\x82\x01a\x04\xebV[\x81\x81\x11\x15a\x05\x19W`\x00`@\x83\x87\x01\x01R[P`\x1f\x01`\x1f\x19\x16\x92\x90\x92\x01`@\x01\x93\x92PPPV[\x805`\x01`\x01`\xa0\x1b\x03\x81\x16\x81\x14a\x05FW`\x00\x80\xfd[\x91\x90PV[`\x00\x80`@\x83\x85\x03\x12\x15a\x05^W`\x00\x80\xfd[a\x05g\x83a\x05/V[\x94` \x93\x90\x93\x015\x93PPPV[`\x00\x80`\x00``\x84\x86\x03\x12\x15a\x05\x8aW`\x00\x80\xfd[a\x05\x93\x84a\x05/V[\x92Pa\x05\xa1` \x85\x01a\x05/V[\x91P`@\x84\x015\x90P\x92P\x92P\x92V[`\x00` \x82\x84\x03\x12\x15a\x05\xc3W`\x00\x80\xfd[a\x05\xcc\x82a\x05/V[\x93\x92PPPV[`\x00\x80`@\x83\x85\x03\x12\x15a\x05\xe6W`\x00\x80\xfd[a\x05\xef\x83a\x05/V[\x91Pa\x05\xfd` \x84\x01a\x05/V[\x90P\x92P\x92\x90PV[`\x01\x81\x81\x1c\x90\x82\x16\x80a\x06\x1aW`\x7f\x82\x16\x91P[` \x82\x10\x81\x14\x15a\x06;WcNH{q`\xe0\x1b`\x00R`"`\x04R`$`\x00\xfd[P\x91\x90PV[cNH{q`\xe0\x1b`\x00R`\x11`\x04R`$`\x00\xfd[`\x00\x82\x82\x10\x15a\x06iWa\x06ia\x06AV[P\x03\x90V[`\x00\x82\x19\x82\x11\x15a\x06\x81Wa\x06\x81a\x06AV[P\x01\x90V\xfe\xa2dipfsX"\x12 p\x02\xb4;\xe3\xbc4x\xfa*\x9d\xc0\x8f\xd5.H\xc4\x9e-\xc5@\x88L}\xae\xaf\x85\xaepm\x01\x10dsolcC\x00\x08\t\x003'

    @classmethod
    def deploy(cls, name_: str, symbol_: str, decimals_: uint8, *, from_: Optional[Union[Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max") -> ERC20:
        """
        Args:
            name_: string
            symbol_: string
            decimals_: uint8
        """
        return cls._deploy([name_, symbol_, decimals_], from_, value, gas_limit)

    @overload
    def balanceOf(self, key0: Address, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> uint256:
        ...

    @overload
    def balanceOf(self, key0: Address, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def balanceOf(self, key0: Address, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[uint256, TransactionObject]:
        """
        Args:
            key0: mapping(address => uint256)
        Returns:
            uint256
        """
        return self._transact("70a08231", [key0], return_tx, request_type, uint256, from_, to, value, gas_limit) if not request_type == 'call' else self._call("70a08231", [key0], return_tx, uint256, from_, to, value, gas_limit)

    @overload
    def allowance(self, key0: Address, key1: Address, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> uint256:
        ...

    @overload
    def allowance(self, key0: Address, key1: Address, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def allowance(self, key0: Address, key1: Address, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[uint256, TransactionObject]:
        """
        Args:
            key0: mapping(address => mapping(address => uint256))
            key1: mapping(address => uint256)
        Returns:
            uint256
        """
        return self._transact("dd62ed3e", [key0, key1], return_tx, request_type, uint256, from_, to, value, gas_limit) if not request_type == 'call' else self._call("dd62ed3e", [key0, key1], return_tx, uint256, from_, to, value, gas_limit)

    @overload
    def totalSupply(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> uint256:
        ...

    @overload
    def totalSupply(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def totalSupply(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[uint256, TransactionObject]:
        """
        Returns:
            uint256
        """
        return self._transact("18160ddd", [], return_tx, request_type, uint256, from_, to, value, gas_limit) if not request_type == 'call' else self._call("18160ddd", [], return_tx, uint256, from_, to, value, gas_limit)

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
    def decimals(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> uint8:
        ...

    @overload
    def decimals(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def decimals(self, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[uint8, TransactionObject]:
        """
        Returns:
            uint8
        """
        return self._transact("313ce567", [], return_tx, request_type, uint8, from_, to, value, gas_limit) if not request_type == 'call' else self._call("313ce567", [], return_tx, uint8, from_, to, value, gas_limit)

    @overload
    def transfer(self, recipient: Address, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def transfer(self, recipient: Address, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def transfer(self, recipient: Address, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[bool, TransactionObject]:
        """
        Args:
            recipient: address
            amount: uint256
        Returns:
            bool
        """
        return self._transact("a9059cbb", [recipient, amount], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("a9059cbb", [recipient, amount], return_tx, bool, from_, to, value, gas_limit)

    @overload
    def approve(self, spender: Address, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def approve(self, spender: Address, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def approve(self, spender: Address, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[bool, TransactionObject]:
        """
        Args:
            spender: address
            amount: uint256
        Returns:
            bool
        """
        return self._transact("095ea7b3", [spender, amount], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("095ea7b3", [spender, amount], return_tx, bool, from_, to, value, gas_limit)

    @overload
    def transferFrom(self, sender: Address, recipient: Address, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def transferFrom(self, sender: Address, recipient: Address, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def transferFrom(self, sender: Address, recipient: Address, amount: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[bool, TransactionObject]:
        """
        Args:
            sender: address
            recipient: address
            amount: uint256
        Returns:
            bool
        """
        return self._transact("23b872dd", [sender, recipient, amount], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("23b872dd", [sender, recipient, amount], return_tx, bool, from_, to, value, gas_limit)

    @overload
    def increaseAllowance(self, spender: Address, addedValue: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def increaseAllowance(self, spender: Address, addedValue: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def increaseAllowance(self, spender: Address, addedValue: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[bool, TransactionObject]:
        """
        Args:
            spender: address
            addedValue: uint256
        Returns:
            bool
        """
        return self._transact("39509351", [spender, addedValue], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("39509351", [spender, addedValue], return_tx, bool, from_, to, value, gas_limit)

    @overload
    def decreaseAllowance(self, spender: Address, subtractedValue: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def decreaseAllowance(self, spender: Address, subtractedValue: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def decreaseAllowance(self, spender: Address, subtractedValue: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[bool, TransactionObject]:
        """
        Args:
            spender: address
            subtractedValue: uint256
        Returns:
            bool
        """
        return self._transact("a457c2d7", [spender, subtractedValue], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("a457c2d7", [spender, subtractedValue], return_tx, bool, from_, to, value, gas_limit)

