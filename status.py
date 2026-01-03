import subprocess
import shutil

def check_ap_support():
    # 1. Check if the 'iw' tool exists
    if not shutil.which("iw"):
        return "Error: 'iw' command not found. Please install it."

    try:
        # 2. Run 'iw list' and capture the output
        result = subprocess.check_output(["iw", "list"], stderr=subprocess.STDOUT, text=True)
        
        # 3. Look for the specific 'AP' capability
        if "* AP" in result:
            return "✅ Your networking card supports AP mode."
        else:
            return "❌ AP mode is NOT supported by this hardware/driver."
            
    except subprocess.CalledProcessError:
        return "Error: Could not retrieve wireless capabilities."

if __name__ == "__main__":
    print(check_ap_support())
