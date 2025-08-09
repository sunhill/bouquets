# Bouquets

A Python application for creating and managing bouquets based on input data.

## Features

- Processes bouquet and flower data to generate bouquet arrangements.
- CLI-based interface for easy interaction.
- Supports unbuffered mode for real-time output.

## Requirements

- Python 3.13 or higher
- pip for dependency management

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bouquets.git
   cd bouquets
   ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To run the bouquet maker application, use the following command:

```bash
python -u src/main.py
```

### Testing
Run the test suite using:
```bash
PYTHONPATH=src pytest
```


## Running in Docker
To build the Docker image for the bouquet maker application, use the following command:

```bash
docker build -t bouquet_maker .
```
To run the application and accept user input, use the following command:
```bash
docker run -it bouquet_maker
```
