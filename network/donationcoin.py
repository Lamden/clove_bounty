from clove.network.bitcoin import Bitcoin


class DonationCoin(Bitcoin):
    """
    Class with all the necessary DonationCoin network information based on
    https://www.github.com/donationcoin-project/donationcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'donationcoin'
    symbols = ('DON', )
    seeds = ("seed.donationcoin.org",
             "seed2.donationcoin.org",
             "seed3.donationcoin.org",
             "seed4.donationcoin.org")
    port = 11060


# No Testnet
