from clove.network.bitcoin import Bitcoin


class SIGMAcoin(Bitcoin):
    """
    Class with all the necessary SIGMAcoin network information based on
    https://github.com/sigmadevelopment/sigma/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'sigmacoin'
    symbols = ('SIGMA', )
    seeds = ("node.walletbuilders.com", )
    port = 8211
    message_start = b'\xdc\x05\xce\x26'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 191
    }

# no testnet
