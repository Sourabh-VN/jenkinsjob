import socket

def get_ip_address():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = '127.0.0.1'
    finally:
        s.close()
    
    return ip_address

if __name__ == '__main__':
    ip = get_ip_address()
    print(f"IP Address: {ip}")
