from clove.network.bitcoin import Bitcoin


class PLNcoin(Bitcoin):
    """
    Class with all the necessary PLNcoin network information based on
    https://github.com/plncoin/PLNcoin_Core/blob/plnc/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'plncoin'
    symbols = ('PLNC', )
    seeds = ("seed.plncoin.org",
             "seed1.plncoin.org",
             "seed2.plncoin.org",
             "seed3.plncoin.org",
             "seed4.plncoin.org",
             "plncoin.org",
             "seed.plncoin.org",
             "plncoin.org",
             "rav3n.dtdns.net")
    port = 9334


class PLNcoinTestNet(PLNcoin):
    """
    Class with all the necessary Diamond testing network information based on
    https://github.com/plncoin/PLNcoin_Core/blob/plnc/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-plncoin'
    seeds = ("testnet.plncoin.org",
             "testnet2.plncoin.org",
             "testnet3.plncoin.org",
             "testnet4.plncoin.org",
             "rav3n.dtdns.net")
    port = 19333
