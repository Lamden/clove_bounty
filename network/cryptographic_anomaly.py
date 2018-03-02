from clove.network.bitcoin import Bitcoin


class CryptographicAnomaly(Bitcoin):
    """
    Class with all the necessary Cryptographic Anomaly network information based on
    https://github.com/CryptographicAnomaly/CryptographicAnomaly2/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'cryptographic_anomaly'
    symbols = ('CGA', )
    seeds = ("cga.dnsseed.crypto2.net", )
    port = 3933
    message_start = b'\x4d\x63\x61\x44'
    base58_prefixes = {
        'PUBKEY_ADDR': 83,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 211
    }

# no testnet
