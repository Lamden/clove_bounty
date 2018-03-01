from clove.network.bitcoin import Bitcoin


class OlympCoin(Bitcoin):
    """
    Class with all the necessary OlympCoin network information based on
    https://github.com/olympcoin/OlympCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'olympcoin'
    symbols = ('OLYMP', )
    seeds = ("40.68.155.213")
    port = 3530
    message_start = b'\xb2\xc4\xd1\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 115,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 243
    }

# no testnet
