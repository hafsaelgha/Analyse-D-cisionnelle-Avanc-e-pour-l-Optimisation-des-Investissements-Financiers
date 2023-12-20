from .config import Config
from .interfaces import VpnAPIScraper
from .interfaces import VpnWebScraper
from scraping_project.shared.ip_rotation.ip_rotators import NordVPNIpRotator

#### Here we use specifically the NordVPN IP rotator and implement
# the IP rotation processing that each scraper class should implement
# for the NordVPN IP rotator !!! ####
class NordVpnAPIScraper(VpnAPIScraper):
    def __init__(self, api_url: str, logger, ip_rotator: NordVPNIpRotator):
        super().__init__(api_url, logger, ip_rotator)
        self.ip_rotator = ip_rotator

    def process_ip_rotation(self):
        if self.ip_rotator.call_counter.call_count == 0:
            self._generate_new_headers() #cookies et autre info, 


class NordVpnWebScraper(VpnWebScraper):
    def __init__(self, logger, ip_rotator: NordVPNIpRotator, proxy=None, local_db_uri=None):
        super().__init__(logger, ip_rotator, proxy, local_db_uri)
        self.ip_rotator = ip_rotator

    def process_ip_rotation(self):
        if self.ip_rotator.call_counter.call_count == 0:  #Fermer le navigateur actuel et changer vpn et lancer un nouveau
            if self.browser:
                self.browser.quit()
                self.browser = None
            self.start_browser(
                headless=Config.headless,
                chrome_driver_path=Config.chrome_path,
                use_docker_options=Config.use_docker,
            )
