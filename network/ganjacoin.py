from clove.network.bitcoin import Bitcoin


class GanjaCoin(Bitcoin):
    """
    Class with all the necessary GanjaCoin network information based on
    https://github.com/GanjaCoinProject/ganjacoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'ganjacoin'
    symbols = ('MRJA', )
    seeds = ("178.62.211.205", "178.62.202.107")
    port = 10995

# no testnet
