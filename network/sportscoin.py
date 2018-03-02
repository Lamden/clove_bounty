from clove.network.bitcoin import Bitcoin


class SportsCoin(Bitcoin):
    """
    Class with all the necessary SportsCoin network information based on
    https://github.com/thesportscoin/sport-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'sportscoin'
    symbols = ('SPORT', )
    nodes = ("63.142.255.39", )
    port = 42986
    message_start = b'\xaa\xa2\xb2\xc4'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 191
    }


# Has no testnet
