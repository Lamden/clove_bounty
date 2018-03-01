from clove.network.bitcoin import Bitcoin


class EmberCoin(Bitcoin):
    """
    Class with all the necessary EmberCoin network information based on
    https://github.com/EmberCoin/Ember/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'embercoin'
    symbols = ('EMB', )
    seeds = ("emb_00.0xify.com",
             "emb_01.0xify.com",
             "emb_02.0xify.com")
    port = 10024

# no testnet
