import csv
import ipaddress

class Firewall:
    """ The constructor creates a dictionary from the CSV file.
    The dictionary's key is a tuple of (direction, protocol, number) and value is a tuple of (port, ip_address).
    The number is so that we can have rules with the same direction and protocol.""" 
    def __init__(self, path_to_CSVfile):
        self.allow_traffic = dict()
        i = 0
        # code inspired by https://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file
        with open(path_to_CSVfile, mode='r') as infile:
            reader = csv.reader(infile)
            for rows in reader:
                i+=1
                self.allow_traffic[(rows[0], rows[1], i)] = (rows[2], rows[3])

    def port_checker(self, rule_port, port):
        port = str(port)
        if '-' in rule_port:
            port_range = rule_port.split('-')
            if port_range[0] <= port and port <= port_range[1]: # if port in range
                return True
            else:
                return False
        else:
            if port == rule_port:
                return True
            else:
                return False

    # This function checks if the ip address matches a rule.
    def ip_checker(self, rule_ip, ip_address):
        if '-' in rule_ip:
            ip_range = rule_ip.split('-')
            # code inspired by https://ttl255.com/working-with-ip-addresses-in-python-ipaddress-library-part-2/#compare
            ip = ipaddress.ip_address(ip_address)
            ip_min = ipaddress.ip_address(ip_range[0])
            ip_max = ipaddress.ip_address(ip_range[1])
            if ip_min <= ip and ip <= ip_max:
                return True
            else:
                return False
        else:
            if ip_address == rule_ip:
                return  True
            else:
                return False

    def accept_packet(self, direction, protocol, port, ip):
        try:
            # If direction and protocol is not in the dictionary, return False.
            if not sum([direction and protocol in key for key in self.allow_traffic.keys()]):
                return False
            else:
            # If it is in the dictionary, see if port and ip address match a rule, in which case return True.
                for rule in self.allow_traffic:
                    if self.port_checker(self.allow_traffic[rule][0], port) and self.ip_checker(self.allow_traffic[rule][1], ip):
                        return True
            # Since no rule matches, return False.
            return False
        except Exception as e:
            print('Something went wrong: ' + str(e))
            return False


def main():
    fw = Firewall("rules.csv")
    print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2")) # matches first rule
    print(fw.accept_packet("inbound", "udp", 53, "192.168.2.1")) # matches third rule
    print(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11")) # matches second rule
    print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
    print(fw.accept_packet("inbound", "udp", 24, "52.12.48.92"))


if __name__ == '__main__':
    # code from https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
