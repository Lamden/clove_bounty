from clove.network.bitcoin import Bitcoin


class Teacoin(Bitcoin):
    """
    Class with all the necessary Teacoin network information based on
    https://github.com/teacoind/teacoin/blob/master/src/chainparams.cpp
    (date of access: 02/21/2018)
    """
    name = 'teacoin'
    symbols = ('TEA', )
    seeds = ("66.85.164.76")
    port = 7921
    message_start = b'\x1a\x2b\x3c\x4e'
    base58_prefixes = {
        'PUBKEY_ADDR': 66,
        'SCRIPT_ADDR': 9,
        'SECRET_KEY': 224
    }

# no testnet
