import random
import smtplib

# Step 1: Generate a 6-digit random number
otp = random.randint(100000, 999999)

# Step 2: Store the number in a variable
otp_code = str(otp)


# Step 3: Send an email with the OTP
def send_otp_email(user_email, otp):
    # SMTP server configuration

    sender_email = "khushisarathe17@gmail.com"  # Update with your email address
    sender_password = "664ty664"  # Update with your email password

    # Email content
    subject = "OTP Verification"
    message = f"Your OTP is: {otp}"

    # Connect to the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, user_email, f"Subject: {subject}\n\n{message}")
    server.quit()


# Step 4: Send the email with OTP to the user
user_email = input("Enter your email address: ")
send_otp_email(user_email, otp_code)
print("OTP has been sent to your email address.")

# Step 5: Request user input for email and OTP verification
user_entered_otp = input("Enter the OTP you received: ")

# Verify the OTP
if user_entered_otp == otp_code:
    print("OTP verification successful!")
else:
    print("OTP verification failed!")
