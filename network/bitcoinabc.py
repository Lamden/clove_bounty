from clove.network.bitcoin import Bitcoin


class BitcoinABC(Bitcoin):
    """
    Class with all the necessary BitcoinABC network information based on
    https://github.com/Bitcoin-ABC/bitcoin-abc/blob/master/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'bitcoinabc'
    symbols = ('BABC', )
    seeds = ("seed.bitcoinabc.org",
             "seed-abc.bitcoinforks.org",
             "btccash-seeder.bitcoinunlimited.info",
             "seed.bitprim.org",
             "seed.deadalnix.me",
             "seeder.criptolayer.net")
    port = 8333
    message_start = b'\xe3\xe1\xf3\xe8'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class BitcoinABCTestNet(BitcoinABC):
    """
    Class with all the necessary BitcoinABC testing network information based on
    https://github.com/Bitcoin-ABC/bitcoin-abc/blob/master/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-bitcoinabc'
    seeds = ("testnet-seed.bitcoinabc.org",
             "testnet-seed-abc.bitcoinforks.org",
             "testnet-seed.bitprim.org",
             "testnet-seed.deadalnix.me",
             "testnet-seeder.criptolayer.net")
    port = 18333
    message_start = b'\xf4\xe5\xf3\xf4'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
