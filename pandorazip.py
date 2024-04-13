import zipfile
import os
import sys

def zip_file(input_file, password_list):
    current_file = input_file
    base_name = os.path.splitext(input_file)[0]
    count = 1

    for password in password_list:
        new_zip_name = f"{base_name}{count}.zip"
        with zipfile.ZipFile(new_zip_name, 'w') as zf:
            zf.setpassword(password.encode('utf-8'))
            zf.write(current_file, arcname=os.path.basename(current_file), compress_type=zipfile.ZIP_DEFLATED)
        
        current_file = base_name + str(count)
        os.rename(new_zip_name, current_file)
        count += 1

    print("Zipping complete. Final file:", current_file)

def unzip_file(input_file, password_list):
    current_file = input_file
    for password in password_list:
        try:
            with zipfile.ZipFile(current_file, 'r') as zf:
                zf.setpassword(password.encode('utf-8'))
                zf.extractall(os.path.dirname(current_file))
            print(f"Successfully unzipped with password: {password}")

            # Prepare the next file name by removing the last digit and extension
            current_file = os.path.splitext(current_file)[0][:-1] + '.zip'
        except RuntimeError:
            print(f"Failed to unzip with password: {password}")
            break
        except FileNotFoundError:
            print(f"No more files to unzip, or next file not found: {current_file}")
            break

def read_password_list(password_file):
    with open(password_file, 'r') as file:
        passwords = [line.strip() for line in file.readlines()]
    return passwords

def main():
    if len(sys.argv) != 4:
        print("Usage: python pandorazip.py <zip|unzip> <path_to_file> <path_to_password_list>")
        sys.exit(1)

    mode = sys.argv[1]
    input_file = sys.argv[2]
    password_file = sys.argv[3]
    passwords = read_password_list(password_file)

    if mode == 'zip':
        zip_file(input_file, passwords)
    elif mode == 'unzip':
        unzip_file(input_file, passwords)
    else:
        print("Invalid mode specified. Use 'zip' or 'unzip'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
