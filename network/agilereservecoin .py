from clove.network.bitcoin import Bitcoin


class Agilereservecoin(Bitcoin):
    """
    Class with all the necessary Agilereservecoin network information based on
   https://github.com/arcoin1/arcoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'agilereservecoin '
    symbols = ('ARC', )
    seeds =  ("seeds.arc.ie1.cn",
              "seed1.arc.ie1.cn",
              "seed2.arc.ie1.cn",
              "tnseeds.arc.ie1.cn")
    port = 8888
 
