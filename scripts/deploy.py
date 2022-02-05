from brownie import FundMe, MockV3Aggregator, network, config
from scripts.utilities import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fundme contract

    # if we are on persistent network like rinkeby, use the associated address
    # otherwise, deploy monks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        priceFeedAddress = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        priceFeedAddress = MockV3Aggregator[-1].address

    fundMe = FundMe.deploy(
        priceFeedAddress,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"Contract deployed to {fundMe}")
    return fundMe


def main():
    deploy_fund_me()
