from clove.network.bitcoin import Bitcoin


class MarxCoin(Bitcoin):
    """
    Class with all the necessary MarxCoin network information based on
    https://github.com/marxcoin01/marx/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'marxcoin'
    symbols = ('MARX', )
    seeds = ("seed4.cryptolife.net", "seed2.cryptolife.net",
             "seed3.cryptolife.net", "electrum3.cryptolife.net")
    port = 41103
    message_start = b'\xfe\xc3\xb9\xde'
    base58_prefixes = {
        'PUBKEY_ADDR': 51,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 179
    }


# Has no testnet
