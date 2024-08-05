# FileOrganizer
Here's a `README.md` file for your GitHub project:

---

# File Organizer

## Description

This Python project automates the organization of files in a specified source folder by moving them into categorized folders based on their file extensions. The script also sends email notifications upon completion or if an error occurs.

## Features

- Automatically moves files to categorized folders.
- Supports different file types such as `.txt`, `.jpg`, `.png`, and `.pdf`.
- Sends email notifications on task completion or error.
- Configurable through a `config.json` file.

## Prerequisites

- Python 3.x
- Required Python libraries: `os`, `shutil`, `json`, `logging`, `smtplib`, `email`, `pytest`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/file-organizer.git
   cd file-organizer
   ```

2. **Install dependencies:**
   Make sure you have `pytest` installed for running tests. You can install it using pip:
   ```bash
   pip install pytest
   ```

3. **Create a configuration file:**
   Create a file named `config.json` in the root directory of the project with the following structure:
   ```json
   {
     "source_folder": "path_to_source_folder",
     "destination_folder": "path_to_destination_folder",
     "email": {
       "smtp_server": "smtp.example.com",
       "port": 587,
       "sender_email": "your_email@example.com",
       "receiver_email": "receiver_email@example.com",
       "password": "your_password"
     }
   }
   ```

## Usage

1. **Run the script:**
   ```bash
   python file_organizer.py
   ```

2. **Check logs:**
   Logs are saved in `file_organizer.log` in the same directory as the script.

## Testing

To run the tests:

```bash
pytest
```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push your branch to the forked repository.
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Karina Nunes

---

Feel free to modify any details to better fit your project or personal preferences!
