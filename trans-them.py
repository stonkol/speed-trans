################################# v0.19.5 ################################
import argparse
from googletrans import Translator
import progressbar

def translate_line(line):
    # Check for lines that should not be translated
    if "\\n" in line or "%.f" in line or "%li%%" in line or "%@" in line:
        return line

    # Check if the line contains '='
    if '=' in line:
        # Split the line into parts before and after '='
        parts = line.split("=")

        # Try to translate the part after '='
        try:
            translated_part = translator.translate(parts[1].strip(), dest=destination_language).text
        except Exception as e:
            print(f" Error: {e}") #Error translating
            translated_part = parts[1].strip()  # Use the original part if translation fails

        # Return the original part before '=' and the translated part
        return f"{parts[0].strip()} = {translated_part} //\n"
    else:
        # If '=' is not present, return the original line
        return line

def translate_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    translated_lines = []
    
    # Set up a progress bar
    widgets = [progressbar.Percentage(), ' ', progressbar.Bar(), progressbar.ETA()]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=len(lines), term_width=49)

    for index, line in enumerate(bar(lines)):
        translated_lines.append(translate_line(line))

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(translated_lines)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Translate specific lines in a file using Google Translate.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")
    parser.add_argument("destination_language", help="Destination language for translation")

    args = parser.parse_args()

    # Set up Google Translate
    translator = Translator()

    # Set the destination language
    destination_language = args.destination_language

    # Translate the file and write the output
    translate_file(args.input_file, args.output_file)