from clove.network.bitcoin import Bitcoin


class Aerium(Bitcoin):
    """
    Class with all the necessary Aerium network information based on
    https://github.com/aeriumcoin/Aerium/blob/master/src/chainparams.cpp
    (date of access: 02/13/2018)
    """
    name = 'aerium'
    symbols = ('AERM', )
    seeds =  ("18.216.79.110",
              "185.223.31.170",
              "45.76.103.65",
              "45.63.48.241",
              "185.223.30.120",
              "128.77.65.71",
              "104.238.181.13",
              "108.61.181.58",
              "45.77.141.139",
              "45.76.82.217",
              "45.76.84.32",
              "45.76.52.41",
              "45.63.93.21",
              "173.233.72.98")
    port = 44444
	
   
class AeriumTestNet(Aerium):
    """
    Class with all the necessary Aerium testing network information based on
    https://github.com/aeriumcoin/Aerium/blob/master/src/chainparams.cpp
    (date of access: 02/13/2018)
    """
    name = 'test-aerium'
    seeds = ("107.22.138.243")
    port = 26178              
	
	
