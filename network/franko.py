from clove.network.bitcoin import Bitcoin


class Franko(Bitcoin):
    """
    Class with all the necessary FRK network information based on
    http://www.github.com/franko-org/franko/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'franko'
    symbols = ('FRK', )
    seeds = ('seed.bitcoin.sipa.be',)
    port = 8333
    message_start = b'\xf9\xbe\xb4\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class FrankoTestNet(Franko):
    """
    Class with all the necessary FRK testing network information based on
    http://www.github.com/franko-org/franko/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-franko'
    seeds = (
        'dnsseed.bluematt.me', 'dnsseed.bitcoin.dashjr.org', 'seed.bitcoinstats.com', 'bitseed.xf2.org',
        'seed.bitcoin.jonasschnelli.ch', 'testnet-seed.alexykot.me', 'testnet-seed.bitcoin.petertodd.org',
        'testnet-seed.bluematt.me', 'testnet-seed.bitcoin.schildbach.de'
    )
    port = 18333
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
