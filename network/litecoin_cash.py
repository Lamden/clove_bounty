from clove.network.bitcoin import Bitcoin


class LitecoinCash(Bitcoin):
    """
    Class with all the necessary LCC network information based on
    https://github.com/litecoincash-project/litecoincash/blob/master/src/chainparams.cpp
    (date of access: 02/21/2018)
    """
    name = 'litecoincash'
    symbols = ('LCC', )
    seeds = (
        'seeds.litecoinca.sh',
        'seeds.minelcc.net',
    )
    port = 62458
