from clove.network.bitcoin import Bitcoin


class Karbo(Bitcoin):
    """
    Class with all the necessary Karbo (KRB) network information based on
    https://github.com/seredat/karbowanec/blob/master/src/CryptoNoteConfig.h
    (date of access: 02/17/2018)
    """
    name = 'karbo'
    symbols = ('KRB', )
    seeds = ('seed1.karbowanec.com', 'seed2.karbowanec.com', 'seed.karbo.cloud', 'seed.karbo.org', 'seed.karbo.io')
    port = 32347

# no testnet
