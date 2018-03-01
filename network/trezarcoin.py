from clove.network.bitcoin import Bitcoin


class Trezarcoin(Bitcoin):
    """
    Class with all the necessary Trezarcoin network information based on
    https://github.com/TrezarCoin/TrezarCoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'trezarcoin'
    symbols = ('TZC', )
    seeds = ("seed0.trezarcoin.com", "seed1.trezarcoin.com", )
    port = 17298
    message_start = b'\xe4\xef\xdb\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 66,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 194
    }

# no testnet
