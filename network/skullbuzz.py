from clove.network.bitcoin import Bitcoin


class SkullBuzz(Bitcoin):
    """
    Class with all the necessary SkullBuzz network information based on
    https://github.com/SkullBuzz/SkullBuzz/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'skullbuzz'
    symbols = ('SKB', )
    nodes = ("104.238.156.128",
             "104.238.152.172",
             "104.238.154.10",
             "107.191.62.71")
    port = 50550
    message_start = b'\x50\x15\x15\x51'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# no testnet
