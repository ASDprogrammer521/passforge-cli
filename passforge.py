import secrets
import string
import math
import sys

def generate_password(length=16, use_upper=True, use_digits=True, use_symbols=True):
    alphabet = string.ascii_lowercase
    required = [secrets.choice(string.ascii_lowercase)]

    if use_upper:
        alphabet += string.ascii_uppercase
        required.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        alphabet += string.digits
        required.append(secrets.choice(string.digits))
    if use_symbols:
        symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        alphabet += symbols
        required.append(secrets.choice(symbols))

    if length < len(required):
        length = len(required)

    remaining = [secrets.choice(alphabet) for _ in range(length - len(required))]
    password_list = required + remaining
    secrets.SystemRandom().shuffle(password_list)
    return "".join(password_list)

def format_time(seconds):
    if seconds < 1:
        return "Instant (< 1 second)"
    minutes = seconds / 60
    if minutes < 60:
        return f"{minutes:.1f} minutes"
    hours = minutes / 60
    if hours < 24:
        return f"{hours:.1f} hours"
    days = hours / 24
    if days < 365:
        return f"{days:.1f} days"
    years = days / 365.25
    if years < 1_000_000:
        return f"{years:,.1f} years"
    if years < 1_000_000_000:
        return f"{years / 1_000_000:,.1f} million years"
    return f"{years / 1_000_000_000:,.1f} billion years"

def audit_password(password):
    pool_size = 0
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    if has_lower:
        pool_size += 26
    if has_upper:
        pool_size += 26
    if has_digit:
        pool_size += 10
    if has_symbol:
        pool_size += 32

    if pool_size == 0:
        pool_size = 26

    entropy = len(password) * math.log2(pool_size)
    combinations = pool_size ** len(password)
    guesses_per_sec = 100_000_000_000
    crack_seconds = combinations / guesses_per_sec

    if entropy < 40:
        rating = "CRITICAL (Very Weak)"
    elif entropy < 60:
        rating = "WEAK"
    elif entropy < 80:
        rating = "MODERATE"
    elif entropy < 100:
        rating = "STRONG"
    else:
        rating = "UNBREAKABLE (Cryptographic Grade)"

    print("\n" + "-" * 56)
    print(f"Password Length  : {len(password)} characters")
    print(f"Character Pool   : {pool_size} possible symbols")
    print(f"Shannon Entropy  : {entropy:.2f} bits")
    print(f"Security Rating  : {rating}")
    print(f"Est. Crack Time  : {format_time(crack_seconds)} (at 100B guesses/sec)")
    print("-" * 56)

def menu_generate():
    try:
        raw_len = input("\nEnter password length (default 16): ").strip()
        length = int(raw_len) if raw_len else 16
        if length < 4 or length > 128:
            print("[!] Length adjusted to safe range (8-128).")
            length = max(8, min(128, length))
    except ValueError:
        length = 16

    upper = input("Include uppercase letters? (Y/n): ").strip().lower() != "n"
    digits = input("Include numbers? (Y/n): ").strip().lower() != "n"
    symbols = input("Include special symbols? (Y/n): ").strip().lower() != "n"

    pwd = generate_password(length, upper, digits, symbols)
    print("\n" + "=" * 56)
    print(f"Generated Password: {pwd}")
    print("=" * 56)
    audit_password(pwd)

def menu_audit():
    pwd = input("\nEnter password to audit: ")
    if not pwd:
        print("[!] Error: Password cannot be empty.")
        return
    audit_password(pwd)

def main():
    while True:
        print("\n========================================================")
        print("     PassForge CLI - Cryptographic Password Utility")
        print("========================================================")
        print("1. Generate Cryptographically Secure Password")
        print("2. Audit Existing Password Strength & Entropy")
        print("3. Exit")
        print("--------------------------------------------------------")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            menu_generate()
        elif choice == "2":
            menu_audit()
        elif choice == "3":
            print("Exiting PassForge...")
            break
        else:
            print("[!] Invalid option. Choose 1-3.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Aborted by user.")
        sys.exit()

#by ASDcuber
