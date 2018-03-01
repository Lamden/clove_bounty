from clove.network.bitcoin import Bitcoin


class PlusCoin(Bitcoin):
    """
    Class with all the necessary PlusCoin network information based on
    https://github.com/BitcoinPlus-org/bitcoinplus/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'pluscoin'
    symbols = ('PLC', )
    seeds = ("seed.xbcplus.com")
    port = 53518

# no testnet
