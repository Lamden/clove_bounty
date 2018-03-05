from clove.network.bitcoin import Bitcoin


class MIScoin(Bitcoin):
    """
    Class with all the necessary MIScoin network information based on
    https://github.com/miscoinproject/miscoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'miscoin'
    symbols = ('MIS', )
    seeds = (
        "seed1.miscoin.org",
        "seed2.miscoin.org"
    )
    port = 14552
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 51,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 179
    }

# no testnet
