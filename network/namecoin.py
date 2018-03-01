from clove.network.bitcoin import Bitcoin


class Namecoin(Bitcoin):
    """
    Class with all the necessary Namecoin (NMC) network information based on
    https://github.com/namecoin/namecoin-core/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'namecoin'
    symbols = ('NMC', )
    seeds = ('nmc.seed.quisquis.de', 'seed.nmc.markasoftware.com')
    port = 8334
    message_start = b'\xf9\xbe\xb4\xfe'
    base58_prefixes = {
        'PUBKEY_ADDR': 52,
        'SCRIPT_ADDR': 13,
        'SECRET_KEY': 180
    }


class NamecoinTestNet(Namecoin):
    """
    Class with all the necessary  Namecoin (NMC) testing network information based on
    https://github.com/namecoin/namecoin-core/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-namecoin'
    seeds = ('dnsseed.test.namecoin.webbtc.com', )
    port = 18334
    message_start = b'\xfa\xbf\xb5\xfe'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
