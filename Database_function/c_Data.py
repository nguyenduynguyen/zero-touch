from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
from jnpr.junos.exception import LockError
from jnpr.junos.exception import UnlockError
from jnpr.junos.exception import CommitError
from jnpr.junos.exception import ConfigLoadError
import os
import subprocess
class Router():
    def replace_text(self,file_name,old_text,new_text):
        with open(file_name, "r+") as file:
            content = file.read()
            new_content = content.replace(old_text,new_text)
            file.seek(0)
            file.write(new_content)
            file.close()
    def check_connection(self,ip_check):
        a= "ok"
        try:
            subprocess.check_output(['ping', '-c', '1', ip_check])
            return a
        except subprocess.CalledProcessError:
            a= "Can not connect to Device"
            return a
    def configuration_router(self,ip_host,username,password,conf_file):
        try:
            dev = Device(host= ip_host,user=username,passwd=password)
            dev.open()
        except ConnectError as err:
            print("Can not connect to Device: {0}".format(err))
            return
        dev.bind(cu=Config)
        # lock the configuration
        print("locking the configuration")
        try:
            dev.cu.lock()
        except LockError as err:
            print("unable to lock configuration : {0}".format(err))
            dev.close()
            return
        # load the configuration
        print("load configuration changes ")
        try:
            # dev.cu.load('set system services netconf traceoptions file test.log',format='set')
            dev.cu.load(path=conf_file, merge=True)
        except (ConfigLoadError,Exception) as err:
            print("unable to load configuration changes : {0}".format(err))
            print("unlocking the configuration")
            try:
                dev.cu.unlock()
            except UnlockError as err:
                print("unable to unlock the configuration: {0}".format(err))
            dev.close()
        print("commit the configuration")
        try:
            dev.cu.commit()
        except CommitError as err:
            print("unable to commit the configuration: {0}".format(err))
            print("unlocking the configuration")
            try:
                dev.cu.unlock()
            except UnlockError as err:
                print("unable to unlock the configuration : {0}".format(err))
            dev.close()
        print("unlocking the configuration")
        try:
            dev.cu.unlock()
        except UnlockError as err:
            print("unable to unlock the configuration : {0}".format(err))
        dev.close()
# a= Router()
# ab= a.configuration_router("10.254.200.5","nguyennd","bh6k8mfmnpk5bkh")
