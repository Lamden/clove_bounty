from clove.network.bitcoin import Bitcoin


class SpaceCash(Bitcoin):
    """
    Class with all the necessary SpaceCash network information based on
    https://github.com/SpaceCash/SpaceCash/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'spacecash'
    symbols = ('SCASH', )
    seeds = ("stratumtest.ddns.net", )
    port = 55554
    message_start = b'\x5a\xc3\x82\xd3'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 191
    }

# no testnet
