from clove.network.bitcoin import Bitcoin


class  Abjcoin(Bitcoin):
    """
    Class with all the necessary  Abjcoin (ABJ) network information based on
    https://github.com/abjcoinblockchain/Abjcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'abjcoin'
    symbols = ('ABJ', )
    seeds =  ('209.188.21.177', '209.188.21.177', '199.188.207.212', '199.188.207.212')
    port = 29303


class  AbjcoinTestNet(Abjcoin):
    """
    Class with all the necessary  Abjcoin (ABJ) network information based on
    https://github.com/abjcoinblockchain/Abjcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-abjcoin'
    symbols = ('ABJ', )
    seeds =  ()
    port = 39303