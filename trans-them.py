################################# v0.19.4 ################################
# pip3 install googletrans==4.0.0-rc1
# pip3 install tqdm
# Adjust the `ncols`` parameter in the `tqdm` function if you want to change the width of the progress bar.
import argparse
from googletrans import Translator
from tqdm import tqdm

def translate_line(line):
    # Check for lines that should not be translated
    if "\\n" in line or "%.f" in line or "%li%%" in line or "%@" in line:
        return line

    # Check if the line contains '='
    if '=' in line:
        # Split the line into parts before and after '='
        parts = line.split("=")
        
        # Translate the part after '='
        translated_part = translator.translate(parts[1].strip(), dest=destination_language).text
        
        # Return the original part before '=' and the translated part
        return f"{parts[0].strip()} = {translated_part} //\n"
    else:
        # If '=' is not present, return the original line
        return line

def translate_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    translated_lines = []
    
    # Set up tqdm progress bar
    with tqdm(total=len(lines), desc="Translating", unit="lines", ncols=87) as pbar:
        for line in lines:
            translated_lines.append(translate_line(line))
            pbar.update(1)  # Update progress bar

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


################################# v0.19.3 ################################
# pip3 install googletrans==4.0.0-rc1
# pip3 install tqdm
# import argparse
# from googletrans import Translator

# def translate_line(line):
#     # Check for lines that should not be translated
#     if "\\n" in line or "%.f" in line or "%li%%" in line or "%@" in line:
#         return line

#     # Check if the line contains '='
#     if '=' in line:
#         # Split the line into parts before and after '='
#         parts = line.split("=")
        
#         # Translate the part after '='
#         translated_part = translator.translate(parts[1].strip(), dest=destination_language).text
        
#         # Return the original part before '=' and the translated part
#         return f"{parts[0].strip()} = {translated_part} //\n"
#     else:
#         # If '=' is not present, return the original line
#         return line

# def translate_file(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as f:
#         lines = f.readlines()

#     translated_lines = [translate_line(line) for line in lines]

#     with open(output_file, 'w', encoding='utf-8') as f:
#         f.writelines(translated_lines)

# if __name__ == "__main__":
#     # Parse command-line arguments
#     parser = argparse.ArgumentParser(description="Translate specific lines in a file using Google Translate.")
#     parser.add_argument("input_file", help="Path to the input file")
#     parser.add_argument("output_file", help="Path to the output file")
#     parser.add_argument("destination_language", help="Destination language for translation")

#     args = parser.parse_args()

#     # Set up Google Translate
#     translator = Translator()

#     # Set the destination language
#     destination_language = args.destination_language

#     # Translate the file and write the output
#     translate_file(args.input_file, args.output_file)