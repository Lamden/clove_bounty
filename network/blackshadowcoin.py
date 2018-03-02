from clove.network.bitcoin import Bitcoin


class BlackShadowCoin(Bitcoin):
    """
    Class with all the necessary BlackShadowCoin network information based on
    https://github.com/blackshadowcoin/bs/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'blackshadowcoin'
    symbols = ('BS', )
    nodes = ("198.199.90.93", )
    port = 48221
    message_start = b'\x94\xe8\xc3\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 9,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 137
    }

# Has no testnet
