from clove.network.bitcoin import Bitcoin


class NooCoin(Bitcoin):
    """
    Class with all the necessary NooCoin network information based on
    https://github.com/neureal/noocoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'noocoin'
    symbols = ('NOO', )
    seeds = ("noocoin.iico.in",
             "home.bown.net",
             "j.iico.in")

    port = 41800
    message_start = b'\xe6\xe8\xe9\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 114,
        'SCRIPT_ADDR': 53,
        'SECRET_KEY': 142
    }


class NooCoinTestNet(NooCoin):
    """
    Class with all the necessary NooCoin testing network information based on
    https://github.com/neureal/noocoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-noocoin'
    seeds = ("noocoin.iico.in",
             "home.bown.net",
             "j.iico.in")
    port = 41810
    message_start = b'\xcb\xf2\xc0\xef'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
