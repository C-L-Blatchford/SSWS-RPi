# SSWS-RPi
A Raspberry Pi based data processing and remote monitoring system designed for deployment at the Snowdon Space Weather Station.
The system receives measurements via serial communication, then processes and stores incoming data. Averaged datasets are generated and automatically uploaded to GitHub, where analysis is performed using GitHub Actions.

# Project Overview
This project aims to develop a robust and autonomous pipeline capable of operating remotely with minimal user intervention. The current implementation uses an Arduino simulator to emulate the space weather data logger's behaviour; including structure of measurements and quality of incoming data. Once deployed with final hardware, the same processing and upload pipeline can be used with live measurements.

# Architecture / System Workflow:
Arduino / Data logger

↓

Serial transfer

↓

Raspberry Pi

↓

Data cleaning

↓

Storage

↓

5-minute averaging

↓

Hourly CSV generation

↓

GitHub upload

↓

Automated analysis (GitHub Actions)

↓

Daily summary plot

# Main Components
logger.py is the RPi acquisition software. Responsibilities include:
- Reading serial data.
- Handling missing or malformed measurements. <-- Validates incoming data and handles missing data.
- Storing raw measurements.
- Generating 5-minute averaged values.
- Creating hourly CSV files.
- Automatically uploading files to GitHub.
- Email notifications.
- Recovery from communication interruptions.

first_communication.ino is the Arduino simulator used during development and testing stages. Realistic serial data is simulated to mimic the expected output from the final space weather logger.

analyse.py is the automated analysis script executed by GitHub actions. The script serves as a placeholder and can be extended to include more sophisticated scientific analysis, but currently the analysis:
- Loads uploaded hourly CSV files.
- Combines available datasets.
- Cleans timestamp data.
- Produces battery-voltage summary plots.
- Saves plots to the repository.

analysis.yml is the GitHub Action workflow that runs automatically when new data is pushed, it then executes analyse.py, generates updated summary plots and commits generated plots back the the repository.

# Reliability features
The system has been designed for unattended operations. To allow for this, implemented features include:
- Automatic restart using systemd.
- Automatic recovery after power interruptions.
- Robust serial data handling.
- Retry logic for GitHub uploads.
- Automated file generations and upload.
- Remote monitoring through GitHub.
- Optional email notifications.

# Future Improvements
Possible developments for the future include:
- Integration with the final space weather logger.
- Additional environmental and space weather analyses.
- Enhanced visualisations.
- Interactive web dashboard.
- Long-term statistical analysis tools.
- Automated alert generation.
