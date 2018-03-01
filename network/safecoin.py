from clove.network.bitcoin import Bitcoin


class SafecCoin(Bitcoin):
    """
    Class with all the necessary SafecCoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'safecoin'
    symbols = ('SFE', )
    seeds = ("seed.bitcoin.sipa.be",
             "dnsseed.bluematt.me",
             "dnsseed.bitcoin.dashjr.org",
             "bitseed.xf2.org")
    port = 8333
    message_start = b'\xe4\xe8\xbd\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 90,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 218
    }


class SafecCoinTestNet(SafecCoin):
    """
    Class with all the necessary SafecCoin testing network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-safecoin'
    seeds = ("testnet-seed.bitcoin.petertodd.org",
             "testnet-seed.bluematt.me")
    port = 18333
    message_start = b'\x45\x76\x65\xba'
    base58_prefixes = {
        'PUBKEY_ADDR': 139,
        'SCRIPT_ADDR': 19,
        'SECRET_KEY': 239
    }
