from clove.network.bitcoin import Bitcoin


class GlobalCoin(Bitcoin):
    """
    Class with all the necessary CryptoBullion network information based on
    https://github.com/cryptogenicbonds/cryptobullion-cbx/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'globalcoin'
    symbols = ('GLC', )
    seeds = ("ip 54.252.196.5", "ip 52.24.129.149")
    port = 55789
    message_start = b'\xe4\xe8\xe9\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 11,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 139
    }


# Has no Testnet
