from clove.network.bitcoin import Bitcoin


class  Alqo(Bitcoin):
    """
    Class with all the necessary  Alqo (ALQO) network information based on
    https://github.com/ALQOCRYPTO/ALQO/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'alqo'
    symbols = ('ALQO', )
    seeds =  ('85.25.138.64', '85.25.251.198', '85.25.251.199', '80.209.227.9', '80.209.228.189', '80.209.228.190', '80.209.228.191', '80.209.228.192', '80.209.228.193', '80.209.228.194', '80.209.228.195', '80.209.228.196', '80.209.228.197')
    port = 55500


class  AlqoTestNet(Aces):
    """
    Class with all the necessary  Alqo (ALQO) network information based on
    https://github.com/ALQOCRYPTO/ALQO/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-alqo'
    symbols = ('ALQO', )
    seeds =  ('85.25.138.64', '85.25.251.198', '85.25.251.199', '80.209.227.9', '80.209.228.189', '80.209.228.190', '80.209.228.191', '80.209.228.192', '80.209.228.193', '80.209.228.194', '80.209.228.195', '80.209.228.196', '80.209.228.197')
    port = 55600