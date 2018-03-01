from clove.network.bitcoin import Bitcoin


class BitcoinAtom(Bitcoin):
    """
    Class with all the necessary Bitcoin Atom (BCA) network information based on
    https://github.com/bitcoin-atom/bitcoin-atom/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'bitcoinatom'
    symbols = ('BCA', )
    seeds = (
        'seed.bitcoin.sipa.be', 'dnsseed.bluematt.me', 'dnsseed.bitcoin.dashjr.org', 'seed.bitcoinstats.com',
        'seed.bitcoin.jonasschnelli.ch', 'seed.btc.petertodd.org', 'seed.bitcoinatom.io', 'seed.bitcoin-atom.org',
        'seed.bitcoinatom.net'
    )
    port = 7333
    message_start = b'\x4f\xc1\x1d\xe8'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 10,
        'SECRET_KEY': 128
    }


class BitcoinAtomTestNet(BitcoinAtom):
    """
    Class with all the necessary Bitcoin Atom (BCA) testing network information based on
    https://github.com/bitcoin-atom/bitcoin-atom/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-bitcoinatom'
    seeds = ('testnet-seed.bitcoin.jonasschnelli.ch', 'seed.tbtc.petertodd.org', 'testnet-seed.bluematt.me',
             'testnet-seed.bitcoinatom.io', 'testnet-seed.bitcoin-atom.org', 'testnet-seed.bitcoinatom.net')
    port = 17333
    message_start = b'\xa6\x8e\x3f\xd6'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
