
from clove.network.bitcoin import Bitcoin


class BitTokens(Bitcoin):
    """
    Class with all the necessary BXT network information based on
    http://www.github.com/BitTokens/BitToken/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'bittokens'
    symbols = ('BXT', )
    seeds = ('node.walletbuilders.com', '84.200.17.159')
    port = 8223


class BitTokensTestNet(BitTokens):
    """
    Class with all the necessary BXT testing network information based on
    http://www.github.com/BitTokens/BitToken/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-bittokens'
    seeds = ()
    port = 18223
