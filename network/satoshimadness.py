from clove.network.bitcoin import Bitcoin


class SatoshiMadness(Bitcoin):
    """
    Class with all the necessary SatoshiMadness network information based on
    https://github.com/playpossat/blocksattime/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'SatoshiMadness'
    symbols = ('MAD', )
    nodes = ("52.27.159.176", )
    port = 5444
    message_start = b'\x2d\x3f\xa2\xf5'
    base58_prefixes = {
        'PUBKEY_ADDR': 52,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 180
    }


# Has no testnet
