# Ophthalmology Data Transformation Application

## Overview

This Flask application is designed specifically for ophthalmology practitioners to upload Excel files containing visual acuity data. It transforms fractional values representing visual acuity (like 6/6) into decimal values for easier analysis.

## Features

- **File Upload**: Users can upload Excel files with visual acuity data.
- **Data Transformation**:
  - Converts common fractional values (e.g., 6/6, 6/12) into their decimal equivalents (e.g., 1.0, 0.5).
  - Handles values such as 'HM', 'PL', and others by replacing them with a standardized value (e.g., 6/600).
- **File Download**: Users can download the processed Excel file after transformation.

## Requirements

- Python 3.x
- Flask
- Pandas
- OpenPyXL (for Excel file handling)

Install the required packages using pip:

```bash
pip install Flask pandas openpyxl
```

## File Structure

```
/your_project_directory
│
├── app.py               # Main application file
├── templates/
│   └── index.html       # HTML template for the upload form
└── Converted_data.xlsx   # Output file (created after processing)
```

## Usage

1. **Run the Application**:
   Open your terminal, navigate to the project directory, and run:

   ```bash
   python main.py
   ```

2. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:5000/`.

3. **Upload an Excel File**:
   Use the provided upload form to select and upload your Excel file containing visual acuity data.

4. **Download the Transformed File**:
   After processing, you will be redirected to download the modified Excel file with decimal values.

## Important Notes

- Ensure the uploaded file is in Excel format (.xlsx or .xls).
- The application currently handles specific visual acuity values; ensure your data aligns with these requirements.
- The application runs in debug mode for development; turn off debug mode in a production environment.

## License

This project is open-source and can be modified for individual or institutional use in ophthalmology data analysis!
