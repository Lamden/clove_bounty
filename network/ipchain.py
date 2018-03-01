from clove.network.bitcoin import Bitcoin


class IPChain(Bitcoin):
    """
    Class with all the necessary IPChain network information based on
    https://github.com/IPCChain/ipchain/blob/master/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'ipchain'
    symbols = ('IPC', )
    seeds = ("seed.ipchainglobal.com",
             "seed.qingdoutech.com")
    port = 15166
    message_start = b'\xda\xd8\xd7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 4,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }


class IPChainTestNet(IPChain):
    """
    Class with all the necessary IPChain testing network information based on
    https://github.com/IPCChain/ipchain/blob/master/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-ipchain'
    seeds = ("seedt.ipchainglobal.com",
             "seedt.qingdoutech.com")
    port = 25166
    message_start = b'\x2a\x28\x27\x2c'
    base58_prefixes = {
        'PUBKEY_ADDR': 3,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
