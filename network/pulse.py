from clove.network.bitcoin import Bitcoin


class Pulse(Bitcoin):
    """
    Class with all the necessary Pulse network information based on
    https://github.com/elcrypto/pulse/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'pulse'
    symbols = ('PULSE', )
    seeds = ("52.34.51.188")
    port = 57152

	

# No Testnet