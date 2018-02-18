from clove.network.bitcoin import Bitcoin


class Darsek(Bitcoin):
    """
    Class with all the necessary Darsek (KED) network information based on
    https://github.com/scificrypto/Darsek/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'darsek'
    symbols = ('KED', )
    seeds = ('dnsseed.ked.altcointech.net', 'seed.ked.altcointech.net')
    port = 8443

# no testnet
