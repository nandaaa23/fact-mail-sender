import keyring


service_names = ["yagmail", "gmail", "smtp"]
username = "your_mail@gmail.com"

for service_name in service_names:
  try:
    keyring.delete_password(service_name, username)
    print(f"Credentials for {username} at {service_name} deleted successfully.")
  except keyring.errors.PasswordDeleteError:
    print(f"Couldn't delete credentials for {username} at {service_name}. Try a different service name.")
    