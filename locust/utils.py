import socket
import time


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def get_ip_suffix():
    ip = get_ip()
    ip_suffix = "{:03}".format(int(ip.split('.')[-1]))
    return ip_suffix


def get_unique_datetime():
    return time.strftime("%d%H%M", time.localtime())


def get_unique_mobile(locust_id):
    ip_suffix = get_ip_suffix()
    return "123{}{:05}".format(ip_suffix, int(locust_id))
