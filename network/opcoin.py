from clove.network.bitcoin import Bitcoin


class OPCoin(Bitcoin):
    """
    Class with all the necessary OPCoin network information based on
    https://github.com/rfo92/opcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'opcoin'
    symbols = ('OPC', )
    seeds = ("OPC01.freeddns.org", "OPC02.freeddns.org", "OPC03.freeddns.org")
    port = 13355
    message_start = b'\x9b\xe0\xd8\xe9'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 156
    }


# Has no testnet
