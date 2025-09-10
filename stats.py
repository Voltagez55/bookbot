def get_num_words(text):
    words = text.split()
    count = len(words)
    return count
from stats import get_num_words
def get_chars_dict(text):
    counts = {} 
    for character_count in text:
        lowered_char = character_count.lower()
        if lowered_char in counts:
           counts[lowered_char] += 1
        else:
            counts[lowered_char] = 1
    return counts
 
def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
