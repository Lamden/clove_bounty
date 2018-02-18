from clove.network.bitcoin import Bitcoin


class LunaCoin(Bitcoin):
    """
    Class with all the necessary Luna Coin (LUNA) network information based on
    https://github.com/lunawallet/lunawallet/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'lunacoin'
    symbols = ('LUNA', )
    seeds = ('212.24.102.92')
    port = 38353

# no testnet
