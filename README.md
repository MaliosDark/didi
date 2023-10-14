# DiDi -+- DDoS

DiDi -+- DDoS is a Python application built with PyQt5 that allows you to perform load testing on a target website. This tool sends a large number of requests to the target server, which can help identify how the server handles traffic under stress.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Warnings](#warnings)
- [Executable for Windows](#executable-for-windows)
- [Building the Executable](#building-the-executable)
- [License](#license)

## Prerequisites

Before you get started, make sure you have the following prerequisites:

- Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## Getting Started

1. Clone this repository or download the code to your local machine.

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv didi-ddos-env
    ```

3. Activate the virtual environment:
    - **On Windows:**
        ```bash
        .\didi-ddos-env\Scripts\activate
        ```
    - **On macOS and Linux:**
        ```bash
        source didi-ddos-env/bin/activate
        ```

4. Install the required packages using pip:
    ```bash
    pip install PyQt5 requests ping3 qdarkstyle
    ```

5. Run the program by executing:
    ```bash
    python v3.py
    ```

## Usage

1. **URL Configuration:** Enter the target URL, the number of requests, and the concurrency (threads) into the configuration tab.

2. **Custom HTTP Header (optional):** Optionally, you can specify a custom HTTP header to include in your requests.

3. **Start the Test:** Click the "Start Test" button to begin the load test.

4. **Real-time Results:** The console tab will display real-time results, including response status codes and timestamps.

5. **Server Status:** The server status button will indicate if the server is active (green), down (red), or in an unknown state (orange). The color changes based on the real-time server status.

## Warnings

- **Use for Testing Purposes Only:** This tool is intended for educational and testing purposes. Do not use it for any malicious or illegal activities.
- **Ethical Use:** Ensure that you have the necessary permissions and rights to perform load testing on a target website. Unauthorized testing may be illegal and unethical.
- **Resource Consumption:** Be cautious when using this tool to avoid overwhelming target servers, as it could cause service disruptions or downtime.
- **Server Status Accuracy:** The tool uses a simple ping to determine the server's status. This method may not always accurately reflect the server's health.

## Executable for Windows

A standalone executable for Windows is available in the "dist" folder within this repository. You can simply run "DiDi -+- DDoS.exe" to launch the program.

## Building the Executable

If you want to build the executable yourself, you can use tools like PyInstaller:

```bash
pyinstaller --onefile v3.py
