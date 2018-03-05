
from clove.network.bitcoin import Bitcoin


class TransferCoin(Bitcoin):
    """
    Class with all the necessary TX network information based on
    http://www.github.com/transferdev/Transfercoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'transfercoin'
    symbols = ('TX', )
    seeds = ('txdns.infernopool.com', 'txdns2.infernopool.com',
             'txdns3.infernopool.com')
    port = 17170
    message_start = b'\xd1\x2e\x1e\xe6'
    base58_prefixes = {
        'PUBKEY_ADDR': 66,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }
