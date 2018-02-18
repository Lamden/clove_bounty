from clove.network.bitcoin import Bitcoin


class  SuperNET(Bitcoin):
    """
    Class with all the necessary  SuperNET (UNITY) network information based on
    https://github.com/SuperNETorg/komodo/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'supernet'
    symbols = ('UNITY', )
    seeds =  ('seeds.komodoplatform.com', 'seeds.komodo.mewhub.com')
    port = 7770


class  SuperNETTestNet(SuperNET):
    """
    Class with all the necessary  SuperNET (UNITY) network information based on
    https://github.com/SuperNETorg/komodo/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-supernet'
    symbols = ('UNITY', )
    seeds =  ()
    port = 17770