from clove.network.bitcoin import Bitcoin


class LeviarCoin(Bitcoin):
    """
    Class with all the necessary LeviarCoin (XLC) network information based on
    https://github.com/leviarcoin/leviarcoin-src/blob/master/src/CryptoNoteConfig.h
    (date of access: 02/17/2018)
    """
    name = 'leviarcoin'
    symbols = ('XLC', )
    seeds = ('46.101.28.201', '138.68.176.26',
             '138.68.58.151', '185.111.216.136')
    port = 18001

# no testnet
