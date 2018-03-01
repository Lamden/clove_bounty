from clove.network.bitcoin import Bitcoin


class DeepOnion(Bitcoin):
    """
    Class with all the necessary ONION network information based on
    https://github.com/deeponion/deeponion/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'deeponion'
    symbols = ('ONION', )
    seeds = (
        'clazvyxuxubl2vgm.onion',
        'xui3kzolhlf7l27o.onion',
        'nikluyytbjyofh3k.onion',
        'jxiwwjdkyfg5pnov.onion',
        'tcqiq5t24mnmkkux.onion',
        't3bauqgknp3uw74u.onion',
        'urrg7up7awygv6qz.onion',
        'ldmhzclj5y3tk52m.onion',
    )
    port = 17570
    message_start = b'\xd1\xf1\xdb\xf2'
    base58_prefixes = {
        'PUBKEY_ADDR': 31,
        'SCRIPT_ADDR': 78,
        'SECRET_KEY': 159
    }


class DeepOnionTestNet(DeepOnion):
    """
    Class with all the necessary ONION testing network information based on
    https://github.com/deeponion/deeponion/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-deeponion'
    seeds = ()
    port = 26550
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
