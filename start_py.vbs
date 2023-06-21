Set ws = CreateObject("Wscript.Shell")
ws.run "cmd /c set_py.bat",0

Set ws2 = CreateObject("Wscript.Shell")
ws.run "cmd /c show_ip.bat",1

