![GhostSendr](GhostSendr.jpg) 

# GhostSendr

**GhostSendr** is a lightweight Python-based SMTP mailer tool designed for both manual and mass email sending. It supports HTML content, SSL SMTP connections, multithreading, and is configured via external JSON and TXT files for maximum flexibility.

---

## Features

- Manual mode (send to specific emails)
- Mass mode (send to list from `mailist.txt`)
- SMTP over SSL (Port 465)
- HTML email support (`content.html`)
- Multithreaded sending for high performance
- Banner styling with `pyfiglet`

---

## Installation

```bash
git clone https://github.com/karranwang/GhostSendr.git
```

```bash
cd VoidMailer
```

```bash
pip install -r requirements.txt
```

```bash
python main.py
```

---

## Configuration

[X] Edit config.json:

{
  "smtp_host": "your.smtp.host",
  "smtp_port": 465,
  "smtp_user": "your@email.com",
  "smtp_pass": "yourpassword",
  "from_name": "Your Name or Team",
  "subject": "Your Email Subject"
}

[X] Edit content.html

---

## Warning

This tools is for Educational and Authorized testing purpose only. Misuse may vilate laws or terms of service.

---

## Licence

MIT Licence
