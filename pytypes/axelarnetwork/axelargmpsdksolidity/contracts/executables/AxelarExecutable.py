from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.contract import Contract, TransactionObject, Address, Wei

from woke.testing.abi_to_type import RequestType
from enum import IntEnum

from pytypes.axelarnetwork.axelargmpsdksolidity.contracts.interfaces.IAxelarExecutable import IAxelarExecutable
from pytypes.axelarnetwork.axelargmpsdksolidity.contracts.interfaces.IAxelarGateway import IAxelarGateway

from woke.testing.primitive_types import uint256
from woke.testing.primitive_types import bytes32


class AxelarExecutable(IAxelarExecutable):
    _abi = {'constructor': {'inputs': [{'internalType': 'address', 'name': 'gateway_', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\xe6\xc4${': {'inputs': [], 'name': 'InvalidAddress', 'type': 'error'}, b'P\x0cD\xb4': {'inputs': [], 'name': 'NotApprovedByGateway', 'type': 'error'}, b'I\x16\x06X': {'inputs': [{'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'sourceAddress', 'type': 'string'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}], 'name': 'execute', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x1a\x98\xb2\xe0': {'inputs': [{'internalType': 'bytes32', 'name': 'commandId', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'sourceAddress', 'type': 'string'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}, {'internalType': 'string', 'name': 'tokenSymbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'executeWithToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x11a\x91\xb6': {'inputs': [], 'name': 'gateway', 'outputs': [{'internalType': 'contract IAxelarGateway', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}}
    _bytecode = b'`\xa0`@R4\x80\x15a\x00\x10W`\x00\x80\xfd[P`@Qa\x06I8\x03\x80a\x06I\x839\x81\x01`@\x81\x90Ra\x00/\x91a\x00gV[`\x01`\x01`\xa0\x1b\x03\x81\x16a\x00VW`@Qc\xe6\xc4${`\xe0\x1b\x81R`\x04\x01`@Q\x80\x91\x03\x90\xfd[`\x01`\x01`\xa0\x1b\x03\x16`\x80Ra\x00\x97V[`\x00` \x82\x84\x03\x12\x15a\x00yW`\x00\x80\xfd[\x81Q`\x01`\x01`\xa0\x1b\x03\x81\x16\x81\x14a\x00\x90W`\x00\x80\xfd[\x93\x92PPPV[`\x80Qa\x05\x8ba\x00\xbe`\x009`\x00\x81\x81`K\x01R\x81\x81`\xe2\x01Ra\x01\xd4\x01Ra\x05\x8b`\x00\xf3\xfe`\x80`@R4\x80\x15a\x00\x10W`\x00\x80\xfd[P`\x046\x10a\x00AW`\x005`\xe0\x1c\x80c\x11a\x91\xb6\x14a\x00FW\x80c\x1a\x98\xb2\xe0\x14a\x00\x89W\x80cI\x16\x06X\x14a\x00\x9eW[`\x00\x80\xfd[a\x00m\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x81V[`@Q`\x01`\x01`\xa0\x1b\x03\x90\x91\x16\x81R` \x01`@Q\x80\x91\x03\x90\xf3[a\x00\x9ca\x00\x976`\x04a\x02\xd5V[a\x00\xb1V[\x00[a\x00\x9ca\x00\xac6`\x04a\x03\xafV[a\x01\xa3V[`\x00\x85\x85`@Qa\x00\xc3\x92\x91\x90a\x04SV[`@Q\x90\x81\x90\x03\x81 c\x18v\xee\xd9`\xe0\x1b\x82R\x91P`\x01`\x01`\xa0\x1b\x03\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x90c\x18v\xee\xd9\x90a\x01\'\x90\x8e\x90\x8e\x90\x8e\x90\x8e\x90\x8e\x90\x89\x90\x8d\x90\x8d\x90\x8d\x90`\x04\x01a\x04\x8cV[` `@Q\x80\x83\x03\x81`\x00\x87\x80;\x15\x80\x15a\x01AW`\x00\x80\xfd[PZ\xf1\x15\x80\x15a\x01UW=`\x00\x80>=`\x00\xfd[PPPP`@Q=`\x1f\x19`\x1f\x82\x01\x16\x82\x01\x80`@RP\x81\x01\x90a\x01y\x91\x90a\x04\xebV[a\x01\x96W`@Qc\x14\x03\x11-`\xe2\x1b\x81R`\x04\x01`@Q\x80\x91\x03\x90\xfd[PPPPPPPPPPPV[`\x00\x82\x82`@Qa\x01\xb5\x92\x91\x90a\x04SV[`@Q\x90\x81\x90\x03\x81 c_ip\xc3`\xe0\x1b\x82R\x91P`\x01`\x01`\xa0\x1b\x03\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x90c_ip\xc3\x90a\x02\x13\x90\x8b\x90\x8b\x90\x8b\x90\x8b\x90\x8b\x90\x89\x90`\x04\x01a\x05\x14V[` `@Q\x80\x83\x03\x81`\x00\x87\x80;\x15\x80\x15a\x02-W`\x00\x80\xfd[PZ\xf1\x15\x80\x15a\x02AW=`\x00\x80>=`\x00\xfd[PPPP`@Q=`\x1f\x19`\x1f\x82\x01\x16\x82\x01\x80`@RP\x81\x01\x90a\x02e\x91\x90a\x04\xebV[a\x02\x82W`@Qc\x14\x03\x11-`\xe2\x1b\x81R`\x04\x01`@Q\x80\x91\x03\x90\xfd[PPPPPPPPV[`\x00\x80\x83`\x1f\x84\x01\x12a\x02\x9eW`\x00\x80\xfd[P\x815g\xff\xff\xff\xff\xff\xff\xff\xff\x81\x11\x15a\x02\xb6W`\x00\x80\xfd[` \x83\x01\x91P\x83` \x82\x85\x01\x01\x11\x15a\x02\xceW`\x00\x80\xfd[\x92P\x92\x90PV[`\x00\x80`\x00\x80`\x00\x80`\x00\x80`\x00\x80`\xc0\x8b\x8d\x03\x12\x15a\x02\xf4W`\x00\x80\xfd[\x8a5\x99P` \x8b\x015g\xff\xff\xff\xff\xff\xff\xff\xff\x80\x82\x11\x15a\x03\x13W`\x00\x80\xfd[a\x03\x1f\x8e\x83\x8f\x01a\x02\x8cV[\x90\x9bP\x99P`@\x8d\x015\x91P\x80\x82\x11\x15a\x038W`\x00\x80\xfd[a\x03D\x8e\x83\x8f\x01a\x02\x8cV[\x90\x99P\x97P``\x8d\x015\x91P\x80\x82\x11\x15a\x03]W`\x00\x80\xfd[a\x03i\x8e\x83\x8f\x01a\x02\x8cV[\x90\x97P\x95P`\x80\x8d\x015\x91P\x80\x82\x11\x15a\x03\x82W`\x00\x80\xfd[Pa\x03\x8f\x8d\x82\x8e\x01a\x02\x8cV[\x91P\x80\x94PP\x80\x92PP`\xa0\x8b\x015\x90P\x92\x95\x98\x9b\x91\x94\x97\x9aP\x92\x95\x98PV[`\x00\x80`\x00\x80`\x00\x80`\x00`\x80\x88\x8a\x03\x12\x15a\x03\xcaW`\x00\x80\xfd[\x875\x96P` \x88\x015g\xff\xff\xff\xff\xff\xff\xff\xff\x80\x82\x11\x15a\x03\xe9W`\x00\x80\xfd[a\x03\xf5\x8b\x83\x8c\x01a\x02\x8cV[\x90\x98P\x96P`@\x8a\x015\x91P\x80\x82\x11\x15a\x04\x0eW`\x00\x80\xfd[a\x04\x1a\x8b\x83\x8c\x01a\x02\x8cV[\x90\x96P\x94P``\x8a\x015\x91P\x80\x82\x11\x15a\x043W`\x00\x80\xfd[Pa\x04@\x8a\x82\x8b\x01a\x02\x8cV[\x98\x9b\x97\x9aP\x95\x98P\x93\x96\x92\x95\x92\x93PPPV[\x81\x83\x827`\x00\x91\x01\x90\x81R\x91\x90PV[\x81\x83R\x81\x81` \x85\x017P`\x00\x82\x82\x01` \x90\x81\x01\x91\x90\x91R`\x1f\x90\x91\x01`\x1f\x19\x16\x90\x91\x01\x01\x90V[\x89\x81R`\xc0` \x82\x01R`\x00a\x04\xa6`\xc0\x83\x01\x8a\x8ca\x04cV[\x82\x81\x03`@\x84\x01Ra\x04\xb9\x81\x89\x8ba\x04cV[\x90P\x86``\x84\x01R\x82\x81\x03`\x80\x84\x01Ra\x04\xd4\x81\x86\x88a\x04cV[\x91PP\x82`\xa0\x83\x01R\x9a\x99PPPPPPPPPPV[`\x00` \x82\x84\x03\x12\x15a\x04\xfdW`\x00\x80\xfd[\x81Q\x80\x15\x15\x81\x14a\x05\rW`\x00\x80\xfd[\x93\x92PPPV[\x86\x81R`\x80` \x82\x01R`\x00a\x05.`\x80\x83\x01\x87\x89a\x04cV[\x82\x81\x03`@\x84\x01Ra\x05A\x81\x86\x88a\x04cV[\x91PP\x82``\x83\x01R\x97\x96PPPPPPPV\xfe\xa2dipfsX"\x12 v\x8d]\x1a\xa3\xe1\xfa\x10Ll\xbeD4\x9b\xaeqi\x1e\xa2\x18\x15\xbd\xf1\xcf\xa2q\x14\xc8`\x16\x06,dsolcC\x00\x08\t\x003'

    @classmethod
    def deploy(cls, gateway_: Address, *, from_: Optional[Union[Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max") -> AxelarExecutable:
        """
        Args:
            gateway_: address
        """
        return cls._deploy([gateway_], from_, value, gas_limit)

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

