<div align="center">

# 🔑 PassForge CLI

**Cryptographically secure password generator and entropy/brute-force resistance auditor.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Security](https://img.shields.io/badge/CSPRNG-secrets%20module-red?style=for-the-badge)]()
[![Dependencies](https://img.shields.io/badge/Dependencies-None-orange?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

</div>

---

## 📖 Overview

**PassForge CLI** is a security tool built on Python's cryptographically strong `secrets` module (CSPRNG) rather than standard pseudo-random generators. It generates high-entropy passwords and evaluates existing passwords against modern GPU cluster brute-force attack speeds.

---

## ⚡ Key Features

- **CSPRNG Generation:** Uses `secrets.choice()` and `secrets.SystemRandom()` for true OS-level cryptographic randomness.
- **Guaranteed Complexity:** Ensures at least one character from every selected character set is included and shuffled securely.
- **Information Entropy Calculator:** Computes exact password entropy in bits ($E = L \times \log_2(R)$).
- **Brute-Force Time Estimation:** Calculates theoretical crack time assuming an offline GPU rig running at **100 billion guesses/second**.

---

## 🚀 Installation & Usage

### 1. Clone the repository
```bash
git clone [https://github.com/ASDcuber/passforge-cli.git](https://github.com/ASDcuber/passforge-cli.git)
cd passforge-cli
