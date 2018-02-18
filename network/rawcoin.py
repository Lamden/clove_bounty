from clove.network.bitcoin import Bitcoin


class Rawcoin(Bitcoin):
    """
    Class with all the necessary Rawcoin (XRC) network information based on
    https://github.com/rawcoin-project/rawcoin/blob/master/src/CryptoNoteConfig.h
    (date of access: 02/17/2018)
    """
    name = 'rawcoin'
    symbols = ('XRC', )
    seeds = ('128.199.153.193', '128.199.216.207', '138.68.46.69', '138.68.129.151')
    port = 32347

# no testnet
