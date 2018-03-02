from clove.network.bitcoin import Bitcoin


class Potcoin(Bitcoin):
    """
    Class with all the necessary Potcoin (POT) network information based on
    https://github.com/potcoin/Potcoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'potcoin'
    symbols = ('POT', )
    seeds = ('dnsseedz.potcoin.info', 'dns1.potcoin.info', )
    port = 4200
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 183
    }


class PotcoinTestNet(Potcoin):
    """
    Class with all the necessary Potcoin (POT) testing network information based on
    https://github.com/potcoin/Potcoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-potcoin'
    seeds = ('testnet-seed.potcoin.com', )
    port = 14200
    message_start = b'\xfe\xc3\xb9\xde'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
