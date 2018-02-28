from clove.network.bitcoin import Bitcoin


class JaneCoin(Bitcoin):
    """
    Class with all the necessary JaneCoin network information based on
    https://github.com/cryptominers-online/janecoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'janecoin'
    symbols = ('JANE', )
    seeds = ('107.170.156.17', )
    port = 13413

# no testnet
