# EPFO Account Access Automation

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

A Python automation script to access your EPFO (Employees' Provident Fund Organization) account, view passbook, and retrieve service history programmatically.

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## ✨ Features

- 🔐 **Secure Login** - Login to EPFO portal with UAN and password
- 📖 **View Passbook** - Access your EPF passbook with complete transaction history
- 📊 **Service History** - Retrieve your complete employment service history
- 💾 **Download Passbook** - Download passbook as PDF for offline access
- ✅ **Input Validation** - Validates UAN format (12 digits)
- 🔒 **Password Security** - Hidden password input for security
- 🤖 **Browser Automation** - Automated navigation through EPFO portal

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7 or higher**
- **Google Chrome Browser** (latest version)
- **ChromeDriver** (compatible with your Chrome version)
- **Active EPFO Account** with UAN and password

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Deadshot0x7/epfo-access-automation.git
cd epfo-access-automation
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
selenium==4.15.2
webdriver-manager==4.0.1
requests==2.31.0
```

### Step 4: Install ChromeDriver

**Option A: Automatic (Recommended)**
```bash
pip install webdriver-manager
```
The script will automatically download the correct ChromeDriver version.

**Option B: Manual**
1. Download ChromeDriver from [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)
2. Extract and add to your system PATH

## 🚀 Usage

### Basic Usage

```bash
python epfo_access.py
```

### Step-by-Step Process

1. **Run the script:**
   ```bash
   python epfo_access.py
   ```

2. **Enter your credentials:**
   ```
   Enter your UAN (Universal Account Number): 123456789012
   Enter your EPFO password: ********
   ```

3. **Confirm your UAN:**
   ```
   UAN entered: 123456789012
   Is this correct? (y/n): y
   ```

4. **Solve the Captcha manually** when the browser opens

5. **Press Enter** after solving captcha

6. **Choose your action:**
   ```
   What would you like to access?
   1. Passbook
   2. Service History
   3. Both
   Enter your choice (1/2/3): 3
   ```

7. **View your data** in the browser window

8. **Download (Optional):** Choose to download passbook when prompted

## ⚙️ Configuration

### Headless Mode

To run the script without opening a visible browser window, uncomment this line in the code:

```python
# chrome_options.add_argument('--headless')
```

### Download Location

By default, files download to your system's default Downloads folder. To change this:

```python
prefs = {
    "download.default_directory": "/path/to/your/folder",
    "download.prompt_for_download": False,
}
chrome_options.add_experimental_option("prefs", prefs)
```

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. ChromeDriver Version Mismatch
**Error:** `SessionNotCreatedException: Message: session not created`

**Solution:**
```bash
pip install --upgrade webdriver-manager
```

#### 2. Element Not Found
**Error:** `NoSuchElementException`

**Solution:** 
- Check your internet connection
- Ensure EPFO portal is accessible
- Try increasing wait times in the script

#### 3. UAN Validation Failed
**Error:** `Invalid UAN! UAN should be 12 digits.`

**Solution:** 
- Ensure your UAN is exactly 12 digits
- Remove any spaces or special characters

#### 4. Captcha Issues
**Problem:** Captcha expires before solving

**Solution:**
- Solve captcha quickly
- Refresh the page if captcha expires
- Ensure stable internet connection

#### 5. Login Failed
**Possible Causes:**
- Incorrect UAN or password
- Account locked due to multiple failed attempts
- EPFO portal maintenance

**Solution:**
- Verify credentials on EPFO portal manually
- Wait 30 minutes if account is locked
- Check EPFO portal status

## 🔒 Security

### Important Security Notes

- ⚠️ **Never share your credentials** with anyone
- ⚠️ **Never commit credentials** to version control
- ⚠️ **Use environment variables** for sensitive data (optional):

```python
import os
uan = os.getenv('EPFO_UAN')
password = os.getenv('EPFO_PASSWORD')
```

- ⚠️ **Keep dependencies updated** to patch security vulnerabilities
- ⚠️ **Use this script only on trusted devices**

### Environment Variables Setup

**Windows:**
```cmd
set EPFO_UAN=123456789012
set EPFO_PASSWORD=yourpassword
```

**Linux/MacOS:**
```bash
export EPFO_UAN=123456789012
export EPFO_PASSWORD=yourpassword
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Update README for new features
- Test thoroughly before submitting PR

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Deadshot0x7

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

## ⚠️ Disclaimer

This is an **unofficial** automation script and is **NOT affiliated** with EPFO or the Government of India.

### Important Points:

- This script is for **personal use only**
- Use at your **own risk**
- The author is **not responsible** for:
  - Any misuse of this script
  - Any data loss or corruption
  - Account suspension or blocking by EPFO
  - Any violations of EPFO terms of service
- Always ensure you comply with **EPFO's terms and conditions**
- This script may **break** if EPFO updates their portal structure
- **Do not use** for commercial purposes
- **Do not share** your credentials with anyone

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Search existing [Issues](https://github.com/Deadshot0x7/epfo-access-automation/issues)
3. Create a new issue with:
   - Error message
   - Python version
   - Operating system
   - Steps to reproduce

## 🔗 Useful Links

- [EPFO Official Portal](https://unifiedportal-mem.epfindia.gov.in/)
- [EPFO Help](https://www.epfindia.gov.in/)
- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Python Documentation](https://docs.python.org/3/)

## 🎯 Roadmap

- [ ] Add support for EPF withdrawal claims
- [ ] Implement OTP-based login
- [ ] Add email notification feature
- [ ] Create GUI interface
- [ ] Add data export to Excel/CSV
- [ ] Schedule automated passbook downloads
- [ ] Multi-account support

## ⭐ Star History

If you find this project helpful, please consider giving it a star! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=Deadshot0x7/epfo-access-automation&type=Date)](https://star-history.com/#Deadshot0x7/epfo-access-automation&Date)

## 👨‍💻 Author

**Deadshot0x7**
- GitHub: [@Deadshot0x7](https://github.com/Deadshot0x7)
- Email: sviquarahmed@gmail.com

## 💖 Support the Project

If you find this project helpful and would like to support its development, you can buy me a coffee! ☕

### UPI Payment
<p align="center">
  <img src="https://img.shields.io/badge/UPI-sviquarahmed@okaxis-orange?style=for-the-badge&logo=upi" alt="UPI">
</p>

**UPI ID:** `sviquarahmed@okaxis`

Your support helps keep this project maintained and improved. Thank you! 🙏

### Other Ways to Support
- ⭐ Star this repository
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 🤝 Contribute code
- 📢 Share with others who might find it useful

## 🙏 Acknowledgments

- Selenium WebDriver team
- Python community
- All contributors to this project
- Everyone who has supported this project

---

**Made with ❤️ for easier EPFO access**

**⚡ Remember:** This tool is meant to simplify your EPFO access, not replace the official portal. Always verify important information on the official EPFO website.

---

<p align="center">
  <sub>If this project helped you, consider supporting it! 💝</sub>
</p>
