from lumibot.brokers.ccxt import Ccxt
from lumibot.data_sources.ccxt_data import CcxtData
from lumibot.example_strategies.crypto_important_functions import ImportantFunctions

# Fake credentials, they do not need to be real
KUCOIN_LIVE = {
    "exchange_id": "kucoin",
    "password": "not_my_pass",
    "apiKey": "a1b2c3d4",
    "secret": "REMOVED_SECRET",
    "sandbox": True,
}


# KRAKEN_CONFIG = {
#     "exchange_id": "kraken",
#     "apiKey": "a1b2c3d4",
#     "secret": "REMOVED_SECRET",
#     "margin": True,
#     "sandbox": False,
# }
KRAKEN_CONFIG = {
    "exchange_id": "kraken",
    "apiKey": "REMOVED_SECRET",
    "secret": "REMOVED_SECRET",
    "margin": True,
    "sandbox": False,
}


def test_initialize_ccxt_broker_legacy():
    """
    This test to make sure the legacy way of initializing the broker still works.
    """

    broker = Ccxt(KRAKEN_CONFIG)
    strategy = ImportantFunctions(
        broker=broker,
    )

    # Assert that strategy.broker is the same as broker
    assert strategy.broker == broker

    # Assert that strategy.data_source is InteractiveBrokersData object
    assert isinstance(strategy.broker.data_source, CcxtData)
