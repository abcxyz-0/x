import xmlrpc.client

def main():
    # Connect to the server
    server = xmlrpc.client.ServerProxy('http://localhost:8000')

    # User input for factorial calculation
    number = int(input("Enter a number to calculate its factorial: "))
    result = server.factorial(number)
    print(f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()