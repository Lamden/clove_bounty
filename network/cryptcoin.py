from clove.network.bitcoin import Bitcoin


class CryptCoin(Bitcoin):
    """
    Class with all the necessary CryptCoin network information based on
    https://github.com/cryptcointeam/cryptcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'cryptcoin'
    symbols = ('CRYPT', )
    seeds = ("seed.cryptco.org")
    port = 17771

# Has no 27114
