from clove.network.bitcoin import Bitcoin


class XCoin(Bitcoin):
    """
    Class with all the necessary XCoin network information based on
    https://github.com/jimblasko/xcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'x-coin'
    symbols = ('XCO', )
    seeds = ("198.105.125.193","198.105.125.194","198.105.122.152")
    port = 14641


