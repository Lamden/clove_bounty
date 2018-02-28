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
