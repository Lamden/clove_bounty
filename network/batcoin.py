from clove.network.bitcoin import Bitcoin


class BatCoin(Bitcoin):
    """
    Class with all the necessary BatCoin (BAT) network information based on
    https://github.com/OriginalBatCoin/BatCoin/blob/master/src/net.cpp
    (date of access: 02/22/2018)
    """
    name = 'batcoin'
    symbols = ('BAT', )
    seeds = ('46.253.203.113', '204.27.58.214', '173.167.113.73')
    port = 10743

# no testnet
