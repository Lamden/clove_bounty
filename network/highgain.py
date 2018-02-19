from clove.network.bitcoin import Bitcoin


class  HighGain(Bitcoin):
    """
    Class with all the necessary  High Gain (HIGH) network information based on
    https://github.com/highgainqubit/highgain/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'highgain'
    symbols = ('HIGH', )
    seeds =  ('34.214.230.207')
    port = 4664


# no testnet