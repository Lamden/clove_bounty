from clove.network.bitcoin import Bitcoin


class PantherCoin(Bitcoin):
    """
    Class with all the necessary PantherCoin network information based on
    https://github.com/panthercoin/Panther/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'panthercoin'
    symbols = ('PINKX', )
    seeds = ("node.walletbuilders.com", )
    port = 6641
    message_start = b'\x1e\x66\x4b\x2c'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 183
    }

# no testnet
