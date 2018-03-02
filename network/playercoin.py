from clove.network.bitcoin import Bitcoin


class PlayerCoin(Bitcoin):
    """
    Class with all the necessary PlayerCoin (PLACO) network information based on
    https://github.com/TheCryptoServices/PlayerCoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'playercoin'
    symbols = ('PLACO', )
    seeds = ('playercoin1.dyndns.org', )
    port = 16666
    message_start = b'\xeb\x3d\x1c\xc4'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 183
    }

# no testnet
