from clove.network.bitcoin import Bitcoin


class CryptoWorldXToken(Bitcoin):
    """
    Class with all the necessary CryptoWorldXToken network information based on
    https://github.com/CryptoWorldX/CWXT/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'cryptoworldxtoken'
    symbols = ('CWXT', )
    seeds = ("node01.cryptoworldx.com")
    port = 16205

# Has no testnet
