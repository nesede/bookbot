def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    #print(f"{num_words} words found in the document")
    num_chars = get_num_chars(text)
    #print(num_chars)
    print_num_chars_sorted(book_path,text)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_chars(text):
    dict = {}
    lowered_string = text.lower()
    for char in lowered_string:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def print_num_chars_sorted(book_path,book_text):
    print(f"--- Begin report of {book_path} ---")
    print(f"{get_num_words(book_text)} words found in the document")
    book_dict_as_list = []
    dict = get_num_chars(book_text)
    #print(dict)
    for char,count in dict.items():
        if char.isalpha():
            book_dict_as_list.append({"name": char, "num": count})
    
    def sort_on(dict):
        return dict["num"]
    
    book_dict_as_list.sort(reverse=True, key=sort_on)
    #print(book_dict_as_list)
    for item in book_dict_as_list:
        print(f"The '{item['name']}' character was found {item['num']} times")
    print(f"--- End report ---")
main()