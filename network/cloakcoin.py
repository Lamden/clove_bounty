from clove.network.bitcoin import Bitcoin


class CloakCoin(Bitcoin):
    """
    Class with all the necessary CloakCoin network information based on
    https://github.com/CloakCoin/CloakCoinRelaunch/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'cloakcoin'
    symbols = ('CLOAK', )
    seeds = ("cloakseed.getsuperconductor.com")
    port = 29662

# Has no testnet
