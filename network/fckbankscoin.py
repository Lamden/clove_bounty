from clove.network.bitcoin import Bitcoin


class FCKBanksCoin(Bitcoin):
    """
    Class with all the necessary FCKBanksCoin network information based on
    https://github.com/fckfoundation/fckbankscoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'fckbankscoin'
    symbols = ('FCV', )
    seeds = ("seed.fckbanks.org")
    port = 21779
	
# no testnet