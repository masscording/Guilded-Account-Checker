# Guilded Account Checker

This script is an educational tool used to check a list of email-password combinations for valid Guilded accounts. It utilizes threading and HTTP requests to efficiently check multiple accounts simultaneously.

## Requirements

Before running the script, make sure you have the following requirements met:

- Python 3+ installed
- Required Python packages: `httpx`, `colorama`. You can install these packages using `pip` by running the following command:

pip install httpx colorama


## Usage

1. **Preparing input files**

 The script requires two input files: `combo.txt` and `proxies.txt`.

 - `combo.txt`: This file should contain a list of email-password combinations in the following format:

   ```
   email1@example.com:password123
   email2@example.com:anotherpassword
   ```

 - `proxies.txt`: This file should contain a list of HTTP proxies, one per line, in the following format:

   ```
   username:password@ip:port
   username:password@ip:port
   ```

2. **Running the script**

 To run the script, open a terminal or command prompt and navigate to the directory containing the script. Then, execute the following command:


The script will start checking the accounts using the provided proxies. It will output the results in real-time, showing the status of each login attempt (HIT, BAD, or TIMEOUT) and the number of each type of result.

If the `combo.txt` or `proxies.txt` file is not found or empty, the script will create an empty file with the same name and display an error message.

## Note

- This script is for educational purposes only. Using it for any malicious or illegal activities is strictly prohibited.
- Be sure to use the script responsibly and only on accounts that you own or have explicit permission to check.

## Disclaimer

The author of this script is not responsible for any misuse, damage, or legal consequences resulting from the use of this tool. Use it at your own risk.

