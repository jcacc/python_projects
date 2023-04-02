import chardet

with open('data\itysl.txt', 'rb') as input_file:
    raw_data = input_file.read()
    detected_encoding = chardet.detect(raw_data)['encoding']

with open('data\itysl.txt', 'r', encoding=detected_encoding) as input_file, open('data\itysl_no_CR.txt', 'w') as output_file:
    # process the file

    for line in input_file:
        # Remove any extra carriage returns from the line and write it to the output file
        output_file.write(line.rstrip() + '\n')
