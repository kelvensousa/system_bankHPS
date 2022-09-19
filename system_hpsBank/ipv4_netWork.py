import re

class Ipv4NetWorkCalculator():
    def __init__(self, ip='', prefix='', net_mask='', net='', broadcast='', ip_number=''):
        self.ip = ip
        self.prefix = prefix
        self.net_mask = net_mask
        self.net = net
        self.broadcast = broadcast
        self.ip_number = ip_number

        if self.ip == '':
            raise ValueError('Not send IP.')

        if ip_has_prefix():
            pass


#
    def ip_has_prefix(self):
        #192.168.20.65/24
        ip_prefix_regexp = re.compile('^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/[0-9]{1,2}$')

        if not ip_prefix_regexp.search(self.ip):
            return

        division_ip = self.ip.split('/'):
        self.ip = division_ip[0]
        self.prefix = division_ip[1]

    def is_ip(self):
        ip_regexp = re.compile('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}')

        if ip_regexp.search(self.ip):
            return True



if __name__=='__main__':
    ipv4 = Ipv4NetWorkCalculator('')

