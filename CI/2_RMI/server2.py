import Pyro4

@Pyro4.expose
class StringConcatenator(object):
    def concatenate_strings(self, str1, str2):
        return str1 + str2

def main():
    daemon = Pyro4.Daemon()
    uri = daemon.register(StringConcatenator)
    
    print("Server URI:", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    main()
