
def count_chars(my_string):
    new_string = my_string.lower()
    chars_histogram = {}
    for i in new_string:
        if i in chars_histogram:
            chars_histogram[i] += 1
        else:
            chars_histogram[i] = 1
    return chars_histogram

def sort_on(dict):
    return dict["num"]

def convert_and_sort(my_dict):
    my_list = []
    for i in my_dict:
        my_list.append({"character":i, "num":my_dict[i]})
    my_list.sort(reverse=True, key=sort_on)
    return my_list

filename = "books/frankenstein.txt"
with open(filename) as f:
    file_contents = f.read()
    words = file_contents.split()
    # print(file_contents)
    # print(f"The total count should be {len(words)}")
    char_hist = count_chars(file_contents)
    # print(f"The char histogram looks like this {char_hist}")
    sorted_characters = convert_and_sort(char_hist)
    # print(f"The sorted chars look like this {sorted_characters}")
    allowed_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for j in sorted_characters:
        if j['character'].isalpha():
            # print(f"j = {j}, ")
            print(f"The {j['character']} character was found {j['num']} times")



# test_string = "abcdefghijklmonopABCDEFmMmMmM"
# print(f"The test return {count_chars(test_string)}")
# test_histo = count_chars(test_string)
# sorted = convert_and_sort(test_histo)
# print(f"converted and sorted is {sorted}")