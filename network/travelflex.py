from clove.network.bitcoin import Bitcoin


class TravelFlex(Bitcoin):
    """
    Class with all the necessary TravelFlex (SPRTS) network information based on
    https://github.com/TravelFlex/TravelFlex/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'travelflex'
    symbols = ('TRF', )
    seeds = ('seed.travelflex.mycryptocoins.net', 'seednodes.travelflex.mycryptocoins.net')
    port = 54322

# no testnet
