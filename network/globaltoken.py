from clove.network.bitcoin import Bitcoin


class GlobalToken(Bitcoin):
    """
    Class with all the necessary GlobalToken (GLT) network information based on
    https://github.com/globaltoken/globaltoken/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'globaltoken'
    symbols = ('GLT', )
    seeds = ('134.255.221.7', 'lameserver.de')
    port = 9319


class GlobalTokenTestNet(GlobalToken):
    """
    Class with all the necessary GlobalToken (GLT) testing network information based on
    https://github.com/globaltoken/globaltoken/blob/master/src/chainparams.cpp    
    (date of access: 02/17/2018)
    """
    name = 'test-globaltoken'
    seeds = ('134.255.221.7')
    port = 19319
