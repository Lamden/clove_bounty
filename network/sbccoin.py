from clove.network.bitcoin import Bitcoin


class StrikeBitClub(Bitcoin):
    """
    Class with all the necessary StrikeBitClub network information based on
    https://github.com/sbccoin/sbccoin-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'strikebitclub'
    symbols = ('SBC', )
    seeds = ("sbc01.seednode.online","sbc02.seednode.online")
    port = 21575


# Has no testnet
 
