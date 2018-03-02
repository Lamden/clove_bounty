from clove.network.bitcoin import Bitcoin


class Cryptonite(Bitcoin):
    """
    Class with all the necessary Cryptonite network information based on
    https://github.com/MiniblockchainProject/Cryptonite/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'cryptonite'
    symbols = ('XCN', )
    seeds = ("gpile.it", )
    port = 8253
    message_start = b'\xf9\xbe\xb4\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class CryptoniteTestNet(Cryptonite):
    """
    Class with all the necessary Diamond testing network information based on
    https://github.com/MiniblockchainProject/Cryptonite/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-cryptonite'
    seeds = ("seed.cryptonite.info", )
    port = 18253
    message_start = b'\x0c\x12\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 87,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
