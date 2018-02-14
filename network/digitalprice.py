from clove.network.bitcoin import Bitcoin


class DigitalPrice(Bitcoin):
    """
    Class with all the necessary DigitalPrice network information based on
    https://github.com/DigitalPrice/DigitalPrice/releases from source
    (date of access: 02/14/2018)
    """
    name = 'digitalprice'
    symbols = ('DP', )
    seeds = ("dns0.digitalprice.org",
             "dns1.digitalprice.org",
             "dns2.digitalprice.org",
             "dns3.digitalprice.org",
             "dns4.digitalprice.org",
             "dns5.digitalprice.org",
             "dns6.digitalprice.org",
             "dns7.digitalprice.org",
             "dns8.digitalprice.org",
             "dns9.digitalprice.org")
    port = 42742

	
