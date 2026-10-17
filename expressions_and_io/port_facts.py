
# Source: RFC 9293 - TCP Source Port and Destination Port are 16 bits.
# Source: RFC 791 - IPv4 addresses have a fixed length of 32 bits.

PORT_BITS = 16
IPV4_BITS = 32

possible_ports = 2 ** PORT_BITS
highest_port = 2 ** PORT_BITS - 1
possible_ipv4_addresses = 2 ** IPV4_BITS

print(f"Possible port numbers: {possible_ports}")
print(f"Highest port number: {highest_port}")
print(f"Possible IPv4 addresses: {possible_ipv4_addresses}")
