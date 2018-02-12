from clove.network.bitcoin import Bitcoin


class Gridcoin(Bitcoin):
    """
    Class with all the necessary Gridcoin network information based on
    https://github.com/gridcoin/gridcoin-research/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Gridcoin'
    symbols = ('GRC', )
    seeds = ("node.gridcoin.us","london.grcnode.co.uk","gridcoin.crypto.fans","www.grcpool.com","nuad.de","seeds.gridcoin.ifoggz-network.xyz")
    port = 32749


# Has no testnet