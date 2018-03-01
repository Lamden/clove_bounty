from clove.network.bitcoin import Bitcoin


class United_Arab_Emirates_Coin(Bitcoin):
    """
    Class with all the necessary United Arab Emirates Coin network information based on
    https://github.com/uaecoin/UAECOIN-United-Arab-Emirates-Coin/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'united_arab_emirates_coin'
    symbols = ('UAEC', )
    seeds = ("107.155.87.16")
    port = 44887

# Has no testnet
