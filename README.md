# Simple SpeedTest CLI

Simple SpeedTest CLI is a lightweight and efficient tool for quickly checking internet speed, including download and upload speeds, and ping. It's built in Python and utilizes the `speedtest-cli` library.

## How to Install & use

To install Simple SpeedTest CLI, follow these simple steps:

1. Clone the repository or download the source code.
2. Navigate to the downloaded directory.
3. Run the following commands:

```bash
pip install -r requirements.txt
python simplecli.py
```
> [!NOTE]
> Python 3.9.0 & pip 20.2.3 was used for development and testing, so other versions are untested but still may work.

## Features
### Server Selection: 
Choose from the top 5 best servers in your area or let the tool select the best server automatically.

### Detailed Metrics: 
Displays comprehensive information such as server name, server ID, location, download and upload speeds, ping, and the time taken for both upload and download tests.

## Built With
[Python](https://www.python.org/): 
A powerful programming language that emphasizes readability and efficiency.

[speedtest-cli](https://pypi.org/project/speedtest-cli/): 
A command line interface for testing internet bandwidth using speedtest.net.

