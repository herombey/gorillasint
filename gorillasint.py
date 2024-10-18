import argparse
import subprocess
import re
import os


def print_ascii_art():
    art = """

        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠉⠛⠳⢤⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⣡⣶⣧⣤⣤⣌⢷⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣞⣫⣾⣿⣿⣿⣿⣿⣿⣞⡇⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⠶⠶⠶⠶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠿⣿⣄⡀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠁⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⣿⣿⣿⣟⢦⣬⡽⠃⠀
       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠀⢠⣾⣿⣿⡿⠛⠋⠀⠉⠉⠙⠻⣿⣿⣦⣿⣿⠿⠿⠛⠋⢙⣷⠀
       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠀⠀⣾⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣶⢀⣠⣭⣽⡆
        ⠀⠀⠀⠀⠀⠀⣠⣶⠶⠷⠿⠾⠶⠶⠶⠶⠶⠶⠿⠛⠁⠀⠀⠀⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⢳⢿⣿⣿⣿⡟⠁⣼⠇⠀
        ⠀⠀⠀⠀⣠⡾⠋⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⠀⣿⣿⣿⣿⣿⣿⣷⣤⣶⣶⣦⣀⠀⠀⢸⡎⣿⣿⣿⣿⣛⡛⣻⠇
        ⠀⠀⠀⣰⠟⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⡀⠀⠀⢿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⡇⢹⣿⣿⡿⠿⠿⠋⠀
        ⠀⠀⢠⡟⣠⣾⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⣷⠈⠁⠀⠀⠀⠀⠀⠀
        ⠀⠀⢸⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡻⣿⣿⣿⣿⣿⣿⣿⣿⠘⣇⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣽⣿⣿⣿⣿⣿⣿⣿⣧⡹⣦⡀⠀⠀⠀⠀⠀
        ⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡋⢸⣿⣿⣿⣿⡛⠓⠉⠉⠈⠻⣦⠀⠀⠀⠀
        ⠀⢰⡟⢻⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠙⣿⣿⣿⣿⣦⡀⠀⠀⠀⢿⡆⠀⠀⠀
        ⢠⡿⠁⠈⣿⣿⣿⣿⣿⣿⡇⢘⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣱⣿⣿⣿⣿⡟⠀⣿⣿⣿⣿⣿⣿⣆⠀⠀⠸⣧⠀⠀⠀
        ⣿⡀⠀⠀⠸⣿⣿⣿⣿⣿⠁⠈⣿⣶⣶⣿⣿⣿⣿⣿⡿⠛⠛⠛⠉⣡⣾⣿⣿⣿⣿⣿⠃⠀⢿⣿⣿⣿⣿⣿⣿⣆⠀⠀⣿⡄⠀⠀
        ⢸⣿⣷⣤⣠⣬⣿⣿⣿⡟⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡿⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⡄⠀⢹⡇⠀⠀
        ⠀⢿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⢘⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣧⠀⢸⣷⠀⠀    
          ⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠀⠀⢻⣿⣿⣿⣿⣿⣿⣷⡄⢸⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣤⣴⡿⠃⠀
        __   ___   __       _ _ _        __  ____ ___ _   _ _____  __    
  __ _ / /  / _ \  \ \ _ __(_) | | __ _ / / / ___|_ _| \ | |_   _| \ \   
 / _` | |  | | | |  | | '__| | | |/ _` | |  \___ \| ||  \| | | |    | |  
| (_| | |  | |_| |  | | |  | | | | (_| | |   ___) | || |\  | | |    | |  
 \__, | |   \___/   | |_|  |_|_|_|\__,_| |  |____/___|_| \_| |_|    | |  
 |___/ \_\         /_/                  \_\                        /_/

by 0xHarambehacks
    """
    print(art)

print_ascii_art()

