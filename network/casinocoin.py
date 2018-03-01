from clove.network.bitcoin import Bitcoin


class CasinoCoin(Bitcoin):
    """
    Class with all the necessary CasinoCoin network information based on
    https://github.com/casinocoin/casinocoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'casinocoin'
    symbols = ('CSC', )
    seeds = ("seed1.casinocoin.info",
             "seed.casinocoin.org",
             "seed.dig0.com",
             "seed2.casinocoin.info",
             "seed1.casinocoin.org",
             "seed1.dig0.com",
             "seed3.casinocoin.info",
             "seed2.casinocoin.org",
             "seed2.dig0.com",
             "seed4.casinocoin.info",
             "seed3.casinocoin.org",
             "seed5.casinocoin.info")
    port = 47950
    message_start = b'\xfa\xc3\xb6\xda'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 156
    }


class CasinoCoinTestNet(CasinoCoin):
    """
    Class with all the necessary CasinoCoin testing network information based on
    https://github.com/casinocoin/casinocoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-casinocoin'
    seeds = ("testnet-seed1.casinocoin.org")
    port = 17950
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 87,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 215
    }
