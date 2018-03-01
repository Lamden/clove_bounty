from clove.network.bitcoin import Bitcoin


class KashhCoin(Bitcoin):
    """
    Class with all the necessary KashhCoin network information based on
    https://github.com/cashhcointech/kashhcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'KashhCoin'
    symbols = ('KASHH', )
    seeds = ("107.180.71.154", "132.148.87.33",
             "132.148.79.97", "132.148.79.99", "148.72.247.78")
    port = 63875
    message_start = b'\xc1\xfd\xfb\x0d'
    base58_prefixes = {
        'PUBKEY_ADDR': 53,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 181
    }


# Has no Testnet
