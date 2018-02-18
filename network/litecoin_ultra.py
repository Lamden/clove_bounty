from clove.network.bitcoin import Bitcoin


class LitecoinUltra(Bitcoin):
    """
    Class with all the necessary Litecoin Ultra (LTCU) network information based on
    https://github.com/TheCryptoServices/LiteCoinUltra/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'litecoinultra'
    symbols = ('LTCU', )
    seeds = ('litecoinultra2.dyndns.org')
    port = 19540

# no testnet
