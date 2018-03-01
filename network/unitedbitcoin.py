from clove.network.bitcoin import Bitcoin


class UnitedBitcoin(Bitcoin):
    """
    Class with all the necessary UnitedBitcoin (UBTC) network information based on
    https://github.com/UnitedBitcoin/UnitedBitcoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'unitedbitcoin'
    symbols = ('UBTC', )
    seeds = ('ip.ub.com', )
    port = 8333
    message_start = b'\xf9\xbe\xb4\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class UnitedBitcoinTestNet(UnitedBitcoin):
    """
    Class with all the necessary UnitedBitcoin (UBTC) testing network information based on
    https://github.com/UnitedBitcoin/UnitedBitcoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-unitedbitcoin'
    seeds = ('testnet-seed.bitcoin.jonasschnelli.ch',
             'seed.tbtc.petertodd.org', 'testnet-seed.bluematt.me')
    port = 18333
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
