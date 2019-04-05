#!/usr/bin/python

"""
Script runs remote commands on multiple hosts
"""

import os
import sys
import json
import string
import threading
import paramiko
import getpass


cmd = "<your cmd>"
password = getpass.getpass("Password: ")

outlock = threading.Lock()


def workon(host):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username='<user>', password=password)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    stdin.write('sudo\n')
    stdin.flush()

    with outlock:
        print(stdout.readlines(json))


def main():
    hosts = ['<IP1>', '<IP2>' ]
    threads = []
    for h in hosts:
        t = threading.Thread(target=workon, args=(h,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
