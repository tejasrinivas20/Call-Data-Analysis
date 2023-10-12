import csv
import xml.etree.ElementTree as ET
import random


def generateRandomNumber(nReqPhnNum):
    """
    Generates a list of random phone numbers with the following format:
    - First two digits are 91
    - Next 3 digits can be between 7 to 9
    - Rest of the 8 digits can be between 0 to 9 but repeating digits should not be more than 4

    Args:
    - nReqPhnNum (int): The number of phone numbers to generate.

    Returns:
    - arr (list): A list of nReqPhnNum random phone numbers.
    """
    arr = []
    for _ in range(nReqPhnNum):
        number = "91"
        number += str(random.randint(7, 9))

        for _ in range(9):
            digit = str(random.randint(0, 9))

            if len(number) >= 4 and digit * 4 in number:
                while digit * 4 in number:
                    digit = str(random.randint(0, 9))
            number += digit

        arr.append(number)

    return arr


def createDict(arr1, arr2):
    """
    Creates a dictionary from two arrays.

    Args:
    arr1 (list): The keys of the dictionary.
    arr2 (list): The values of the dictionary.

    Returns:
    dict: A dictionary with keys from arr1 and values from arr2.
    """
    dict = {}
    for i in range(len(arr1)):
        dict[arr1[i]] = arr2[i]
    return dict


def xml_to_csv(xml_file_path: str, csv_file_path: str) -> None:
    """
    This function converts an XML file containing call data to a CSV file with only following headers:
    Phone_no, Duration, Date_spec, Type, Date&Time, Contact_Name.

    Args:
    xml_file_path (str): The path of the XML file to be converted.
    csv_file_path (str): The path of the CSV file to be created.

    Returns:
    None
    """
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    csv_file = open(csv_file_path, 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(["Phone_no", "Duration", "Date_spec",
                        "Type", "Date&Time", "Contact_Name"])

    for call in root.findall('.//call'):
        phone_no = call.get('number', '')
        duration = call.get('duration', '')
        date_spec = call.get('date', '')
        call_type = call.get('type', '')
        readable_date = call.get('readable_date', '')
        contact_name = call.get('contact_name', '')

        csv_writer.writerow([phone_no, duration, date_spec,
                            call_type, readable_date, contact_name])

    csv_file.close()


def transform_name(name):
    """
    Transforms a full name into a first name and first letter of second name format.

    Args:
        name (str): The full name to transform.

    Returns:
        str: The transformed name in the format of "first_name first letter of second name".
    """
    parts = name.split()
    if len(parts) == 1:
        return name
    else:
        first_name = parts[0]
        last_name_initial = parts[-1][0]
        return f"{first_name} {last_name_initial}"
