from clove.network.bitcoin import Bitcoin


class Sprouts(Bitcoin):
    """
    Class with all the necessary Sprouts (SPRTS) network information based on
    https://github.com/SproutsCommunityRep/sprouts/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'sprouts'
    symbols = ('SPRTS', )
    seeds = ('seed.sproutcoin.org', 'seed2.sproutcoin.org', 'seed3.sproutcoin.org', 'seed4.sproutcoin.org',
             'seed5.sproutcoin.org', 'seed6.sproutcoin.org', 'seed7.sproutcoin.org')
    port = 9901

# no testnet
