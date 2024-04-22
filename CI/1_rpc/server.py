import Pyro4 
@Pyro4.expose 
class FactorialServer: 
    def factorial(self, n): 
        result = 1 
        for i in range(1, n + 1): 
            result *= i 
        return result 
daemon = Pyro4.Daemon() # Make a Pyro daemon 
ns = Pyro4.locateNS() # Find the name server 
uri = daemon.register(FactorialServer) # Register the server object with a name in the  name server 
ns.register("factorial.server", uri) # Register the object with a name in the name server
print("Factorial server ready.") 
daemon.requestLoop() # Start the event loop of the server to wait for calls 