
from clove.network.bitcoin import Bitcoin


class Monoeci(Bitcoin):
    """
    Class with all the necessary Monoeci network information based on
    https://github.com/monacocoin-net/monoeci-core/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'monoeci'
    symbols = ('XMCC', )
    seeds = ("163.172.157.172",
             "dorado.monoeci.io",
             "block.monoeci.io")
    port = 24157
	
# no testnet
