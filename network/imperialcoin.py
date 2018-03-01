from clove.network.bitcoin import Bitcoin


class Imperialcoin(Bitcoin):
    """
    Class with all the necessary Diamond Imperialcoin information based on
    https://github.com/ImperialCoin/ImperialCoin/blob/newmaster/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'imperialcoin'
    symbols = ('IPC', )
    nodes = ("68.232.180.111",
             "54.94.148.228")
    port = 10240
    message_start = b'\x0A\x05\x03\x0C'
    base58_prefixes = {
        'PUBKEY_ADDR': 1,
        'SCRIPT_ADDR': 30,
        'SECRET_KEY': 224
    }

# no testnet