def run_dehashed(domain, base_output_file):
    """Run dehashed.py with the provided domain and return the cracked and hash output files."""
    command = f"python3 /mnt/c/Tools/dehashed.py -d {domain} -o {base_output_file}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode != 0:
        print(f"Error running dehashed.py: {result.stderr.decode('utf-8')}")
    
    cracked_file = f"{base_output_file}_cracked.txt"
    hashes_file = f"{base_output_file}_hashes.txt"
    if not os.path.exists(cracked_file):
        raise FileNotFoundError(f"Dehashed cracked file '{cracked_file}' was not created. Check if dehashed.py ran correctly.")
    
    if not os.path.exists(hashes_file):
        raise FileNotFoundError(f"Dehashed hash file '{hashes_file}' was not created. Check if dehashed.py ran correctly.")

    return cracked_file, hashes_file

def run_crosslinked(format_str, company_name, output_file):
    """Run crosslinked with the provided format and company name."""
    output_file_with_ext = output_file + ".txt"

    command = f'crosslinked -f "{format_str}" "{company_name}" -o {output_file}'
    subprocess.run(command, shell=True)

    if not os.path.exists(output_file_with_ext):
        raise FileNotFoundError(f"Crosslinked output file '{output_file_with_ext}' was not created. Check if crosslinked ran correctly.")
    
    return output_file_with_ext

def extract_emails_from_file(file_path):
    """Extracts all emails from the given file."""
    emails = set()  
    with open(file_path, 'r') as f:
        for line in f:
            emails_in_line = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', line)
            emails.update(emails_in_line)
    return emails

def extract_usernames(emails):
    """Extract usernames by removing domain part from email."""
    usernames = set()
    for email in emails:
        username = email.split('@')[0]  
        usernames.add(username)
    return usernames

def extract_passwords_and_hashes(cracked_file, hashes_file):
    """Extracts passwords from the cracked file and only raw hashes from the hashes file."""
    passwords = set()
    hashes = set()

    with open(cracked_file, 'r') as f:
        for line in f:
            passwords.add(line.strip())  

    with open(hashes_file, 'r') as f:
        for line in f:
            parts = re.split(r'[\s,:]', line.strip())
            raw_hash = max(parts, key=len)
            hashes.add(raw_hash)

    return passwords, hashes

def save_to_file(data, file_path):
    """Save data to a file, one item per line."""
    with open(file_path, 'w') as f:
        for item in sorted(data):  
            f.write(f"{item}\n")

def main():
    parser = argparse.ArgumentParser(description="Combine OSINT tool outputs into a single file.")
    
    parser.add_argument('-phonebook', required=True, help="Input file from phonebook.cz")
    parser.add_argument('-crosslinked', nargs=3, help="Arguments for crosslinked: format_str, company_name, output_file")
    parser.add_argument('-dehashed', help="Domain for running dehashed.py")

    args = parser.parse_args()

    all_emails = set()
    all_usernames = set()
    all_passwords = set()
    all_hashes = set()

    phonebook_emails = extract_emails_from_file(args.phonebook)
    all_emails.update(phonebook_emails)

    if args.crosslinked:
        format_str, company_name, crosslinked_output = args.crosslinked
        crosslinked_file = run_crosslinked(format_str, company_name, crosslinked_output)
        crosslinked_emails = extract_emails_from_file(crosslinked_file)
        all_emails.update(crosslinked_emails)

    if args.dehashed:
        cracked_file, hashes_file = run_dehashed(args.dehashed, "dehashed_output")
        dehashed_emails = extract_emails_from_file(cracked_file)  # Assuming emails may be in the cracked file
        all_emails.update(dehashed_emails)

        passwords, hashes = extract_passwords_and_hashes(cracked_file, hashes_file)
        all_passwords.update(passwords)
        all_hashes.update(hashes)

    all_usernames = extract_usernames(all_emails)

    save_to_file(all_emails, "emails.txt")
    save_to_file(all_usernames, "usernames.txt")
    save_to_file(all_passwords, "passwords.txt")
    save_to_file(all_hashes, "hashes.txt")

    print("OSINT data processing completed. Files saved: emails.txt, usernames.txt, passwords.txt, hashes.txt")

if __name__ == "__main__":
    main()
