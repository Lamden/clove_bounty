from clove.network.bitcoin import Bitcoin


class ATBcoin(Bitcoin):
    """
    Class with all the necessary ATBcoin (ATB) network information based on
    https://github.com/segwit/atbcoin/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'atbcoin'
    symbols = ('ATB', )
    seeds = ('node1.atbcoin.com', 'node2.atbcoin.com', 'node3.atbcoin.com')
    port = 15442


class ATBcoinTestNet(ATBcoin):
    """
    Class with all the necessary ATBcoin (ATB) testing network information based on
    https://github.com/segwit/atbcoin/blob/master/src/chainparams.cpp   
    (date of access: 02/16/2018)
    """
    name = 'test-atbcoin'
    seeds = ('78.46.248.224', 'n1.aitibicoin.com', 'n2.aitibicoin.com', 'n3.aitibicoin.com')
    port = 25443
