from clove.network.bitcoin import Bitcoin


class MoneyCoin(Bitcoin):
    """
    Class with all the necessary MoneyCoin network information based on
    https://github.com/moneyproject/moneycoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'moneycoin'
    symbols = ('MONEY', )
    seeds = ("seed.moneycoin.pw")
    port = 15554
	
# no testnet