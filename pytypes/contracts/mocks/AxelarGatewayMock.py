from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.contract import Contract, TransactionObject, Address, Wei

from enum import IntEnum
from woke.testing.abi_to_type import RequestType

from pytypes.axelarnetwork.axelargmpsdksolidity.contracts.interfaces.IERC20MintableBurnable import IERC20MintableBurnable

from woke.testing.primitive_types import bytes32
from woke.testing.primitive_types import uint256


class IAxelarGatewayMock(Contract):
    _abi = {b'\x9a\x8a\x05\x92': {'inputs': [], 'name': 'chainId', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x99\xda~\t': {'inputs': [{'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'contractAddress', 'type': 'string'}, {'internalType': 'string', 'name': 'sender', 'type': 'string'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}], 'name': 'executeCallContract', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf5V\xab\xd1': {'inputs': [{'internalType': 'string', 'name': 'sourceChain', 'type': 'string'}, {'internalType': 'string', 'name': 'contractAddress', 'type': 'string'}, {'internalType': 'string', 'name': 'sender', 'type': 'string'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}, {'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'executeCallContractWithToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xcd\xdf\x86\x97': {'inputs': [{'internalType': 'string', 'name': 'destinationAddress', 'type': 'string'}, {'internalType': 'string', 'name': 'symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'executeSendToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _bytecode = b''

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
    _bytecode = b'`\x80`@R4\x80\x15b\x00\x00\x11W`\x00\x80\xfd[P`@Qb\x00"B8\x03\x80b\x00"B\x839\x81\x01`@\x81\x90Rb\x00\x004\x91b\x00\x01\rV[\x80Qb\x00\x00I\x90`\x00\x90` \x84\x01\x90b\x00\x00QV[PPb\x00\x02&V[\x82\x80Tb\x00\x00_\x90b\x00\x01\xe9V[\x90`\x00R` `\x00 \x90`\x1f\x01` \x90\x04\x81\x01\x92\x82b\x00\x00\x83W`\x00\x85Ub\x00\x00\xceV[\x82`\x1f\x10b\x00\x00\x9eW\x80Q`\xff\x19\x16\x83\x80\x01\x17\x85Ub\x00\x00\xceV[\x82\x80\x01`\x01\x01\x85U\x82\x15b\x00\x00\xceW\x91\x82\x01[\x82\x81\x11\x15b\x00\x00\xceW\x82Q\x82U\x91` \x01\x91\x90`\x01\x01\x90b\x00\x00\xb1V[Pb\x00\x00\xdc\x92\x91Pb\x00\x00\xe0V[P\x90V[[\x80\x82\x11\x15b\x00\x00\xdcW`\x00\x81U`\x01\x01b\x00\x00\xe1V[cNH{q`\xe0\x1b`\x00R`A`\x04R`$`\x00\xfd[`\x00` \x80\x83\x85\x03\x12\x15b\x00\x01!W`\x00\x80\xfd[\x82Q`\x01`\x01`@\x1b\x03\x80\x82\x11\x15b\x00\x019W`\x00\x80\xfd[\x81\x85\x01\x91P\x85`\x1f\x83\x01\x12b\x00\x01NW`\x00\x80\xfd[\x81Q\x81\x81\x11\x15b\x00\x01cWb\x00\x01cb\x00\x00\xf7V[`@Q`\x1f\x82\x01`\x1f\x19\x90\x81\x16`?\x01\x16\x81\x01\x90\x83\x82\x11\x81\x83\x10\x17\x15b\x00\x01\x8eWb\x00\x01\x8eb\x00\x00\xf7V[\x81`@R\x82\x81R\x88\x86\x84\x87\x01\x01\x11\x15b\x00\x01\xa7W`\x00\x80\xfd[`\x00\x93P[\x82\x84\x10\x15b\x00\x01\xcbW\x84\x84\x01\x86\x01Q\x81\x85\x01\x87\x01R\x92\x85\x01\x92b\x00\x01\xacV[\x82\x84\x11\x15b\x00\x01\xddW`\x00\x86\x84\x83\x01\x01R[\x98\x97PPPPPPPPV[`\x01\x81\x81\x1c\x90\x82\x16\x80b\x00\x01\xfeW`\x7f\x82\x16\x91P[` \x82\x10\x81\x14\x15b\x00\x02 WcNH{q`\xe0\x1b`\x00R`"`\x04R`$`\x00\xfd[P\x91\x90PV[a \x0c\x80b\x00\x026`\x009`\x00\xf3\xfe`\x80`@R4\x80\x15a\x00\x10W`\x00\x80\xfd[P`\x046\x10a\x00\xcfW`\x005`\xe0\x1c\x80c\x9a\x8a\x05\x92\x11a\x00\x8cW\x80c\xc5\xd1N\x07\x11a\x00fW\x80c\xc5\xd1N\x07\x14a\x01\xb4W\x80c\xcd\xdf\x86\x97\x14a\x01\xc7W\x80c\xf5V\xab\xd1\x14a\x01\xdaW\x80c\xf6\xa5\xf9\xf5\x14a\x01\xedW`\x00\x80\xfd[\x80c\x9a\x8a\x05\x92\x14a\x01nW\x80c\xb5Ap\x84\x14a\x01\x83W\x80c\xbc\x00\xc2\x16\x14a\x01\x96W`\x00\x80\xfd[\x80c\x18v\xee\xd9\x14a\x00\xd4W\x80c\x1c\x92\x11_\x14a\x01\x06W\x80c&\xefi\x9d\x14a\x01\x1bW\x80c_ip\xc3\x14a\x01.W\x80ci\xf6g\xed\x14a\x01HW\x80c\x99\xda~\t\x14a\x01[W[`\x00\x80\xfd[a\x00\xf1a\x00\xe26`\x04a\x12\xbaV[`\x01\x99\x98PPPPPPPPPV[`@Q\x90\x15\x15\x81R` \x01[`@Q\x80\x91\x03\x90\xf3[a\x01\x19a\x01\x146`\x04a\x13nV[a\x02\x08V[\x00[a\x01\x19a\x01)6`\x04a\x14\x07V[a\x03FV[a\x00\xf1a\x01<6`\x04a\x14\xa9V[`\x01\x96\x95PPPPPPV[a\x01\x19a\x01V6`\x04a\x15BV[a\x06\xa2V[a\x01\x19a\x01i6`\x04a\x15\x98V[a\x07\xbaV[a\x01va\x08pV[`@Qa\x00\xfd\x91\x90a\x16\xb7V[a\x01\x19a\x01\x916`\x04a\x16\xd1V[a\x08\xfeV[a\x00\xf1a\x01\xa46`\x04a\x17\x9cV[`\x01\x9a\x99PPPPPPPPPPV[a\x01\x19a\x01\xc26`\x04a\x18iV[a\n\xf2V[a\x01\x19a\x01\xd56`\x04a\x18\x86V[a\x0c\xbaV[a\x01\x19a\x01\xe86`\x04a\x18\xf9V[a\r\xbcV[a\x00\xf1a\x01\xfb6`\x04a\x19\xf5V[`\x01\x97\x96PPPPPPPV[`\x00`@Q` \x01a\x02\x1a\x91\x90a\x1bfV[`@Q` \x81\x83\x03\x03\x81R\x90`@R\x80Q\x90` \x01 \x86\x86`@Q` \x01a\x02C\x92\x91\x90a\x1b\xa2V[`@Q` \x81\x83\x03\x03\x81R\x90`@R\x80Q\x90` \x01 \x14\x15a\x02\x80W`@QbF\x1b\xcd`\xe5\x1b\x81R`\x04\x01a\x02w\x90a\x1b\xbeV[`@Q\x80\x91\x03\x90\xfd[`\x00`\x01\x87\x87`@Qa\x02\x94\x92\x91\x90a\x1b\xebV[\x90\x81R`@Q\x90\x81\x90\x03` \x01\x90 T`\x01`\x01`\xa0\x1b\x03\x16\x90P\x80a\x02\xccW`@QbF\x1b\xcd`\xe5\x1b\x81R`\x04\x01a\x02w\x90a\x1b\xfbV[`\x01`\x01`\xa0\x1b\x03\x81\x16c\x99\xda~\t`\x00\x87\x87a\x02\xe83a\x0f1V[\x88\x88`@Q\x87c\xff\xff\xff\xff\x16`\xe0\x1b\x81R`\x04\x01a\x03\x0b\x96\x95\x94\x93\x92\x91\x90a\x1c)V[`\x00`@Q\x80\x83\x03\x81`\x00\x87\x80;\x15\x80\x15a\x03%W`\x00\x80\xfd[PZ\xf1\x15\x80\x15a\x039W=`\x00\x80>=`\x00\xfd[PPPPPPPPPPPV[`\x00`@Q` \x01a\x03X\x91\x90a\x1bfV[`@Q` \x81\x83\x03\x03\x81R\x90`@R\x80Q\x90` \x01 \x87\x87`@Q` \x01a\x03\x81\x92\x91\x90a\x1b\xa2V[`@Q` \x81\x83\x03\x03\x81R\x90`@R\x80Q\x90` \x01 \x14\x15a\x03\xb5W`@QbF\x1b\xcd`\xe5\x1b\x81R`\x04\x01a\x02w\x90a\x1b\xbeV[`\x00`\x01\x88\x88`@Qa\x03\xc9\x92\x91\x90a\x1b\xebV[\x90\x81R`@Q\x90\x81\x90\x03` \x01\x90 T`\x01`\x01`\xa0\x1b\x03\x16\x90P\x80a\x04\x01W`@QbF\x1b\xcd`\xe5\x1b\x81R`\x04\x01a\x02w\x90a\x1b\xfbV[`\x00`\x02\x85\x85`@Qa\x04\x15\x92\x91\x90a\x1b\xebV[\x90\x81R`@Q\x90\x81\x90\x03` \x01\x90 T`\x01`\x01`\xa0\x1b\x03\x16\x90P\x80a\x04MW`@QbF\x1b\xcd`\xe5\x1b\x81R`\x04\x01a\x02w\x90a\x1c\x85V[`@Qcp\xa0\x821`\xe0\x1b\x81R3`\x04\x82\x01R\x83\x90`\x01`\x01`\xa0\x1b\x03\x83\x16\x90cp\xa0\x821\x90`$\x01` `@Q\x80\x83\x03\x81\x86\x80;\x15\x80\x15a\x04\x8eW`\x00\x80\xfd[PZ\xfa\x15\x80\x15a\x04\xa2W=`\x00\x80>=`\x00\xfd[PPPP`@Q=`\x1f\x19`\x1f\x82\x01\x16\x82\x01\x80`@RP\x81\x01\x90a\x04\xc6\x91\x90a\x1c\xb3V[\x10\x15a\x05\x0bW`@QbF\x1b\xcd`\xe5\x1b\x81R` `\x04\x82\x01R`\x14`$\x82\x01RsINSUFFICIENT_BALANCE``\x1b`D\x82\x01R`d\x01a\x02wV[`@Qcn\xb1v\x9f`\xe1\x1b\x81R3`\x04\x82\x01R0`$\x82\x01R\x83\x90`\x01`\x01`\xa0\x1b\x03\x83\x16\x90c\xddb\xed>\x90`D\x01` `@Q\x80\x83\x03\x81\x86\x80;\x15\x80\x15a\x05RW`\x00\x80\xfd[PZ\xfa\x15\x80\x15a\x05fW=`\x00\x80>=`\x00\xfd[PPPP`@Q=`\x1f\x19`\x1f\x82\x01\x16\x82\x01\x80`@RP\x81\x01\x90a\x05\x8a\x91\x90a\x1c\xb3V[\x10\x15a\x05\xd1W`@QbF\x1b\xcd`\xe5\x1b\x81R` `\x04\x82\x01R`\x16`$\x82\x01RuINSUFFICIENT_ALLOWANCE`P\x1b`D\x82\x01R`d\x01a\x02wV[`@Qc\'p\xa7\xeb`\xe2\x1b\x81R3`\x04\x82\x01R`$\x81\x01\x84\x90R`\x01`\x01`\xa0\x1b\x03\x82\x16\x90c\x9d\xc2\x9f\xac\x90`D\x01`\x00`@Q\x80\x83\x03\x81`\x00\x87\x80;\x15\x80\x15a\x06\x19W`\x00\x80\xfd[PZ\xf1\x15\x80\x15a\x06-W=`\x00\x80>=`\x00\xfd[PP`@Qc\xcd\xdf\x86\x97`\xe0\x1b\x81R`\x01`\x01`\xa0\x1b\x03\x85\x16\x92Pc\xcd\xdf\x86\x97\x91Pa\x06e\x90\x8a\x90\x8a\x90\x8a\x90\x8a\x90\x8a\x90`\x04\x01a\x1c\xccV[`\x00`@Q\x80\x83\x03\x81`\x00\x87\x80;\x15\x80\x15a\x06\x7fW`\x00\x80\xfd[PZ\xf1\x15\x80\x15a\x06\x93W=`\x00\x80>=`\x00\xfd[PPPPPPPPPPPPPV[`\x01`\x01`\xa0\x1b\x03\x81\x16a\x06\xf0W`@QbF\x1b\xcd`\xe5\x1b\x81R` `\x04\x82\x01R`\x15`$\x82\x01RtINVALID_TOKEN_ADDRESS`X\x1b`D\x82\x01R`d\x01a\x02wV[`\x00`\x01`\x01`\xa0\x1b\x03\x16`\x02\x84\x84`@Qa\x07\r\x92\x91\x90a\x1b\xebV[\x90\x81R`@Q\x90\x81\x90\x03` \x01\x90 T`\x01`\x01`\xa0\x1b\x03\x16\x14a\x07sW`@QbF\x1b\xcd`\xe5\x1b\x81R` `\x04\x82\x01R`\x18`$\x82\x01R\x7fTOKEN_ALREADY_REGISTERED\x00\x00\x00\x00\x00\x00\x00\x00`D\x82\x01R`d\x01a\x02wV[\x80`\x02\x84\x84`@Qa\x07\x86\x92\x91\x90a\x1b\xebV[\x90\x81R`@Q\x90\x81\x90\x03` \x01\x90 \x80T`\x01`\x01`\xa0\x1b\x03\x92\x90\x92\x16`\x01`\x01`\xa0\x1b\x03\x19\x90\x92\x16\x91\x90\x91\x17\x90UPPPV[a\x07\xf9\x86\x86\x80\x80`\x1f\x01` \x80\x91\x04\x02` \x01`@Q\x90\x81\x01`@R\x80\x93\x92\x91\x90\x81\x81R` \x01\x83\x83\x80\x82\x847`\x00\x92\x01\x91\x90\x91RPa\x11s\x92PPPV[`@Qc\t"\xc0\xcb`\xe3\x1b\x81R`\x01`\x01`\xa0\x1b\x03\x91\x90\x91\x16\x90cI\x16\x06X\x90a\x084\x90`\x00\x90\x8c\x90\x8c\x90\x8a\x90\x8a\x90\x8a\x90\x8a\x90`\x04\x01a\x1d\x06V[`\x00`@Q\x80\x83\x03\x81`\x00\x87\x80;\x15\x80\x15a\x08NW`\x00\x80\xfd[PZ\xf1\x15\x80\x15a\x08bW=`\x00\x80>=`\x00\xfd[PPPPPPPPPPPPV[`\x00\x80Ta\x08}\x90a\x1a\x8bV[\x80`\x1f\x01` \x80\x91\x04\x02` \x01`@Q\x90\x81\x01`@R\x80\x92\x91\x90\x81\x81R` \x01\x82\x80Ta\x08\xa9\x90a\x1a\x8bV[\x80\x15a\x08\xf6W\x80`\x1f\x10a\x08\xcbWa\x01\x00\x80\x83T\x04\x02\x83R\x91` \x01\x91a\x08\xf6V[\x82\x01\x91\x90`\x00R` `\x00 \x90[\x81T\x81R\x90`\x01\x01\x90` \x01\x80\x83\x11a\x08\xd9W\x82\x90\x03`\x1f\x16\x82\x01\x91[PPPPP\x81V[`\x00`@Q` \x01a\t\x10\x91\x90a\x1bfV[`@Q` \x81\x83\x03\x03\x81R\x90`@R\x80Q\x90` \x01 \x89\x89`@Q` \x01a\t9\x92\x91\x90a\x1b\xa2V[`@Q` \x81\x83\x03\x03\x81R\x90`@R\x80Q\x90` \x01 \x14\x15a\tmW`@QbF\x1b\xcd`\xe5\x1b\x81R`\x04\x01a\x02w\x90a\x1b\xbeV[`\x00`\x01\x8a\x8a`@Qa\t\x81\x92\x91\x90a\x1b\xebV[\x90\x81R`@Q\x90\x81\x90\x03` \x01\x90 T`\x01`\x01`\xa0\x1b\x03\x16\x90P\x80a\t\xb9W`@QbF\x1b\xcd`\xe5\x1b\x81R`\x04\x01a\x02w\x90a\x1b\xfbV[`\x00`\x02\x85\x85`@Qa\t\xcd\x92\x91\x90a\x1b\xebV[\x90\x81R`@Q\x90\x81\x90\x03` \x01\x90 T`\x01`\x01`\xa0\x1b\x03\x16\x90P\x80a\n\x05W`@QbF\x1b\xcd`\xe5\x1b\x81R`\x04\x01a\x02w\x90a\x1c\x85V[`@Qc\'p\xa7\xeb`\xe2\x1b\x81R3`\x04\x82\x01R`$\x81\x01\x84\x90R`\x01`\x01`\xa0\x1b\x03\x82\x16\x90c\x9d\xc2\x9f\xac\x90`D\x01`\x00`@Q\x80\x83\x03\x81`\x00\x87\x80;\x15\x80\x15a\nMW`\x00\x80\xfd[PZ\xf1\x15\x80\x15a\naW=`\x00\x80>=`\x00\xfd[PPPP\x81`\x01`\x01`\xa0\x1b\x03\x16c\xf5V\xab\xd1`\x00\x8b\x8ba\n\x8a3`\x01`\x01`\xa0\x1b\x03\x16a\x0f1V[\x8c\x8c\x8c\x8c\x8c`@Q\x8ac\xff\xff\xff\xff\x16`\xe0\x1b\x81R`\x04\x01a\n\xb3\x99\x98\x97\x96\x95\x94\x93\x92\x91\x90a\x1dVV[`\x00`@Q\x80\x83\x03\x81`\x00\x87\x80;\x15\x80\x15a\n\xcdW`\x00\x80\xfd[PZ\xf1\x15\x80\x15a\n\xe1W=`\x00\x80>=`\x00\xfd[PPPPPPPPPPPPPPPV[`\x00`@Q` \x01a\x0b\x04\x91\x90a\x1bfV[`@Q` \x81\x83\x03\x03\x81R\x90`@R\x80Q\x90` \x01 \x81`\x01`\x01`\xa0\x1b\x03\x16c\x9a\x8a\x05\x92`@Q\x81c\xff\xff\xff\xff\x16`\xe0\x1b\x81R`\x04\x01`\x00`@Q\x80\x83\x03\x81\x86\x80;\x15\x80\x15a\x0bSW`\x00\x80\xfd[PZ\xfa\x15\x80\x15a\x0bgW=`\x00\x80>=`\x00\xfd[PPPP`@Q=`\x00\x82>`\x1f=\x90\x81\x01`\x1f\x19\x16\x82\x01`@Ra\x0b\x8f\x91\x90\x81\x01\x90a\x1d\xe7V[`@Q` \x01a\x0b\x9f\x91\x90a\x16\xb7V[`@Q` \x81\x83\x03\x03\x81R\x90`@R\x80Q\x90` \x01 \x14\x15a\x0c\x03W`@QbF\x1b\xcd`\xe5\x1b\x81R` `\x04\x82\x01R`\x18`$\x82\x01R\x7fCHAIN_ALREADY_REGISTERED\x00\x00\x00\x00\x00\x00\x00\x00`D\x82\x01R`d\x01a\x02wV[\x80`\x01\x82`\x01`\x01`\xa0\x1b\x03\x16c\x9a\x8a\x05\x92`@Q\x81c\xff\xff\xff\xff\x16`\xe0\x1b\x81R`\x04\x01`\x00`@Q\x80\x83\x03\x81\x86\x80;\x15\x80\x15a\x0c?W`\x00\x80\xfd[PZ\xfa\x15\x80\x15a\x0cSW=`\x00\x80>=`\x00\xfd[PPPP`@Q=`\x00\x82>`\x1f=\x90\x81\x01`\x1f\x19\x16\x82\x01`@Ra\x0c{\x91\x90\x81\x01\x90a\x1d\xe7V[`@Qa\x0c\x88\x91\x90a\x1e\x93V[\x90\x81R`@Q\x90\x81\x90\x03` \x01\x90 \x80T`\x01`\x01`\xa0\x1b\x03\x92\x90\x92\x16`\x01`\x01`\xa0\x1b\x03\x19\x90\x92\x16\x91\x90\x91\x17\x90UPV[`\x00`\x02\x84\x84`@Qa\x0c\xce\x92\x91\x90a\x1b\xebV[\x90\x81R`@Q\x90\x81\x90\x03` \x01\x90 T`\x01`\x01`\xa0\x1b\x03\x16\x90P\x80a\r\x06W`@QbF\x1b\xcd`\xe5\x1b\x81R`\x04\x01a\x02w\x90a\x1c\x85V[\x80`\x01`\x01`\xa0\x1b\x03\x16c@\xc1\x0f\x19a\rT\x88\x88\x80\x80`\x1f\x01` \x80\x91\x04\x02` \x01`@Q\x90\x81\x01`@R\x80\x93\x92\x91\x90\x81\x81R` \x01\x83\x83\x80\x82\x847`\x00\x92\x01\x91\x90\x91RPa\x11s\x92PPPV[`@Q`\x01`\x01`\xe0\x1b\x03\x19`\xe0\x84\x90\x1b\x16\x81R`\x01`\x01`\xa0\x1b\x03\x90\x91\x16`\x04\x82\x01R`$\x81\x01\x85\x90R`D\x01`\x00`@Q\x80\x83\x03\x81`\x00\x87\x80;\x15\x80\x15a\r\x9cW`\x00\x80\xfd[PZ\xf1\x15\x80\x15a\r\xb0W=`\x00\x80>=`\x00\xfd[PPPPPPPPPPV[`\x00`\x02\x84\x84`@Qa\r\xd0\x92\x91\x90a\x1b\xebV[\x90\x81R`@Q\x90\x81\x90\x03` \x01\x90 T`\x01`\x01`\xa0\x1b\x03\x16\x90P\x80a\x0e\x08W`@QbF\x1b\xcd`\xe5\x1b\x81R`\x04\x01a\x02w\x90a\x1c\x85V[`\x00a\x0eI\x8b\x8b\x80\x80`\x1f\x01` \x80\x91\x04\x02` \x01`@Q\x90\x81\x01`@R\x80\x93\x92\x91\x90\x81\x81R` \x01\x83\x83\x80\x82\x847`\x00\x92\x01\x91\x90\x91RPa\x11s\x92PPPV[`@Qc@\xc1\x0f\x19`\xe0\x1b\x81R`\x01`\x01`\xa0\x1b\x03\x80\x83\x16`\x04\x83\x01R`$\x82\x01\x86\x90R\x91\x92P\x90\x83\x16\x90c@\xc1\x0f\x19\x90`D\x01`\x00`@Q\x80\x83\x03\x81`\x00\x87\x80;\x15\x80\x15a\x0e\x97W`\x00\x80\xfd[PZ\xf1\x15\x80\x15a\x0e\xabW=`\x00\x80>=`\x00\xfd[PPPP\x80`\x01`\x01`\xa0\x1b\x03\x16c\x1a\x98\xb2\xe0`\x00\x80\x1b\x8f\x8f\x8d\x8d\x8d\x8d\x8d\x8d\x8d`@Q\x8bc\xff\xff\xff\xff\x16`\xe0\x1b\x81R`\x04\x01a\x0e\xf0\x9a\x99\x98\x97\x96\x95\x94\x93\x92\x91\x90a\x1e\xafV[`\x00`@Q\x80\x83\x03\x81`\x00\x87\x80;\x15\x80\x15a\x0f\nW`\x00\x80\xfd[PZ\xf1\x15\x80\x15a\x0f\x1eW=`\x00\x80>=`\x00\xfd[PPPPPPPPPPPPPPPPPV[`@Q``\x82\x81\x1bk\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x19\x16` \x83\x01R\x90`\x00\x90`4\x01`@\x80Q`\x1f\x19\x81\x84\x03\x01\x81R\x82\x82\x01\x90\x91R`\x10\x82Ro\x18\x18\x99\x19\x9a\x1a\x9b\x1b\x9c\x1c\xb0\xb11\xb22\xb3`\x81\x1b` \x83\x01R\x80Q\x90\x92P`\x00\x90a\x0f\x97\x90`\x02a\x1f4V[a\x0f\xa2\x90`\x02a\x1fSV[`\x01`\x01`@\x1b\x03\x81\x11\x15a\x0f\xb9Wa\x0f\xb9a\x1d\xd1V[`@Q\x90\x80\x82R\x80`\x1f\x01`\x1f\x19\x16` \x01\x82\x01`@R\x80\x15a\x0f\xe3W` \x82\x01\x81\x806\x837\x01\x90P[P\x90P`\x03`\xfc\x1b\x81`\x00\x81Q\x81\x10a\x0f\xfeWa\x0f\xfea\x1fkV[` \x01\x01\x90`\x01`\x01`\xf8\x1b\x03\x19\x16\x90\x81`\x00\x1a\x90SP`\x0f`\xfb\x1b\x81`\x01\x81Q\x81\x10a\x10-Wa\x10-a\x1fkV[` \x01\x01\x90`\x01`\x01`\xf8\x1b\x03\x19\x16\x90\x81`\x00\x1a\x90SP`\x00[\x83Q\x81\x10\x15a\x11jW\x82`\x04\x85\x83\x81Q\x81\x10a\x10eWa\x10ea\x1fkV[\x01` \x01Q\x82Q`\x01`\x01`\xf8\x1b\x03\x19\x90\x91\x16\x90\x91\x1c`\xf8\x1c\x90\x81\x10a\x10\x8dWa\x10\x8da\x1fkV[\x01` \x01Q`\x01`\x01`\xf8\x1b\x03\x19\x16\x82a\x10\xa8\x83`\x02a\x1f4V[a\x10\xb3\x90`\x02a\x1fSV[\x81Q\x81\x10a\x10\xc3Wa\x10\xc3a\x1fkV[` \x01\x01\x90`\x01`\x01`\xf8\x1b\x03\x19\x16\x90\x81`\x00\x1a\x90SP\x82\x84\x82\x81Q\x81\x10a\x10\xedWa\x10\xeda\x1fkV[` \x91\x01\x01Q\x81Q`\xf8\x91\x90\x91\x1c`\x0f\x16\x90\x81\x10a\x11\rWa\x11\ra\x1fkV[\x01` \x01Q`\x01`\x01`\xf8\x1b\x03\x19\x16\x82a\x11(\x83`\x02a\x1f4V[a\x113\x90`\x03a\x1fSV[\x81Q\x81\x10a\x11CWa\x11Ca\x1fkV[` \x01\x01\x90`\x01`\x01`\xf8\x1b\x03\x19\x16\x90\x81`\x00\x1a\x90SPa\x11c\x81a\x1f\x81V[\x90Pa\x10GV[P\x94\x93PPPPV[\x80Q`\x00\x90\x82\x90`*\x14a\x11\x8aWP`\x00\x92\x91PPV[`\x00\x80`\x02[`*\x81\x10\x15a\x12hW\x83\x81\x81Q\x81\x10a\x11\xabWa\x11\xaba\x1fkV[\x01` \x01Q`\xf8\x1c\x91P`a\x82\x10\x80\x15\x90a\x11\xcaWP`f\x82`\xff\x16\x11\x15[\x15a\x11\xe1Wa\x11\xda`W\x83a\x1f\x9cV[\x91Pa\x12=V[`A\x82`\xff\x16\x10\x15\x80\x15a\x11\xf9WP`F\x82`\xff\x16\x11\x15[\x15a\x12\tWa\x11\xda`7\x83a\x1f\x9cV[`0\x82`\xff\x16\x10\x15\x80\x15a\x12!WP`9\x82`\xff\x16\x11\x15[\x15a\x121Wa\x11\xda`0\x83a\x1f\x9cV[P`\x00\x95\x94PPPPPV[`\x02a\x12J\x82`)a\x1f\xbfV[`\xff\x84\x16\x91\x1b\x1b\x92\x90\x92\x17\x91\x80a\x12`\x81a\x1f\x81V[\x91PPa\x11\x90V[P\x90\x94\x93PPPPV[`\x00\x80\x83`\x1f\x84\x01\x12a\x12\x84W`\x00\x80\xfd[P\x815`\x01`\x01`@\x1b\x03\x81\x11\x15a\x12\x9bW`\x00\x80\xfd[` \x83\x01\x91P\x83` \x82\x85\x01\x01\x11\x15a\x12\xb3W`\x00\x80\xfd[\x92P\x92\x90PV[`\x00\x80`\x00\x80`\x00\x80`\x00\x80`\x00`\xc0\x8a\x8c\x03\x12\x15a\x12\xd8W`\x00\x80\xfd[\x895\x98P` \x8a\x015`\x01`\x01`@\x1b\x03\x80\x82\x11\x15a\x12\xf6W`\x00\x80\xfd[a\x13\x02\x8d\x83\x8e\x01a\x12rV[\x90\x9aP\x98P`@\x8c\x015\x91P\x80\x82\x11\x15a\x13\x1bW`\x00\x80\xfd[a\x13\'\x8d\x83\x8e\x01a\x12rV[\x90\x98P\x96P``\x8c\x015\x95P`\x80\x8c\x015\x91P\x80\x82\x11\x15a\x13GW`\x00\x80\xfd[Pa\x13T\x8c\x82\x8d\x01a\x12rV[\x9a\x9d\x99\x9cP\x97\x9a\x96\x99\x95\x98\x94\x97\x96`\xa0\x015\x94\x93PPPPV[`\x00\x80`\x00\x80`\x00\x80``\x87\x89\x03\x12\x15a\x13\x87W`\x00\x80\xfd[\x865`\x01`\x01`@\x1b\x03\x80\x82\x11\x15a\x13\x9eW`\x00\x80\xfd[a\x13\xaa\x8a\x83\x8b\x01a\x12rV[\x90\x98P\x96P` \x89\x015\x91P\x80\x82\x11\x15a\x13\xc3W`\x00\x80\xfd[a\x13\xcf\x8a\x83\x8b\x01a\x12rV[\x90\x96P\x94P`@\x89\x015\x91P\x80\x82\x11\x15a\x13\xe8W`\x00\x80\xfd[Pa\x13\xf5\x89\x82\x8a\x01a\x12rV[\x97\x9a\x96\x99P\x94\x97P\x92\x95\x93\x94\x92PPPV[`\x00\x80`\x00\x80`\x00\x80`\x00`\x80\x88\x8a\x03\x12\x15a\x14"W`\x00\x80\xfd[\x875`\x01`\x01`@\x1b\x03\x80\x82\x11\x15a\x149W`\x00\x80\xfd[a\x14E\x8b\x83\x8c\x01a\x12rV[\x90\x99P\x97P` \x8a\x015\x91P\x80\x82\x11\x15a\x14^W`\x00\x80\xfd[a\x14j\x8b\x83\x8c\x01a\x12rV[\x90\x97P\x95P`@\x8a\x015\x91P\x80\x82\x11\x15a\x14\x83W`\x00\x80\xfd[Pa\x14\x90\x8a\x82\x8b\x01a\x12rV[\x98\x9b\x97\x9aP\x95\x98\x94\x97\x95\x96``\x90\x95\x015\x94\x93PPPPV[`\x00\x80`\x00\x80`\x00\x80`\x80\x87\x89\x03\x12\x15a\x14\xc2W`\x00\x80\xfd[\x865\x95P` \x87\x015`\x01`\x01`@\x1b\x03\x80\x82\x11\x15a\x14\xe0W`\x00\x80\xfd[a\x14\xec\x8a\x83\x8b\x01a\x12rV[\x90\x97P\x95P`@\x89\x015\x91P\x80\x82\x11\x15a\x15\x05W`\x00\x80\xfd[Pa\x15\x12\x89\x82\x8a\x01a\x12rV[\x97\x9a\x96\x99P\x94\x97\x94\x96\x95``\x90\x95\x015\x94\x93PPPPV[`\x01`\x01`\xa0\x1b\x03\x81\x16\x81\x14a\x15?W`\x00\x80\xfd[PV[`\x00\x80`\x00`@\x84\x86\x03\x12\x15a\x15WW`\x00\x80\xfd[\x835`\x01`\x01`@\x1b\x03\x81\x11\x15a\x15mW`\x00\x80\xfd[a\x15y\x86\x82\x87\x01a\x12rV[\x90\x94P\x92PP` \x84\x015a\x15\x8d\x81a\x15*V[\x80\x91PP\x92P\x92P\x92V[`\x00\x80`\x00\x80`\x00\x80`\x00\x80`\x80\x89\x8b\x03\x12\x15a\x15\xb4W`\x00\x80\xfd[\x885`\x01`\x01`@\x1b\x03\x80\x82\x11\x15a\x15\xcbW`\x00\x80\xfd[a\x15\xd7\x8c\x83\x8d\x01a\x12rV[\x90\x9aP\x98P` \x8b\x015\x91P\x80\x82\x11\x15a\x15\xf0W`\x00\x80\xfd[a\x15\xfc\x8c\x83\x8d\x01a\x12rV[\x90\x98P\x96P`@\x8b\x015\x91P\x80\x82\x11\x15a\x16\x15W`\x00\x80\xfd[a\x16!\x8c\x83\x8d\x01a\x12rV[\x90\x96P\x94P``\x8b\x015\x91P\x80\x82\x11\x15a\x16:W`\x00\x80\xfd[Pa\x16G\x8b\x82\x8c\x01a\x12rV[\x99\x9c\x98\x9bP\x96\x99P\x94\x97\x93\x96\x92\x95\x94PPPV[`\x00[\x83\x81\x10\x15a\x16vW\x81\x81\x01Q\x83\x82\x01R` \x01a\x16^V[\x83\x81\x11\x15a\x16\x85W`\x00\x84\x84\x01R[PPPPV[`\x00\x81Q\x80\x84Ra\x16\xa3\x81` \x86\x01` \x86\x01a\x16[V[`\x1f\x01`\x1f\x19\x16\x92\x90\x92\x01` \x01\x92\x91PPV[` \x81R`\x00a\x16\xca` \x83\x01\x84a\x16\x8bV[\x93\x92PPPV[`\x00\x80`\x00\x80`\x00\x80`\x00\x80`\x00`\xa0\x8a\x8c\x03\x12\x15a\x16\xefW`\x00\x80\xfd[\x895`\x01`\x01`@\x1b\x03\x80\x82\x11\x15a\x17\x06W`\x00\x80\xfd[a\x17\x12\x8d\x83\x8e\x01a\x12rV[\x90\x9bP\x99P` \x8c\x015\x91P\x80\x82\x11\x15a\x17+W`\x00\x80\xfd[a\x177\x8d\x83\x8e\x01a\x12rV[\x90\x99P\x97P`@\x8c\x015\x91P\x80\x82\x11\x15a\x17PW`\x00\x80\xfd[a\x17\\\x8d\x83\x8e\x01a\x12rV[\x90\x97P\x95P``\x8c\x015\x91P\x80\x82\x11\x15a\x17uW`\x00\x80\xfd[Pa\x17\x82\x8c\x82\x8d\x01a\x12rV[\x9a\x9d\x99\x9cP\x97\x9a\x96\x99\x95\x98\x94\x97\x96`\x80\x015\x94\x93PPPPV[`\x00\x80`\x00\x80`\x00\x80`\x00\x80`\x00\x80`\xe0\x8b\x8d\x03\x12\x15a\x17\xbbW`\x00\x80\xfd[\x8a5\x99P` \x8b\x015`\x01`\x01`@\x1b\x03\x80\x82\x11\x15a\x17\xd9W`\x00\x80\xfd[a\x17\xe5\x8e\x83\x8f\x01a\x12rV[\x90\x9bP\x99P`@\x8d\x015\x91P\x80\x82\x11\x15a\x17\xfeW`\x00\x80\xfd[a\x18\n\x8e\x83\x8f\x01a\x12rV[\x90\x99P\x97P``\x8d\x015\x91Pa\x18\x1f\x82a\x15*V[\x90\x95P`\x80\x8c\x015\x94P`\xa0\x8c\x015\x90\x80\x82\x11\x15a\x18<W`\x00\x80\xfd[Pa\x18I\x8d\x82\x8e\x01a\x12rV[\x91P\x80\x94PP\x80\x92PP`\xc0\x8b\x015\x90P\x92\x95\x98\x9b\x91\x94\x97\x9aP\x92\x95\x98PV[`\x00` \x82\x84\x03\x12\x15a\x18{W`\x00\x80\xfd[\x815a\x16\xca\x81a\x15*V[`\x00\x80`\x00\x80`\x00``\x86\x88\x03\x12\x15a\x18\x9eW`\x00\x80\xfd[\x855`\x01`\x01`@\x1b\x03\x80\x82\x11\x15a\x18\xb5W`\x00\x80\xfd[a\x18\xc1\x89\x83\x8a\x01a\x12rV[\x90\x97P\x95P` \x88\x015\x91P\x80\x82\x11\x15a\x18\xdaW`\x00\x80\xfd[Pa\x18\xe7\x88\x82\x89\x01a\x12rV[\x96\x99\x95\x98P\x96`@\x015\x94\x93PPPPV[`\x00\x80`\x00\x80`\x00\x80`\x00\x80`\x00\x80`\x00`\xc0\x8c\x8e\x03\x12\x15a\x19\x1aW`\x00\x80\xfd[`\x01`\x01`@\x1b\x03\x80\x8d5\x11\x15a\x190W`\x00\x80\xfd[a\x19=\x8e\x8e5\x8f\x01a\x12rV[\x90\x9cP\x9aP` \x8d\x015\x81\x10\x15a\x19SW`\x00\x80\xfd[a\x19c\x8e` \x8f\x015\x8f\x01a\x12rV[\x90\x9aP\x98P`@\x8d\x015\x81\x10\x15a\x19yW`\x00\x80\xfd[a\x19\x89\x8e`@\x8f\x015\x8f\x01a\x12rV[\x90\x98P\x96P``\x8d\x015\x81\x10\x15a\x19\x9fW`\x00\x80\xfd[a\x19\xaf\x8e``\x8f\x015\x8f\x01a\x12rV[\x90\x96P\x94P`\x80\x8d\x015\x81\x10\x15a\x19\xc5W`\x00\x80\xfd[Pa\x19\xd6\x8d`\x80\x8e\x015\x8e\x01a\x12rV[\x81\x94P\x80\x93PPP`\xa0\x8c\x015\x90P\x92\x95\x98\x9bP\x92\x95\x98\x9b\x90\x93\x96\x99PV[`\x00\x80`\x00\x80`\x00\x80`\x00`\xa0\x88\x8a\x03\x12\x15a\x1a\x10W`\x00\x80\xfd[\x875\x96P` \x88\x015`\x01`\x01`@\x1b\x03\x80\x82\x11\x15a\x1a.W`\x00\x80\xfd[a\x1a:\x8b\x83\x8c\x01a\x12rV[\x90\x98P\x96P`@\x8a\x015\x91P\x80\x82\x11\x15a\x1aSW`\x00\x80\xfd[Pa\x1a`\x8a\x82\x8b\x01a\x12rV[\x90\x95P\x93PP``\x88\x015a\x1at\x81a\x15*V[\x80\x92PP`\x80\x88\x015\x90P\x92\x95\x98\x91\x94\x97P\x92\x95PV[`\x01\x81\x81\x1c\x90\x82\x16\x80a\x1a\x9fW`\x7f\x82\x16\x91P[` \x82\x10\x81\x14\x15a\x1a\xc0WcNH{q`\xe0\x1b`\x00R`"`\x04R`$`\x00\xfd[P\x91\x90PV[\x80T`\x00\x90`\x01\x81\x81\x1c\x90\x80\x83\x16\x80a\x1a\xe0W`\x7f\x83\x16\x92P[` \x80\x84\x10\x82\x14\x15a\x1b\x02WcNH{q`\xe0\x1b`\x00R`"`\x04R`$`\x00\xfd[\x83\x88R` \x88\x01\x82\x80\x15a\x1b\x1dW`\x01\x81\x14a\x1b.Wa\x1bYV[`\xff\x19\x87\x16\x82R\x82\x82\x01\x97Pa\x1bYV[`\x00\x89\x81R` \x90 `\x00[\x87\x81\x10\x15a\x1bSW\x81T\x84\x82\x01R\x90\x86\x01\x90\x84\x01a\x1b:V[\x83\x01\x98PP[PPPPPPP\x92\x91PPV[` \x81R`\x00a\x16\xca` \x83\x01\x84a\x1a\xc6V[\x81\x83R\x81\x81` \x85\x017P`\x00\x82\x82\x01` \x90\x81\x01\x91\x90\x91R`\x1f\x90\x91\x01`\x1f\x19\x16\x90\x91\x01\x01\x90V[` \x81R`\x00a\x1b\xb6` \x83\x01\x84\x86a\x1byV[\x94\x93PPPPV[` \x80\x82R`\x13\x90\x82\x01Rr)\xa2\xa7*/\xaa\'\xaf\xab\xa9\'\xa7#\xaf\xa1\xa4 \xa4\xa7`i\x1b`@\x82\x01R``\x01\x90V[\x81\x83\x827`\x00\x91\x01\x90\x81R\x91\x90PV[` \x80\x82R`\x14\x90\x82\x01Rs\x10\xd2\x10RS\x97\xd3\x93\xd5\x17\xd4\x91Q\xd2T\xd5\x11T\x91Q`b\x1b`@\x82\x01R``\x01\x90V[`\x80\x81R`\x00a\x1c<`\x80\x83\x01\x89a\x1a\xc6V[\x82\x81\x03` \x84\x01Ra\x1cO\x81\x88\x8aa\x1byV[\x90P\x82\x81\x03`@\x84\x01Ra\x1cc\x81\x87a\x16\x8bV[\x90P\x82\x81\x03``\x84\x01Ra\x1cx\x81\x85\x87a\x1byV[\x99\x98PPPPPPPPPV[` \x80\x82R`\x14\x90\x82\x01Rs\x15\x13\xd2\xd1S\x97\xd3\x93\xd5\x17\xd4\x91Q\xd2T\xd5\x11T\x91Q`b\x1b`@\x82\x01R``\x01\x90V[`\x00` \x82\x84\x03\x12\x15a\x1c\xc5W`\x00\x80\xfd[PQ\x91\x90PV[``\x81R`\x00a\x1c\xe0``\x83\x01\x87\x89a\x1byV[\x82\x81\x03` \x84\x01Ra\x1c\xf3\x81\x86\x88a\x1byV[\x91PP\x82`@\x83\x01R\x96\x95PPPPPPV[\x87\x81R`\x80` \x82\x01R`\x00a\x1d `\x80\x83\x01\x88\x8aa\x1byV[\x82\x81\x03`@\x84\x01Ra\x1d3\x81\x87\x89a\x1byV[\x90P\x82\x81\x03``\x84\x01Ra\x1dH\x81\x85\x87a\x1byV[\x9a\x99PPPPPPPPPPV[`\xc0\x81R`\x00a\x1di`\xc0\x83\x01\x8ca\x1a\xc6V[\x82\x81\x03` \x84\x01Ra\x1d|\x81\x8b\x8da\x1byV[\x90P\x82\x81\x03`@\x84\x01Ra\x1d\x90\x81\x8aa\x16\x8bV[\x90P\x82\x81\x03``\x84\x01Ra\x1d\xa5\x81\x88\x8aa\x1byV[\x90P\x82\x81\x03`\x80\x84\x01Ra\x1d\xba\x81\x86\x88a\x1byV[\x91PP\x82`\xa0\x83\x01R\x9a\x99PPPPPPPPPPV[cNH{q`\xe0\x1b`\x00R`A`\x04R`$`\x00\xfd[`\x00` \x82\x84\x03\x12\x15a\x1d\xf9W`\x00\x80\xfd[\x81Q`\x01`\x01`@\x1b\x03\x80\x82\x11\x15a\x1e\x10W`\x00\x80\xfd[\x81\x84\x01\x91P\x84`\x1f\x83\x01\x12a\x1e$W`\x00\x80\xfd[\x81Q\x81\x81\x11\x15a\x1e6Wa\x1e6a\x1d\xd1V[`@Q`\x1f\x82\x01`\x1f\x19\x90\x81\x16`?\x01\x16\x81\x01\x90\x83\x82\x11\x81\x83\x10\x17\x15a\x1e^Wa\x1e^a\x1d\xd1V[\x81`@R\x82\x81R\x87` \x84\x87\x01\x01\x11\x15a\x1ewW`\x00\x80\xfd[a\x1e\x88\x83` \x83\x01` \x88\x01a\x16[V[\x97\x96PPPPPPPV[`\x00\x82Qa\x1e\xa5\x81\x84` \x87\x01a\x16[V[\x91\x90\x91\x01\x92\x91PPV[\x8a\x81R`\xc0` \x82\x01R`\x00a\x1e\xc9`\xc0\x83\x01\x8b\x8da\x1byV[\x82\x81\x03`@\x84\x01Ra\x1e\xdc\x81\x8a\x8ca\x1byV[\x90P\x82\x81\x03``\x84\x01Ra\x1e\xf1\x81\x88\x8aa\x1byV[\x90P\x82\x81\x03`\x80\x84\x01Ra\x1f\x06\x81\x86\x88a\x1byV[\x91PP\x82`\xa0\x83\x01R\x9b\x9aPPPPPPPPPPPV[cNH{q`\xe0\x1b`\x00R`\x11`\x04R`$`\x00\xfd[`\x00\x81`\x00\x19\x04\x83\x11\x82\x15\x15\x16\x15a\x1fNWa\x1fNa\x1f\x1eV[P\x02\x90V[`\x00\x82\x19\x82\x11\x15a\x1ffWa\x1ffa\x1f\x1eV[P\x01\x90V[cNH{q`\xe0\x1b`\x00R`2`\x04R`$`\x00\xfd[`\x00`\x00\x19\x82\x14\x15a\x1f\x95Wa\x1f\x95a\x1f\x1eV[P`\x01\x01\x90V[`\x00`\xff\x82\x16`\xff\x84\x16\x80\x82\x10\x15a\x1f\xb6Wa\x1f\xb6a\x1f\x1eV[\x90\x03\x93\x92PPPV[`\x00\x82\x82\x10\x15a\x1f\xd1Wa\x1f\xd1a\x1f\x1eV[P\x03\x90V\xfe\xa2dipfsX"\x12 \x8dU\xd4SI\xcc\xf2\x01\x88\x8c\x10J\x96{ \xa5\xd8\x8b\xc4\x8acb\x83\xea\xa1\xbb\x11\'\xd3U\xea\xa7dsolcC\x00\x08\t\x003'

    @classmethod
    def deploy(cls, chain: str, *, from_: Optional[Union[Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max") -> AxelarGatewayMock:
        """
        Args:
            chain: string
        """
        return cls._deploy([chain], from_, value, gas_limit)

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

