from clove.network.bitcoin import Bitcoin


class SPEC(Bitcoin):
    """
    Class with all the necessary SPEC network information based on
    https://github.com/SpecDevelopment/spec-wallet/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'SPEC'
    symbols = ('SPEC', )
    seeds = ("node.speccoin.com",
             "node2.speccoin.com")
    port = 4319
