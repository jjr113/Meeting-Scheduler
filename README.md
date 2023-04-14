# Meeting-Scheduler
This repository contains the code for a one-on-one scheduler for MDS-Rely Research Center. Here are the installation instructions to run the code on your local machine:

## Prerequisites
* Python 3.x installed on your system <br>
* pip (Python package manager) installed on your system <br>
* NOTE: If the spreadsheet being used does not follow these specific rules then this algorithm will NOT work. The spreadsheet column "Who would you like to meet with? (Check up to 5)" needs to either contain the EXACT name from "What is your name?" or "What is your affiliation?" columns. If there is more than one desired person to meet with then seperate each entry with ";".
## Installation
1. Download the code by clicking on the green "Code" button at the top of the page and selecting "Download ZIP"
2. Extract the downloaded ZIP file to your desired location
## Setup
1. Open a terminal/command prompt window and navigate to the location where you extracted the ZIP file.
1. Type the following commands in the terminal to install the required dependencies:<br>
```
  pip install pandas
  pip install openyxl
```
## Running the Scheduler
1. To run the scheduler, navigate to the extracted folder in your terminal/command prompt window.
2. Type the following command in the terminal to start the scheduler:
```
  python main.py
```
<br>That's it! You can now use the one-on-one scheduler for MDS-Rely Research Center. If you have any questions or issues, please feel free to contact the developer.
