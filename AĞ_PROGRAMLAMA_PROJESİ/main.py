import json
import pandas as pd
from pyvis.network import Network
from collections import defaultdict
import webbrowser

# Load the JSON file with UTF-8 encoding
with open('veri.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract packet data
packets = data  # Adjust this if your JSON structure is different

# Create a DataFrame to store relevant data
packet_list = []

for packet in packets:
    layer = packet['_source']['layers']
    frame = layer.get('frame', {})
    ip_layer = layer.get('ip', {})
    protocol = frame.get('frame.coloring_rule.name', '')
    length = int(frame.get('frame.len', 0))  # Convert length to integer

    packet_info = {
        'frame_number': frame.get('frame.number', ''),
        'src_ip': ip_layer.get('ip.src', ''),
        'dst_ip': ip_layer.get('ip.dst', ''),
        'protocol': protocol,
        'length': length
    }
    
    packet_list.append(packet_info)

df = pd.DataFrame(packet_list)

# Aggregate packets by src_ip and dst_ip
edge_dict = defaultdict(lambda: {'count': 0, 'protocols': set(), 'lengths': []})

for _, row in df.iterrows():
    src = row['src_ip']
    dst = row['dst_ip']
    protocol = row['protocol']
    length = row['length']
    
    if src and dst:
        edge_dict[(src, dst)]['count'] += 1
        edge_dict[(src, dst)]['protocols'].add(protocol)
        edge_dict[(src, dst)]['lengths'].append(length)

# Define color mappings for different count ranges
def get_edge_color(protocols):
    protocol_color_map = {
        'HTTP': 'blue',
        'HTTPS': 'green',
        'DNS': 'red',
        'TCP': 'orange',
        'UDP': 'salmon',
        'SMTP': 'purple',
        'FTP': 'brown',
        'SSH': 'pink',
        'ICMP': 'cyan',
        'ARP': 'magenta',
        'TELNET': 'lime',
        'POP3': 'gold',
        'IMAP': 'teal',
        'SNMP': 'olive',
        'NTP': 'navy',
        'DHCP': 'indigo',
        'LDAP': 'violet',
        'SMB': 'coral',
        'RDP': 'yellow',
        'SSL': 'darkred',
        'TLS': 'darkgreen',
        'IKEv2': 'darkblue',
        'IPsec': 'darkorange',
        'GRE': 'sienna',
        'BGP': 'steelblue',
        'MPLS': 'tan',
        'OSPF': 'tomato',
        'RIP': 'wheat',
        'VRRP': 'darkslategray',
        'IGMP': 'cadetblue',
        # İhtiyacınız olan diğer protokol türlerini buraya ekleyebilirsiniz
    }
    
    default_color = 'gray'  # Belirli bir protokol türüne renk ataması yoksa varsayılan gri renk
    
    # İlk protokolü alıp onun rengini alıyoruz
    for protocol in protocols:
        color = protocol_color_map.get(protocol, default_color)
        if color != default_color:
            return color
    
    # Eğer hiçbir renk ataması yapmadıysak, varsayılan rengi döndürüyoruz
    return default_color

# Create a PyVis network
net = Network(height='750px', width='100%', notebook=True, directed=True)

# Add nodes and edges based on aggregated data
nodes = set()
for (src, dst), info in edge_dict.items():
    if src not in nodes:
        net.add_node(src, label=src)
        nodes.add(src)
    if dst not in nodes:
        net.add_node(dst, label=dst)
        nodes.add(dst)
    
    protocols = info['protocols']
    count = info['count']
    lengths = info['lengths']
    
    # Choose a color for the edge based on protocols
    color = get_edge_color(protocols)
    
    # Set title for the edge
    title = f"Protocols: {', '.join(protocols)}\nCount: {count}\nMin Length: {min(lengths)}\nMax Length: {max(lengths)}"
    
    # Kalınlığı paket sayısına göre ayarla
    thickness = count
    
    # Add the edge with specified color and thickness
    net.add_edge(src, dst, title=title, color=color, arrows='to', width=thickness)

# Generate the visualization and save it as an HTML file
html_file = 'packet_network.html'
net.show(html_file)

# Open the generated HTML file in the default web browser
webbrowser.open(html_file)
