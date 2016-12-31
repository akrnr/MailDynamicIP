# Main application
#
# @author   Orhun Dalabasmaz
# @since    Dec, 2016

import time
import httplib2
from MailService import *
from config.IPConfig import file_name, host_name


def trim(val):
    return val.strip(' \t\n\r')


def log(msg):
    dt = time.strftime("%Y-%m-%d %H:%M:%S")
    print '[' + dt + '] - ' + msg


def get_ip_address():
    resp, content = httplib2.Http().request("http://ipinfo.io/ip")
    return trim(content)


def check_last_ip(ip):
    file = open(file_name, 'a+')
    file.seek(0, 0)
    last_ip = trim(file.readline())
    is_ip_changed = not(ip == last_ip)
    if is_ip_changed:
        file = open(file_name, 'w')
        file.write(ip + '\n')
    file.close()
    return is_ip_changed


if __name__ == '__main__':
    ip = get_ip_address()
    is_ip_changed = check_last_ip(ip)
    if is_ip_changed:
        log('IP changed! ' + ip)
        send_mail(host_name + ' [IP Changed]', ip)
    else:
        log('IP not changed.')
