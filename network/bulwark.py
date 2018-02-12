
from clove.network.bitcoin import Bitcoin


class Bulwark(Bitcoin):
    """
    Class with all the necessary SEND network information based on
    https://github.com/bulwark-crypto/Bulwark/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'bulwark'
    symbols = ('BWK', )
    seeds = (
        'bwkseed.mempool.pw',
        'bulwark-dns-seed04.ssus.tech'
    )
    port = 52543


class BulwarkTestNet(Bulwark):
    """
    Class with all the necessary SEND testing network information based on
    https://github.com/bulwark-crypto/Bulwark/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-bulwark'
    seeds = (
        'test01.bulwarkcrypto.com',
        'test02.bulwarkcrypto.com',
        'test03.bulwarkcrypto.com',
    )
    port = 42133
