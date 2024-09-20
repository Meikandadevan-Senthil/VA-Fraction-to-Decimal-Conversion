from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded.', 400

    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file.', 400

    # Process the Excel file
    df = pd.read_excel(file)

    # Data transformation
    df = transform_data(df)

    # Save the modified DataFrame to a new Excel file
    output_file = 'Converted_data.xlsx'
    df.to_excel(output_file, index=False)

    # Redirect to download the file
    return redirect(url_for('download_file', filename=output_file))

def transform_data(df):
    # Replace specific values
    df.replace({'HM': '6/600', 'HM+': '6/600', 'PL': '6/600', 
                 'PL+': '6/600', 'NPL': '6/600', 'CF': '6/600'}, inplace=True)

    # Function to convert 'a/b' to decimal
    def convert_fraction(value):
        if isinstance(value, str):
            value = value.replace('P', '')  # Remove 'P'
            if '/' in value:
                try:
                    numerator, denominator = map(float, value.split('/'))
                    return numerator / denominator  # Perform the division
                except ValueError:
                    return value  # Return original if conversion fails
        return value  # Return original if not a string

    # Apply the conversion function to each element in the DataFrame
    df = df.applymap(convert_fraction)

    return df

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(os.getcwd(), filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
