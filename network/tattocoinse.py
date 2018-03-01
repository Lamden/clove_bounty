from clove.network.bitcoin import Bitcoin


class TattocoinSE(Bitcoin):
    """
    Class with all the necessary Tattocoin Standard Edition (TSE) network information based on
    https://github.com/CryptoCoderz/Tattoocoin-TSE/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'tattocoinse'
    symbols = ('TSE', )
    seeds = ('195.74.52.227', '149.56.154.65')
    port = 9959
    message_start = b'\x72\x7c\x80\x10'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 193
    }


class TattocoinSETestNet(TattocoinSE):
    """
    Class with all the necessary Tattocoin Standard Edition (TSE) testing network information based on
    https://github.com/CryptoCoderz/Tattoocoin-TSE/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-tattocoinse'
    seeds = ('91.134.120.210')
    port = 19959
