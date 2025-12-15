def http_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _: # default case
            return "Unknown"

if __name__ == "__main__":
    code = int(input("Enter HTTP status code: "))   # Take status code from user
    result = http_status(code)                       # Call the function
    print(f"Status: {result}")                       # Display result