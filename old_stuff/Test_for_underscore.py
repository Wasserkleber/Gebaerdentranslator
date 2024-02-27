file_path = 'C:\\Gebaerdenstuff\\output.txt' #Path zum Text-File mit den Untersteich Wörtern


class TrieNode: #Klasse mit Funktionen für das Finden von Wörtern mit Unterstrich
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def insert(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True 

def search(root, word): #Sucht die Wörter indem es guckt ob Buchstaben existieren
    node = root
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    return node.is_end_of_word

def build_trie(words): #Baut TrieNode
    root = TrieNode()
    for word in words:
        insert(root, word)
    return root

def is_concatenated(word):
    return '_' in word

def remove_duplicate_concatenations(words): #Sucht nach Unterstrichwörtern die mehrfach existieren und entfernt sie
    seen = set()
    result = []
    for word in words:
        if is_concatenated(word):
            if word not in seen:
                seen.add(word)
                result.append(word)
        else:
            result.append(word)
    return result


def check_filenames_and_replace(trie_root, filenames, words): #Gibt liste richtig geordnet mit Unterstrich Wörtern zurück
    # Erstelle eine Liste von Wörtern, die in den Dateinamen vorkommen
    matched_files = set()
    for filename in filenames:
        parts = filename.replace('.mp4', '').split('_')
        if all(search(trie_root, part) for part in parts):
            matched_files.add(filename.replace('.mp4', ''))

    # Ersetze die entsprechenden Wörter in der words-Liste durch die Dateinamen
    result = []
    for word in words:
        replaced = False
        for file in matched_files:
            if word in file.split('_'):
                result.append(file)
                replaced = True
                break
        if not replaced:
            result.append(word)

    return result

def read_words_from_file(file_path): #Ließt die Unterstrich Wörter aus dem File und gibt sie als set zurück
        words_set = set()
        with open(file_path, 'r') as file:
            for line in file:
                words_set.add(line.strip().lower())
        return words_set

def test(words): #Main Funktion, welche alle Funktionen ausführt
    #words = ["katze", "tafel", "abschreiben", "bombe", "abholen","von", "der", "lol", "essen", "aufbauen", "essem", "dort", "wie", "zu", "und", "ab", "warum", "es ist", "deshalb", "anal", "dich", "jetzt", "ich"] #Testwörter
    trie_root = build_trie(words)
    filenames = read_words_from_file(file_path)
    result = check_filenames_and_replace(trie_root, filenames, words)
    result = remove_duplicate_concatenations(result)
    print(result)
    return(result)
