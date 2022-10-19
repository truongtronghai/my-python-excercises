def countWordsInFile(fname):
    with open(fname,"r") as fh:
        file_content = fh.read().replace("\n"," ")
        file_words = file_content.split(" ")
        return len(file_words)

# print(countWordsInFile("temp.txt"))