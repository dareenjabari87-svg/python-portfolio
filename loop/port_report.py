# port_report.py
# A Port Report

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

ports_checked = 0

for port in range(start_port, end_port + 1):
    if port <= 1023:
        print(f"{port}: system")
    elif port <= 49151:
        print(f"{port}: user")
    else:
        print(f"{port}: dynamic")

    ports_checked += 1

print(f"Ports checked: {ports_checked}")