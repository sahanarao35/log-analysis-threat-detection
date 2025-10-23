Log Analysis & Threat Detection

# Log Analysis and Threat Detection

This project analyzes Linux authentication logs to detect suspicious login attempts, such as repeated failed SSH logins, and generates a report of potentially malicious IP addresses. It is a beginner-friendly cybersecurity project showcasing log parsing, threat detection, and reporting skills.

---

## 🧰 Tools and Technologies
- **Python 3** – for scripting and data processing  
- **Pandas** – for data manipulation  
- **Regex** – for pattern matching in logs  
- **CSV** – for storing output report  
- Optional: **AbuseIPDB / VirusTotal API** (for future enhancement)

---

## 📁 Project Structure
log-analysis-threat-detection/
│
├── data/
│ └── sample_logs.log # Sample log file to analyze
│
├── scripts/
│ └── analyze_logs.py # Python script for analysis
│
├── reports/
│ └── suspicious_ips.csv # Output report of suspicious IPs
│
├── README.md # Project overview
└── requirements.txt # Python dependencies


## 🚀 How to Run
1. Clone the repository:
git clone https://github.com/<your-username>/log-analysis-threat-detection.git

Navigate to the scripts folder:
cd log-analysis-threat-detection/scripts

Install dependencies:
pip install -r ../requirements.txt

Run the analysis script:
python analyze_logs.py

Check the output report:

/reports/suspicious_ips.csv
This file contains IP addresses with failed login attempts above the defined threshold.

📊 Sample Output
IP_Address	Failed_Attempts
203.0.113.45	6
198.51.100.23	5

🔧 Features
Parses Linux auth.log style files
Counts failed SSH login attempts per IP
Flags IPs exceeding a threshold (default: 5)
Generates a CSV report for SOC or threat investigation

🌟 Future Enhancements
Integrate with AbuseIPDB or VirusTotal API to verify suspicious IPs
Visualize failed login attempts using Matplotlib
Add a notebook version with step-by-step analysis for easier demonstration
Extend to other log types (firewall, web server, Windows logs)

📌 References
Linux auth.log format
Python Regex Documentation
Pandas Documentation

