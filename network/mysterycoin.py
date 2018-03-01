from clove.network.bitcoin import Bitcoin


class MysteryCoin(Bitcoin):
    """
    Class with all the necessary MysteryCoin network information based on
    https://github.com/MysteryCoin/MysteryCoinHasSecrets/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'mysterycoin'
    symbols = ('MYST', )
    seeds = ("dnsseed.mysterycoin.org", )
    port = 11030
    message_start = b'\xf9\xbe\xb4\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }

# no testnet
