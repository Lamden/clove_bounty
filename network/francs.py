from clove.network.bitcoin import Bitcoin


class Francs(Bitcoin):
    """
    Class with all the necessary Francs network information based on
    https://github.com/FRN-Crypto/FRN/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'francs'
    symbols = ('FRN', )
    seeds = ("185.14.184.239",
             "157.161.128.59",
             "188.165.194.146",
             "104.131.19.87",
             "144.76.238.2",
             "167.160.36.126",
             "108.61.10.90",
             "85.25.198.151")
    port = 12834
    message_start = b'\xee\xea\xae\xef'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 163
    }

# No testnet
