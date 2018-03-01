from clove.network.bitcoin import Bitcoin


class Victoriouscoin(Bitcoin):
    """
    Class with all the necessary Victoriouscoin network information based on
    https://github.com/VictoriousCoin/Victorious-Coin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'victoriouscoin'
    symbols = ('VTY', )
    seeds = ("node.walletbuilders.com")
    port = 7955
    message_start = b'\xb2\x88\xa7\x6d'
    base58_prefixes = {
        'PUBKEY_ADDR': 70,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 198
    }

# no testnet
