from scripts.deploy import deploy_fund_me
from scripts.utilities import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import network, accounts
import pytest


def test_fund_and_withdraw():
    account = get_account()
    fundMe = deploy_fund_me()
    entranceFee = fundMe.getEntranceFee()
    tx = fundMe.fund({"from": account, "value": entranceFee})
    tx.wait(1)
    assert fundMe.addressToAmountFunded(account.address) == entranceFee
    tx2 = fundMe.withdraw({"from": account})
    tx2.wait(1)
    assert fundMe.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing!")
    fundMe = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(AttributeError):
        fundMe.withdraw({"from": bad_actor})
