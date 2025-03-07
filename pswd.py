import argparse
import clipboard
from storage import PasswordManagerFile

def main():
    database = PasswordManagerFile()
    parser = argparse.ArgumentParser(description="Password Manager CLI")
    parser.add_argument("-gk", "--gen-key", help="Generate key", action="store_true")
    parser.add_argument("-sk", "--set-key", help="Set key")
    parser.add_argument("-l", "--list", help="List all passwords", action="store_true")
    parser.add_argument("-a", "--add", nargs=3, metavar=("USERNAME", "PASSWORD-LENGTH", "WEBSITE"), help="Add a new registry")
    parser.add_argument("-d", "--delete", type=int, help="Delete a password")
    parser.add_argument("-e", "--edit", nargs=2, metavar=("ID", "NEW-PASSWORD"), help="Change password")
    parser.add_argument('-g', '--get', type=int, help="Get password")
    parser.add_argument('-c', '--clear', action="store_true", help="Clear passwords")
    args = parser.parse_args()
    
    if args.gen_key:
        database._gen_key()
        print("Key generated")
    elif args.set_key:
        database._set_key(args.set_key)
        print("Key set")
    elif args.add:
        database.add(args.add[0], args.add[1], args.add[2])
        database.print()
    elif args.list:
        database.print()
    elif args.delete:
        database.delete(args.delete)
        database.print()
    elif args.edit:
        database.edit(int(args.edit[0]), args.edit[1])
        database.print()
    elif args.get:
        database.get(args.get)
        print(f"Password copied to clipboard")
    elif args.clear:
        clipboard.copy('')
    else:
        print("No command specified")

if __name__ == "__main__":
    main()