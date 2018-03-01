from clove.network.bitcoin import Bitcoin


class Boomcoin(Bitcoin):
    """
    Class with all the necessary Boomcoin network information based on
    https://github.com/Boom-Coin/stealthboomcoin/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'Boomcoin'
    symbols = ('BOOM', )
    seeds = ("107.170.88.155", "104.131.35.160")
    port = 28175
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 24,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 152
    }

# Has no testnet
