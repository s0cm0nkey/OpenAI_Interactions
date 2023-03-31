# OpenAI_Interactions
Tools, scripts, and Ideas for interacting with OpenAI

This repository is to document and share out ideas for interacting with OpenAI in various ways.

## OpenAIExplain.py
[OpenAiExplain.py](https://github.com/s0cm0nkey/OpenAI_Interactions/blob/main/OpenAIExplain.py) - Simple python script that allows you to take a command line string that you are unfamilair with, and submit it to OpenAI to explain.
Super helpful for junior Security Analysts who are not as familiar with all of the commands and parameters found in CLI tools.

**Input:**

*"C:\Windows\system32.cmd.exe" /c ping.exe -n02 -w 500 192.168.8.11>C:\Users\s0cm0nkey\AppData\Local\Temp\radBBE9D.tmp*

**Output:**

*The command string is running the Windows Command Prompt (cmd.exe) utility with the "/c" switch, which instructs the command prompt to execute a specified command and then exit. The command being executed is the "ping.exe" utility, which is used to send an ICMP echo request to a specified host and receive an ICMP echo reply. The "-n 2" switch specifies that two requests should be sent, and the "-w 500" switch specifies the timeout (in milliseconds) for each request. Finally, the IP address of the host to which the requests should be sent is "192.168.8.11", and the output of the command will be written to the file "C:\Users\s0cm0nkey\AppData\Local\Temp\radBBE9D.tmp".*
