from clove.network.bitcoin import Bitcoin


class Quotient(Bitcoin):
    """
    Class with all the necessary Quotient network information based on
    https://github.com/CedricProfit/Quotient/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Quotient'
    symbols = ('XQN', )
    seeds = ("seed.quotientcoin.com")
    port = 30994
    message_start = b'\xef\xb2\xfa\xf2'
    base58_prefixes = {
        'PUBKEY_ADDR': 58,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 186
    }


# Has no Testnet
