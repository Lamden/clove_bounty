from clove.network.bitcoin import Bitcoin


class EDRCoin(Bitcoin):
    """
    Class with all the necessary EDRCoin network information based on
    https://github.com/EDRCoin/EDRcoin-src/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'edrcoin'
    symbols = ('EDRC', )
    seeds = ("seed1.cryptolife.net",
             "seed2.cryptolife.net")
    port = 33918
    message_start = b'\xf3\xe4\xd2\xe3'
    base58_prefixes = {
        'PUBKEY_ADDR': 93,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 221
    }

# No testnet
