import glob
path = "./books/*.txt"

def count_words():
    for filename in glob.glob(path):
        with open(filename, 'r') as f:
            file_contents = f.read()
    words = file_contents.split()
    return len(words)

def count_letters():
    letter_dic = {}
    for filename in glob.glob(path):
        with open("./books/frankenstein.txt") as f:
            file_contents = f.read().lower()
        for line  in  file_contents:
            for c in line:
                if c in letter_dic:
                    letter_dic[c] += 1
                else:
                    letter_dic[c] = 1
    return letter_dic

def sort_chars(char_dic):
    sort_dic = []
    temp_dic = [(k,v) for k,v in char_dic.items()]
    sort_dic = sorted(temp_dic, key=lambda tup:tup[1], reverse=True)
    return sort_dic

def print_letter_count(total_letters):
    for i, t  in enumerate(total_letters):
        if t[0].isalpha():
            print(f"The '{t[0]}' character was found {t[1]} times")

def main():
    total_words = count_words()
    print(f'--- Begin report of books/text ---\n{total_words} words found in the document\n')
    total_letters = sort_chars(count_letters())
    print_letter_count(total_letters)
    print("--- End report ---")

main()

