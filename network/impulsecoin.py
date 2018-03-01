from clove.network.bitcoin import Bitcoin


class ImpulseCoin(Bitcoin):
    """
    Class with all the necessary ImpulseCoin network information based on
    https://github.com/impulsecoin/impulsecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'impulsecoin'
    symbols = ('IMPS', )
    seeds = ("node1.impulsecoin.io",
             "node2.impulsecoin.io",
             "node3.impulsecoin.io",
             "node4.impulsecoin.io",
             "node5.impulsecoin.io")
    port = 23765
    message_start = b'\x11\xc3\x82\xd2'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 50,
        'SECRET_KEY': 128
    }


# Has no testnet
