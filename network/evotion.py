from clove.network.bitcoin import Bitcoin


class Evotion(Bitcoin):
    """
    Class with all the necessary Evotion (EVO) network information based on
    https://github.com/evoshiun/Evotion/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'evotion'
    symbols = ('EVO', )
    nodes = ('52.33.170.107', )
    port = 9393
    message_start = b'\xa4\xd2\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 22,
        'SCRIPT_ADDR': 51,
        'SECRET_KEY': 150
    }

# no testnet
