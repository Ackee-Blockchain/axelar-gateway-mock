from pytypes.contracts.mocks.AxelarGatewayMock import AxelarGatewayMock
from pytypes.contracts.ExampleContract import ExampleContract
from pytypes.axelarnetwork.axelargmpsdksolidity.contracts.test.ERC20MintableBurnable import ERC20MintableBurnable

from woke.testing.contract import dev_interface, Address, Wei
from woke.testing.utils import connect, snapshot_and_revert


@connect(dev_interface, "http://127.0.0.1:8545")
@snapshot_and_revert(dev_interface)
def test_send_token():
    # deploy gateways
    # gateway1 should emulate AxelarGateway on chain1
    # gateway2 should emulate AxelarGateway on chain2
    gateway1 = AxelarGatewayMock.deploy("chain1")
    gateway2 = AxelarGatewayMock.deploy("chain2")

    # register gateways so that they know about each other
    gateway1.registerChain(gateway2)
    gateway2.registerChain(gateway1)

    # deploy tokens
    # token1 should represent a token on chain1
    # token2 should represent the same token on chain2
    token1 = ERC20MintableBurnable.deploy("token", "TKN", 10)
    token2 = ERC20MintableBurnable.deploy("token", "TKN", 10)

    # register tokens so that gateways know about them
    gateway1.registerToken("TKN", token1)
    gateway2.registerToken("TKN", token2)

    # user1 wants to send 100 TKN from chain1 to user2 on chain2
    user1 = Address("0x4516d3f5b2e5b6e1f062f18e3d2f5f6a77469285")
    # give user1 some Ether so that he can pay for gas
    user1.balance = Wei.from_ether(100)
    assert user1.balance == Wei.from_ether(100)
    user2 = Address("0x781d3f5b2e5b6e1f062f18e3d2f5f6a774692851")

    # give user1 200 TKN (on chain1)
    token1.mint(user1, 200)

    assert token1.balanceOf(user1) == 200
    assert token1.balanceOf(user2) == 0
    assert token2.balanceOf(user1) == 0
    assert token2.balanceOf(user2) == 0

    token1.approve(gateway1, 100, from_=user1)

    # user1 sends 100 TKN from chain1 to user2 on chain2
    gateway1.sendToken("chain2", str(user2), "TKN", 100, from_=user1)

    assert token1.balanceOf(user1) == 100
    assert token2.balanceOf(user2) == 100


@connect(dev_interface, "http://127.0.0.1:8545")
@snapshot_and_revert(dev_interface)
def test_call_contract():
    # deploy gateways
    # gateway1 should emulate AxelarGateway on chain1
    # gateway2 should emulate AxelarGateway on chain2
    gateway1 = AxelarGatewayMock.deploy("chain1")
    gateway2 = AxelarGatewayMock.deploy("chain2")

    # register gateways so that they know about each other
    gateway1.registerChain(gateway2)
    gateway2.registerChain(gateway1)

    # contract1 wants to send a message from chain1 to contract2 on chain2
    contract1 = ExampleContract.deploy(gateway1)
    # give contract1 some Ether so that it can pay for gas
    Address(contract1).balance = Wei.from_ether(100)
    assert Address(contract1).balance == Wei.from_ether(100)
    contract2 = ExampleContract.deploy(gateway2)

    # make the actual call
    contract1.send("chain2", str(Address(contract2)), b"testing message")

    # check that the message was received
    assert contract2.lastMessage() == ExampleContract.Message(
        "chain1",
        str(Address(contract1)).lower(),
        b"testing message",
        "",
        0
    )


@connect(dev_interface, "http://127.0.0.1:8545")
@snapshot_and_revert(dev_interface)
def test_call_contract_with_token():
    # deploy gateways
    # gateway1 should emulate AxelarGateway on chain1
    # gateway2 should emulate AxelarGateway on chain2
    gateway1 = AxelarGatewayMock.deploy("chain1")
    gateway2 = AxelarGatewayMock.deploy("chain2")

    # register gateways so that they know about each other
    gateway1.registerChain(gateway2)
    gateway2.registerChain(gateway1)

    # deploy tokens
    # token1 should represent a token on chain1
    # token2 should represent the same token on chain2
    token1 = ERC20MintableBurnable.deploy("token", "TKN", 10)
    token2 = ERC20MintableBurnable.deploy("token", "TKN", 10)

    # register tokens so that gateways know about them
    gateway1.registerToken("TKN", token1)
    gateway2.registerToken("TKN", token2)

    # contract1 wants to send a message and 100 TKN from chain1 to contract2 on chain2
    contract1 = ExampleContract.deploy(gateway1)
    # give contract1 some Ether so that it can pay for gas
    Address(contract1).balance = Wei.from_ether(100)
    assert Address(contract1).balance == Wei.from_ether(100)
    contract2 = ExampleContract.deploy(gateway2)

    # give contract1 200 TKN (on chain1)
    token1.mint(contract1, 200)

    assert token1.balanceOf(contract1) == 200
    assert token1.balanceOf(contract2) == 0
    assert token2.balanceOf(contract1) == 0
    assert token2.balanceOf(contract2) == 0

    # make the actual call and send 100 TKN
    contract1.sendWithToken("chain2", str(Address(contract2)), b"testing message", token1, "TKN", 100)

    # check that the message and tokens were received
    assert contract2.lastMessage() == ExampleContract.Message(
        "chain1",
        str(Address(contract1)).lower(),
        b"testing message",
        "TKN",
        100
    )
    assert token1.balanceOf(contract1) == 100
    assert token2.balanceOf(contract2) == 100
