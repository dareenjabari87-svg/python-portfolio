device_name = "edge-router"

# Syntax error: variable names cannot start with a number.
device_ip = "192.0.2.1"

# Syntax error: "class" is a Python keyword and cannot be used as a variable name.
device_type = "router"

# Runtime error: "twenty-two" cannot be converted to an integer.
port = 22

# Runtime error: device_nam is not defined; the correct variable name is device_name.
print("Device:", device_name)

print("Backup IP:", device_ip)
print("Type:", device_type)
print("Port:", port)