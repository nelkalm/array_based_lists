# check whether two words (or phrases) are anagrams or not

def is_anagram(word1, word2):
    total_match = 0
    for char in word1:
        if char in word2:
            total_match += 1

    if total_match == len(word1):
        return True
    return False


def is_anagram_efficient(word1, word2):
    # check if the length are equal. If not, they are not anagrams
    if len(word1) != len(word2):
        return False

    # bottleneck, O(NlogN)
    # sort the characters
    word1 = sorted(word1)
    word2 = sorted(word2)

    # compare characters for each index, O(N)
    for index in range(len(word1)):
        if word1[index] != word2[index]:
            return False

    return True


if __name__ == '__main__':
    print(is_anagram('restful', 'fluster'))
    print(is_anagram_efficient('restful', 'fluster'))
