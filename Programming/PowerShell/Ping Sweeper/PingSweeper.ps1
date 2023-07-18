$scriptPath = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition
$ipAddresses = Get-Content -Path "$scriptPath\ping.txt"
$outputFile = Join-Path -Path $scriptPath -ChildPath "ping_results.txt"

foreach ($ip in $ipAddresses) {
    if ($ip -like '*\*') {
        $rangeStart, $rangeEnd = $ip -split '\s+'
        $rangeStart = $rangeStart.Trim()
        $rangeEnd = $rangeEnd.Trim()
        
        $rangeStartIP = [System.Net.IPAddress]::Parse($rangeStart)
        $rangeEndIP = [System.Net.IPAddress]::Parse($rangeEnd)
        
        $currentIP = $rangeStartIP
        
        while ($currentIP.CompareTo($rangeEndIP) -le 0) {
            $pingReply = Test-Connection -ComputerName $currentIP.IPAddressToString -Count 1 -Quiet
            
            if ($pingReply) {
                "${currentIP.IPAddressToString}: Reply" | Out-File -Append -FilePath $outputFile
            }
            else {
                "${currentIP.IPAddressToString}: No Reply" | Out-File -Append -FilePath $outputFile
            }
            
            $currentIP = [System.Net.IPAddress]::Parse($currentIP.GetAddressBytes() + 1)
        }
    }
    else {
        $pingReply = Test-Connection -ComputerName $ip -Count 1 -Quiet
    
        if ($pingReply) {
            "${ip}: Reply" | Out-File -Append -FilePath $outputFile
        }
        else {
            "${ip}: No Reply" | Out-File -Append -FilePath $outputFile
        }
    }
}

Write-Host "Ping sweep completed. Results saved in $outputFile"
