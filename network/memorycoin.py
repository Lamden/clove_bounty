from clove.network.bitcoin import Bitcoin


class Memorycoin(Bitcoin):
    """
    Class with all the necessary Memorycoin network information based on
    https://github.com/memorycoin/memorycoin/blob/psforkinit/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'memorycoin'
    symbols = ('MMC', )
    seeds = ("69.30.249.2",
             "104.223.6.205",
             "192.187.113.218")
    port = 1968

# no testnet
