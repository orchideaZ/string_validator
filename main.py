import argparse
import difflib
import os
import os
import traceback


def read_txt_file(filename):
    """Reads the content of a txt file."""
    
    with open(filename, 'r', encoding='utf-8-sig') as file:
        return file.read()

def compare_texts(text1, text2):
    # Split the texts into lines
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()

    # Create a Differ object
    d = difflib.Differ()

    # Calculate the differences
    diff = d.compare(lines1, lines2)

    # Print the differences
    for line in diff:
        print(line)


def main():

    parser = argparse.ArgumentParser(description="Compare two texts and find the differences.")
    
    parser.add_argument('file1', type=str, help='Path to the first text file')
    parser.add_argument('file2', type=str, help='Path to the second text file')

    args = parser.parse_args()

    text1 = read_txt_file(args.file1)
    text2 = read_txt_file(args.file2)
    compare_texts(text1, text2)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Construct the full path to PythonError.txt in the same directory as main.py
        error_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "PythonError.txt")
        
        # Write the error message and traceback to PythonError.txt
        with open(error_file_path, "w+") as file:
            file.write(f"Exception occurred: {str(e)}\n")
            file.write(f"Traceback:\n{traceback.format_exc()}")
