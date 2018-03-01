from clove.network.bitcoin import Bitcoin


class Honey(Bitcoin):
    """
    Class with all the necessary Honey network information based on
    https://github.com/cryptofun/honey/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'honey'
    symbols = ('HONEY', )
    seeds = ("honey.thecryptochat.net")
    port = 40638

# no testnet
