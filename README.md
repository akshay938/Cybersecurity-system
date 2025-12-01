# Cybersecurity-system 
# 🔐 Cybersecurity System  
*A Vulnerability Analysis & Security Scanning Tool*

This project is a complete cybersecurity toolkit designed to analyze URLs, detect vulnerabilities, classify spam, and generate actionable reports. It combines Machine Learning, Python-based scanners, security headers analysis, and automated testing to improve application security posture.

---

## 🚀 Features

### 🔍 **1. Vulnerability Scanning**
- SQL Injection detection  
- XSS (Cross-Site Scripting) checks  
- URL validation  
- Malicious content checking  
- Suspicious behavior and patterns detection  

### 🧠 **2. Spam Detection (Machine Learning)**
- ML classifier using **TF-IDF + Naive Bayes**
- Detects spam vs non-spam messages  
- Fast inference with real-time results  

### 🌐 **3. Security Header Analysis**
- Checks presence of critical headers:
  - HSTS  
  - CSP  
  - X-XSS-Protection  
  - X-Frame-Options  
- Provides practical recommendations  

### 🛡 **4. SSL & Certificate Evaluation**
- Validates TLS versions  
- Certificate expiry checks  
- Weak cipher identification  

### 📡 **5. Open Port Scanning**
- Lightweight port scanning using socket connections  
- Detects open ports and potential misconfigurations  

### 📊 **6. PDF/Console Reporting**
- Structured vulnerability summary  
- Severity-based rating  
- Developer-friendly remediation tips  

---

## 🧰 **Tech Stack**

| Layer | Tools Used |
|-------|------------|
| **Programming** | Python |
| **ML** | TF-IDF, Naive Bayes |
| **Libraries** | scikit-learn, requests, urllib, pandas |
| **Security** | Header analysis, SSL checks |
| **Deployment** | GitHub |

---

## 📁 **Project Structure**

Cybersecurity-system/
│── data/ # ML datasets (spam/ham)
│── modules/ # Python security scanning modules
│── report/ # Reports / outputs
│── main.py # Main entry script
│── requirements.txt # Dependencies
│── README.md # Documentation (this file)
└── tempCodeRunnerFile.py