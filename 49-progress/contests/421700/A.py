'''
Sometimes some words like "localization" or "internationalization" are so long that writing them many times in one text is quite tiresome.

Let's consider a word too long, if its length is strictly more than 10 characters. All too long words should be replaced with a special abbreviation.

This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.

Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".

You are suggested to automatize the process of changing the words with abbreviations. At that all too long words should be replaced by the abbreviation and the words that are not too long should not undergo any changes.

Input
The first line contains an integer 𝑛 (1≤𝑛≤100). Each of the following 𝑛 lines contains one word. All the words consist of lowercase Latin letters and possess the lengths of from 1 to 100 characters.

Output
Print 𝑛 lines. The 𝑖-th line should contain the result of replacing of the 𝑖-th word from the input data.

input
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis

output
word
l10n
i18n
p43s

'''

def main():
    n = int(input())
    for _ in range(n):
        word = input()
        if len(word) > 10:
            print(word[0] + str(len(word) - 2) + word[-1])
        else:
            print(word)

if __name__ == '__main__':
    main()

