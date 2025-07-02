def get_num_words(text):
    words = text.split() #separates words by finding whitespaces
    return len(words)


def get_char_counts(text):
    text = text.lower()
    char_counts = {} # a dictionary of chars and counts
    for char in text:
        if char in char_counts:
            char_counts[char] += 1 #updates key of a particular char by 1
        else:
            char_counts[char] = 1 #new char encountered add to dictionary
    return char_counts


def sort_char_counts(char_counts):
    # convert the dictionary of form {"char": x, "num": y} to list of dicts
    sorted_list = [{"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()]
    
    # Now sort by num
    sorted_list.sort(key = lambda item: item["num"], reverse = True)
    return sorted_list