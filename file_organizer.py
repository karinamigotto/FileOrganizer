import os
import shutil
import json
import logging
import smtplib
from email.mime.text import MIMEText

# Configure logging
logging.basicConfig(filename='file_organizer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def organize_files(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        logging.error(f"Source folder '{source_folder}' does not exist.")
        return
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    ext_folder_map = {
        '.txt': 'Text_Files',
        '.jpg': 'Images',
        '.png': 'Images',
        '.pdf': 'Documents'
        # Add more extensions and folder names as needed
    }

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1]
            folder_name = ext_folder_map.get(ext, 'Others')
            folder_path = os.path.join(destination_folder, folder_name)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            shutil.move(file_path, os.path.join(folder_path, filename))
            logging.info(f"Moved: {filename} to {folder_name}")

def send_notification(subject, body):
    config = load_config()
    email_config = config['email']

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_config['sender_email']
    msg['To'] = email_config['receiver_email']

    with smtplib.SMTP(email_config['smtp_server'], email_config['port']) as server:
        server.starttls()
        server.login(email_config['sender_email'], email_config['password'])
        server.send_message(msg)

if __name__ == "__main__":
    config = load_config()
    source_folder = config['source_folder']
    destination_folder = config['destination_folder']

    try:
        organize_files(source_folder, destination_folder)
        send_notification("File Organization Complete", "The file organization task has been completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        send_notification("File Organization Error", f"An error occurred: {e}")
