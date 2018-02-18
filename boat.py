from clove.network.bitcoin import Bitcoin


class  Boat(Bitcoin):
    """
    Class with all the necessary  Boat (BOAT) network information based on
    https://github.com/cryptofun/blas/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'boat'
    symbols = ('BOAT', )
    seeds =  ('seed1.Doubloon.trade', 'seed2.Doubloon.trade', 'seed3.Doubloon.trade', 'seed4.Doubloon.trade')
    port = 33827


class  BoatTestNet(Boat):
    """
    Class with all the necessary  Boat (BOAT) network information based on
    https://github.com/cryptofun/blas/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-boat'
    symbols = ('BOAT', )
    seeds =  ()
    port = 33728