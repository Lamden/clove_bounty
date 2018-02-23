
from clove.network.bitcoin import Bitcoin


class BitcoinCashPlus(Bitcoin):
    """
    Class with all the necessary BCP network information based on
    https://github.com/bitcoincashplus/bitcoincashplus/blob/master/src/chainparams.cpp
    (date of access: 02/21/2018)
    """
    name = 'bitcoin-cash-plus'
    symbols = ('BCP', )
    seeds = (
        'seed.bcpfork.org',
        'seed.bcpseeds.net',
        'seed.bitcoincashplus.org',
    )
    port = 8337


class BitcoinCashPlusTestNet(BitcoinCashPlus):
    """
    Class with all the necessary BCP testing network information based on
    https://github.com/bitcoincashplus/bitcoincashplus/blob/master/src/chainparams.cpp
    (date of access: 02/21/2018)
    """
    name = 'test-bitcoin-cash-plus'
    seeds = (
        'test-seed.bcpfork.org',
        'test-seed.bcpseeds.net',
        'test-seed.bitcoincashplus.org',
    )
    port = 18337
