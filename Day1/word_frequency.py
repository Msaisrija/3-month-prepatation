# def word_frequency(text):
#     words = text.split(" ")
#     freq ={}

#     for word in words:
#         if word in freq :
#             freq[word] = freq[word]+1
#         else :
#             freq[word] = 1

#     return freq


# print(word_frequency("apple banana apple orange banana apple"))



def word_frequency(text):
    words = text.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq
print(word_frequency("apple banana apple orange banana apple"))