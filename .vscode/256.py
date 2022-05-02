def is_palindrome(word):
    print(word)
    if len(word)<2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])


word=input('입력하세요: ')
print(is_palindrome(word))