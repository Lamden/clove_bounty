
from clove.network.bitcoin import Bitcoin


class PIVX(Bitcoin):
    """
    Class with all the necessary PIVX network information based on
    http://www.github.com/PIVX-Project/PIVX/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'pivx'
    symbols = ('PIVX', )
    seeds = ('pivx.seed.fuzzbawls.pw',)
    port = 51472


class PIVXTestNet(PIVX):
    """
    Class with all the necessary PIVX testing network information based on
    http://www.github.com/PIVX-Project/PIVX/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-pivx'
    seeds = ('pivx.seed2.fuzzbawls.pw', 'coin-server.com', 's3v3nh4cks.ddns.net', '178.254.23.111', 'pivx-testnet.seed.fuzzbawls.pw', 'pivx-testnet.seed2.fuzzbawls.pw', 's3v3nh4cks.ddns.net', '88.198.192.110')
    port = 51474
