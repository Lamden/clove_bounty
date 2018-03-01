
from clove.network.bitcoin import Bitcoin


class BitcoinDiamond(Bitcoin):
    """
    Class with all the necessary BCD network information based on
    http://www.github.com/eveybcd/BitcoinDiamond/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'bitcoindiamond'
    symbols = ('BCD', )
    seeds = ('seed1.dns.btcd.io', 'seed2.dns.btcd.io', 'seed3.dns.btcd.io',
             'seed4.dns.btcd.io', 'seed5.dns.btcd.io', 'seed6.dns.btcd.io')
    port = 7117
    message_start = b'\xbd\xde\xb4\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class BitcoinDiamondTestNet(BitcoinDiamond):
    """
    Class with all the necessary BCD testing network information based on
    http://www.github.com/eveybcd/BitcoinDiamond/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-bitcoindiamond'
    seeds = ('testnet-seed.bitcoin.jonasschnelli.ch', 'seed.tbtc.petertodd.org',
             'testnet-seed.bluematt.me', 'testnet-seed.bitcoin.schildbach.de')
    port = 18333
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
