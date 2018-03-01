from clove.network.bitcoin import Bitcoin


class BeaverCoin(Bitcoin):
    """
    Class with all the necessary BeaverCoin network information based on
    https://github.com/BeaverCoin-Project/beavercoin/blob/master-0.10/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'beavervoin'
    symbols = ('BVC', )
    seeds = ("dnsseed.beavercoin.org", )
    port = 2333
    message_start = b'\xfd\xc2\xb8\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 176
    }


class BeaverCoinTestNet(BeaverCoin):
    """
    Class with all the necessary BeaverCoin testing network information based on
    https://github.com/BeaverCoin-Project/beavercoin/blob/master-0.10/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-beavervoin'
    seeds = ("testnet-seed.beavercoin.org", )
    port = 12333
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
