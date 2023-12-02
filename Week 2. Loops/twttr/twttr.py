def main():
    word = input("Input: ")
    print("Output: ", end ="")
    print(shorten(word))

def shorten(word):
    no_vowel_word = ""
    for c in word:
        if c not in ["A", "E", "I", "O", "U",
                "a", "e", "i", "o", "u"]:
            no_vowel_word += c

    return no_vowel_word

if __name__ == "__main__":
    main()