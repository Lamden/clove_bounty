from clove.network.bitcoin import Bitcoin


class Hshare(Bitcoin):
    """
    Class with all the necessary Hshare network information based on
    https://github.com/HcashOrg/Hshare/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'hshare'
    symbols = ('HSR', )
    seeds = ("hshare-dns1.h.cash",
             "hshare-dns2.h.cash",
             "hshare-dns3.h.cash")
    port = 11616
    message_start = b'\x71\x31\x21\x11'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 193
    }


class HshareTestNet(Hshare):
    """
    Class with all the necessary Hshare testing network information based on
    https://github.com/HcashOrg/Hshare/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-hshare'
    seeds = ("testnode1.hshareplatform.com", )
    port = 26178
    message_start = b'\x71\x31\x21\x11'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 193
    }
