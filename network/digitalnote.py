from clove.network.bitcoin import Bitcoin


class DigitalNote(Bitcoin):
    """
    Class with all the necessary Digital Note (XDN) network information based on
    https://github.com/xdn-project/digitalnote/blob/master/src/CryptoNoteConfig.h
    (date of access: 02/16/2018)
    """
    name = 'digitalnote'
    symbols = ('XDN', )
    seeds = ('64.34.219.46', '66.172.27.42', '66.172.27.6',
             '76.74.170.207', '76.74.219.163')
    port = 42080

# no testnet
