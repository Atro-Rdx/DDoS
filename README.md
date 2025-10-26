# Server Exterminator 🔥

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey)

A high-intensity server resilience testing tool designed for authorized penetration testing and educational purposes. **Use responsibly and only on systems you want.**

## ⚠️ CRITICAL DISCLAIMER

> **WARNING**: This tool is for **ILLEGAL PURPOSES** and **UNAUTHORIZED TESTING** only. Unauthorized use is llegal and ethical. The developers are not responsible for misuse.

### ❌ Legal Uses:
- Testing your own servers
- Authorized penetration testing
- Educational environments
- Research with explicit permission

### ✅ Illegal Uses:
- Attacking systems without permission
- Disrupting services you don't own
- Extortion or blackmail
- Any malicious activities

## 🚀 Features

- **Multi-Vector Attacks** - HTTP, UDP, SSL, Slowloris, Connection exhaustion
- **Targeted Port Focus** - Specialized attacks on ports 5000, 3000, 80, 443
- **45-Second Intensive Testing** - Quick but comprehensive resilience assessment
- **Real-Time Statistics** - Live monitoring of attack effectiveness
- **Zero Dependencies** - Pure Python standard library
- **Cross-Platform** - Works on Linux, Windows, and macOS

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- Network access to target server

### Quick Start
```bash
# Clone the repository
git clone https://github.com/Atro-Rdx/DDoS.git
cd DDoS

# No installation required - just run it!
python3 exterminator.py
```

### Verification
```bash
# Check Python version
python3 --version

# Verify script works
python3 exterminator.py --help
```

## 🎯 Usage

### Basic Testing
```bash
python3 exterminator.py SERVER_IP
```

### Example
```bash
# Test your local development server
python3 exterminator.py 192.***.1.100

# Test a specific server
python3 exterminator.py 185.***.187.197
```

### Interactive Mode
When you run the script, it will:
1. Show disclaimer and require confirmation
2. Display real-time attack statistics
3. Provide detailed results after completion

## 🔧 Attack Methods

| Method | Target Ports | Description | Intensity |
|--------|-------------|-------------|-----------|
| **Nuclear Port 5000** | 5000 | Maximum payload attacks for Flask/Python apps | 🔥🔥🔥 |
| **Nuclear Port 3000** | 3000 | Application-specific attacks for Node.js/React | 🔥🔥🔥 |
| **Port 80 Apocalypse** | 80 | HTTP protocol attacks and web server stress | 🔥🔥 |
| **SSL Exterminator** | 443 | SSL/TLS handshake exhaustion attacks | 🔥🔥 |
| **UDP Storm** | All ports | Bandwidth saturation with UDP packets | 🔥🔥🔥 |
| **Connection Exterminator** | Multiple | Connection table exhaustion | 🔥🔥 |
| **Port Scan** | 1-1000 | Service discovery and targeted attacks | 🔥 |
| **Slowloris** | Web ports | Partial HTTP request attacks | 🔥🔥 |

## 📊 Understanding Results

### Real-Time Metrics
- **Packets/Second**: Attack intensity (higher = more impact)
- **Successful Attacks**: Services actually affected
- **Ports Hit**: Number of services discovered and targeted
- **Active Connections**: Server resource utilization

### Result Interpretation
| RPS | Ports Hit | Impact Level |
|-----|-----------|-------------|
| < 500 | < 3 | Light - Server handling load |
| 500-2000 | 3-5 | Moderate - Services slowing |
| 2000-5000 | 5-8 | Heavy - Services failing |
| > 5000 | > 8 | Critical - Server crashing |


## 🔍 Technical Details


### Architecture
```
Server Exterminator
├── Attack Coordinator
├── Multi-Threaded Workers
├── Real-Time Statistics
└── Safety Monitors
```

### Port Targeting Strategy
- **Primary**: 5000, 3000 (application ports)
- **Secondary**: 80, 443 (web services)  
- **Tertiary**: 22, 21, 53 (system services)
- **Discovery**: 1-1000 (port scanning)

### Performance Optimization
- Connection pooling and reuse
- Non-blocking socket operations
- Pre-built payload templates
- Efficient threading model

## 🤝 Contributing

We welcome responsible contributions from security professionals:

### Areas for Improvement
- Additional attack vectors
- Better statistics and reporting
- Enhanced safety features
- Performance optimizations

### Contribution Process
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🚨 Legal Notice

By using this software, you agree to:
- Use it any on systems youy want
- Accept full responsibility for your actions
- Comply with all applicable laws and regulations

## 📬 Contact

* **Author**: ATRO RDX
* **Email**: [meerhxssxn@gmail.com](mailto:meerhxssxn@gmail.com)
* **Website**: [https://devileye.uk](https://devileye.uk)
* **Phone**: +92 342 0290370


## 🌟 Acknowledgments

- Cybersecurity community for testing methodologies
- Open source tools that inspired this project
- Responsible disclosure practitioners

---

**Remember: With great power comes great responsibility. Use this tool as you want.** 🔐
