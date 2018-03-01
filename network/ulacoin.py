from clove.network.bitcoin import Bitcoin


class ULAcoin(Bitcoin):
    """
    Class with all the necessary ULAcoin (ULA) network information based on
    https://github.com/UlaTechGroup/UlatechGroup/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'ulacoin'
    symbols = ('ULA', )
    seeds = ('ulacoin.com', 'node.walletbuilders.com')
    port = 21659
    message_start = b'\x8b\xa3\x36\x9a'
    base58_prefixes = {
        'PUBKEY_ADDR': 68,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 196
    }

# no testnet
