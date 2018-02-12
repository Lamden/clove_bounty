from clove.network.bitcoin import Bitcoin


class Piggycoin(Bitcoin):
    """
    Class with all the necessary Piggycoin network information based on
    https://github.com/piggycoin/newpiggycoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'piggycoin'
    symbols = ('PIGGY', )
    seeds = ("piggynodes.piggy-coin.com",
             "piggynodes.piggyfacts.com",
             "piggynodes.blockpunk.com",
             "piggynodes.neurocis.me")
    port = 54481


# Has no testnet
