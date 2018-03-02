from clove.network.bitcoin import Bitcoin


class ProjectX(Bitcoin):
    """
    Class with all the necessary Project-X (NANOX) network information based on
    https://github.com/Tillkoeln/x/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'projectx'
    symbols = ('NANOX', )
    seeds = (
        'dnsseed111.ddns.net',
        'p-x.ddns.net',
        'stratumtest.ddns.net',
        'dns-seed.ddns.net',
        'node4.version2.org',
    )
    port = 42123
    message_start = b'\x5a\xc3\x82\xd3'
    base58_prefixes = {
        'PUBKEY_ADDR': 75,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 203
    }

# no testnet
