from clove.network.bitcoin import Bitcoin


class AtomicCoin(Bitcoin):
    """
    Class with all the necessary AtomicCoin network information based on
    https://github.com/Atomic-coin/ATOM-Atomic-coin/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'atomiccoin'
    symbols = ('ATOM', )
    seeds = ("199.127.226.157")
    port = 8567

# Has no testnet
