def csv_to_dict(file_name: str) -> dict:
    """Reads a csv file which has Japanese kanji vocabulary in it, and returns
    a Kanji dictionary with Kanji vocabulary being the key, the tuple pair of
    its pronunciation list and English meaning being the value.
    
    Args:
      file_name: the name of the file where all the Japanese vocabulary is
        written.
    Returns:
      kanji_dict: a dictionary of the Japanese Kanji vocabulary.
    """
    kanji_dict = dict()
    csv_file = open(file_name)
    for line in csv_file:
        line_list = line.split()
        pron_end = 1
        for text in line_list[2:]:
            pron_end += 1
            if text == ';':
                break
        pron_list = line_list[2:pron_end]
        mean = " ".join(line_list[pron_end + 1:])
        kanji_dict[line_list[0]] = (pron_list, mean)
    return kanji_dict

def dict_to_csv(kanji_dict: dict, file_name: str) -> str:
    """Takes a kanji dictionary variable, writes everything in the dictionary
    into a file, and returns the string name of the file.

    Args:
      kanji_dict: the kanji dictionary variable.
      file_name: the name of the file on which the dictionary is being written.
    Returns:
      file_name: the name of the file on which the dictionary is being written.
    """
    csv_file = open(file_name, 'w')
    for word in kanji_dict:
        line = word + ' : ' + ' '.join(kanji_dict[word][0]) + ' ; ' + kanji_dict[word][1] + '\n'
        csv_file.write(line)
    return file_name
