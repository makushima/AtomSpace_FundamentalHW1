def convert_size():
    input_str = input("Enter size (e.g., 1K, 2M, 3G): ").strip()
    
    try:
        number = int(input_str[:-1])
        suffix = input_str[-1].upper()
        
        match suffix:
            case 'K':
                bytes_value = number * 1024
            case 'M':
                bytes_value = number * 1024 ** 2
            case 'G':
                bytes_value = number * 1024 ** 3
            case _:
                print("Unknown suffix. Use K, M, or G.")
                return

        print(f"{bytes_value} bytes")
    except ValueError:
        print("Invalid format. Please enter a number followed by a suffix, e.g., 1K.")

convert_size()

