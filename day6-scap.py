from scapy.all import IP, ICMP, sr1

# Define the target IP address
target_ip = "www.google.com"

# Craft an ICMP packet (ping request)
packet = IP(dst=target_ip) / ICMP()

# Send the packet and receive a response
response = sr1(packet, timeout=2, verbose=False)

# Check if a response was revieved
if response:
    print(f"Received response from {response.src}")
else:
    print("No respone received")