from clove.network.bitcoin import Bitcoin


class Cryptonite(Bitcoin):
    """
    Class with all the necessary Cryptonite network information based on
    https://github.com/MiniblockchainProject/Cryptonite/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'cryptonite'
    symbols = ('XCN', )
    seeds = ("gpile.it")
    port = 8253


class CryptoniteTestNet(Cryptonite):
    """
    Class with all the necessary Diamond testing network information based on
    https://github.com/MiniblockchainProject/Cryptonite/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-cryptonite'
    seeds = ("seed.cryptonite.info")
    port = 18253
