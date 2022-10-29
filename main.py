import glob
import fnmatch

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_letters(file_contents):
    letter_dic = {}
    contents_lowered = file_contents.lower()
    for line  in  contents_lowered:
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
    path = './texts/*.*'
    for filename in glob.glob(path):
        if (fnmatch.fnmatch(filename, '*.txt') or fnmatch.fnmatch(filename, '*.docx') or fnmatch.fnmatch(filename, '*.odt') or 
            fnmatch.fnmatch(filename, '*.pdf') or fnmatch.fnmatch(filename, '*.md') or fnmatch.fnmatch(filename, '*.rtf') or
            fnmatch.fnmatch(filename, '*mdx') or fnmatch.fnmatch(filename, '*.html')):
            with open(filename, 'r') as f:
                file_contents = f.read()
            total_words = count_words(file_contents)
            print_name = filename[8:]
            print(f'--- Begin report of {print_name} ---\n{total_words} words found in the document\n')
            total_letters = sort_chars(count_letters(file_contents))
            print_letter_count(total_letters)
            print(f'--- End report of {print_name} ---\n')

main()

