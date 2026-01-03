import subprocess
import shutil

def check_service_status(service_name):
    """Checks if a systemd service is active."""
    try:
        # Runs 'systemctl is-active' which returns 'active' or 'inactive'
        result = subprocess.run(
            ["systemctl", "is-active", service_name],
            capture_output=True,
            text=True
        )
        status = result.stdout.strip()
        if status == "active":
            return f"✅ {service_name}: Running"
        else:
            return f"❌ {service_name}: {status}"
    except Exception:
        return f"❓ {service_name}: Not found or error"

def check_ap_capabilities():
    """Checks if the hardware supports AP mode."""
    if not shutil.which("iw"):
        return "⚠️  'iw' tool not found. Cannot check hardware."
    
    try:
        output = subprocess.check_output(["iw", "list"], text=True)
        return "✅ Hardware: AP Mode Supported" if "* AP" in output else "❌ Hardware: AP Mode NOT Supported"
    except:
        return "❓ Hardware: Error checking capabilities"

def main():
    print("--- AP Status Report ---")
    # 1. Check Hardware
    print(check_ap_capabilities())
    
    # 2. Check Services
    services = ["hostapd", "dnsmasq", "nftables"]
    for service in services:
        print(check_service_status(service))

if __name__ == "__main__":
    main()
