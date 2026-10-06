# System Health Check

A lightweight Python utility for checking basic system health information such as CPU usage, memory consumption, disk space, and operating system details.

## Features

* Display operating system information
* Show CPU usage
* Monitor memory usage
* Check available disk space
* Display hostname and system architecture
* Provide a simple overall health status
* Warn when resource usage is high

## Requirements

* Python 3.8 or newer
* `psutil`

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/system-health-check.git
cd system-health-check
```

Install the required dependency:

```bash
pip install psutil
```

## Usage

Run the health check with:

```bash
python health_check.py
```

Example output:

```text
=============================================
        SYSTEM HEALTH CHECK
=============================================
OS:           Windows 11
Architecture: AMD64
Hostname:     DESKTOP-PC
Python:       3.12.4
CPU Usage:    18.2%
Memory:       7.4 GB / 16.0 GB
Memory Usage: 46.3%
Disk Usage:   186.2 GB / 476.8 GB
Disk Used:    39.0%
---------------------------------------------
Status:       HEALTHY
=============================================
```

## How It Works

The script collects basic system statistics using Python's standard library and the `psutil` package.

CPU and memory information are retrieved from the operating system, while disk usage is calculated using the available filesystem information.

The program then compares resource usage against predefined thresholds and displays a warning when unusually high usage is detected.

## Project Structure

```text
system-health-check/
├── health_check.py
└── README.md
```

## Resource Thresholds

The default warning thresholds are:

| Resource | Warning Level |
| -------- | ------------- |
| CPU      | 90% or higher |
| Memory   | 90% or higher |
| Disk     | 90% or higher |

These values can be adjusted directly in `health_check.py` if needed.

## Supported Platforms

The utility is designed to work on common platforms supported by Python and `psutil`, including:

* Windows
* Linux
* macOS

## Privacy

System information is processed locally by the script. The utility does not upload collected information to an external server.

## License

This project is released under the MIT License.

See the `LICENSE` file for details.

## Contributing

Contributions and suggestions are welcome. Feel free to open an issue or submit a pull request.

## Disclaimer

This project is intended for basic system monitoring and educational purposes.
