from clove.network.bitcoin import Bitcoin


class Dopecoin(Bitcoin):
    """
    Class with all the necessary Dopecoin (DOPE) network information based on
    https://github.com/dopecoin-dev/DopeCoinGold/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'dopecoin'
    symbols = ('DOPE', )
    seeds = ('dnsseed.dopecoin.com', '188.166.89.189',
             '37.120.190.76', '37.120.186.85', '188.68.52.172')
    port = 40420

# no testnet
