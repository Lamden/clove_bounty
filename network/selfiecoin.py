from clove.network.bitcoin import Bitcoin


class Selfiecoin(Bitcoin):
    """
    Class with all the necessary Selfiecoin network information based on
    https://github.com/selfiecoin/slfi/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Selfiecoin'
    symbols = ('SLFI', )
    seeds = ("192.3.196.25")
    port = 6070
    message_start = b'\x69\xf0\x0f\x69'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 183
    }


# Has no testnet
