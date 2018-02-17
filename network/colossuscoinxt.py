from clove.network.bitcoin import Bitcoin


class ColossusCoinXT(Bitcoin):
    """
    Class with all the necessary ColossusCoinXT (COLX) network information based on
    https://github.com/ColossusCoinXT/ColossusCoinXT/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'colossuscoinxt'
    symbols = ('COLX', )
    seeds = ('colxseed.presstab.pw')
    port = 51572

# no testnet