from clove.network.bitcoin import Bitcoin


class BillaryCoin(Bitcoin):
    """
    Class with all the necessary BillaryCoin network information based on
    https://github.com/billary/billarycoinsource/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'BillaryCoin'
    symbols = ('BLRY', )
    seeds = ('node.walletbuilders.com', )
    port = 6791
    message_start = b'\xdb\x13\x84\x33'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }
