from clove.network.bitcoin import Bitcoin


class DeltaCredits(Bitcoin):
    """
    Class with all the necessary DeltaCredits network information based on
    https://github.com/Gladimor/DeltaCredits/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'deltacredits'
    symbols = ('DCRE', )
    nodes = ("108.61.72.49", )
    port = 31414
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 30,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 158
    }

# Has no testnet
