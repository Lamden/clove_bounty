from clove.network.bitcoin import Bitcoin


class PupaCoin(Bitcoin):
    """
    Class with all the necessary PupaCoin network information based on
    https://github.com/pupac/pupa/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'pupacoin'
    symbols = ('PUPA', )
    seeds = ("213.169.33.11")
    port = 6811
	
   
class PupaCoinTestNet(PupaCoin):
    """
    Class with all the necessary PupaCoin testing network information based on
    https://github.com/pupac/pupa/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-pupacoin'
    seeds = ("test1.PupaCoin.pw")
    port = 16811              