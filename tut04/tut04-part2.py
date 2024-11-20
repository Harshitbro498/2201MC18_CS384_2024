from collections import defaultdict, Counter

def categorize_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        sorted_key = ''.join(sorted(word))
        anagram_dict[sorted_key].append(word)
    return anagram_dict

def calculate_character_frequencies(anagram_dict):
    frequency_dict = {}
    for key, group in anagram_dict.items():
        char_count = Counter()
        for word in group:
            char_count.update(word)
        frequency_dict[key] = {char: count * len(group) for char, count in char_count.items()}
    return frequency_dict

def find_highest_frequency_group(frequency_dict, anagram_dict):
    max_frequency = 0
    max_group = None
    for key, char_freq in frequency_dict.items():
        total_frequency = sum(char_freq.values())
        if total_frequency > max_frequency:
            max_frequency = total_frequency
            max_group = key
    return max_group, anagram_dict[max_group], max_frequency

def main():
    words = input("Enter words separated by spaces: ").split()
    words = [word.lower() for word in words]

    anagram_dict = categorize_anagrams(words)
    frequency_dict = calculate_character_frequencies(anagram_dict)
    max_group_key, max_group_words, max_frequency = find_highest_frequency_group(frequency_dict, anagram_dict)

    print("\nStored words in anagram groups:")
    sorted_words = sorted([word for group in anagram_dict.values() for word in group])
    print(sorted_words)

    print("\nAnagram Dictionary:")
    result_dict = {anagram_dict[key][0]: group for key, group in anagram_dict.items()}
    print(result_dict)

    print(f"\nGroup with the highest total character frequency:")
    print(f"Group: {max_group_words}")
    print(f"Character Frequencies: {frequency_dict[max_group_key]}")
    print(f"Total Frequency: {max_frequency}")

if __name__ == "__main__":
    main()
