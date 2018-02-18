from clove.network.bitcoin import Bitcoin


class Judgecoin(Bitcoin):
    """
    Class with all the necessary Judgecoin network information based on
    https://github.com/judgecrypto/judgecoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'judgecoin'
    symbols = ('JUDGE', )
    seeds = ("seed1.judgecoin.com",
             "seed2.judgecoin.com",
             "seed3.judgecoin.com",
             "seed4.judgecoin.com",
             "seed5.judgecoin.com")
    port = 14788

# no testnet