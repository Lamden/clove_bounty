from clove.network.bitcoin import Bitcoin


class Cypher(Bitcoin):
    """
    Class with all the necessary CYP network information based on
    https://github.com/neworldorder/braveneworld/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'cypher'
    symbols = ('CYP', )
    seeds = (
        '54.148.121.237',
    )
    port = 5424


class CypherTestNet(Cypher):
    """
    Class with all the necessary CYP testing network information based on
    https://github.com/neworldorder/braveneworld/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-cypher'
    seeds = ()
    port = 28224
