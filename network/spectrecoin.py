from clove.network.bitcoin import Bitcoin


class Spectrecoin(Bitcoin):
    """
    Class with all the necessary Spectrecoin (XSPEC) network information based on
    https://github.com/XSPECOfficial/spectre/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'spectrecoin'
    symbols = ('XSPEC', )
    seeds = ('node1.spectreproject.io', 'node2.spectreproject.io',
             'node3.spectreproject.io', 'node4.spectreproject.io')
    port = 37347
    message_start = b'\xb5\x22\x5c\xd3'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 136,
        'SECRET_KEY': 179
    }

# no testnet
