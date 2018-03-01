from clove.network.bitcoin import Bitcoin


class PlanetCoin(Bitcoin):
    """
    Class with all the necessary PlanetCoin network information based on
    https://github.com/planetcoin/planetcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'planetcoin'
    symbols = ('PLANET', )
    nodes = ("178.62.235.171", )
    port = 10410
    message_start = b'\xcb\xfb\xfa\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 6,
        'SECRET_KEY': 183
    }

# no testnet
