import os
from random import randint
from typing import Optional

from ..exceptions import InvalidSessionPasswordOrNordVPNNotInstalledException
from ..exceptions import SudoModeNeedsSessionPasswordException
from .commands import Commands
from .interface import AbstractIpRotator
from .schemas import CallCounter

#une instruction os est reussie si son code de statut == 0
def check_unix_success_status_code(unix_status_code: int) -> bool:
    # Checking success of Unix status code for os.system instructions
    return unix_status_code == 0

#class NordVPNIpRotator implemente l'interface AbstractIpRotator
class NordVPNIpRotator(AbstractIpRotator):
    def __init__(
        self,
        login_id: str,
        password: str,
        session_password: Optional[str] = None, #obligatoire si sudo_mode = True
        sudo_mode: bool = False,
        call_counter: CallCounter = CallCounter(),
    ):
        
        """
        READ THIS !!!! :
        sudo_mode is True when we need to force sudo execution in the session. Meaning we need to provide
        a valid session password for us to be able to operate NordVPN.
        If sudo_mode is False, we do not need to provide a session password and everything will
        operate smoothly.
        The command line calls are always formatted using the session password, but it's okay
        as the formatting method of the <str> class does not format fileds that are not existent
        i.e. not defined by '{some_field}'
        ================================================
        ALSO THIS IS VERY IMPORTANT !!!! :
        ALWAYS VALIDATE an IP rotator before using it with the method .validate_ip_rotator(self).
        It was separated from the __init__ method to make its instructions testable.
        ================================================
        ALSO VERY IMPORTANT !!!!:
        Make sure you have run the installation command with .install_and_login(self) before
        trying to validate the ip rotator.
        If NordVPN is not installed, the validation will automatically fail.
        ================================================
        RUN THIS TO MAKE SURE EVERYTHING WORKS FINE ON YOUR MACHINE:
        First uninstall nordvpn with :
        sudo apt remove nordvpn && sudo apt purge nordvpn
        Then run this from a Python terminal/notebook:
        (session password is the current user's password on the machine)
        '''
        from scraping_project.shared.ip_rotation.ip_rotators import NordVPNIpRotator

        rotator = NordVPNIpRotator(login_id="account@gmail.com", password="password", session_password="session_password", sudo_mode=True)
        rotator.login() # First login
        rotator.validate_ip_rotator() # Then validate
        rotator.connect_to_vpn() # Connect
        rotator.disconnect_from_vpn() # Disconnect
        rotator.logout() # Logout

        '''

        If the install works properly on your machine, all these instructions should
        be executed.
        """
        self.login_id = login_id
        self.password = password
        self.session_password = session_password
        self.sudo_mode = sudo_mode
        self.call_counter = call_counter
    """
    verifie les conditions necessaires pour utiliser l'objet NordVPN : 
    si le mode sudo est activé, fournir session_password; 
    et verifier qu'il est valide et que NordVPN est installe
    """
    def validate_ip_rotator(self):
        if self.session_password is None and self.sudo_mode:
            raise SudoModeNeedsSessionPasswordException(value=None)
        if not self._validate_session_password():  #session_password valide et NordVPN installe
            raise InvalidSessionPasswordOrNordVPNNotInstalledException(value=self.session_password)
        
    """
    Selectionner un serveur aleatoirement
    parmi la liste des serveurs nordvpn_servers_list
    """
    def _choose_server(self) -> str:
        idx = randint(0, len(Commands.nordvpn_servers_list) - 1)
        return Commands.nordvpn_servers_list[idx]
    """
    Pour valider le mot de passe de session: 
    sudo_mode est activé --> executer une commande pour verifier la validité de session_password
        le resultat de cette commande est --> unix_status_code: 
            si unix_status_code != 256 : commande executee avec succes --> session_password valide
            sinon unix_status_code = 256 : echec --> session_password invalide
    sudo_mode desactive --> session_password non requis
    """
    def _validate_session_password(self) -> bool:
        if self.sudo_mode:
            unix_status_code = os.system(Commands.version_command[True].format(session_password=self.session_password))
            if unix_status_code == 256:
                return False
            return True
        return True
#Verifier que NordVPN est correctement installe 
    def check_installation(self) -> bool:
        install_status_code = os.system(
            Commands.version_command[self.sudo_mode].format(session_password=self.session_password), #verifier la version de VPN deja installee
        ) #=0 si installe sinon !=
        return check_unix_success_status_code(install_status_code)
#Se connecter a NordVPN after the installation
    def login(self) -> bool:
        login_status_code = os.system(
            Commands.nordvpn_login_command[self.sudo_mode].format(
                login=self.login_id,
                password=self.password,
                session_password=self.session_password,
            ),
        )
        return check_unix_success_status_code(login_status_code)
#Etablir la connexion VPN avec un serveur VPN specifique
    def connect_to_vpn(self) -> bool:
        server = self._choose_server()
        connect_status_code = os.system(
            Commands.nordvpn_connect_command[self.sudo_mode].format(
                server=server,
                session_password=self.session_password,
            ),
        )
        return check_unix_success_status_code(connect_status_code)
#pourquoi le serveur auquel on veut se deconnecter n'est pas specifie?
    def disconnect_from_vpn(self) -> bool:
        disconnect_status_code = os.system(
            Commands.nordvpn_disconnect_command[self.sudo_mode].format(session_password=self.session_password),
        )
        return check_unix_success_status_code(disconnect_status_code)

    def logout(self) -> bool:
        logout_status_code = os.system(
            Commands.nordvpn_logout_command[self.sudo_mode].format(session_password=self.session_password),
        )
        return check_unix_success_status_code(logout_status_code)

    def tutorial(self) -> str:
        print(Commands.nordvpn_tutorial)
        return Commands.nordvpn_tutorial

    def launch(self):
        # If IP rotator is not installed, install it; and then login
        self.login()
        # Validate that the IP rotator has the correct parameters to run properly
        # (usually installation and sudo password if needed)
        self.validate_ip_rotator()
        # Connect to VPN
        self.connect_to_vpn()
        # Set call count to 0 that triggers IP switch using rotator
        self.call_counter.call_count = 0

    def add_call(self):
        self.call_counter.call_count += 1 #self.call_counter.increment() ?
        if self.call_counter.call_count == 0:
            self.rotate_ip()
