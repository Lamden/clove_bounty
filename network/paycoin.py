from clove.network.bitcoin import Bitcoin


class PayCoin(Bitcoin):
    """
    Class with all the necessary PayCoin network information based on
    https://github.com/PaycoinFoundation/paycoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'paycoin'
    symbols = ('XPY', )
    seeds = ("dnsseed.paycoin.com",
             "dnsseed.paycoinfoundation.org",
             "dnsseed.xpydev.org")

    port = 8998


class PayCoinTestNet(Bitcoin):
    """
    Class with all the necessary PayCoin testing network information based on
    https://github.com/PaycoinFoundation/paycoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-paycoin'
    seeds = ("tseed.paycoin.com",
             "testnet-seed.paycoin.mitchellcash.com")
    port = 9000
