from clove.network.bitcoin import Bitcoin


class IndiaCoin(Bitcoin):
    """
    Class with all the necessary India Coin (INDIA) network information based on
    https://github.com/indiadev/india/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'indiacoin'
    symbols = ('INDIA', )
    seeds = ('104.200.67.220')
    port = 19679

# no testnet
