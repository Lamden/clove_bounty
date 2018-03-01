from clove.network.bitcoin import Bitcoin


class DickCoin(Bitcoin):
    """
    Class with all the necessary DickCoin network information based on
    https://github.com/DickCoin/Source/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'dickcoin'
    symbols = ('DCK', )
    seeds = ("seed1.cryptolife.net",
             "seed2.cryptolife.net",
             "seed3.cryptolife.net",
             "electrum1.cryptolife.net",
             "wallet.cryptolife.net",
             "explore.cryptolife.net")
    port = 41018
    message_start = b'\xc4\xf8\xe7\xe8'
    base58_prefixes = {
        'PUBKEY_ADDR': 31,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 159
    }

# Has no testnet
