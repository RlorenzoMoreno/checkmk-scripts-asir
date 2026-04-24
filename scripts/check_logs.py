#!/usr/bin/env python3

# Proyecto ASIR - Monitorización Checkmk
# Script local check: análisis de logs

log_file = "/var/log/syslog"
error_count = 0

with open(log_file, "r") as f:
    lines = f.readlines()[-50:]
    for line in lines:
        if "error" in line.lower():
            error_count += 1

if error_count == 0:
    state = 0
    status = "OK"
elif error_count < 5:
    state = 1
    status = "WARNING"
else:
    state = 2
    status = "CRITICAL"

print(f"{state} Check_Logs - {status}: {error_count} errores encontrados")
