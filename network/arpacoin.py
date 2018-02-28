from clove.network.bitcoin import Bitcoin


class ArpaCoin(Bitcoin):
    """
    Class with all the necessary ArpaCoin network information based on
    https://github.com/arpacoin/arpacoin/blob/master/src/chainparams.cpp
    (date of access: 02/13/2018)
    """
    name = 'arpacoin'
    symbols = ('ARPA', )
    seeds = ("109.237.25.123")
    port = 56631


# Has no testnet
