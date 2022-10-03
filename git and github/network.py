import os
import shutil
import socket

def check_reboot():
    """return True if the computer has a pending reboot"""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Return True if there isn't enough disk space, False otherwise"""
    du = shutil.disk_usage(disk)
    #calc % free space
    percent_free = 100 * du.free / du.total
    #calc free gb
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return True
    return False

def check_root_full():
    """Returns True if root partition is full, False otherwise"""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_network():
    """return True if network, false if not"""
    try:
        socket.gethostbyname("www.google.com")
        return True
    except:
        return False

def main():
    checks=[
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root partition full."),
        (check_network, "Network detected")
    ]
    everything_ok=True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok=False
        
    if not everything_ok:
        sys.exit(1)
