from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.contract import Contract, TransactionObject, Address, Wei

from woke.testing.abi_to_type import RequestType
from enum import IntEnum

from pytypes.openzeppelin.contracts.token.ERC721.extensions.IERC721Metadata import IERC721Metadata
from pytypes.openzeppelin.contracts.utils.introspection.ERC165 import ERC165
from pytypes.openzeppelin.contracts.utils.Context import Context
from pytypes.openzeppelin.contracts.token.ERC721.IERC721 import IERC721

from woke.testing.primitive_types import uint256
from woke.testing.primitive_types import bytes4


class ERC721(IERC721Metadata, IERC721, ERC165, Context):
    _abi = {'constructor': {'inputs': [{'internalType': 'string', 'name': 'name_', 'type': 'string'}, {'internalType': 'string', 'name': 'symbol_', 'type': 'string'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\x8c[\xe1\xe5\xeb\xec}[\xd1OqB}\x1e\x84\xf3\xdd\x03\x14\xc0\xf7\xb2)\x1e[ \n\xc8\xc7\xc3\xb9%': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'approved', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, b'\x170~\xab9\xaba\x07\xe8\x89\x98E\xad=Y\xbd\x96S\xf2\x00\xf2 \x92\x04\x89\xca+Y7il1': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'ApprovalForAll', 'type': 'event'}, b'\xdd\xf2R\xad\x1b\xe2\xc8\x9bi\xc2\xb0h\xfc7\x8d\xaa\x95+\xa7\xf1c\xc4\xa1\x16(\xf5ZM\xf5#\xb3\xef': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, b'\t^\xa7\xb3': {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'approve', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x08\x18\x12\xfc': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'getApproved', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe9\x85\xe9\xc5': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'operator', 'type': 'address'}], 'name': 'isApprovedForAll', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x06\xfd\xde\x03': {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'cR!\x1e': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'ownerOf', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'B\x84.\x0e': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'safeTransferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb8\x8dO\xde': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'safeTransferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa2,\xb4e': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'setApprovalForAll', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceId', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x95\xd8\x9bA': {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc8{V\xdd': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'tokenURI', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'#\xb8r\xdd': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _bytecode = b'`\x80`@R4\x80\x15b\x00\x00\x11W`\x00\x80\xfd[P`@Qb\x00\x13\xd78\x03\x80b\x00\x13\xd7\x839\x81\x01`@\x81\x90Rb\x00\x004\x91b\x00\x01\xdbV[\x81Qb\x00\x00I\x90`\x00\x90` \x85\x01\x90b\x00\x00hV[P\x80Qb\x00\x00_\x90`\x01\x90` \x84\x01\x90b\x00\x00hV[PPPb\x00\x02\x82V[\x82\x80Tb\x00\x00v\x90b\x00\x02EV[\x90`\x00R` `\x00 \x90`\x1f\x01` \x90\x04\x81\x01\x92\x82b\x00\x00\x9aW`\x00\x85Ub\x00\x00\xe5V[\x82`\x1f\x10b\x00\x00\xb5W\x80Q`\xff\x19\x16\x83\x80\x01\x17\x85Ub\x00\x00\xe5V[\x82\x80\x01`\x01\x01\x85U\x82\x15b\x00\x00\xe5W\x91\x82\x01[\x82\x81\x11\x15b\x00\x00\xe5W\x82Q\x82U\x91` \x01\x91\x90`\x01\x01\x90b\x00\x00\xc8V[Pb\x00\x00\xf3\x92\x91Pb\x00\x00\xf7V[P\x90V[[\x80\x82\x11\x15b\x00\x00\xf3W`\x00\x81U`\x01\x01b\x00\x00\xf8V[cNH{q`\xe0\x1b`\x00R`A`\x04R`$`\x00\xfd[`\x00\x82`\x1f\x83\x01\x12b\x00\x016W`\x00\x80\xfd[\x81Q`\x01`\x01`@\x1b\x03\x80\x82\x11\x15b\x00\x01SWb\x00\x01Sb\x00\x01\x0eV[`@Q`\x1f\x83\x01`\x1f\x19\x90\x81\x16`?\x01\x16\x81\x01\x90\x82\x82\x11\x81\x83\x10\x17\x15b\x00\x01~Wb\x00\x01~b\x00\x01\x0eV[\x81`@R\x83\x81R` \x92P\x86\x83\x85\x88\x01\x01\x11\x15b\x00\x01\x9bW`\x00\x80\xfd[`\x00\x91P[\x83\x82\x10\x15b\x00\x01\xbfW\x85\x82\x01\x83\x01Q\x81\x83\x01\x84\x01R\x90\x82\x01\x90b\x00\x01\xa0V[\x83\x82\x11\x15b\x00\x01\xd1W`\x00\x83\x85\x83\x01\x01R[\x96\x95PPPPPPV[`\x00\x80`@\x83\x85\x03\x12\x15b\x00\x01\xefW`\x00\x80\xfd[\x82Q`\x01`\x01`@\x1b\x03\x80\x82\x11\x15b\x00\x02\x07W`\x00\x80\xfd[b\x00\x02\x15\x86\x83\x87\x01b\x00\x01$V[\x93P` \x85\x01Q\x91P\x80\x82\x11\x15b\x00\x02,W`\x00\x80\xfd[Pb\x00\x02;\x85\x82\x86\x01b\x00\x01$V[\x91PP\x92P\x92\x90PV[`\x01\x81\x81\x1c\x90\x82\x16\x80b\x00\x02ZW`\x7f\x82\x16\x91P[` \x82\x10\x81\x14\x15b\x00\x02|WcNH{q`\xe0\x1b`\x00R`"`\x04R`$`\x00\xfd[P\x91\x90PV[a\x11E\x80b\x00\x02\x92`\x009`\x00\xf3\xfe`\x80`@R4\x80\x15a\x00\x10W`\x00\x80\xfd[P`\x046\x10a\x00\xcfW`\x005`\xe0\x1c\x80ccR!\x1e\x11a\x00\x8cW\x80c\xa2,\xb4e\x11a\x00fW\x80c\xa2,\xb4e\x14a\x01\xb3W\x80c\xb8\x8dO\xde\x14a\x01\xc6W\x80c\xc8{V\xdd\x14a\x01\xd9W\x80c\xe9\x85\xe9\xc5\x14a\x01\xecW`\x00\x80\xfd[\x80ccR!\x1e\x14a\x01wW\x80cp\xa0\x821\x14a\x01\x8aW\x80c\x95\xd8\x9bA\x14a\x01\xabW`\x00\x80\xfd[\x80c\x01\xff\xc9\xa7\x14a\x00\xd4W\x80c\x06\xfd\xde\x03\x14a\x00\xfcW\x80c\x08\x18\x12\xfc\x14a\x01\x11W\x80c\t^\xa7\xb3\x14a\x01<W\x80c#\xb8r\xdd\x14a\x01QW\x80cB\x84.\x0e\x14a\x01dW[`\x00\x80\xfd[a\x00\xe7a\x00\xe26`\x04a\x0cXV[a\x02(V[`@Q\x90\x15\x15\x81R` \x01[`@Q\x80\x91\x03\x90\xf3[a\x01\x04a\x02zV[`@Qa\x00\xf3\x91\x90a\x0c\xcdV[a\x01$a\x01\x1f6`\x04a\x0c\xe0V[a\x03\x0cV[`@Q`\x01`\x01`\xa0\x1b\x03\x90\x91\x16\x81R` \x01a\x00\xf3V[a\x01Oa\x01J6`\x04a\r\x15V[a\x033V[\x00[a\x01Oa\x01_6`\x04a\r?V[a\x04NV[a\x01Oa\x01r6`\x04a\r?V[a\x04\x7fV[a\x01$a\x01\x856`\x04a\x0c\xe0V[a\x04\x9aV[a\x01\x9da\x01\x986`\x04a\r{V[a\x04\xfaV[`@Q\x90\x81R` \x01a\x00\xf3V[a\x01\x04a\x05\x80V[a\x01Oa\x01\xc16`\x04a\r\x96V[a\x05\x8fV[a\x01Oa\x01\xd46`\x04a\r\xe8V[a\x05\x9eV[a\x01\x04a\x01\xe76`\x04a\x0c\xe0V[a\x05\xd6V[a\x00\xe7a\x01\xfa6`\x04a\x0e\xc4V[`\x01`\x01`\xa0\x1b\x03\x91\x82\x16`\x00\x90\x81R`\x05` \x90\x81R`@\x80\x83 \x93\x90\x94\x16\x82R\x91\x90\x91R T`\xff\x16\x90V[`\x00`\x01`\x01`\xe0\x1b\x03\x19\x82\x16c\x80\xacX\xcd`\xe0\x1b\x14\x80a\x02YWP`\x01`\x01`\xe0\x1b\x03\x19\x82\x16c[^\x13\x9f`\xe0\x1b\x14[\x80a\x02tWPc\x01\xff\xc9\xa7`\xe0\x1b`\x01`\x01`\xe0\x1b\x03\x19\x83\x16\x14[\x92\x91PPV[```\x00\x80Ta\x02\x89\x90a\x0e\xf7V[\x80`\x1f\x01` \x80\x91\x04\x02` \x01`@Q\x90\x81\x01`@R\x80\x92\x91\x90\x81\x81R` \x01\x82\x80Ta\x02\xb5\x90a\x0e\xf7V[\x80\x15a\x03\x02W\x80`\x1f\x10a\x02\xd7Wa\x01\x00\x80\x83T\x04\x02\x83R\x91` \x01\x91a\x03\x02V[\x82\x01\x91\x90`\x00R` `\x00 \x90[\x81T\x81R\x90`\x01\x01\x90` \x01\x80\x83\x11a\x02\xe5W\x82\x90\x03`\x1f\x16\x82\x01\x91[PPPPP\x90P\x90V[`\x00a\x03\x17\x82a\x06JV[P`\x00\x90\x81R`\x04` R`@\x90 T`\x01`\x01`\xa0\x1b\x03\x16\x90V[`\x00a\x03>\x82a\x04\x9aV[\x90P\x80`\x01`\x01`\xa0\x1b\x03\x16\x83`\x01`\x01`\xa0\x1b\x03\x16\x14\x15a\x03\xb1W`@QbF\x1b\xcd`\xe5\x1b\x81R` `\x04\x82\x01R`!`$\x82\x01R\x7fERC721: approval to current owne`D\x82\x01R`9`\xf9\x1b`d\x82\x01R`\x84\x01[`@Q\x80\x91\x03\x90\xfd[3`\x01`\x01`\xa0\x1b\x03\x82\x16\x14\x80a\x03\xcdWPa\x03\xcd\x813a\x01\xfaV[a\x04?W`@QbF\x1b\xcd`\xe5\x1b\x81R` `\x04\x82\x01R`>`$\x82\x01R\x7fERC721: approve caller is not to`D\x82\x01R\x7fken owner nor approved for all\x00\x00`d\x82\x01R`\x84\x01a\x03\xa8V[a\x04I\x83\x83a\x06\xacV[PPPV[a\x04X3\x82a\x07\x1aV[a\x04tW`@QbF\x1b\xcd`\xe5\x1b\x81R`\x04\x01a\x03\xa8\x90a\x0f2V[a\x04I\x83\x83\x83a\x07\x99V[a\x04I\x83\x83\x83`@Q\x80` \x01`@R\x80`\x00\x81RPa\x05\x9eV[`\x00\x81\x81R`\x02` R`@\x81 T`\x01`\x01`\xa0\x1b\x03\x16\x80a\x02tW`@QbF\x1b\xcd`\xe5\x1b\x81R` `\x04\x82\x01R`\x18`$\x82\x01Rw\x11T\x90\xcd\xcc\x8cN\x88\x1a[\x9d\x98[\x1aY\x08\x1d\x1b\xda\xd9[\x88\x12Q`B\x1b`D\x82\x01R`d\x01a\x03\xa8V[`\x00`\x01`\x01`\xa0\x1b\x03\x82\x16a\x05dW`@QbF\x1b\xcd`\xe5\x1b\x81R` `\x04\x82\x01R`)`$\x82\x01R\x7fERC721: address zero is not a va`D\x82\x01Rh64\xb2\x107\xbb\xb72\xb9`\xb9\x1b`d\x82\x01R`\x84\x01a\x03\xa8V[P`\x01`\x01`\xa0\x1b\x03\x16`\x00\x90\x81R`\x03` R`@\x90 T\x90V[```\x01\x80Ta\x02\x89\x90a\x0e\xf7V[a\x05\x9a3\x83\x83a\t5V[PPV[a\x05\xa83\x83a\x07\x1aV[a\x05\xc4W`@QbF\x1b\xcd`\xe5\x1b\x81R`\x04\x01a\x03\xa8\x90a\x0f2V[a\x05\xd0\x84\x84\x84\x84a\n\x04V[PPPPV[``a\x05\xe1\x82a\x06JV[`\x00a\x05\xf8`@\x80Q` \x81\x01\x90\x91R`\x00\x81R\x90V[\x90P`\x00\x81Q\x11a\x06\x18W`@Q\x80` \x01`@R\x80`\x00\x81RPa\x06CV[\x80a\x06"\x84a\n7V[`@Q` \x01a\x063\x92\x91\x90a\x0f\x80V[`@Q` \x81\x83\x03\x03\x81R\x90`@R[\x93\x92PPPV[`\x00\x81\x81R`\x02` R`@\x90 T`\x01`\x01`\xa0\x1b\x03\x16a\x06\xa9W`@QbF\x1b\xcd`\xe5\x1b\x81R` `\x04\x82\x01R`\x18`$\x82\x01Rw\x11T\x90\xcd\xcc\x8cN\x88\x1a[\x9d\x98[\x1aY\x08\x1d\x1b\xda\xd9[\x88\x12Q`B\x1b`D\x82\x01R`d\x01a\x03\xa8V[PV[`\x00\x81\x81R`\x04` R`@\x90 \x80T`\x01`\x01`\xa0\x1b\x03\x19\x16`\x01`\x01`\xa0\x1b\x03\x84\x16\x90\x81\x17\x90\x91U\x81\x90a\x06\xe1\x82a\x04\x9aV[`\x01`\x01`\xa0\x1b\x03\x16\x7f\x8c[\xe1\xe5\xeb\xec}[\xd1OqB}\x1e\x84\xf3\xdd\x03\x14\xc0\xf7\xb2)\x1e[ \n\xc8\xc7\xc3\xb9%`@Q`@Q\x80\x91\x03\x90\xa4PPV[`\x00\x80a\x07&\x83a\x04\x9aV[\x90P\x80`\x01`\x01`\xa0\x1b\x03\x16\x84`\x01`\x01`\xa0\x1b\x03\x16\x14\x80a\x07mWP`\x01`\x01`\xa0\x1b\x03\x80\x82\x16`\x00\x90\x81R`\x05` \x90\x81R`@\x80\x83 \x93\x88\x16\x83R\x92\x90R T`\xff\x16[\x80a\x07\x91WP\x83`\x01`\x01`\xa0\x1b\x03\x16a\x07\x86\x84a\x03\x0cV[`\x01`\x01`\xa0\x1b\x03\x16\x14[\x94\x93PPPPV[\x82`\x01`\x01`\xa0\x1b\x03\x16a\x07\xac\x82a\x04\x9aV[`\x01`\x01`\xa0\x1b\x03\x16\x14a\x08\x10W`@QbF\x1b\xcd`\xe5\x1b\x81R` `\x04\x82\x01R`%`$\x82\x01R\x7fERC721: transfer from incorrect `D\x82\x01Rd7\xbb\xb72\xb9`\xd9\x1b`d\x82\x01R`\x84\x01a\x03\xa8V[`\x01`\x01`\xa0\x1b\x03\x82\x16a\x08rW`@QbF\x1b\xcd`\xe5\x1b\x81R` `\x04\x82\x01R`$\x80\x82\x01R\x7fERC721: transfer to the zero add`D\x82\x01Rcress`\xe0\x1b`d\x82\x01R`\x84\x01a\x03\xa8V[a\x08}`\x00\x82a\x06\xacV[`\x01`\x01`\xa0\x1b\x03\x83\x16`\x00\x90\x81R`\x03` R`@\x81 \x80T`\x01\x92\x90a\x08\xa6\x90\x84\x90a\x0f\xc5V[\x90\x91UPP`\x01`\x01`\xa0\x1b\x03\x82\x16`\x00\x90\x81R`\x03` R`@\x81 \x80T`\x01\x92\x90a\x08\xd4\x90\x84\x90a\x0f\xdcV[\x90\x91UPP`\x00\x81\x81R`\x02` R`@\x80\x82 \x80T`\x01`\x01`\xa0\x1b\x03\x19\x16`\x01`\x01`\xa0\x1b\x03\x86\x81\x16\x91\x82\x17\x90\x92U\x91Q\x84\x93\x91\x87\x16\x91\x7f\xdd\xf2R\xad\x1b\xe2\xc8\x9bi\xc2\xb0h\xfc7\x8d\xaa\x95+\xa7\xf1c\xc4\xa1\x16(\xf5ZM\xf5#\xb3\xef\x91\xa4PPPV[\x81`\x01`\x01`\xa0\x1b\x03\x16\x83`\x01`\x01`\xa0\x1b\x03\x16\x14\x15a\t\x97W`@QbF\x1b\xcd`\xe5\x1b\x81R` `\x04\x82\x01R`\x19`$\x82\x01R\x7fERC721: approve to caller\x00\x00\x00\x00\x00\x00\x00`D\x82\x01R`d\x01a\x03\xa8V[`\x01`\x01`\xa0\x1b\x03\x83\x81\x16`\x00\x81\x81R`\x05` \x90\x81R`@\x80\x83 \x94\x87\x16\x80\x84R\x94\x82R\x91\x82\x90 \x80T`\xff\x19\x16\x86\x15\x15\x90\x81\x17\x90\x91U\x91Q\x91\x82R\x7f\x170~\xab9\xaba\x07\xe8\x89\x98E\xad=Y\xbd\x96S\xf2\x00\xf2 \x92\x04\x89\xca+Y7il1\x91\x01`@Q\x80\x91\x03\x90\xa3PPPV[a\n\x0f\x84\x84\x84a\x07\x99V[a\n\x1b\x84\x84\x84\x84a\x0b5V[a\x05\xd0W`@QbF\x1b\xcd`\xe5\x1b\x81R`\x04\x01a\x03\xa8\x90a\x0f\xf4V[``\x81a\n[WPP`@\x80Q\x80\x82\x01\x90\x91R`\x01\x81R`\x03`\xfc\x1b` \x82\x01R\x90V[\x81`\x00[\x81\x15a\n\x85W\x80a\no\x81a\x10FV[\x91Pa\n~\x90P`\n\x83a\x10wV[\x91Pa\n_V[`\x00\x81g\xff\xff\xff\xff\xff\xff\xff\xff\x81\x11\x15a\n\xa0Wa\n\xa0a\r\xd2V[`@Q\x90\x80\x82R\x80`\x1f\x01`\x1f\x19\x16` \x01\x82\x01`@R\x80\x15a\n\xcaW` \x82\x01\x81\x806\x837\x01\x90P[P\x90P[\x84\x15a\x07\x91Wa\n\xdf`\x01\x83a\x0f\xc5V[\x91Pa\n\xec`\n\x86a\x10\x8bV[a\n\xf7\x90`0a\x0f\xdcV[`\xf8\x1b\x81\x83\x81Q\x81\x10a\x0b\x0cWa\x0b\x0ca\x10\x9fV[` \x01\x01\x90`\x01`\x01`\xf8\x1b\x03\x19\x16\x90\x81`\x00\x1a\x90SPa\x0b.`\n\x86a\x10wV[\x94Pa\n\xceV[`\x00`\x01`\x01`\xa0\x1b\x03\x84\x16;\x15a\x0c7W`@Qc\n\x85\xbd\x01`\xe1\x1b\x81R`\x01`\x01`\xa0\x1b\x03\x85\x16\x90c\x15\x0bz\x02\x90a\x0by\x903\x90\x89\x90\x88\x90\x88\x90`\x04\x01a\x10\xb5V[` `@Q\x80\x83\x03\x81`\x00\x87\x80;\x15\x80\x15a\x0b\x93W`\x00\x80\xfd[PZ\xf1\x92PPP\x80\x15a\x0b\xc3WP`@\x80Q`\x1f=\x90\x81\x01`\x1f\x19\x16\x82\x01\x90\x92Ra\x0b\xc0\x91\x81\x01\x90a\x10\xf2V[`\x01[a\x0c\x1dW=\x80\x80\x15a\x0b\xf1W`@Q\x91P`\x1f\x19`?=\x01\x16\x82\x01`@R=\x82R=`\x00` \x84\x01>a\x0b\xf6V[``\x91P[P\x80Qa\x0c\x15W`@QbF\x1b\xcd`\xe5\x1b\x81R`\x04\x01a\x03\xa8\x90a\x0f\xf4V[\x80Q\x81` \x01\xfd[`\x01`\x01`\xe0\x1b\x03\x19\x16c\n\x85\xbd\x01`\xe1\x1b\x14\x90Pa\x07\x91V[P`\x01\x94\x93PPPPV[`\x01`\x01`\xe0\x1b\x03\x19\x81\x16\x81\x14a\x06\xa9W`\x00\x80\xfd[`\x00` \x82\x84\x03\x12\x15a\x0cjW`\x00\x80\xfd[\x815a\x06C\x81a\x0cBV[`\x00[\x83\x81\x10\x15a\x0c\x90W\x81\x81\x01Q\x83\x82\x01R` \x01a\x0cxV[\x83\x81\x11\x15a\x05\xd0WPP`\x00\x91\x01RV[`\x00\x81Q\x80\x84Ra\x0c\xb9\x81` \x86\x01` \x86\x01a\x0cuV[`\x1f\x01`\x1f\x19\x16\x92\x90\x92\x01` \x01\x92\x91PPV[` \x81R`\x00a\x06C` \x83\x01\x84a\x0c\xa1V[`\x00` \x82\x84\x03\x12\x15a\x0c\xf2W`\x00\x80\xfd[P5\x91\x90PV[\x805`\x01`\x01`\xa0\x1b\x03\x81\x16\x81\x14a\r\x10W`\x00\x80\xfd[\x91\x90PV[`\x00\x80`@\x83\x85\x03\x12\x15a\r(W`\x00\x80\xfd[a\r1\x83a\x0c\xf9V[\x94` \x93\x90\x93\x015\x93PPPV[`\x00\x80`\x00``\x84\x86\x03\x12\x15a\rTW`\x00\x80\xfd[a\r]\x84a\x0c\xf9V[\x92Pa\rk` \x85\x01a\x0c\xf9V[\x91P`@\x84\x015\x90P\x92P\x92P\x92V[`\x00` \x82\x84\x03\x12\x15a\r\x8dW`\x00\x80\xfd[a\x06C\x82a\x0c\xf9V[`\x00\x80`@\x83\x85\x03\x12\x15a\r\xa9W`\x00\x80\xfd[a\r\xb2\x83a\x0c\xf9V[\x91P` \x83\x015\x80\x15\x15\x81\x14a\r\xc7W`\x00\x80\xfd[\x80\x91PP\x92P\x92\x90PV[cNH{q`\xe0\x1b`\x00R`A`\x04R`$`\x00\xfd[`\x00\x80`\x00\x80`\x80\x85\x87\x03\x12\x15a\r\xfeW`\x00\x80\xfd[a\x0e\x07\x85a\x0c\xf9V[\x93Pa\x0e\x15` \x86\x01a\x0c\xf9V[\x92P`@\x85\x015\x91P``\x85\x015g\xff\xff\xff\xff\xff\xff\xff\xff\x80\x82\x11\x15a\x0e9W`\x00\x80\xfd[\x81\x87\x01\x91P\x87`\x1f\x83\x01\x12a\x0eMW`\x00\x80\xfd[\x815\x81\x81\x11\x15a\x0e_Wa\x0e_a\r\xd2V[`@Q`\x1f\x82\x01`\x1f\x19\x90\x81\x16`?\x01\x16\x81\x01\x90\x83\x82\x11\x81\x83\x10\x17\x15a\x0e\x87Wa\x0e\x87a\r\xd2V[\x81`@R\x82\x81R\x8a` \x84\x87\x01\x01\x11\x15a\x0e\xa0W`\x00\x80\xfd[\x82` \x86\x01` \x83\x017`\x00` \x84\x83\x01\x01R\x80\x95PPPPPP\x92\x95\x91\x94P\x92PV[`\x00\x80`@\x83\x85\x03\x12\x15a\x0e\xd7W`\x00\x80\xfd[a\x0e\xe0\x83a\x0c\xf9V[\x91Pa\x0e\xee` \x84\x01a\x0c\xf9V[\x90P\x92P\x92\x90PV[`\x01\x81\x81\x1c\x90\x82\x16\x80a\x0f\x0bW`\x7f\x82\x16\x91P[` \x82\x10\x81\x14\x15a\x0f,WcNH{q`\xe0\x1b`\x00R`"`\x04R`$`\x00\xfd[P\x91\x90PV[` \x80\x82R`.\x90\x82\x01R\x7fERC721: caller is not token owne`@\x82\x01Rm\x1c\x88\x1b\x9b\xdc\x88\x18\\\x1c\x1c\x9b\xdd\x99Y`\x92\x1b``\x82\x01R`\x80\x01\x90V[`\x00\x83Qa\x0f\x92\x81\x84` \x88\x01a\x0cuV[\x83Q\x90\x83\x01\x90a\x0f\xa6\x81\x83` \x88\x01a\x0cuV[\x01\x94\x93PPPPV[cNH{q`\xe0\x1b`\x00R`\x11`\x04R`$`\x00\xfd[`\x00\x82\x82\x10\x15a\x0f\xd7Wa\x0f\xd7a\x0f\xafV[P\x03\x90V[`\x00\x82\x19\x82\x11\x15a\x0f\xefWa\x0f\xefa\x0f\xafV[P\x01\x90V[` \x80\x82R`2\x90\x82\x01R\x7fERC721: transfer to non ERC721Re`@\x82\x01Rq1\xb2\xb4\xbb2\xb9\x104\xb6\xb862\xb6\xb2\xb7:2\xb9`q\x1b``\x82\x01R`\x80\x01\x90V[`\x00`\x00\x19\x82\x14\x15a\x10ZWa\x10Za\x0f\xafV[P`\x01\x01\x90V[cNH{q`\xe0\x1b`\x00R`\x12`\x04R`$`\x00\xfd[`\x00\x82a\x10\x86Wa\x10\x86a\x10aV[P\x04\x90V[`\x00\x82a\x10\x9aWa\x10\x9aa\x10aV[P\x06\x90V[cNH{q`\xe0\x1b`\x00R`2`\x04R`$`\x00\xfd[`\x01`\x01`\xa0\x1b\x03\x85\x81\x16\x82R\x84\x16` \x82\x01R`@\x81\x01\x83\x90R`\x80``\x82\x01\x81\x90R`\x00\x90a\x10\xe8\x90\x83\x01\x84a\x0c\xa1V[\x96\x95PPPPPPV[`\x00` \x82\x84\x03\x12\x15a\x11\x04W`\x00\x80\xfd[\x81Qa\x06C\x81a\x0cBV\xfe\xa2dipfsX"\x12 E\xe2x\xb7g\t{\x946\x0c\xad\xe44@U\x83\xd5\xf5\x7f\xfb\x8a&\x8d\xad\xc9\x15\x96\xf8l?\xdb\x8adsolcC\x00\x08\t\x003'

    @classmethod
    def deploy(cls, name_: str, symbol_: str, *, from_: Optional[Union[Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max") -> ERC721:
        """
        Args:
            name_: string
            symbol_: string
        """
        return cls._deploy([name_, symbol_], from_, value, gas_limit)

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

    @overload
    def balanceOf(self, owner: Address, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> uint256:
        ...

    @overload
    def balanceOf(self, owner: Address, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def balanceOf(self, owner: Address, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[uint256, TransactionObject]:
        """
        Args:
            owner: address
        Returns:
            uint256
        """
        return self._transact("70a08231", [owner], return_tx, request_type, uint256, from_, to, value, gas_limit) if not request_type == 'call' else self._call("70a08231", [owner], return_tx, uint256, from_, to, value, gas_limit)

    @overload
    def ownerOf(self, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Address:
        ...

    @overload
    def ownerOf(self, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def ownerOf(self, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[Address, TransactionObject]:
        """
        Args:
            tokenId: uint256
        Returns:
            address
        """
        return self._transact("6352211e", [tokenId], return_tx, request_type, Address, from_, to, value, gas_limit) if not request_type == 'call' else self._call("6352211e", [tokenId], return_tx, Address, from_, to, value, gas_limit)

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

    @overload
    def approve(self, to_: Address, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def approve(self, to_: Address, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def approve(self, to_: Address, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            to_: address
            tokenId: uint256
        """
        return self._transact("095ea7b3", [to_, tokenId], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("095ea7b3", [to_, tokenId], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def getApproved(self, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Address:
        ...

    @overload
    def getApproved(self, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def getApproved(self, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[Address, TransactionObject]:
        """
        Args:
            tokenId: uint256
        Returns:
            address
        """
        return self._transact("081812fc", [tokenId], return_tx, request_type, Address, from_, to, value, gas_limit) if not request_type == 'call' else self._call("081812fc", [tokenId], return_tx, Address, from_, to, value, gas_limit)

    @overload
    def setApprovalForAll(self, operator: Address, approved: bool, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def setApprovalForAll(self, operator: Address, approved: bool, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def setApprovalForAll(self, operator: Address, approved: bool, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            operator: address
            approved: bool
        """
        return self._transact("a22cb465", [operator, approved], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("a22cb465", [operator, approved], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def isApprovedForAll(self, owner: Address, operator: Address, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> bool:
        ...

    @overload
    def isApprovedForAll(self, owner: Address, operator: Address, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def isApprovedForAll(self, owner: Address, operator: Address, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[bool, TransactionObject]:
        """
        Args:
            owner: address
            operator: address
        Returns:
            bool
        """
        return self._transact("e985e9c5", [owner, operator], return_tx, request_type, bool, from_, to, value, gas_limit) if not request_type == 'call' else self._call("e985e9c5", [owner, operator], return_tx, bool, from_, to, value, gas_limit)

    @overload
    def transferFrom(self, from__: Address, to_: Address, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def transferFrom(self, from__: Address, to_: Address, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def transferFrom(self, from__: Address, to_: Address, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            from__: address
            to_: address
            tokenId: uint256
        """
        return self._transact("23b872dd", [from__, to_, tokenId], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("23b872dd", [from__, to_, tokenId], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def safeTransferFrom(self, from__: Address, to_: Address, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def safeTransferFrom(self, from__: Address, to_: Address, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def safeTransferFrom(self, from__: Address, to_: Address, tokenId: uint256, *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            from__: address
            to_: address
            tokenId: uint256
        """
        return self._transact("42842e0e", [from__, to_, tokenId], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("42842e0e", [from__, to_, tokenId], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def safeTransferFrom(self, from__: Address, to_: Address, tokenId: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def safeTransferFrom(self, from__: Address, to_: Address, tokenId: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def safeTransferFrom(self, from__: Address, to_: Address, tokenId: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Address, str]] = None, to: Optional[Union[Address, str, Contract]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            from__: address
            to_: address
            tokenId: uint256
            data: bytes
        """
        return self._transact("b88d4fde", [from__, to_, tokenId, data], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("b88d4fde", [from__, to_, tokenId, data], return_tx, type(None), from_, to, value, gas_limit)

