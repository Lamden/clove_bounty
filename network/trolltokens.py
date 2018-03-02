from clove.network.bitcoin import Bitcoin


class TrollTokens(Bitcoin):
    """
    Class with all the necessary trolltokens network information based on
    https://github.com/Justbob1956/TrollTokens/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'trolltokens'
    symbols = ('TKN', )
    nodes = ("68.117.4.111", )
    port = 16385
    message_start = b'\xa4\xd2\xf8\xa4'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 183
    }

# no testnet
