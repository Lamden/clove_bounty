from clove.network.bitcoin import Bitcoin


class Pesobit(Bitcoin):
    """
    Class with all the necessary Pesobit network information based on
    https://github.com/pesobitph/pesobit-source/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'pesobit'
    symbols = ('PSB', )
    seeds = ("212.24.104.88")
    port = 7867

# no testnet
