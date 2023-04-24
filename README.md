# OpenAI_Interactions
Tools, scripts, and Ideas for interacting with OpenAI

This repository is to document and share out ideas for interacting with OpenAI in various ways.

Here is a link to my Gitbook with research articles I have written about my explorations into AI integration.
https://s0cm0nkey.gitbook.io/s0cm0nkeys-research-articles/v/openai-research/

## OpenAIExplain.py
[OpenAiExplain.py](https://github.com/s0cm0nkey/OpenAI_Interactions/blob/main/OpenAIExplain.py) - Simple python script that allows you to take a command line string that you are unfamilair with, and submit it to OpenAI to explain.
Super helpful for junior Security Analysts who are not as familiar with all of the commands and parameters found in CLI tools.

**Input:**

*"C:\Windows\system32.cmd.exe" /c ping.exe -n02 -w 500 192.168.8.11>C:\Users\s0cm0nkey\AppData\Local\Temp\radBBE9D.tmp*

**Output:**

*The command string is running the Windows Command Prompt (cmd.exe) utility with the "/c" switch, which instructs the command prompt to execute a specified command and then exit. The command being executed is the "ping.exe" utility, which is used to send an ICMP echo request to a specified host and receive an ICMP echo reply. The "-n 2" switch specifies that two requests should be sent, and the "-w 500" switch specifies the timeout (in milliseconds) for each request. Finally, the IP address of the host to which the requests should be sent is "192.168.8.11", and the output of the command will be written to the file "C:\Users\s0cm0nkey\AppData\Local\Temp\radBBE9D.tmp".*

**BUT WAIT THERE'S MORE!**

Can also be used to explain unfamiliar detection logic such as SNORT rules.
![Screen Shot 2023-03-31 at 3 18 16 PM](https://user-images.githubusercontent.com/74802544/229210059-baa19fa0-1269-4501-9629-1b0d48d9f244.png)

Output:
*This SNORT rule is used to detect traffic related to the Trojan TeleBots BCS-server CnC Beacon, which is a malicious software used to steal data. The rule is triggered when a POST request is sent from the home network to an external HTTP port with a body containing a value field within 6 bytes, and a Content-Type and Referer header. If the rule is triggered, an alert will be sent and the traffic will be blocked. The alert will have the reference URL of www.welivesecurity.com/2016/12/13/rise-telebots-analyzing-disruptive-killdisk-attacks/ and the class type of trojan-activity. The rule also has a unique sid of 2023652 and a revision number of 1.*
