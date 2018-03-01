from clove.network.bitcoin import Bitcoin


class HTML5COIN(Bitcoin):
    """
    Class with all the necessary HTML5COIN network information based on
    https://github.com/HTMLCOIN/HTML5/blob/master-1.x/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'html5coin'
    symbols = ('HTML5', )
    seeds = ("seed.htmlcoin.net")
    port = 6877
    message_start = b'\xa8\xa3\xa1\xa4'
    base58_prefixes = {
        'PUBKEY_ADDR': 40,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 168
    }

# no testnet
