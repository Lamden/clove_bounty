from clove.network.bitcoin import Bitcoin


class Bottlecaps(Bitcoin):
    """
    Class with all the necessary Bottlecaps network information based on
    https://github.com/bottlecaps-foundation/bottlecaps/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bottlecaps'
    symbols = ('CAP', )
    seeds = ("seed.bottlecaps.org", "cap.nodes.btcrypt.net", )
    port = 7685
    message_start = b'\xe4\xe8\xe9\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 34,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 162
    }

# Has no testnet
