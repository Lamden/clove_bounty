from clove.network.bitcoin import Bitcoin


class SuperBitcoin(Bitcoin):
    """
    Class with all the necessary  SuperBitcoin (SBTC) network information based on
    https://github.com/superbitcoin/SuperBitcoin/blob/master/src/config/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'superbitcoin'
    symbols = ('SBTC', )
    seeds = ('seed.superbtca.com', 'seed.superbtca.info', 'seed.superbtc.org')
    port = 8334
    message_start = b'\xf9\xbe\xb4\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class SuperBitcoinTestNet(SuperBitcoin):
    """
    Class with all the necessary  SuperBitcoin (SBTC) network information based on
    https://github.com/superbitcoin/SuperBitcoin/blob/master/src/config/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-superbitcoin'
    symbols = ('SBTC', )
    seeds = ('seedtest.superbtc.org')
    port = 18334
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
