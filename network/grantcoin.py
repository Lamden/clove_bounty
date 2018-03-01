from clove.network.bitcoin import Bitcoin


class Grantcoin(Bitcoin):
    """
    Class with all the necessary Grantcoin network information based on
    https://github.com/grantcoin/grantcoin/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'grantcoin'
    symbols = ('GRT', )
    seeds = ("seed.bitcoin.sipa.be",
             "dnsseed.bluematt.me",
             "dnsseed.bitcoin.dashjr.org",
             "bitseed.xf2.org")
    port = 8333

# no testnet
