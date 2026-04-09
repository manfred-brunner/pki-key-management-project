#  PKI & Certificate Lifecycle Project (OpenSSL + Azure Key Vault)

##  Overview

This project demonstrates a **real-world implementation of a Public Key Infrastructure (PKI)** combined with **cloud-based certificate management using Azure Key Vault**.

The goal was to simulate how certificates are created, managed, and rotated in an enterprise environment.

---

##  Architecture

```
Root CA (offline)
   ↓
Intermediate CA
   ↓
Server Certificate (localhost)
   ↓
HTTPS Demo Server (Python)
   ↓
Azure Key Vault (secure storage & versioning)
```

---

##  Technologies Used

* OpenSSL (PKI & certificate generation)
* Azure Key Vault (certificate storage & lifecycle management)
* Python (HTTPS demo server)
* WSL (Linux environment on Windows)

---

##  Key Features

### 1. PKI Implementation

* Created Root CA and Intermediate CA
* Implemented certificate signing workflow
* Managed CA database (`index.txt`, `serial`)

---

### 2. Certificate Lifecycle Management

* Generated TLS certificates with Subject Alternative Names (SAN)
* Built full certificate chain (Root → Intermediate → Server)
* Demonstrated certificate renewal and rotation

---

### 3. HTTPS Demo Service

* Implemented a local HTTPS server using Python
* Configured TLS with custom certificates
* Debugged real-world TLS issues (SAN, trust chain)

---

### 4. Azure Key Vault Integration

* Exported certificates as `.pfx`
* Imported into Azure Key Vault
* Implemented RBAC for secure access
* Demonstrated certificate versioning (multiple versions under same name)

---

## 🔄 Certificate Rotation Demo

* Created initial certificate (`v1`)
* Imported into Key Vault
* Generated a new certificate (`v2`)
* Re-imported under the same name
* Verified multiple versions in Key Vault

---

## 🧠 Key Learnings

* Importance of Subject Alternative Names (SAN)
* Certificate chain validation and trust model
* OpenSSL CA state management (`index.txt`)
* Azure RBAC vs traditional access control
* Practical certificate lifecycle challenges

---

## 🚀 How to Run

Start the HTTPS server:

```bash
python3 demo-server.py
```

Then open:

```
https://localhost:4443
```



## 📌 Future Improvements

* mTLS (client certificate authentication)
* Automated certificate rotation
* Integration with real applications or APIs
