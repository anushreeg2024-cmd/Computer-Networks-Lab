import scapy
from scapy.all import rdpcap
from collections import Counter
packets = rdpcap("Anushree.pcap")
print("Total packets:", len(packets))
src_ips = set()
dst_ips = set()
protocols = []
for pkt in packets:
    if pkt.haslayer("IP"):
        src_ips.add(pkt["IP"].src)
        dst_ips.add(pkt["IP"].dst)
        protocols.append(pkt["IP"].proto)
print("Number of Source IPs:", len(src_ips))
print("Number of Destination IPs:", len(dst_ips))
print("Number of Protocols Used:", len(set(protocols)))
proto_count = Counter(protocols)
print("Packets per Protocol:")
for proto, count in proto_count.items():
    print(proto, ":", count)