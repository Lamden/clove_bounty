from clove.network.bitcoin import Bitcoin


class HOdlcoin(Bitcoin):
    """
    Class with all the necessary HOdlcoin network information based on
    https://github.com/HOdlcoin/HOdlcoin/blob/HODLCoin0.11.3/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'hodlcoin'
    symbols = ('HODL', )
    seeds = ("westcoast.hodlcoin.com",
             "eastcoast.hodlcoin.com",
             "europe.hodlcoin.com",
             "asia.hodlcoin.com",
             "seed.hodlcoin.oo.fi",
             "seed.hodlcoin.dk",
             "seed.hodlcoin.com",
             "174.140.166.133",
             "54.201.171.55",
             "54.213.104.91")
    port = 1989

# no testnet
