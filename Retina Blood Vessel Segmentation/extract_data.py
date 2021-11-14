from zipfile import ZipFile

def extract_data():
    """
    This function extracts the data from DRIVES.zip to DRIVES folder in the desired format
    """
    with ZipFile('DRIVE.zip', 'r') as zip_file:
        zip_file.extractall('./')