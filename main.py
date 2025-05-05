import smtplib
import json
import threading
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pyfiglet import figlet_format
import os

MAX_THREADS = 5           # Max threads
DELAY_PER_EMAIL = 5      # Delay per seconds

def banner():
    print(figlet_format("GhostSendr"))
    print("   github @karranwang")

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def load_html():
    with open("content.html", "r", encoding="utf-8") as f:
        return f.read()

def send_email(smtp_info, to_email, html_content):
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = smtp_info["subject"]
        msg["From"] = f"{smtp_info['from_name']} <{smtp_info['smtp_user']}>"
        msg["To"] = to_email

        part = MIMEText(html_content, "html")
        msg.attach(part)

        with smtplib.SMTP_SSL(smtp_info["smtp_host"], smtp_info["smtp_port"]) as server:
            server.login(smtp_info["smtp_user"], smtp_info["smtp_pass"])
            server.sendmail(smtp_info["smtp_user"], to_email, msg.as_string())
        print(f"[+] Email sent to {to_email}")
    except Exception as e:
        print(f"[-] Failed to send to {to_email}: {e}")

def thread_limiter(sem, smtp_info, email, html_content):
    with sem:
        send_email(smtp_info, email, html_content)
        time.sleep(DELAY_PER_EMAIL)

def mass_mode(smtp_info, html_content):
    filename = input("Enter mailist filename (e.g. mailist.txt): ").strip()
    if not os.path.exists(filename):
        print(f"File '{filename}' not found!")
        return

    with open(filename, "r") as f:
        emails = [line.strip() for line in f if line.strip()]

    sem = threading.Semaphore(MAX_THREADS)
    threads = []

    for email in emails:
        t = threading.Thread(target=thread_limiter, args=(sem, smtp_info, email, html_content))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def manual_mode(smtp_info, html_content):
    input_emails = input("Enter comma-separated emails: ")
    emails = [e.strip() for e in input_emails.split(",") if e.strip()]
    for email in emails:
        send_email(smtp_info, email, html_content)
        time.sleep(DELAY_PER_EMAIL)

def main():
    banner()
    smtp_info = load_config()
    html_content = load_html()

    print("\n[1] Manual Mode")
    print("[2] Mass Mode")
    choice = input("Choose sending mode: ")

    if choice == "1":
        manual_mode(smtp_info, html_content)
    elif choice == "2":
        mass_mode(smtp_info, html_content)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
