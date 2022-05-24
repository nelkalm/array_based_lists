# check whether two words (or phrases) are anagrams or not

def is_anagram(word1, word2):
    total_match = 0
    for char in word1:
        if char in word2:
            total_match += 1
    
    if total_match == len(word1):
        return True
    return False


if __name__ == '__main__':
    print(is_anagram('restful', 'fluster'))
