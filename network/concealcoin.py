from clove.network.bitcoin import Bitcoin


class ConcealCoin(Bitcoin):
    """
    Class with all the necessary ConcealCoin network information based on
    https://github.com/concealcoin/concealcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'concealcoin'
    symbols = ('CNL', )
    seeds = ("54.76.49.245")
    port = 27712
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 128
    }

# Has no testnet
