# v0.17 ############################################################
# pip3 install googletrans==4.0.0-rc1
# pip3 install regex
# Create a Python script, let's call it translate.py, with the following content:
import sys
import re
from googletrans import Translator

def translate_line(line, translator, dest_language):
    parts = line.split(' = ', 1)
    if len(parts) == 2:
        translated_part = translator.translate(parts[1], dest=dest_language).text
        return f"{parts[0]} = {translated_part}"
    return line

def translate_file(input_file, output_file, dest_language):
    translator = Translator()

    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    translated_lines = [translate_line(line.strip(), translator, dest_language) for line in lines]

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(translated_lines))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python translate.py input_file output_file dest_language")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    dest_language = sys.argv[3]

    translate_file(input_file, output_file, dest_language)

# Run the Script: $ python3 translate.py input.txt output.txt es


# v0.15 ############################################################
# import argparse
# from googletrans import Translator

# def read_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#     return lines

# def write_file(file_path, lines):
#     with open(file_path, 'w', encoding='utf-8') as file:
#         file.writelines(lines)

# def translate_lines(lines, target_language):
#     translator = Translator()

#     for i, line in enumerate(lines):
#         if " = " in line:
#             key, value = map(str.strip, line.split("" = "", 1))
#             translation = translator.translate(value, dest=target_language).text
#             lines[i] = f"{key} = {translation}\n"

#     return lines

# def main():
#     parser = argparse.ArgumentParser(description='Translate specific lines in a file.')
#     parser.add_argument('input_file', type=str, help='Path to the input file')
#     parser.add_argument('output_file', type=str, help='Path to the output file')
#     parser.add_argument('target_language', type=str, help='Target language for translation (e.g., "es" for Spanish)')

#     args = parser.parse_args()

#     lines = read_file(args.input_file)
#     translated_lines = translate_lines(lines, args.target_language)
#     write_file(args.output_file, translated_lines)

# if __name__ == '__main__':
#     main()

# $ pip install googletrans==4.0.0-rc1
# $ python translate.py input.txt output.txt es
# Replace input.txt with the path to your input file, output.txt with the desired path for the output file, and es with the language code you want to translate to (e.g., "es" for Spanish).


# # v0.10 ############################################################
# from googletrans import Translator

# def translate_file(input_file, output_file, target_language):
#     translator = Translator()

#     with open(input_file, 'r', encoding='utf-8') as f:
#         lines = f.readlines()

#     translated_lines = []

#     for line in lines:
#         if '=' in line:
#             key, value = map(str.strip, line.split('=', 1))
#             translated_value = translator.translate(value, dest=target_language).text
#             translated_lines.append(f'{key} = {translated_value}\n')
#         else:
#             translated_lines.append(line)

#     with open(output_file, 'w', encoding='utf-8') as f:
#         f.writelines(translated_lines)

# if __name__ == "__main__":
#     input_file = input("Enter the path to the input file: ")
#     output_file = input("Enter the path to the output file: ")
#     target_language = input("Enter the target language (e.g., 'fr' for French): ")

#     translate_file(input_file, output_file, target_language)

#     print(f'Translation completed. Check the output file: {output_file}')