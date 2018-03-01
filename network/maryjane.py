from clove.network.bitcoin import Bitcoin


class MaryJane(Bitcoin):
    """
    Class with all the necessary MaryJane network information based on
    https://github.com/MaryJaneCoin/maryjane/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'maryjane'
    symbols = ('MARYJ', )
    seeds = ("maryjseed.earlz.net",
             "chainz.cryptoid.info")
    port = 19559
