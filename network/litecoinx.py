from clove.network.bitcoin import Bitcoin


class LiteCoinX(Bitcoin):
    """
    Class with all the necessary LiteCoinX network information based on
    https://bitbucket.org/LiteCoinXProject/litecoinx/src/c52883aa2a5ee0c45d858d3ace1790f3e9d3b624/src/net.cpp?at=master&fileviewer=file-view-default
    (date of access: 02/16/2018)
    """
    name = 'litecoinx'
    symbols = ('LTCX', )
    seeds = ("108.61.196.125","114.215.110.130")
    port = 12316

# no testnet