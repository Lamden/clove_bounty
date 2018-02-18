from clove.network.bitcoin import Bitcoin


class Pure(Bitcoin):
    """
    Class with all the necessary Pure network information based on
    https://github.com/puredev321/pure/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'pure'
    symbols = ('PURE', )
    seeds = ("dns0.purealt.org",
             "dns1.purealt.org",
             "dns2.purealt.org",
             "dns3.purealt.org",
             "dns4.purealt.org",
             "dns5.purealt.org",
             "dns6.purealt.org",
             "dns7.purealt.org",
             "dns8.purealt.org",
             "dns9.purealt.org")
    port = 32745

# no testnet