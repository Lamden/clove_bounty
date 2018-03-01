from clove.network.bitcoin import Bitcoin


class GanjaCoin(Bitcoin):
    """
    Class with all the necessary GanjaCoin network information based on
    https://github.com/GanjaCoinProject/ganjacoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'ganjacoin'
    symbols = ('MRJA', )
    nodes = ("178.62.211.205", "178.62.202.107", )
    port = 10995
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 166
    }

# no testnet
