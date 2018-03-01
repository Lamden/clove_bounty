from clove.network.bitcoin import Bitcoin


class Kronecoin(Bitcoin):
    """
    Class with all the necessary Kronecoin network information based on
    https://github.com/Kronecoin/Kronecoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'kronecoin'
    symbols = ('KRONE', )
    seeds = ("seed.kronecoin.org", )
    port = 16765
    message_start = b'\xd2\xca\xaf\xeb'
    base58_prefixes = {
        'PUBKEY_ADDR': 45,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 173
    }
