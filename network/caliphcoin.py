from clove.network.bitcoin import Bitcoin


class CaliphCoin(Bitcoin):
    """
    Class with all the necessary CaliphCoin network information based on
    https://github.com/caliphcoin/CaliphCoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'caliphcoin'
    symbols = ('CALC', )
    seeds = ("213.252.245.164",
             "213.252.245.142",
             "electrum3.cryptolife.net")
    port = 29291

# Has no testnet
