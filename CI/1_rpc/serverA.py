import xmlrpc.server
import math

class MathServices:
    def factorial(self, n):
        """Function to compute the factorial of a number."""
        return math.factorial(n)

# Set up the server
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")

# Register MathServices instance to handle requests
server.register_instance(MathServices())

# Run the server's main loop
server.serve_forever()