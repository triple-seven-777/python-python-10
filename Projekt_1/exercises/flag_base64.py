# Skorzystaj z biblioteki (modułu) base64 oraz funkcji b64decode aby ją zdekodować.

import base64


encoded_string = "SGV4QXJjYW5he3ByYWt0eWN6bnktcHl0aG9uLW1hai0yMDI1"

def decode_base64(encoded_string):
    """
    Decode a base64 encoded string.
    Args:
        encoded_string (str): The base64 encoded string to decode.
    Returns:
        str: The decoded string.
    """
    try:
        # Decode the base64 string
        decoded_bytes = base64.b64decode(encoded_string)
        # Convert bytes to string
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string
    except Exception as e:
        print(f"Error decoding base64 string: {e}")
        return None
    
def main():
    # Use the predefined encoded string
    decoded_string = decode_base64(encoded_string)
    
    # Print the decoded string
    if decoded_string:
        print(f"Decoded string: {decoded_string}")  
    else:
        print("Failed to decode the string.")

if __name__ == "__main__":
    main()

