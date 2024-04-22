import Pyro4 
uri = "PYRONAME:factorial.server" # Get the URI of the server object from the name  server 
factorial_server = Pyro4.Proxy(uri) 
number = int(input("Enter the number to calculate factorial: ")) 
result = factorial_server.factorial(number) 
print(f"The factorial  of {number} is {result}")
