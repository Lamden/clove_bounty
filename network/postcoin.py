from clove.network.bitcoin import Bitcoin


class PostCoin(Bitcoin):
    """
    Class with all the necessary PostCoin network information based on
    https://github.com/postcoindevelopers/postcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'postcoin'
    symbols = ('POST', )
    nodes = ("5.45.66.18", )
    port = 9130
    message_start = b'\x35\xc3\xd6\xa2'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 183
    }


# Has no testnet
