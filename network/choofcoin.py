from clove.network.bitcoin import Bitcoin


class ChoofCoin(Bitcoin):
    """
    Class with all the necessary ChoofCoin network information based on
    https://github.com/choofcoin/choofcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'choofcoin'
    symbols = ('CHOOF', )
    nodes = ("162.243.1.45", )
    port = 7777
    message_start = b'\xa4\xa6\xfd\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 156
    }

# Has no testnet
