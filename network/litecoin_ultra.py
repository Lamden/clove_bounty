from clove.network.bitcoin import Bitcoin


class LitecoinUltra(Bitcoin):
    """
    Class with all the necessary Litecoin Ultra (LTCU) network information based on
    https://github.com/TheCryptoServices/LiteCoinUltra/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'litecoinultra'
    symbols = ('LTCU', )
    seeds = ('litecoinultra2.dyndns.org')
    port = 19540
    message_start = b'\xcd\x22\xd1\xa5'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 176
    }

# no testnet
