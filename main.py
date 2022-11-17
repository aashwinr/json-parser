import argparse
from json_tokenizer import JSONTokenizer
from json_types import *
from json_parser import JSONParser

def main(filename):
    with open(filename, encoding='utf-8') as file:
        file_contents = file.read()
        tokenizer = JSONTokenizer(file_contents)
        tokenized = tokenizer.tokenize()
        parser = JSONParser(tokenized)
        parsed = parser.parse()
        print('Tokenized output:', tokenized)
        print('Parsed output:', parsed)


parser = argparse.ArgumentParser(
    prog = 'JSON Parser',
    description = 'This program can parse valid JSON Files'
)
parser.add_argument('-f', '--file', type = str, action = 'store', required = True, dest = 'filename', help = 'Provide the path of the JSON File')
args = parser.parse_args()
main(args.filename)