from clove.network.bitcoin import Bitcoin


class PirateBlocks(Bitcoin):
    """
    Class with all the necessary Pirate Blocks (SKULL) network information based on
    https://github.com/pirateblocks/PBlocks/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'pirateblocks'
    symbols = ('SKULL', )
    seeds = ('pblocks.servep2p.com')
    port = 27991
    message_start = b'\xa1\xac\xcc\x71'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 32,
        'SECRET_KEY': 145
    }

# no testnet
