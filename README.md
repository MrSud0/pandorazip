# PandoraZip

PandoraZip is a Python-based command-line interface (CLI) tool designed for secure file handling. It allows users to zip and unzip files iteratively using a list of passwords, each step modifying the file extension to add layers of security similar to the mythical Pandora's box.

## Features

- **Multiple Zipping**: Iteratively zip a file with each password provided in a list, each time removing the previous extension and adding a new layer of protection.
- **Iterative Unzipping**: Unzip files that have been zipped multiple times with different passwords, attempting each password in sequence.
- **CLI Based**: Simple and straightforward command-line usage.

## Installation

To use PandoraZip, you will need Python installed on your system. You can download Python from [Python's official website](https://www.python.org/downloads/). Once Python is installed, clone this repository to your local machine.

```bash
git clone https://github.com/MrSud0/pandorazip.git
cd pandorazip
```

PandoraZip requires no external libraries beyond the Python standard library, making it easy to set up and use.

## Usage

### Zipping Files

To zip a file, you need to provide the path to the file and the path to a text file containing your list of passwords (one password per line). Use the following command:

```bash
python pandorazip.py zip <path_to_file> <path_to_password_list>
```

### Unzipping Files

To unzip a file, provide the path to the initial zipped file (after multiple zippings) and the path to the same password list used for zipping. Use the following command:

```bash
python pandorazip.py unzip <path_to_file> <path_to_password_list>
```

### Example

```bash
# Zipping
python pandorazip.py zip example.txt passwords.txt

# Unzipping
python pandorazip.py unzip example5.zip passwords.txt
```

## Contributing

Contributions to PandoraZip are welcome! Feel free to fork the repository, make changes, and submit pull requests. If you find bugs or have suggestions, please open an issue in the repository.

## License

PandoraZip is open source and free to use under the MIT License. See the LICENSE file for more details.

## Disclaimer

PandoraZip is provided "as is", without warranty of any kind. Use of this tool is at your own risk. The author is not responsible for any damages that might occur.

---

Enjoy using PandoraZip for your file security needs! For more information and updates, stay tuned to this repository.
```
