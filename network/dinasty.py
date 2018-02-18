from clove.network.bitcoin import Bitcoin


class Dinasty(Bitcoin):
    """
    Class with all the necessary Dinasty (DCY) network information based on
    https://github.com/dinastyoffreedom/dinastycoin/blob/master/src/CryptoNoteConfig.h
    (date of access: 02/17/2018)
    """
    name = 'dinasty'
    symbols = ('DCY', )
    seeds = ('212.237.18.169', '94.177.178.226', '94.177.178.107', '77.81.235.77',
			 '77.81.235.178', '77.81.235.78', '89.46.76.87')
    port = 37175

# no testnet
