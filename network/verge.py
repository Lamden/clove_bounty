from clove.network.bitcoin import Bitcoin


class Verge(Bitcoin):
    """
    Class with all the necessary Verge (XVG) network information based on
    https://github.com/vergecurrency/VERGE/blob/master/src/net.cpp
    (date of access: 02/22/2018)
    """
    name = 'verge'
    symbols = ('XVG', )
    seeds = ('5n4gl3kvntyanp63.onion',
             '5onui2lfl3iwdhrf.onion',
             '7sfrhwc6l4oohb5h.onion',
             'plxs66tqlzbnh3ua.onion',
             'ie4vffvggaz6xhbj.onion',
             'kw5bdikypbbxaf2g.onion',
             'n5ln6ke2vc47glpl.onion')
    port = 21102
    message_start = b'\xf7\xa7\x7e\xff'
    base58_prefixes = {
        'PUBKEY_ADDR': 30,
        'SCRIPT_ADDR': 33,
        'SECRET_KEY': 158
    }

# no testnet
