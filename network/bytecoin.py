from clove.network.bitcoin import Bitcoin


class Bytecoin(Bitcoin):
    """
    Class with all the necessary Bytecoin (BCN) network information based on
    https://github.com/bcndev/bytecoin/blob/master/src/CryptoNoteConfig.hpp
    (date of access: 02/22/2018)
    """
    name = 'bytecoin'
    symbols = ('BCN', )
    nodes = ('207.246.127.160', '108.61.174.232',
             '45.32.156.183', '45.76.29.96')
    port = 8080

# no testnet
