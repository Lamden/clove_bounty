from clove.network.bitcoin import Bitcoin


class UNCoin(Bitcoin):
    """
    Class with all the necessary UNCoin network information based on
    https://github.com/belledejour/uncoin-source-code/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'UNCoin'
    symbols = ('LUX', )
    seeds = ('120.27.44.15', '114.215.178.237', '115.29.224.192')
    port = 33156


class UNCoinTestNet(UNCoin):
    """
    Class with all the necessary UNCoin testing network information based on
    https://github.com/belledejour/uncoin-source-code/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-Uncoin'
    seeds = ()
    port = 33157 
	
	
	