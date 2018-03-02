from clove.network.bitcoin import Bitcoin


class Flycoin(Bitcoin):
    """
    Class with all the necessary Flycoin network information based on
    https://github.com/CryptoUnited-Clients/Flycoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'flycoin'
    symbols = ('FLY', )
    seeds = ("fly.dnsalias.com",
             "167.114.224.79",
             "167.114.224.82",
             "www.walletbootstraps.com",
             "4.6.147.2")
    port = 41568
