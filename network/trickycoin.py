from clove.network.bitcoin import Bitcoin


class TrickyCoin(Bitcoin):
    """
    Class with all the necessary TrickyCoin network information based on
    https://github.com/beatscoindev/beatscoinv2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'trickycoin'
    symbols = ('TRICK', )
    seeds = ("52.11.105.205")
    port = 13414
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 153
    }


# Has no testnet
