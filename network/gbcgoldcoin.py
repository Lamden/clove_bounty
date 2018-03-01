from clove.network.bitcoin import Bitcoin


class GBCGoldCoin(Bitcoin):
    """
    Class with all the necessary GBCGoldCoin network information based on
    https://github.com/jpgagnon/qbc/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'gbcgoldcoin'
    symbols = ('GBC', )
    seeds = ("dnsseed.qbc.io", )
    port = 56790
    message_start = b'\xd3\xed\xc9\xf1'
    base58_prefixes = {
        'PUBKEY_ADDR': 58,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 186
    }


class GBCGoldCoinTestNet(GBCGoldCoin):
    """
    Class with all the necessary GBCGoldCoin testing network information based on
    https://github.com/jpgagnon/qbc/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-gbcgoldcoin'
    seeds = ("testnet-seed.qbc.io", )
    port = 46790
    message_start = b'\xd3\xed\xc9\xf1'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
