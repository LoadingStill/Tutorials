# Ping Sweep PowerShell Script

The Ping Sweep PowerShell Script is a utility that automates the process of pinging multiple IP addresses or IP address ranges to identify active hosts on a network. This script is useful for network administrators, security professionals, or anyone who needs to assess the availability and responsiveness of devices within a specified IP range.

## Features

- Performs a ping sweep on a list of IP addresses or IP address ranges.
- Records ping results (Reply or No Reply) for each IP address in a separate file.
- Supports both individual IP addresses and CIDR notation for IP address ranges.

## Usage

1. Create a file named `ping.txt` in the same directory as the `ping-sweep.ps1` script.
   - Add the IP addresses or IP address ranges you want to ping to the `ping.txt` file, each on a separate line.

      Example `ping.txt` contents:
      ```
      192.168.0.1
      10.1.25.0/24
      ```

2. Run the PowerShell script `ping-sweep.ps1` using PowerShell. The script will automatically create a `ping_results.txt` file in the same directory as the script.

   Example command:
