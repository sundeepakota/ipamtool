# IP Address Lookup Tool

The IP Address Lookup Tool is a simple web application built using Flask that allows users to search for IP addresses, CIDR notations, and associated information.


## Features

- **Search by CIDR Notation:** Users can enter CIDR notations (e.g., 192.168.1.0/24) to search for specific IP address ranges.
- **Search by Location or Comments:** Users can enter keywords to search for specific locations or comments associated with IP addresses.
- **User-Friendly Interface:** The tool provides a clean and user-friendly interface for easy navigation.

## How to Use

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Flask application using `python run.py`.
4. Open your web browser and navigate to `http://localhost:5000`.
5. Enter your search query in the provided form and click the "Search" button.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy (optional if you decide to switch to a database)
