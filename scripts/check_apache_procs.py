#!/usr/bin/env python3

# Proyecto ASIR - Monitorización Checkmk
# Script local check: procesos de Apache

import subprocess

result = subprocess.getoutput("pgrep -c apache2 2>/dev/null")

try:
    count = int(result)
except:
    count = 0

if count >= 1:
    state = 0
    status = "OK"
else:
    state = 2
    status = "CRITICAL"

print(f"{state} Apache_Processes - {status}: {count} procesos activos")
