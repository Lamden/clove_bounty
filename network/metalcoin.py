from clove.network.bitcoin import Bitcoin


class MetalCoin(Bitcoin):
    """
    Class with all the necessary MetalCoin network information based on
    https://github.com/metalde/metalcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'metalcoin'
    symbols = ('METAL', )
    nodes = ('104.236.4.12', )
    port = 22332
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 178
    }


# Has no testnet
