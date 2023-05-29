from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
import os
import subprocess
class Router():
    def check_connection(self,ip_check):
        a= "ok"
        try:
            subprocess.check_output(['ping', '-c', '1', ip_check])
            return a
        except subprocess.CalledProcessError:
            a= "Can not connect to Device"
            return False

a= Router()
ab = a.check_connection('8.8.8.8')
print(ab)