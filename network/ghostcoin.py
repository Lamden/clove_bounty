from clove.network.bitcoin import Bitcoin


class Ghostcoin(Bitcoin):
    """
    Class with all the necessary Ghostcoin network information based on
    https://github.com/ghostcoinproject/ghostcoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'ghostcoin'
    symbols = ('GHOST', )
    seeds = ("54.39.20.116")
    port = 9334


class GhostcoinTestNet(Ghostcoin):
    """
    Class with all the necessary Ghostcoin testing network information based on
    https://github.com/ghostcoinproject/ghostcoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-ghostcoin'
    seeds = ("testnet-seed.ghostcoin.info")
    port = 19334
