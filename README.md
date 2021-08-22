# vba_bin_runner
Basic python tools to generate shellcode runner in vba
The stub use ZwAllocateVirtualMemory to allocate memory, RtlMoveMemory to write memory and EnumDateFormatsW to execute shellcode.

You can generate meterpreter/reverse_http (compatible cobalt strike), reverse_tcp and reverse_shell. 
In antiscan.me i have 0/26 detections in scantime. In runtime i bypass Defender and Kaspersky but if you use c2 some function can be detected by AV.

If the stub is detected you can edit/add junk code and change the function to allocate/write/execute. 
You can easyer edit this with : https://github.com/karttoon/trigen/blob/master/function_VBA_notes.txt

The macro self inject shellcode in word process, after macro is enabled the Word Application crash, if you want to patch this you can edit stub to inject shellcode in other process (explorer.exe for exemple).
If you use meterpreter you can add automigrate in your listener to keep connection after Word Application crash.

To keep stub long time no-detect use antiscan.me to check and no virus total. 

NB : Please don't use this for illegal activity

# For education only
