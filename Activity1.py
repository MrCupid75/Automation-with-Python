import re
import argparse

#count number of each words in a file and save in another file
def analyse_data(input_file, output_file):
    
    with open(input_file, 'r') as f:
        text = f.read()

    words = re.findall(r'\b\w+\b', text.lower()) #return a list of words
    word_counts = {}    #dict to store words and count value pairs

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    with open(output_file, 'w') as f:
        for word, count in word_counts.items():
            f.write(f"{word} : count {count}\n")

parser = argparse.ArgumentParser(description="Analyse Data from a file")
parser.add_argument('input_file', help='Path to input file')
parser.add_argument('output_file', help='Path to output file')

arguments = ['data.txt', 'result.txt']

args = parser.parse_args(arguments)

analyse_data(args.input_file, args.output_file)