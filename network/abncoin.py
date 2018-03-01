from clove.network.bitcoin import Bitcoin


class Abncoin(Bitcoin):
    """
    Class with all the necessary Abncoin network information based on
    https://github.com/AbnMainDev/abncoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'abncoin'
    symbols = ('ABN', )
    seeds = ("node.walletbuilders.com", )
    port = 10267
    message_start = b'\x3b\x40\x9d\x4f'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# no testnet
