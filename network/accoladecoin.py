from clove.network.bitcoin import Bitcoin


class AccoladeCoin(Bitcoin):
    """
    Class with all the necessary AccoladeCoin network information based on
    https://github.com/AccoladeCoin/accoladecoin-core/blob/master/Accolade-master/src/chainparams.cpp
    (date of access: 02/13/2018)
    """
    name = 'accoladecoin'
    symbols = ('ACCO', )
    seeds =  ("45.55.85.44","45.55.169.173","104.236.230.23","45.55.248.114")
    port = 13117
	
   
# No testnet