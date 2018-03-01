from clove.network.bitcoin import Bitcoin


class Viorcoin(Bitcoin):
    """
    Class with all the necessary Viorcoin network information based on
    https://github.com/ROIV/ViorCoin-Wallet/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'viorcoin'
    symbols = ('VIOR', )
    nodes = ("178.62.244.59", "178.62.147.100", )
    port = 51737
    message_start = b'\xfa\xf2\xef\xb4'
    base58_prefixes = {
        'PUBKEY_ADDR': 70,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 198
    }

# no testnet
