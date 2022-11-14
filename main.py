import argparse
from json_tokenizer import JSON_Tokenizer

def main(filename):
    with open(filename, encoding='utf-8') as file:
        file_contents = file.read()
        tokenizer = JSON_Tokenizer(file_contents)
        tokenized = tokenizer.tokenize()
        print(tokenized)

parser = argparse.ArgumentParser(
    prog = 'JSON Parser',
    description = 'This program can parse valid JSON Files'
)
parser.add_argument('-f', '--file', type = str, action = 'store', required = True, dest = 'filename', help = 'Provide the path of the JSON File')
args = parser.parse_args()
main(args.filename)