from clove.network.bitcoin import Bitcoin


class ArtByte(Bitcoin):
    """
    Class with all the necessary ArtByte (ABY) network information based on
    https://github.com/AppleByteMe/AppleByte/blob/master-0.13/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'artbyte'
    symbols = ('ABY', )
    seeds = ('dnsseed1.artbyte.me', 'dnsseed2.artbyte.me')
    port = 8608
    message_start = b'\xea\xaf\xa5\xca'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 151
    }


class ArtByteTestNet(ArtByte):
    """
    Class with all the necessary ArtByte (ABY) testing network information based on
    https://github.com/AppleByteMe/AppleByte/blob/master-0.13/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-artbyte'
    seeds = ('testnet-dnsseed1.artbyte.me', )
    port = 18608
    message_start = b'\xeb\xb0\xa6\xcb'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 193
    }
