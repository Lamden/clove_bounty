from clove.network.bitcoin import Bitcoin


class  Era(Bitcoin):
    """
    Class with all the necessary  Era (ERA) network information based on
    https://github.com/cryptofun/blas/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'era'
    symbols = ('ERA', )
    seeds =  ('216.144.230.95')
    port = 14442


class  EraTestNet(Era):
    """
    Class with all the necessary  Era (ERA) network information based on
    https://github.com/cryptofun/blas/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-era'
    symbols = ('ERA', )
    seeds =  ('216.144.230.95')
    port = 24442