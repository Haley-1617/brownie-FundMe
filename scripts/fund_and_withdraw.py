from brownie import FundMe, MockV3Aggregator, network, config
from scripts.utilities import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def fund():
    fundMe = FundMe[-1]
    account = get_account()
    entranceFee = fundMe.getEntranceFee()
    print(f"The current entrance fee is {entranceFee}")
    print("Funding...")
    fundMe.fund({"from": account, "value": entranceFee})


def withdraw():
    fundMe = FundMe[-1]
    account = get_account()
    fundMe.withdraw({"from": account})


def main():
    fund()
    withdraw()
