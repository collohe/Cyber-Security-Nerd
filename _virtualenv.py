import requests
import pandas as pd

# Example 1: Fetch IP Blacklist
url = "https://dnschecker.org/ip-blacklist-checker.php?query=192.168.10.1"
response = requests.get(url)

if response.status_code == 200:
    data = response.text.splitlines()
    # Skip header rows if needed
    ips = [line.strip() for line in data if line and not line.startswith("#")]
    df = pd.DataFrame(ips, columns=["Malicious_IP"])
    df.to_csv("malicious_ips.csv", index=False)
    print("[+] Malicious IPs saved to malicious_ips.csv")
else:
    print(f"Failed to fetch IPs: {response.status_code}")
