from clove.network.bitcoin import Bitcoin


class Imperialcoin(Bitcoin):
    """
    Class with all the necessary Diamond Imperialcoin information based on
    https://github.com/ImperialCoin/ImperialCoin/blob/newmaster/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'imperialcoin'
    symbols = ('IPC', )
    seeds = ("68.232.180.111",
             "54.94.148.228")
    port = 10240
	
# no testnet