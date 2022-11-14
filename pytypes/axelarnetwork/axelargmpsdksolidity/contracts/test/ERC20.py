from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.contract import Contract, Library, TransactionObject, Address, Wei

from woke.testing.abi_to_type import RequestType
from enum import IntEnum

from pytypes.axelarnetwork.axelargmpsdksolidity.contracts.interfaces.IERC20 import IERC20

from woke.testing.primitive_types import uint256
from woke.testing.primitive_types import uint8


class ERC20(IERC20):
    _abi = {'constructor': {'inputs': [{'internalType': 'string', 'name': 'name_', 'type': 'string'}, {'internalType': 'string', 'name': 'symbol_', 'type': 'string'}, {'internalType': 'uint8', 'name': 'decimals_', 'type': 'uint8'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'm\x18{(': {'inputs': [], 'name': 'InvalidAccount', 'type': 'error'}, b'\x8c[\xe1\xe5\xeb\xec}[\xd1OqB}\x1e\x84\xf3\xdd\x03\x14\xc0\xf7\xb2)\x1e[ \n\xc8\xc7\xc3\xb9%': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, b'\xdd\xf2R\xad\x1b\xe2\xc8\x9bi\xc2\xb0h\xfc7\x8d\xaa\x95+\xa7\xf1c\xc4\xa1\x16(\xf5ZM\xf5#\xb3\xef': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, b'\xddb\xed>': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\t^\xa7\xb3': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'1<\xe5g': {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa4W\xc2\xd7': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'subtractedValue', 'type': 'uint256'}], 'name': 'decreaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'9P\x93Q': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'addedValue', 'type': 'uint256'}], 'name': 'increaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x06\xfd\xde\x03': {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x95\xd8\x9bA': {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x18\x16\r\xdd': {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa9\x05\x9c\xbb': {'inputs': [{'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'#\xb8r\xdd': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _bytecode = "60a06040523480156200001157600080fd5b506040516200097c3803806200097c8339810160408190526200003491620001e2565b8251620000499060039060208601906200006f565b5081516200005f9060049060208501906200006f565b5060ff1660805250620002a49050565b8280546200007d9062000267565b90600052602060002090601f016020900481019282620000a15760008555620000ec565b82601f10620000bc57805160ff1916838001178555620000ec565b82800160010185558215620000ec579182015b82811115620000ec578251825591602001919060010190620000cf565b50620000fa929150620000fe565b5090565b5b80821115620000fa5760008155600101620000ff565b634e487b7160e01b600052604160045260246000fd5b600082601f8301126200013d57600080fd5b81516001600160401b03808211156200015a576200015a62000115565b604051601f8301601f19908116603f0116810190828211818310171562000185576200018562000115565b81604052838152602092508683858801011115620001a257600080fd5b600091505b83821015620001c65785820183015181830184015290820190620001a7565b83821115620001d85760008385830101525b9695505050505050565b600080600060608486031215620001f857600080fd5b83516001600160401b03808211156200021057600080fd5b6200021e878388016200012b565b945060208601519150808211156200023557600080fd5b5062000244868287016200012b565b925050604084015160ff811681146200025c57600080fd5b809150509250925092565b600181811c908216806200027c57607f821691505b602082108114156200029e57634e487b7160e01b600052602260045260246000fd5b50919050565b6080516106bc620002c0600039600061011e01526106bc6000f3fe608060405234801561001057600080fd5b50600436106100a95760003560e01c80633950935111610071578063395093511461015257806370a082311461016557806395d89b4114610185578063a457c2d71461018d578063a9059cbb146101a0578063dd62ed3e146101b357600080fd5b806306fdde03146100ae578063095ea7b3146100cc57806318160ddd146100ef57806323b872dd14610106578063313ce56714610119575b600080fd5b6100b66101de565b6040516100c391906104da565b60405180910390f35b6100df6100da36600461054b565b61026c565b60405190151581526020016100c3565b6100f860025481565b6040519081526020016100c3565b6100df610114366004610575565b610282565b6101407f000000000000000000000000000000000000000000000000000000000000000081565b60405160ff90911681526020016100c3565b6100df61016036600461054b565b6102d9565b6100f86101733660046105b1565b60006020819052908152604090205481565b6100b6610310565b6100df61019b36600461054b565b61031d565b6100df6101ae36600461054b565b610354565b6100f86101c13660046105d3565b600160209081526000928352604080842090915290825290205481565b600380546101eb90610606565b80601f016020809104026020016040519081016040528092919081815260200182805461021790610606565b80156102645780601f1061023957610100808354040283529160200191610264565b820191906000526020600020905b81548152906001019060200180831161024757829003601f168201915b505050505081565b6000610279338484610361565b50600192915050565b6001600160a01b038316600090815260016020908152604080832033845290915281205460001981146102c3576102c385336102be8685610657565b610361565b6102ce8585856103fe565b506001949350505050565b3360008181526001602090815260408083206001600160a01b038716845290915281205490916102799185906102be90869061066e565b600480546101eb90610606565b3360008181526001602090815260408083206001600160a01b038716845290915281205490916102799185906102be908690610657565b60006102793384846103fe565b6001600160a01b038316158061037e57506001600160a01b038216155b1561039c57604051630da30f6560e31b815260040160405180910390fd5b6001600160a01b0383811660008181526001602090815260408083209487168084529482529182902085905590518481527f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b92591015b60405180910390a3505050565b6001600160a01b038316158061041b57506001600160a01b038216155b1561043957604051630da30f6560e31b815260040160405180910390fd5b6001600160a01b03831660009081526020819052604081208054839290610461908490610657565b90915550506001600160a01b0382166000908152602081905260408120805483929061048e90849061066e565b92505081905550816001600160a01b0316836001600160a01b03167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef836040516103f191815260200190565b600060208083528351808285015260005b81811015610507578581018301518582016040015282016104eb565b81811115610519576000604083870101525b50601f01601f1916929092016040019392505050565b80356001600160a01b038116811461054657600080fd5b919050565b6000806040838503121561055e57600080fd5b6105678361052f565b946020939093013593505050565b60008060006060848603121561058a57600080fd5b6105938461052f565b92506105a16020850161052f565b9150604084013590509250925092565b6000602082840312156105c357600080fd5b6105cc8261052f565b9392505050565b600080604083850312156105e657600080fd5b6105ef8361052f565b91506105fd6020840161052f565b90509250929050565b600181811c9082168061061a57607f821691505b6020821081141561063b57634e487b7160e01b600052602260045260246000fd5b50919050565b634e487b7160e01b600052601160045260246000fd5b60008282101561066957610669610641565b500390565b6000821982111561068157610681610641565b50019056fea26469706673582212207002b43be3bc3478fa2a9dc08fd52e48c49e2dc540884c7daeaf85ae706d011064736f6c63430008090033"

    @classmethod
    def deploy(cls, name_: str, symbol_: str, decimals_: uint8, *, from_: Optional[Union[Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max") -> ERC20:
        """
        Args:
            name_: string
            symbol_: string
            decimals_: uint8
        """
        return cls._deploy([name_, symbol_, decimals_], from_, value, gas_limit, {})

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

