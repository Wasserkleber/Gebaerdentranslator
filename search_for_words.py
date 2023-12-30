import itertools

file_path = 'C:\\Gebaerdenstuff\\output.txt'  # Pfad zur Datei anpassen

def search_for_words_with_underscores(words):
    def read_words_from_file(file_path):
        """Read words from a file and return them as a set."""
        words_set = set()
        with open(file_path, 'r') as file:
            for line in file:
                words_set.add(line.strip().lower())
        return words_set

    def find_and_replace_match(file_words, words):
        """Find a match and replace the matched words in the list with the concatenation."""
        for n in range(2, len(words) + 1):
            for perm in itertools.permutations(words, n):
                concatenated = "_".join(perm) + ".mp4"
                #print(f"Checking: {concatenated}") #print the words beeing checked
                if concatenated.lower() in file_words:
                    new_words = [word if word not in perm else "_".join(perm) for word in words]
                    seen = set()
                    new_words = [x for x in new_words if not (x in seen or seen.add(x))]
                    return True, new_words
        return False, words

    def check_permutations_in_file(file_path, words):
        """Check permutations of words in the file and replace found words."""
        file_words = read_words_from_file(file_path)
        updated_words = words.copy()

        while True:
            match_found, updated_words = find_and_replace_match(file_words, updated_words)
            if not match_found:
                break

        return updated_words

    return check_permutations_in_file(file_path, words)


#testwords = ["katze", "tafel", "abschreiben", "zu", "und", "ab", "bombe", "von", "der", ]

#print(search_for_words_with_underscores(testwords))