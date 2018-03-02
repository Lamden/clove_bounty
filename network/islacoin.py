from clove.network.bitcoin import Bitcoin


class IslaCoin(Bitcoin):
    """
    Class with all the necessary IslaCoin network information based on
    https://github.com/islacoin/islacoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'islacoin'
    symbols = ('ISL', )
    seeds = ("seed1.islacoin.net", "seed2.islacoin.net", "seed3.islacoin.net", )
    port = 9731
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 102,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 230
    }


# Has no testnet
