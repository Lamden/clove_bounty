from clove.network.bitcoin import Bitcoin


class UnitaryStatus_Dollar(Bitcoin):
    """
    Class with all the necessary UnitaryStatus Dollar network information based on
    https://github.com/usde-project/USDE/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'unitarystatus_dollar'
    symbols = ('USDE', )
    seeds = ("liteminers.com")
    port = 54449

# no testnet
