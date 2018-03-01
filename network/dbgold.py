from clove.network.bitcoin import Bitcoin


class DBGold(Bitcoin):
    """
    Class with all the necessary DBG network information based on
    https://github.com/dbgold/dbgold/blob/master/src/net.cpp
    (date of access: 01/18/2018)
    """
    name = 'dbgold'
    symbols = ('DBG', )
    nodes = (
        '178.62.122.246',
    )
    port = 32113
    message_start = b'\x04\xa1\xb1\xb5'
    base58_prefixes = {
        'PUBKEY_ADDR': 31,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 159
    }


class DBGoldTestNet(DBGold):
    """
    Class with all the necessary DBG testing network information based on
    https://github.com/dbgold/dbgold/blob/master/src/net.cpp
    (date of access: 01/18/2018)
    """
    name = 'test-dbgold'
    seeds = ()
    port = 44443
