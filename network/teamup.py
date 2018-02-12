from clove.network.bitcoin import Bitcoin


class TeamUp(Bitcoin):
    """
    Class with all the necessary TeamUp network information based on
    https://github.com/teamupdev/teamup/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'teamup'
    symbols = ('TEAM', )
    seeds = ("185.106.122.32")
    port = 37091


# Has no testnet