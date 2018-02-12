from clove.network.bitcoin import Bitcoin


class BERNcash(Bitcoin):
    """
    Class with all the necessary BERNcash network information based on
    https://github.com/berniecoin/berncash/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'BERNcash'
    symbols = ('BERN', )
    seeds = ('westseed.bern.cash', 
             'eastseed.bern.cash',
			 'cwi-seed01.bern.cash', 
			 'cwi-seed02.bern.cash', 
			 'cwi-seed03.bern.cash', 
			 'cwi-seed04.bern.cash', 
			 'cwi-seed05.bern.cash', 
			 'cwi-seed06.bern.cash', 
			 'cwi-seed07.bern.cash', 
			 'cwi-seed08.bern.cash', 
			 'cwi-seed09.bern.cash', 
			 'cwi-seed10.bern.cash', 
			 'cwi-seed11.bern.cash', 
			 'cwi-seed12.bern.cash', 
			 'cwi-seed13.bern.cash', 
			 'cwi-seed14.bern.cash', 
			 'cwi-seed15.bern.cash', 
			 'cwi-seed16.bern.cash', 
			 'cwi-seed17.bern.cash', 
			 'cwi-seed18.bern.cash', 
			 'cwi-seed19.bern.cash', 
			 'cwi-seed20.bern.cash', 
			 'cwi-seed21.bern.cash', 
			 'cwi-seed22.bern.cash', 
			 'cwi-seed23.bern.cash', 
			 'cwi-seed24.bern.cash', 
			 'cwi-seed25.bern.cash')
    port = 32020


class BERNcashTestNet(BERNcash):
    """
    Class with all the necessary BERNcash testing network information based on
    https://github.com/berniecoin/berncash/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-BERNcash'
    seeds = ()
    port = 42020  
	
	
	