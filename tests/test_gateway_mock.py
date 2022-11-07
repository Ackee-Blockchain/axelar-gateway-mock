from pytypes.contracts.mocks.AxelarGatewayMock import AxelarGatewayMock
from pytypes.contracts.ExampleContract import ExampleContract
from pytypes.node_modules.axelarnetwork.axelargmpsdksolidity.contracts.test.ERC20MintableBurnable import ERC20MintableBurnable

from woke.testing.contract import dev_interface, Address, Wei

def test_send_token():
    dev_interface.connect(8545)

    gateway1 = AxelarGatewayMock.deploy("chain1")
    gateway2 = AxelarGatewayMock.deploy("chain2")
    gateway1.registerChain(gateway2)
    gateway2.registerChain(gateway1)

    token1 = ERC20MintableBurnable.deploy("token", "TKN", 10)
    token2 = ERC20MintableBurnable.deploy("token", "TKN", 10)

    gateway1.registerToken("TKN", token1)
    gateway2.registerToken("TKN", token2)

    user1 = Address("0x4516d3f5b2e5b6e1f062f18e3d2f5f6a77469285")
    user1.balance = Wei.from_ether(100)
    user2 = Address("0x781d3f5b2e5b6e1f062f18e3d2f5f6a774692851")

    token1.mint(user1, 100)
    assert token1.balanceOf(user1) == 100
    token1.approve(gateway1, 100, from_=user1)

    gateway1.sendToken("chain2", str(user2), "TKN", 100, from_=user1)

    assert token2.balanceOf(user2) == 100


def test_call_contract():
    dev_interface.connect(8545)

    gateway1 = AxelarGatewayMock.deploy("chain1")
    gateway2 = AxelarGatewayMock.deploy("chain2")
    gateway1.registerChain(gateway2)
    gateway2.registerChain(gateway1)

    contract1 = ExampleContract.deploy(gateway1)
    Address(contract1).balance = Wei.from_ether(100)
    contract2 = ExampleContract.deploy(gateway2)

    contract1.send("chain2", str(Address(contract2)), b"testing message")

    assert contract2.lastMessage() == ExampleContract.Message(
        "chain1", str(Address(contract1)).lower(), b"testing message", "", 0)


def test_call_contract_with_token():
    dev_interface.connect(8545)

    gateway1 = AxelarGatewayMock.deploy("chain1")
    gateway2 = AxelarGatewayMock.deploy("chain2")
    gateway1.registerChain(gateway2)
    gateway2.registerChain(gateway1)

    token1 = ERC20MintableBurnable.deploy("token", "TKN", 10)
    token2 = ERC20MintableBurnable.deploy("token", "TKN", 10)

    gateway1.registerToken("TKN", token1)
    gateway2.registerToken("TKN", token2)

    contract1 = ExampleContract.deploy(gateway1)
    Address(contract1).balance = Wei.from_ether(100)
    contract2 = ExampleContract.deploy(gateway2)

    token1.mint(contract1, 200)
    assert token1.balanceOf(contract1) == 200

    contract1.sendWithToken("chain2", str(Address(contract2)), b"testing message", token1, "TKN", 200)

    assert contract2.lastMessage() == ExampleContract.Message(
        "chain1", str(Address(contract1)).lower(), b"testing message", "TKN", 200)
    assert token2.balanceOf(contract2) == 200
