# Ping Sweep PowerShell Script

The Ping Sweep PowerShell Script is a utility that automates the process of pinging multiple IP addresses or IP address ranges to identify active hosts on a network. This script is useful for network administrators, security professionals, or anyone who needs to assess the availability and responsiveness of devices within a specified IP range.

## Features

- Performs a ping sweep on a list of IP addresses or IP address ranges.
- Records ping results (Reply or No Reply) for each IP address in a separate file.
- Supports both individual IP addresses and CIDR notation for IP address ranges.

## Usage

1. Create a file named `ping.txt` and list the IP addresses or IP address ranges you want to ping, each on a separate line. Ensure that the `ping.txt` file is located in the same directory as the `ping-sweep.ps1` script.

    - Example `ping.txt` contents:
    ```
    192.168.0.1
    10.1.25.0/24
    ```

2. Run the PowerShell script `ping-sweep.ps1` using PowerShell. The `ping_results.txt` file will be created in the same directory as the script.

    - Example command:
    ```
    PS C:\Path\To\Script> .\ping-sweep.ps1
    ```

3. After execution, the ping results will be saved in a file named `ping_results.txt` located in the same directory as the script.

## Supported Devices

The Ping Sweep PowerShell Script can be used on any device that supports PowerShell, including:
- Windows computers (Desktops, Laptops, Servers)
- Virtual machines running Windows OS
- Windows-based network devices

## Limitations

- The script requires administrative privileges to execute the `Test-Connection` cmdlet.
- The script assumes that the target IP addresses are reachable from the machine where it is executed.
- For comprehensive network scanning or vulnerability assessments, specialized tools and techniques should be used.
