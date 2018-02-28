from clove.network.bitcoin import Bitcoin


class Bones(Bitcoin):
    """
    Class with all the necessary Bones network information based on
    https://github.com/BonesCoin/Bones/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'Bones'
    symbols = ('BONES', )
    seeds = ("seed.Bones.com",
             "209.208.111.233")
    port = 55355


# Has no testnet
