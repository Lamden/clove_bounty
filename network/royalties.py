from clove.network.bitcoin import Bitcoin


class Royalties(Bitcoin):
    """
    Class with all the necessary Royalties (XRY) network information based on
    https://github.com/Vetro7/RoyaltiesCLI/blob/master/src/CryptoNoteConfig.h
    (date of access: 02/18/2018)
    """
    name = 'royalties'
    symbols = ('XRY', )
    seeds = ('108.61.215.239', '45.76.115.89',
             '45.32.199.3', '45.32.203.114', '45.63.43.26')
    port = 23888

# no testnet
