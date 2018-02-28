from clove.network.bitcoin import Bitcoin


class Bottlecaps(Bitcoin):
    """
    Class with all the necessary Bottlecaps network information based on
    https://github.com/bottlecaps-foundation/bottlecaps/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bottlecaps'
    symbols = ('CAP', )
    seeds = ("seed.bottlecaps.org", "cap.nodes.btcrypt.net")
    port = 7685

# Has no testnet
