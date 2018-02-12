from clove.network.bitcoin import Bitcoin


class OPCoin(Bitcoin):
    """
    Class with all the necessary OPCoin network information based on
    https://github.com/rfo92/opcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'opcoin'
    symbols = ('OPC', )
    seeds = ("OPC01.freeddns.org","OPC02.freeddns.org","OPC03.freeddns.org")
    port = 13355


# Has no testnet

