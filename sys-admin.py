import os
import subprocess

#os.system("ls -l")
#subprocess.run(["ls","-l","README.md"])

command = "ps"
commandArgument = "-x"

print("Gather information system with command: %s %s" % (command, commandArgument))
subprocess.run([command, commandArgument])
