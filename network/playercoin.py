from clove.network.bitcoin import Bitcoin


class PlayerCoin(Bitcoin):
    """
    Class with all the necessary PlayerCoin (PLACO) network information based on
    https://github.com/TheCryptoServices/PlayerCoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'playercoin'
    symbols = ('PLACO', )
    seeds = ('playercoin1.dyndns.org')
    port = 16666

# no testnet
