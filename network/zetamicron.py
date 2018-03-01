from clove.network.bitcoin import Bitcoin


class ZetaMicron(Bitcoin):
    """
    Class with all the necessary ZetaMicron (ZMC) network information based on
    https://github.com/zmcdev/ZMcron/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'zetamicron'
    symbols = ('ZMC', )
    seeds = ('node.walletbuilders.com')
    port = 9077
    message_start = b'\xa4\x50\xb2\x41'
    base58_prefixes = {
        'PUBKEY_ADDR': 80,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 208
    }

# no testnet
