#Script to send email with info about our server

#a function that returns an IP addresa starting with 192
function getIP {
(Get-NetIPAddress).IPv4Address | Select-String "192*"
}
function getName {
(Get-LocalUser) | Select-String "Admin*"
}
function getHost {
(Get-Host).Name
}
function getVersion{
(Get-Host).Version
}
function getDate {
(Get-Date)
}
#Set Date
$Date=getDate

#Set Version
$Version=getVersion

#Set HostName
$myHost=getHost

#Set UserName
$env:USERNAME=getName

#Set IP Address
$IP=getIP

#Set the body variable
$BODY = "This is my IP Address: $IP , User is $env:USERNAME , the host name is: $myHost , the Version is $Version , and the date is: $Date ."

#build and send the email
Send-MailMessage -To "16eyerlyj@gmail.com" -From "me@gmail.com"  -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -Port 587 -UseSsl -Credential (Get-Credential)

#confirmation the code worked
Write-Host("Email Sent")