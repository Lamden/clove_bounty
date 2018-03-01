from clove.network.bitcoin import Bitcoin


class FlutterCoin(Bitcoin):
    """
    Class with all the necessary FlutterCoin network information based on
    https://www.github.com/ofeefee/fluttercoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'fluttercoin'
    symbols = ('FLT', )
    seeds = ('dnsseed.fluttercoin.me', )
    port = 7408
    message_start = b'\xcf\xd1\xe8\xea'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 163
    }


# Has no testnet
