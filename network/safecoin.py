from clove.network.bitcoin import Bitcoin


class SafecCoin(Bitcoin):
    """
    Class with all the necessary SafecCoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'safecoin'
    symbols = ('SFE', )
    seeds = ("seed.bitcoin.sipa.be",
             "dnsseed.bluematt.me",
             "dnsseed.bitcoin.dashjr.org",
             "bitseed.xf2.org")
    port = 8333


class SafecCoinTestNet(SafecCoin):
    """
    Class with all the necessary SafecCoin testing network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-safecoin'
    seeds = ("testnet-seed.bitcoin.petertodd.org",
             "testnet-seed.bluematt.me")
    port = 18333
