from clove.network.bitcoin import Bitcoin


class AeroMe(Bitcoin):
    """
    Class with all the necessary AeroMe network information based on
    https://github.com/aeromasterdev/am-aerome/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'aerome'
    symbols = ('AM', )
    seeds = ("aerome.publicvm.com",
             "aerome2.publicvm.com",
             "aerome3.publicvm.com",
             "aerome4.publicvm.com",
             "aerome5.publicvm.com")
    port = 6221


# Has no testnet
