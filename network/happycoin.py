from clove.network.bitcoin import Bitcoin


class Happycoin(Bitcoin):
    """
    Class with all the necessary Happycoin network information based on
    https://www.github.com/happycoinmaster/happycoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'happycoin'
    symbols = ('HPC', )
    seeds = ("159.203.165.4","seed5.cryptolife.net","seed3.cryptolife.net","electrum5.cryptolife.net","seed4.cryptolife.net","explore.cryptolife.net")
    port = 12846


# Has no testnet