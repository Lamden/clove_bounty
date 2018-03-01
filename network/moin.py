from clove.network.bitcoin import Bitcoin


class Moin(Bitcoin):
    """
    Class with all the necessary Moin (MOIN) network information based on
    https://github.com/MOIN/moin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'moin'
    symbols = ('MOIN', )
    seeds = ('seed.discovermoin.com', 'seed2.discovermoin.com', )
    port = 7997
    message_start = b'\x23\xfc\x25\x9c'
    base58_prefixes = {
        'PUBKEY_ADDR': 51,
        'SCRIPT_ADDR': 115,
        'SECRET_KEY': 179
    }


class MoinTestNet(Moin):
    """
    Class with all the necessary Moin (MOIN) testing network information based on
    https://github.com/MOIN/moin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-moin'
    seeds = ('testnet-seed.discovermoin.com', )
    port = 17997
    message_start = b'\xfa\x10\x70\x2f'
    base58_prefixes = {
        'PUBKEY_ADDR': 112,
        'SCRIPT_ADDR': 177,
        'SECRET_KEY': 250
    }
