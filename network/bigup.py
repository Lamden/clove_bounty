from clove.network.bitcoin import Bitcoin


class BigUp(Bitcoin):
    """
    Class with all the necessary BigUp (BIGUP) network information based on
    https://github.com/BigUps/wallet/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'bigup'
    symbols = ('BIGUP', )
    seeds = ('52.26.37.254', '216.189.153.244', '45.55.236.105', '54.191.50.172', '173.206.93.227', '81.2.249.166',
             '144.76.71.141', '76.69.227.172', '87.2.53.225', '185.93.68.25', 'seed1.bigup.club')
    port = 61609

# no testnet
