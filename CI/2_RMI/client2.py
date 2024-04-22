import Pyro4

def main():
    uri = input("Enter the URI of the server: ")
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    concat_server = Pyro4.Proxy(uri)
    concatenated_str = concat_server.concatenate_strings(str1, str2)
    
    print("Concatenated String:", concatenated_str)

if __name__ == "__main__":
    main()
