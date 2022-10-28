def count_words():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    print(len(words))

def count_letters():
    letter_dic = {}
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read().lower()
        for line  in  file_contents:
            for c in line:
                if c in letter_dic:
                    letter_dic[c] += 1
                else:
                    letter_dic[c] = 1
    print(letter_dic)
        
def main():
    count_words()
    count_letters()

main()

