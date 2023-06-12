import pyshorteners

print("Welcome to URL shortener")
long_URL = str(input("Enter the URL you want to shorten : "))
obj_ref = pyshorteners.Shortener()
shorten_URL = obj_ref.tinyurl.short(long_URL)
print("The shortened URL is ", shorten_URL)
