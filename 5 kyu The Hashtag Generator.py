def generate_hashtag(s):
    s = s.split()
    s = [i.capitalize() for i in s]
    s = '#' + ''.join(s)



print(generate_hashtag(''), False, 'Expected an empty string to return False')
print(generate_hashtag('Do We have A Hashtag'), '#', 'Expeted a Hashtag (#) at the beginning.')
print(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
print(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
print(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
print(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
print(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
print(generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
print(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')