from clove.network.bitcoin import Bitcoin


class Omicron(Bitcoin):
    """
    Class with all the necessary Omicron network information based on
    https://www.github.com/gladimor/omicron-investment-platform/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'omicron'
    symbols = ('OMC', )
    seeds = ('159.203.62.235')
    port = 8519


# Has no Testnet
