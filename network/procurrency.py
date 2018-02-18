from clove.network.bitcoin import Bitcoin


class ProCurrency(Bitcoin):
    """
    Class with all the necessary ProCurrency network information based on
    https://github.com/procommerce-io/procurrency/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'procurrency'
    symbols = ('PROC', )
    seeds = ("194.135.80.127",
             "185.5.53.201",
             "185.5.54.65",
             "185.69.53.90",
             "45.63.51.33",
             "45.32.167.248",
             "45.76.5.197",
             "45.32.176.210",
             "45.76.88.24",
             "45.76.104.85",
             "71.213.148.206",
             "67.197.66.122",
             "75.70.40.167",
             "66.222.148.57",
             "47.157.52.95")
    port = 35950
	
# no testnet