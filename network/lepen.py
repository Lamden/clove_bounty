from clove.network.bitcoin import Bitcoin


class LePen(Bitcoin):
    """
    Class with all the necessary LePen network information based on
    https://github.com/beatscoindev/beatscoinv2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'lepen'
    symbols = ('LEPEN', )
    seeds = ('192.169.7.83')
    port = 45010
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 153
    }

# Has no testnet
