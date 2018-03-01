from clove.network.bitcoin import Bitcoin


class SmartCoin(Bitcoin):
    """
    Class with all the necessary SmartCoin network information based on
    https://github.com/psionin/smartcoin/blob/0.11/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'smartcoin'
    symbols = ('SMC', )
    seeds = ("dnsseed.smartcoin.cc", )
    port = 58585
    message_start = b'\xde\xfa\xce\xd0'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 191
    }


class SmartCoinTestNet(SmartCoin):
    """
    Class with all the necessary SmartCoin testing network information based on
    https://github.com/psionin/smartcoin/blob/0.11/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-smartcoin'
    seeds = ("testnet-seed.alexykot.me",
             "testnet-seed.bitcoin.petertodd.org",
             "testnet-seed.bluematt.me",
             "testnet-seed.bitcoin.schildbach.de")
    port = 18333
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
