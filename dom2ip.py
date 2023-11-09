import socket
import concurrent.futures

def resolve_domain(domain):
    domain = domain.strip()
    try:
        ip = socket.gethostbyname(domain)
        print(f"Resolved {domain} to {ip}")
        return ip
    except socket.gaierror:
        print(f"Could not resolve {domain}")
        return None

def domain_to_ip(input_file, output_file):
    with open(input_file, 'r') as f_in:
        domains = f_in.readlines()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        ips = list(executor.map(resolve_domain, domains))

    with open(output_file, 'w') as f_out:
        for ip in ips:
            if ip is not None:
                f_out.write(f'{ip}\n')

# Call the function with your input and output file paths
domain_to_ip('input.txt', 'output.txt')
