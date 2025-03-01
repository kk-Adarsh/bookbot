from stats import get_file_content
from stats import get_alpha_count_dict
from sys import argv
from sys import exit

if len(argv) != 2:
    print('Usage: python3 main.py <path_to_book>') 
    exit(1)
file_path = argv[1]
def main():
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}')
    print('----------- Word Count ----------')
    length_of_words = len(get_file_content(file_path).split())
    print(f'Found {length_of_words} total words')
    print('--------- Character Count -------')
    alpha_dict = get_alpha_count_dict(get_file_content(file_path))
    for item in alpha_dict:
        name = item['name']
        count = item['count']
        print(f'{name}: {count}')
    print('============= END ===============')

main()
