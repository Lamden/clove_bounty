from clove.network.bitcoin import Bitcoin


class AsiaCoin(Bitcoin):
    """
    Class with all the necessary AsiaCoin network information based on
    https://github.com/AsiaCoin/AsiaCoinFix/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'asiacoin'
    symbols = ('AC', )
    seeds = ("dnsseedac.planetdollar.org")
    port = 35656

# Has no testnet
