import re
import pandas as pd
from collections import Counter

# Load log file
log_file = "../data/sample_logs.log"

# Regex pattern to match failed SSH logins
pattern = r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)"

with open(log_file, "r") as f:
    logs = f.read()

# Extract IPs
ips = re.findall(pattern, logs)
ip_counts = Counter(ips)

# Convert to DataFrame
df = pd.DataFrame(ip_counts.items(), columns=["IP_Address", "Failed_Attempts"])
df = df.sort_values(by="Failed_Attempts", ascending=False)

# Flag suspicious IPs
threshold = 5
suspicious = df[df["Failed_Attempts"] > threshold]

# Save results
suspicious.to_csv("../reports/suspicious_ips.csv", index=False)
print("✅ Report generated at /reports/suspicious_ips.csv")
