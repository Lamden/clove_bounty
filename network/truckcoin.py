from clove.network.bitcoin import Bitcoin


class Truckcoin(Bitcoin):
    """
    Class with all the necessary Truckcoin network information based on
    https://github.com/beatscoindev/beatscoinv2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'truckcoin'
    symbols = ('TRK', )
    seeds = ("dns.seed.truckcoin.net",
             "dns.seed2.truckcoin.net",
             "node1.truckcoin.net",
             "node2.truckcoin.net",
             "node3.truckcoin.net")
    port = 18775
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 153
    }


# Has no testnet
