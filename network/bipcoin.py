from clove.network.bitcoin import Bitcoin


class Bipcoin(Bitcoin):
    """
    Class with all the necessary Bipcoin (BIP) network information based on
    https://github.com/BEASTLICK-INTERNET-POLICY-COMMISSION/bipcoin/blob/master/src/CryptoNoteConfig.h
    (date of access: 02/17/2018)
    """
    name = 'bipcoin'
    symbols = ('BIP', )
    seeds = ('bipcoin.freedomfeens.com', 'bipcoin.alienseed.com')
    port = 18870

# no testnet
