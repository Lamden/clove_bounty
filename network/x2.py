from clove.network.bitcoin import Bitcoin


class X2(Bitcoin):
    """
    Class with all the necessary X2 network information based on
    https://github.com/x2team2017/x2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'x2'
    symbols = ('X2', )
    seeds = ("5.146.140.4","x2team2017.ddns.net","185.61.151.109","185.61.151.132","stratumtest.ddns.net")
    port = 16384


#Has no test