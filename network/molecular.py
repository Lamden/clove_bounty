from clove.network.bitcoin import Bitcoin


class Molecular(Bitcoin):
    """
    Class with all the necessary Molecular network information based on
    https://github.com/moleculecoin/molecule/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'molecular'
    symbols = ('MOL', )
    seeds = ("seed.moleculecoin.com",
             "blocks.moleculecoin.com")
    port = 11879
    message_start = b'\xfe\xa5\x03\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 44,
        'SCRIPT_ADDR': 9,
        'SECRET_KEY': 172
    }
