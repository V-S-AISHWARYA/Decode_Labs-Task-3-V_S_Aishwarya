A lightweight, secure, and customizable command-line utility built in Python to generate cryptographically strong passwords. This tool ensures high entropy by leveraging Python's native secrets module, making the generated passwords highly resistant to brute-force and dictionary attacks.

💥 Features
Cryptographically Secure: Powered by the secrets module rather than the pseudo-random random module.

Customizable Complexity: Fine-tune password length and toggle specific character sets (uppercase, lowercase, digits, and special characters).

Zero Dependencies: Relies entirely on the Python Standard Library—no pip install required.

Clean CLI Interface: Simple and intuitive user experience right from the terminal.

Character Set Aggregation: The script dynamically builds a character pool based on user preferences utilizing Python's string constants (string.ascii_letters, string.digits, etc.).

Secure Selection: It loops for the duration of the specified length, pulling unpredictable characters from the pool using secrets.choice().

Output: The characters are joined and printed to the terminal cleanly, minimizing any local caching or footprint.

Security Best Practices Implemented
Entropy over Randomness: secrets uses the most secure source of randomness provided by your operating system (e.g., /dev/urandom on Unix), making it suitable for managing secrets such as passwords and account tokens.

Default Length: The application defaults to a minimum of 12–14 characters, adhering to modern cybersecurity compliance guidelines.
