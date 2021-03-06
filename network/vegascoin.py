from clove.network.bitcoin import Bitcoin


class VegasCoin(Bitcoin):
    """
    Class with all the necessary VegasCoin network information based on
    https://github.com/VegasCoin/vegascoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'vegascoin'
    symbols = ('VGC', )
    seeds = ("node.vegascoin.co",
             "nodes.vegascoin.co",
             "west.eu.nodes.vegascoin.co",
             "east.eu.nodes.vegascoin.co",
             "east.us.nodes.vegascoin.co",
             "west.us.nodes.vegascoin.co",
             "asia.nodes.vegascoin.co",
             "oceania.nodes.vegascoin.co")
    port = 52400
    message_start = b'\xfc\xd9\xb7\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 58,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 186
    }

# no testnet
