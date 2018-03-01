from clove.network.bitcoin import Bitcoin


class Antibitcoin(Bitcoin):
    """
    Class with all the necessary Antibitcoin network information based on
    https://github.com/antibitcoin/antibitcoin-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Antibitcoin'
    symbols = ('ANTI', )
    nodes = ('188.213.171.167', '108.61.165.75', )
    port = 11650
    message_start = b'\xa4\xd2\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 50,
        'SECRET_KEY': 151
    }


# Has no Testnet
