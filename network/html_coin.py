from clove.network.bitcoin import Bitcoin


class Htmlcoin(Bitcoin):
    """
    Class with all the necessary HTMLCOIN (HTML) network information based on
    https://github.com/HTMLCOIN/HTMLCOIN/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'htmlcoin'
    symbols = ('HTML', )
    seeds = ('seed1.htmlcoin.com', 'seed2.htmlcoin.com', 'seed3.htmlcoin.com', 'seed4.htmlcoin.com')
    port = 4888


class HtmlcoinTestNet(Htmlcoin):
    """
    Class with all the necessary HTMLCOIN (HTML) testing network information based on
    https://github.com/HTMLCOIN/HTMLCOIN/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-htmlcoin'
    seeds = ('testnet-seed1.htmlcoin.com', 'testnet-seed2.htmlcoin.com')
    port = 14888
