import shutil
import os
from pathlib import Path

def backup_configs():
    # 1. Define where to save things locally
    local_backup_dir = Path("./conf")
    local_backup_dir.mkdir(exist_ok=True)
    
    # 2. Map of "Service Name": "Expected Path"
    # We use lists for paths in case your system uses non-standard locations
    config_map = {
        "hostapd": ["/etc/hostapd/hostapd.conf", "/etc/hostapd.conf"],
        "dnsmasq": ["/etc/dnsmasq.conf", "/etc/dnsmasq.d/"],
        "nftables": ["/etc/nftables.conf", "/etc/sysconfig/nftables.conf"],
        "custom": ["/usr/local/bin/setup-hotspot-ip.sh"]
        # "interfaces": ["/etc/network/interfaces", "/etc/netplan/"]
    }

    print(f"--- Backing up configs to {local_backup_dir.absolute()} ---")

    for service, paths in config_map.items():
        found = False
        for path_str in paths:
            source = Path(path_str)
            
            if source.exists():
                dest = local_backup_dir / source.name
                try:
                    # Handle both files and entire directories (like dnsmasq.d)
                    if source.is_dir():
                        shutil.copytree(source, dest, dirs_exist_ok=True)
                    else:
                        shutil.copy2(source, dest)
                    
                    print(f"✅ {service}: Copied {path_str}")
                    found = True
                    break # Stop looking once we find a valid config
                except PermissionError:
                    print(f"❌ {service}: Permission denied. Run with sudo.")
                    found = True
                    break
                except Exception as e:
                    print(f"❌ {service}: Error copying {path_str} ({e})")
        
        if not found:
            print(f"⚠️  {service}: No config file found in standard locations.")

if __name__ == "__main__":
    backup_configs()
