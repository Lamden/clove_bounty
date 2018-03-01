from clove.network.bitcoin import Bitcoin


class TakCoin(Bitcoin):
    """
    Class with all the necessary TakCoin network information based on
    https://github.com/takcoindevcoin/tak/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'takcoin'
    symbols = ('TAK', )
    seeds = ("node.walletbuilders.com")
    port = 32965

# no testnet
