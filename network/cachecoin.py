from clove.network.bitcoin import Bitcoin


class CacheCoin(Bitcoin):
    """
    Class with all the necessary CacheCoin network information based on
    https://github.com/kalgecin/cachecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'cachecoin'
    symbols = ('CACH', )
    seeds = ('seed.novacoin.su')
    port = 2225


# Has no Testnet