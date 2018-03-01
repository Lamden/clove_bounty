from clove.network.bitcoin import Bitcoin


class Cryptographic_Anomaly(Bitcoin):
    """
    Class with all the necessary Cryptographic Anomaly network information based on
    https://github.com/CryptographicAnomaly/CryptographicAnomaly2/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'cryptographic_anomaly'
    symbols = ('CGA', )
    seeds = ("cga.dnsseed.crypto2.net")
    port = 3933

# no testnet
