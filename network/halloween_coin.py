from clove.network.bitcoin import Bitcoin


class HalloweenCoin(Bitcoin):
    """
    Class with all the necessary HalloweenCoin network information based on
    https://www.github.com/hesdeadjim/halloweencoinfinal/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'halloweencoin'
    symbols = ('HALLO', )
    seeds = ("91.134.120.210", "149.56.154.75")
    port = 35727


# Has no Testnet
