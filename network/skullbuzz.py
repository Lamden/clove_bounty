from clove.network.bitcoin import Bitcoin


class SkullBuzz(Bitcoin):
    """
    Class with all the necessary SkullBuzz network information based on
    https://github.com/SkullBuzz/SkullBuzz/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'skullbuzz'
    symbols = ('SKB', )
    seeds = ("104.238.156.128",
             "104.238.152.172",
             "104.238.154.10",
             "107.191.62.71")
    port = 50550

# no testnet
