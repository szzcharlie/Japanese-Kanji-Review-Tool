from tkinter import *
from unit_test import *
from data_transfer import *
import numpy as np
import pygame
import random

"""Takes an external file that records the learning history, and transforms it
to a dictionary variable in python, so as to use it afterwards.

If the user never used this program before or the file is not found, initiate
an empty dictionary variable.
"""
try:
    kanji_history = csv_to_dict("kanji_dict.csv")
except FileNotFoundError:
    kanji_history = dict()


def add_word_to_file(file_name: str, word: str, pron1: str, pron2: str, pron3: str, pron4: str, pron5: str, pron6: str, meaning: str):
    """Takes a file name, a Japanese word written in Kanji, 6 hiragana
    pronunciations for each character and the english meaning of the word,
    and write all those information of the word on a single line at the end
    of the file.

    Args:
      file_name: the name of the file in which the word is written.
      word: Japanese word written in kanji.
      pron1: the hiragana pronunciation of the 1st character.
      pron2: the hiragana pronunciation of the 2nd character.
      pron3: the hiragana pronunciation of the 3rd character.
      pron4: the hiragana pronunciation of the 4th character.
      pron5: the hiragana pronunciation of the 5th character.
      pron6: the hiragana pronunciation of the 6th character.
      meaning: English meaning for the word.
    Returns: None
    """
    csv_file = open(file_name, 'a')
    pronunciation = pron1 + ' ' + pron2 + ' ' + pron3 + ' ' + pron4 + ' ' + pron5 + ' ' + pron6
    pron_list = pronunciation.split()
    kanji_history[word] = (pron_list, meaning)
    line = word + ' : ' + ' '.join(pron_list) + ' ; ' + meaning + '\n'
    csv_file.write(line)

def change_pron_or_mean(file_name: str, word: str, pron1: str, pron2: str, pron3: str, pron4: str, pron5: str, pron6: str, meaning: str):
    """Takes a file name, a Japanese word written in Kanji, 6 hiragana
    pronunciations for each character and the english meaning of the word,
    and updates all those information for the word in the learning history
    dictionary, and also updates them in the file.

    Args:
      file_name: the name of the file in which the word is written.
      word: Japanese word written in kanji.
      pron1: the hiragana pronunciation of the 1st character.
      pron2: the hiragana pronunciation of the 2nd character.
      pron3: the hiragana pronunciation of the 3rd character.
      pron4: the hiragana pronunciation of the 4th character.
      pron5: the hiragana pronunciation of the 5th character.
      pron6: the hiragana pronunciation of the 6th character.
      meaning: English meaning for the word.
    Returns: None
    """
    pronunciation = pron1 + ' ' + pron2 + ' ' + pron3 + ' ' + pron4 + ' ' + pron5 + ' ' + pron6
    pron_list = pronunciation.split()
    kanji_history[word] = (pron_list, meaning)
    org_file = open(file_name, 'r')
    org_lines = org_file.readlines()
    new_file = open(file_name, 'w')
    for line in org_lines:
        if line[0:len(word)] == word and line[len(word)] == ' ':
            update_line = word + ' : ' + ' '.join(pron_list) + ' ; ' + meaning + '\n'
            new_file.write(update_line)
        else:
            new_file.write(line)

def add_or_change(file_name: str, word: str, pron1: str, pron2: str, pron3: str, pron4: str, pron5: str, pron6: str, meaning: str):
    """Takes a file name, a Japanese word written in Kanji, 6 hiragana
    pronunciations for each character and the english meaning of the word,
    and then, if the word is not in the kanji history dictionary, add the word
    to the dictionary. Else if the word is already in the kanji dictionary,
    raise a user interface to ask the user whether the user wants to update
    the pronunciation or english meaning inforamtion of the word.

    Args:
      file_name: the name of the file in which the word is written.
      word: Japanese word written in kanji.
      pron1: the hiragana pronunciation of the 1st character.
      pron2: the hiragana pronunciation of the 2nd character.
      pron3: the hiragana pronunciation of the 3rd character.
      pron4: the hiragana pronunciation of the 4th character.
      pron5: the hiragana pronunciation of the 5th character.
      pron6: the hiragana pronunciation of the 6th character.
      meaning: English meaning for the word.
    Returns: None
    """
    if word not in kanji_history:
        add_word_to_file(file_name, word, pron1, pron2, pron3, pron4, pron5, pron6, meaning)
    else:
        change = Frame(root)
        change.grid(row=0, column=0, sticky='news')
        Label(change, text = 'The word you are adding already existed in the learning history.').pack()
        Label(change, text = 'Do you want to update it with the pronunciation and meaning you just typed in?').pack()
        Button(change, text = 'Yes, update it.', command = lambda:
               [change_pron_or_mean(file_name, word, pron1, pron2, pron3, pron4, pron5, pron6, meaning), add.tkraise()]).pack()
        Button(change, text = 'No, go back.', command = add.tkraise).pack()
        change.tkraise()

def word_remove(file_name: str, word: str):
    """Takes a file name and a Japanese word written in Kanji, check if the word
    exists in the learning history dictionary. If it is, remove the word from
    the dictionary and also from the external file recording all the learning
    history. If it does not exist, show a message on the user interface saying
    that the word is not found.

    Args:
      file_name: the name of the file in which the word is written.
      word: Japanese word written in kanji.
    Returns: None
    """
    item = kanji_history.pop(word, 'The word is not found.')
    if item == 'The word is not found.':
        remove_message.config(text = item)
    else:
        remove_message.config(text = word + 'has been removed.')
        org_file = open(file_name, 'r')
        org_lines = org_file.readlines()
        new_file = open(file_name, 'w')
        for line in org_lines:
            if line[0:len(word)] != word or line[len(word)] != ' ':
                new_file.write(line)

def look_up(word: str):
    """Takes a Japanese word written in Kanji, looks for its pronunciation and
    english meaning in the dictionary, and then shows them in the user
    interface. If the word is not found in the dictionary, a message will be
    shown on the user interface, telling the user the word is not found.

    Args:
      word: Japanese word written in kanji.
    Returns: a user interface showing the result of the search.
    """
    lookup = Frame(root)
    lookup.grid(row=0, column=0, sticky='news')
    Label(lookup, text = 'Kanji word: Pronunciation for each character; English meaning').pack()
    if word not in kanji_history:
        Label(lookup, text = "Sorry, the word is not found in the learning history.").pack()
    else:
        line = word + ' : ' + ' '.join(kanji_history[word][0]) + ' ; ' + kanji_history[word][1]
        Label(lookup, text = line).pack()
    Button(lookup, text = 'Main Menu', command = welcome.tkraise).pack()
    lookup.tkraise()

def search_pron(char: str, kanji_dict: dict) -> dict:
    """Takes a kanji character and a kanji dictionary, looks for all the words
    that contains this kanji character, and organize them into a new dictionary
    according to the pronunciation of the character, which means that each
    different pronunciation of the character will become the keys of the
    dictionary, following a list of example words as the value.

    Args:
      char: one single kanji character.
      kanji_dict: a kanji vocabulary dictionary.
    Returns:
      pron_dict: a dictionary with different pronunciation of the single kanji
        character as the key, and list of example words with this pronunciation
        as the value.
    """
    pron_dict = dict()
    for key in kanji_dict:
        if char in key:
            pron_index = 0
            for letter in key:
                if letter == char:
                    break
                pron_index += 1
            pron = kanji_dict[key][0][pron_index]
            if pron not in pron_dict:
                pron_list = []
                pron_list.append((key, kanji_dict[key]))
                pron_dict[pron] = pron_list
            else:
                pron_list = pron_dict[pron]
                pron_list.append((key, kanji_dict[key]))
                pron_dict[pron] = pron_list
    return pron_dict

def show_search(char: str, kanji_dict: dict):
    """Takes a kanji character and a kanji dictionary, calls the search_pron
    function to generate a newly organized dictionary, and print out the
    dictionary in the user interface, showing the user all the possible
    pronunciations of a single kanji character they have already learnt,
    along with the example words.

    Args:
      char: one single kanji character.
    Returns: a user interface showing the result of the search.
    """
    search = Frame(root)
    search.grid(row=0, column=0, sticky='news')
    Label(search, text = 'Prounciation').grid(row=0, column=0)
    Label(search, text = 'Examples').grid(row=0, column=1)
    row_num = 1
    
    if len(char) == 1:
        if char in "あいうえお かきくけこ はひふへほ なにぬねの たちつてと さしすせそ まみむめも らりるれろ やゆよ わをん がぎぐげご ざじずぜぞ ばびぶベボ ぱぴぷぺぽ だぢづでど ゃゅょっ":
            Label(search,
                  text = "Please enter kanji character instead of hiragana character.").grid(row=1, column=0, columnspan=2)
            row_num += 1
        else:
            pron_dict = search_pron(char, kanji_dict)
            if pron_dict == {}:
                Label(search, text = "Sorry, nothing is found.").grid(row=1, column=0, columnspan=2)
                row_num += 1
            else:
                for pron in pron_dict:
                    Label(search, text = pron).grid(row=row_num, column=0)
                    for word in pron_dict[pron]:
                        example = word[0] + ' : ' + ' '.join(word[1][0]) + ' ; ' + word[1][1]
                        Label(search, text = example).grid(row=row_num, column=1)
                        row_num += 1
    else:
        Label(search, text = "Please enter only one character.").grid(row=1, column=0, columnspan=2)
        row_num += 1

    Button(search, text = 'Main Menu', command = welcome.tkraise).grid(row=row_num, column=0)
    search.tkraise()

def show_kanji_dict_file(file_name = 'kanji_dict.csv'):
    """Generates an interface which can print all the lines in a well-written
    Japanese vocabulary csv file (or just the learning history file
    'kanji_dict.csv'), along with buttons to return and shift between pages.

    Args:
      file_name: the name of the Japanese kanji vocabulary file.
    Returns: an interface which prints at most 10 words in the file.
    """
    show_all = Frame(root)
    show_all.grid(row=0, column=0, sticky='news')
    try:
        csv_file = open(file_name)
        serial = 1
        all_word = ()
        for line in csv_file:
            edited_word = str(serial) + '. ' + line
            all_word = all_word + (edited_word, )
            serial += 1
        if len(all_word) <= 10:
            Label(show_all, text = 'Kanji word: Pronunciation for each character; English meaning').grid(row=0, column=0)
            row_number = 1
            for edited_word in all_word:
                Label(show_all, text = edited_word).grid(row = row_number, column = 0)
                row_number += 1
            Button(show_all, text = "Main Menu", command = welcome.tkraise).grid(row = row_number, column = 0)
        else:
            Label(show_all, text = 'Kanji word: Pronunciation for each character; English meaning').grid(row=0, columnspan=4)
            row_number = 1
            while row_number <= 10:
                Label(show_all, text = all_word[row_number - 1]).grid(row = row_number, columnspan=4)
                row_number += 1
            total_page = (len(all_word) + 9) // 10
            Button(show_all, text = "Main Menu", command = welcome.tkraise).grid(row = row_number, column = 0)
            Label(show_all, text = '1/' + str(total_page)).grid(row = row_number, column = 2)
            Button(show_all, text = "Next", command = lambda: page_shift(all_word, 2)).grid(row = row_number, column = 3)
    except FileNotFoundError:
        Label(show_all, text = "No record of kanji learning is found.").grid(row=0, column=0)
        Button(show_all, text = "Main Menu", command = welcome.tkraise).grid(row=1, column=0)   
    show_all.tkraise()

def page_shift(all_word: tuple, page: int):
    """Takes a tuple of all the words in the kanji learning history and a
    page number, selects the 10 words that match the page number and prints
    them onto the interface, along with buttons to return to the main menu and
    shift between different pages.

    Args:
      all_word: a tuple of all the edited words that are ready to be printed
                onto the interface.
    Returns: an interface which prints out the words that match the page number.
    """
    new_page = Frame(root)
    new_page.grid(row=0, column=0, sticky='news')
    Label(new_page, text = 'Kanji word: Pronunciation for each character; English meaning').grid(row=0, columnspan=4)
    total_page = (len(all_word) + 9) // 10
    if page == total_page:
        this_page_word = all_word[(page-1)*10:]
        row_number = 1
        for edited_word in this_page_word:
            Label(new_page, text = edited_word).grid(row = row_number, columnspan = 4)
            row_number += 1
        Button(new_page, text = "Main Menu", command = welcome.tkraise).grid(row = row_number, column = 0)
        Button(new_page, text = "Prev", command = lambda: page_shift(all_word, page-1)).grid(row = row_number, column = 1)
        Label(new_page, text = str(page) + '/' + str(total_page)).grid(row = row_number, column = 2)
    else:
        this_page_word = all_word[(page-1)*10 : page*10]
        row_number = 1
        for edited_word in this_page_word:
            Label(new_page, text = edited_word).grid(row = row_number, columnspan = 4)
            row_number += 1
        Button(new_page, text = "Main Menu", command = welcome.tkraise).grid(row = row_number, column = 0)
        Button(new_page, text = "Prev", command = lambda: page_shift(all_word, page-1)).grid(row = row_number, column = 1)
        Label(new_page, text = str(page) + '/' + str(total_page)).grid(row = row_number, column = 2)
        Button(new_page, text = "Next", command = lambda: page_shift(all_word, page+1)).grid(row = row_number, column = 3)

def random_ten_with_prons(start: int, end: int, kanji_dict: dict) -> dict:
    """Randomly select 10 words in the range to generate a new dictionary, with
    the string of pronunciation being the only thing in the value.

    Args:
      start: the starting point of a range
      end: the end point of a range
      kanji_dict: the kanji dictionary
    Returns:
      ten_word: the dictionary of ten words with their pronunciations.
    """
    ten_key_list = random.sample(list(kanji_dict)[start-1:end], 10)
    ten_word = dict()
    for key in ten_key_list:
        ten_word[key] = ''.join(kanji_dict[key][0])
    return ten_word

def random_ten_with_means(start: int, end: int, kanji_dict: dict) -> dict:
    """Randomly select 10 words in the range to generate a new dictionary, with
    the string of english meaning being the only thing in the value.

    Args:
      start: the starting point of a range
      end: the end point of a range
      kanji_dict: the kanji dictionary
    Returns:
      ten_word: the dictionary of ten words with their english meanings.
    """
    ten_key_list = random.sample(list(kanji_dict)[start-1:end], 10)
    ten_word = dict()
    for key in ten_key_list:
        ten_word[key] = kanji_dict[key][1]
    return ten_word

def grade(user_ans_list, correct_ans_list, check_list, score_label):
    """Grade the answers of the quiz from the users, mark the correct one
    with check mark, the wrong one with cross, and then generate a score of
    quiz for the user.

    Args:
      user_ans_list: the list of user entries which has user's answers for quiz.
      correct_ans_list: the list of the solutions of the quiz.
      check_list: the list of the labels of mark symbols on the user interface.
      score_label: the label of the score message.
    Returns: None
    """
    score = 0
    for i in range(0, len(user_ans_list)):
        if user_ans_list[i].get() == correct_ans_list[i]:
            score += 1
            check_list[i].config(text = "✓")
        else:
            check_list[i].config(text = "𐄂")
    score_label.config(text = "Your score: " + str(score) + "/10.")

def generate_quiz(start: str, end: str, kanji_dict: dict, quiz_type: str):
    """Takes two strings of digits which represent the starting point and the
    end point of a range, and a kanji dictionary, which will be used to select
    the words of the quiz, and also a string which decides the type of the
    quiz, generate a user interface with the specific type of quiz for the user
    to complete, along with a 'Submit' button to grade the quiz, and also a
    'Check Solution' button to view the solution of the quiz.

    Args:
      start: a string of digits which represents the starting point of a range.
      end: a string of digits which represents the ending point of a range.
      kanji_dict: the kanji dictionary
      quiz_type: a string which decides the type of the quiz.
    Returns: a user interface which gives the user a quiz of 10 vocabulary.
    """
    quiz = Frame(root)
    quiz.grid(row=0, column=0, sticky='news')
    Label(quiz, text = quiz_type).grid(row=0, columnspan=2)

    sol = Frame(root)
    sol.grid(row=0, column=0, sticky='news')
    Label(sol, text = 'Solution of the Quiz').grid(row=0)
    
    try:
        int_start = int(start)
        int_end = int(end)
        if int_end - int_start < 9 or int_start < 1 or int_start > len(kanji_dict) - 9:
            int_start = 1
            int_end = len(kanji_dict)
    except ValueError:
        int_start = 1
        int_end = len(kanji_dict)

    if quiz_type == 'Pronunciation Quiz':
        word_dict = random_ten_with_prons(int_start, int_end, kanji_dict)
        ques_list = list(word_dict)
        sol_list = list(word_dict.values())
    elif quiz_type == 'Translation Quiz':
        word_dict = random_ten_with_means(int_start, int_end, kanji_dict)
        ques_list = list(word_dict.values())
        sol_list = list(word_dict)

    # Print out the solutions of the quiz on the solution interface
    for i in range(0, 10):
        Label(sol, text = ques_list[i] + ': ' + sol_list[i]).grid(row=i+1)
    Button(sol, text = 'Go back to Quiz', command = quiz.tkraise).grid(row=11)

    # Set up the quiz interface
    ans1 = Entry(quiz, width=12)
    ans2 = Entry(quiz, width=12)
    ans3 = Entry(quiz, width=12)
    ans4 = Entry(quiz, width=12)
    ans5 = Entry(quiz, width=12)
    ans6 = Entry(quiz, width=12)
    ans7 = Entry(quiz, width=12)
    ans8 = Entry(quiz, width=12)
    ans9 = Entry(quiz, width=12)
    ans10 = Entry(quiz, width=12)
    ans_list = [ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10]

    check1 = Label(quiz)
    check2 = Label(quiz)
    check3 = Label(quiz)
    check4 = Label(quiz)
    check5 = Label(quiz)
    check6 = Label(quiz)
    check7 = Label(quiz)
    check8 = Label(quiz)
    check9 = Label(quiz)
    check10 = Label(quiz)
    check_list = [check1, check2, check3, check4, check5, check6, check7, check8, check9, check10]
    
    for i in range(0,10):
        Label(quiz, text = ques_list[i] + ':').grid(row=i+1, column=0)
        ans_list[i].grid(row=i+1, column=1)
        check_list[i].grid(row=i+1, column=2)

    score = Label(quiz)
    score.grid(row=11, column=1)
    Button(quiz, text = 'Submit',
           command = lambda: grade(ans_list, sol_list,
                                   check_list, score)).grid(row=11, column=0)

    Button(quiz, text = 'Check the solution', command = sol.tkraise).grid(row=12, column=1)
    Button(quiz, text = 'Go back', command = ask_range_interface).grid(row=12, column=0)

    quiz.tkraise()

class Card:
    """The class of flip cards which records all the necessary information of a
    card, including the word on the card, the x-coordinate and the y-coordinate
    of the left-top point where the card will be positioned.
    """
    def __init__(self, word, x, y):
        self.flip = False
        self.match = False
        self.word = word
        self.x = x
        self.y = y

def match_game(start: str, end: str):
    """Takes two strings of digits which represent the starting point and the
    end point of a range, use this range to randomly generate 10 words from the
    kanji learning history dictionary, and use the 10 words to generate 10 pairs
    of cards having the original kanji word and its pronunciation, mix the 20
    cards, and start the game of memory matching. In the game, if one card is
    clicked, the word on the card will be displayed. If another card is flipped
    and they are a pair of kanji word and its pronunciation, they are matched
    and these two cards will disappear on the screen. If they are not a pair,
    both the two cards will be flipped back, and score points will be deducted. 

    Args:
      start: a string of digits which represents the starting point of a range.
      end: a string of digits which represents the ending point of a range.
    Returns: the surface of the matching game.
    """
    try:
        int_start = int(start)
        int_end = int(end)
        if int_end - int_start < 9 or int_start < 1 or int_start > len(kanji_history) - 9:
            int_start = 1
            int_end = len(kanji_history)
    except ValueError:
        int_start = 1
        int_end = len(kanji_history)

    pron_dict = random_ten_with_prons(int_start, int_end, kanji_history)
    voc_list = list(pron_dict)
    pron_list = list(pron_dict.values())
    total = voc_list + pron_list
    random.shuffle(total)

    # Store all the cards with their information in a numpy array,
    # with the position matching the position on the game interface.
    all_card = np.empty([4,5], object)
    for r in range(0,4):
        for c in range(0,5):
            card_obj = Card(total[r*5+c], c*200+5, r*200+5)
            all_card[r][c] = card_obj

    pygame.init()
    pygame.display.set_caption('Memory Matching Game')
    screen = pygame.display.set_mode((1000, 840))
    clock = pygame.time.Clock()
    font = pygame.font.Font('f910-shin-comic-2.01.otf', 28)
    smallfont = pygame.font.Font('f910-shin-comic-2.01.otf', 20)
    running = True
    score = 100
    try_pair = 0
    click_num = 0
    click_card = []

    while running:
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if click_num < 2:
                    xclick, yclick = pygame.mouse.get_pos()
                    row_num = int(yclick//200)
                    col_num = int(xclick//200)
                    if -1 < row_num < 4 and -1 < col_num < 5:
                        current_card = all_card[row_num][col_num]
                        if current_card.flip == False and current_card.match == False:
                            current_card.flip = True
                            click_card.append(current_card)
                            click_num += 1
                
        for card_array in all_card:
            for card in card_array:
                if card.match == False and card.flip == False:
                    pygame.draw.rect(screen, 'grey', (card.x, card.y, 190, 190))
                if card.flip == True:
                    pygame.draw.rect(screen, 'pink', (card.x, card.y, 190, 190))
                    text = font.render(card.word, True, 'black')
                    textRect = text.get_rect()
                    textRect.center = (card.x+95, card.y+95)
                    screen.blit(text, textRect)
                        
        if click_num == 2:
            if click_card[0].word in voc_list:
                if pron_dict[click_card[0].word] == click_card[1].word:
                    click_card[0].match = click_card[1].match = True
                else:
                    try_pair += 1
                    if 5 < try_pair <= 10:
                        score -= 2
                    elif try_pair > 10:
                        score -= 3
            elif click_card[1].word in voc_list:
                if pron_dict[click_card[1].word] == click_card[0].word:
                    click_card[0].match = click_card[1].match = True
                else:
                    try_pair += 1
                    if 5 < try_pair <= 10:
                        score -= 2
                    elif try_pair > 10:
                        score -= 3
            else:
                try_pair += 1
                if 5 < try_pair <= 10:
                    score -= 2
                elif try_pair > 10:
                    score -= 3
            click_card[0].flip = click_card[1].flip = False
            click_card = []
            click_num = 0

        scoreLabel = smallfont.render("Flip the cards and try to match pairs of kanji word and its pronunciation! Your score: "+str(score),
                                      True, 'black')
        scoreRect = scoreLabel.get_rect()
        scoreRect.center = (500, 820)
        screen.blit(scoreLabel, scoreRect)

        pygame.display.flip()
        clock.tick(3)

    pygame.quit()


# User Interface Design
# The label and buttons for ask_range interface
def ask_range_interface():
    """Check if there are more than 10 words in the learning history.
    If there are not, pop out a message telling the user to learn more words.
    If there are, pop out an interface asking the range of words they want to
    include for quiz and game and also asking whether they want to do quiz or
    play game."""
    ask_range = Frame(root)
    ask_range.grid(row=0, column=0, sticky='news')
    
    if len(kanji_history) < 10:
        Label(ask_range, text = "Now there are less than 10 words in your learning history.").pack()
        Label(ask_range, text = "Learn more kanji words and then come back to try quiz and game.").pack()
        Button(ask_range, text = 'Main Menu', command = welcome.tkraise).pack()
    else:
        Label(ask_range, text = "There are in total " + str(len(kanji_history)) + " words in the dictionary now.").grid(row=0, columnspan=2)
        Label(ask_range, text = "Please enter a range of what to include in the quiz or game.").grid(row=1, columnspan=2)
        Label(ask_range, text = "10 random words will be selected in this range.").grid(row=2, columnspan=2)
        Label(ask_range, text = "The difference between start and end must be bigger than 8.").grid(row=3, columnspan=2)
        Label(ask_range, text = "If the range is invalid, the system will randomly choose 10 from all words.").grid(row=4, columnspan=2)
        Label(ask_range, text = "You can hit 'Okay' to check the validity of your range if you are unsure.").grid(row=5, columnspan=2)

        Label(ask_range, text = "The start point: (may not be lower than 1)").grid(row=6, column=0)
        range_start = Entry(ask_range, width=8)
        range_start.grid(row=6, column=1)

        Label(ask_range, text = "The end point: (may not be greater than " + str(len(kanji_history)) + ")").grid(row=7)
        range_end = Entry(ask_range, width=8)
        range_end.grid(row=7, column=1)

        range_message = Label(ask_range)
        range_message.grid(row=8, column=0)

        def check_range(start_point: str, end_point: str):
            """Takes two strings of digits that represent the start point and end point
            of a range, checks whether this is a valid range that can be used to
            gnerate quizzes, and show the message of validity on the interface.

            Args:
              start_point: a string of digits that is the start point of a range.
              end_point: a string of digits that is the end point of a range.
            Returns: None
            """
            try:
                start = int(start_point)
                end = int(end_point)
                if start <= 0 or end <= 0:
                    range_message.config(text = "Invalid range: not positive integers.")
                elif end - start < 9:
                    range_message.config(text = "Invalid range: Difference is not big enough.")
                elif start > len(kanji_history) - 9:
                    range_message.config(text = "Invalid range: start point is too big.")
                elif end > len(kanji_history):
                    range_message.config(text = "Invalid range: end point is out of range.")
                else:
                    range_message.config(text = "This is a valid range.")
            except ValueError:
                range_message.config(text = "Invalid range: not integers.")

        Button(ask_range, text = "Okay",
               command = lambda: check_range(range_start.get(),range_end.get())).grid(row=8, column=1)

        Button(ask_range, text = "Start a pronunciation quiz",
               command = lambda: [generate_quiz(range_start.get(), range_end.get(),
                                                kanji_history, 'Pronunciation Quiz'),
                                  range_start.delete(0,'end'), range_end.delete(0,'end'),
                                  range_message.config(text='')]).grid(row=9, columnspan=2)

        Button(ask_range, text = "Start a translation quiz",
               command = lambda: [generate_quiz(range_start.get(), range_end.get(),
                                                kanji_history, 'Translation Quiz'),
                                  range_start.delete(0,'end'), range_end.delete(0,'end'),
                                  range_message.config(text='')]).grid(row=10, columnspan=2)

        Button(ask_range, text = "Play memory matching game",
               command = lambda: [match_game(range_start.get(), range_end.get()),
                                  range_start.delete(0,'end'), range_end.delete(0,'end'),
                                  range_message.config(text='')]).grid(row=11, columnspan=2)

        Button(ask_range, text = "Main Menu", command = welcome.tkraise).grid(row=12, columnspan=2)

    ask_range.tkraise()

# Initiate all the interfaces
root = Tk()
welcome = Frame(root)
add = Frame(root)
remove = Frame(root)

welcome.grid(row=0, column=0, sticky='news')
add.grid(row=0, column=0, sticky='news')
remove.grid(row=0, column=0, sticky='news')

# The label and buttons for welcome interface
Label(welcome, text = "Ready to learn Japanese Kanji?").grid(row=0, columnspan=2)
Button(welcome, text = "Add the kanji you have learnt today.",
       command = add.tkraise).grid(row=1, columnspan=2)
Button(welcome, text = "Remove a kanji word from the dictionary.",
       command = remove.tkraise).grid(row=2, columnspan=2)

Label(welcome, text = "Enter one kanji word:").grid(row=3, column=0)
single_word = Entry(welcome, width=10)
single_word.grid(row=3, column=1)
Button(welcome, text = "Look up the pronunciation and meaning.",
       command = lambda: [look_up(single_word.get()),
                          single_word.delete(0,'end')]).grid(row=4, columnspan=2)
Label(welcome, text = "Enter one kanji character:").grid(row=5, column=0)
single_kan = Entry(welcome, width=10)
single_kan.grid(row=5, column=1)
Button(welcome, text = "Search for all prononciations with examples.",
       command = lambda: [show_search(single_kan.get(), kanji_history),
                          single_kan.delete(0,'end')]).grid(row=6, columnspan=2)

Button(welcome, text = "Quiz and Game", command = ask_range_interface).grid(row=7, columnspan=2)
Button(welcome, text = "Show the entire kanji learning history.",
       command = show_kanji_dict_file).grid(row=8, columnspan=2)
Button(welcome, text = "Finished Learning.",
       command = root.destroy).grid(row=9, columnspan=2)

# The label and buttons for adding vocab interface
Label(add, text = 'Vocabulary written in Kanji:').grid(row=0, column=0, columnspan=2)
kanji = Entry(add, width=38)
kanji.grid(row=0, column=2, columnspan=6)

Label(add, text = 'Hiragana for each character:').grid(row=1, column=0, columnspan=2)
char1 = Entry(add, width=5)
char1.grid(row=1, column=2)
char2 = Entry(add, width=5)
char2.grid(row=1, column=3)
char3 = Entry(add, width=5)
char3.grid(row=1, column=4)
char4 = Entry(add, width=5)
char4.grid(row=1, column=5)
char5 = Entry(add, width=5)
char5.grid(row=1, column=6)
char6 = Entry(add, width=5)
char6.grid(row=1, column=7)

Label(add, text = '1st char').grid(row=2, column=2)
Label(add, text = '2nd char').grid(row=2, column=3)
Label(add, text = '3rd char').grid(row=2, column=4)
Label(add, text = '4th char').grid(row=2, column=5)
Label(add, text = '5th char').grid(row=2, column=6)
Label(add, text = '6th char').grid(row=2, column=7)

Label(add, text = 'English meaning:').grid(row=3, column=0, columnspan=2)
eng = Entry(add, width=38)
eng.grid(row=3, column=2, columnspan=6)

Button(add, text = 'Main Menu', command = welcome.tkraise).grid(row=4, column=0)
Button(add, text = 'Add',
       command = lambda: [add_or_change('kanji_dict.csv', kanji.get(),char1.get(),char2.get(),
                                        char3.get(),char4.get(),char5.get(),char6.get(),eng.get()),
                          kanji.delete(0,'end'),char1.delete(0,'end'),char2.delete(0,'end'),
                          char3.delete(0,'end'),char4.delete(0,'end'),char5.delete(0,'end'),
                          char6.delete(0,'end'),eng.delete(0,'end')]).grid(row=4, column=2)

# The label and buttons for remove interface
Label(remove, text = "Enter the kanji word you want to remove:").grid(row=0, columnspan=2)
remove_word = Entry(remove)
remove_word.grid(row=1, columnspan=2)
remove_message = Label(remove)
remove_message.grid(row=2, columnspan=2)
Button(remove, text = 'Main Menu',
       command = lambda: [remove_message.config(text=''),
                          welcome.tkraise()]).grid(row=3, column=0)
Button(remove, text = 'Remove',
       command = lambda: [word_remove('kanji_dict.csv', remove_word.get()),
                          remove_word.delete(0,'end')]).grid(row=3, column=1)


if __name__ == '__main__':
    # Instructions on testing the interface
    # If you want to run the tests, remove the comment
    """
    print("\nHere are a few instructions of how you can know the program is running well.\n")
    print("If you've never used this program before,")
    print("you can start by pressing the button 'Add the kanji you have learnt today'")
    print("to add your onw kanji learning vocabulary.\n")
    print("If you directly press the button 'Show the entire kanji learning history'")
    print("without adding any vocabulary, you will see a user interface telling you that:")
    print("'No record of kanji learning is found'.\n")
    print("But if you have added vocabulary before,")
    print("even if you haven't added after you opened the program,")
    print("as long as you have used the program and added before,")
    print("when you press the button 'Show the entire kanji learning history',")
    print("you will see the complete learning history of kanji vocabulary in the interface,")
    print("in the format 'kanji : pronunciation ; meaning'.\n")
    print("An example 'kanji_dict.csv' file is included in the github for you to use,")
    print("but you can also create your own with the adding word feature.\n")
    print("If you type one kanji vocabulary you have already learned in the")
    print("first text bar and hit search, you will see its pronunciation and meaning.\n")
    print("If you type one single kanji character you have already learned")
    print("in the second text bar and hit search,")
    print("you will see all the possible pronunciations being listed on the user interface,")
    print("with each pronunciation having its corresponding examples.\n")
    print("You can hit 'quiz and game' button to try on the quiz or game function.")
    print("You must have at least 10 words in the learning history to start a quiz.")
    print("When you are in the quiz, you can open kanji_dict.csv file to find the solution,")
    print("and play to see if python is grading your quiz correctly.\n")
    print("If you want to try on the game function, remember to have the font file")
    print("'f910-shin-comic-2.01.otf' in the same directory as the program python file.")
    print("Otherwise, the Japanese characters cannot be displayed on the game interface.\n")
    print("The rule of the memory matching game is that you will keep flipping cards,")
    print("to see what is on the other side of the card.")
    print("Your job is to match pairs of kanji word and its pronunciation.")
    print("If the two cards you have flipped do not match, they will turn back again.")
    print("So you have to memorize what is on the cards you have already flipped.\n")
        
    # add_word_to_file, csv_to_dict and dict_to_csv unit tests
    example = {"怒った" : (["ど", "っ", "た"], "to get angry")}
    add_word_to_file("example_dict.csv", "怒った", "ど", "っ", "た", "", "", "", "to get angry")
    generic_test(csv_to_dict, ("example_dict.csv",), (example,))
    generic_test(csv_to_dict, (dict_to_csv(example, "example_dict.csv"),), (example,))

    example["習慣じゃない"] = (["なら", "かん", "じ", "ゃ", "な", "い"], "habit")
    add_word_to_file("example_dict.csv", "習慣じゃない", "なら", "かん", "じ", "ゃ", "な", "い", "habit")
    generic_test(csv_to_dict, ("example_dict.csv",), (example,))
    generic_test(csv_to_dict, (dict_to_csv(example, "example_dict.csv"),), (example,))

    # check if add_word_to_file adds the words to kanji_history dictionary
    result = True
    for word in example:
        if kanji_history[word] != example[word]:
            result = False
    if result == True:
        print("All the three words have been successfully added to kanji_history by function add_word_to_file.\n")

    # change_pron_or_mean unit tests
    change_pron_or_mean("example_dict.csv", "怒った", "おこ", "っ", "た", "", "", "", "to get angry (short form past tense)")
    example["怒った"] = (["おこ", "っ", "た"], "to get angry (short form past tense)")
    generic_test(csv_to_dict, ("example_dict.csv",), (example,))
    
    change_pron_or_mean("example_dict.csv", "習慣じゃない", "しゅう", "かん", "じ", "ゃ", "な", "い", "not habit")
    example["習慣じゃない"] = (["しゅう", "かん", "じ", "ゃ", "な", "い"], "not habit")
    generic_test(csv_to_dict, ("example_dict.csv",), (example,))

    # add_or_change unit tests: only test the case of adding
    add_or_change("example_dict.csv", "練習します", "れん", "しゅう", "し", "ま", "す", "", "to practice (long form)")
    example["練習します"] = (["れん", "しゅう", "し", "ま", "す"], "to practice (long form)")
    generic_test(csv_to_dict, ("example_dict.csv",), (example,))

    add_or_change("example_dict.csv", "習って", "なら", "っ", "て", "", "", "", "to learn (te form)")
    example["習って"] = (["なら", "っ", "て"], "to learn (te form)")
    generic_test(csv_to_dict, ("example_dict.csv",), (example,))

    # search_pron unit tests
    organized_dict1 = {"なら" : [("習って", (["なら", "っ", "て"], "to learn (te form)"))],
                       "しゅう" : [("習慣じゃない", (["しゅう", "かん", "じ", "ゃ", "な", "い"], "not habit")),
                                ("練習します", (["れん", "しゅう", "し", "ま", "す"], "to practice (long form)"))]}
    generic_test(search_pron, ("習", example), (organized_dict1,))

    organized_dict2 = {"おこ" : [("怒った", (["おこ", "っ", "た"], "to get angry (short form past tense)"))]}
    generic_test(search_pron, ("怒", example), (organized_dict2,))

    # random_ten unit tests
    example["果物じゃない"] = (["くだ", "もの", "じ", "ゃ", "な", "い"], "not fruit")
    example["楽しそうに"] = (["たの", "し", "そ", "う", "に"], "joyfully")
    example["答えます"] = (["こた", "え", "ま", "す"], "to answer (long form)")
    example["表して"] = (["あらわ", "し", "て"], "to express, to show (te form)")
    example["勇気"] = (["ゆう", "き"], "courage")
    example["雪"] = (["ゆき"], "snow")

    ran_ex_pron = {"怒った": "おこった", "習慣じゃない": "しゅうかんじゃない",
                   "練習します": "れんしゅうします", "習って": "ならって",
                   "果物じゃない": "くだものじゃない", "楽しそうに": "たのしそうに",
                   "答えます": "こたえます", "表して": "あらわして",
                   "勇気": "ゆうき", "雪": "ゆき"}
    
    ran_ex_mean = {"怒った": "to get angry (short form past tense)",
                   "習慣じゃない": "not habit",
                   "練習します": "to practice (long form)",
                   "習って": "to learn (te form)",
                   "果物じゃない": "not fruit", "楽しそうに": "joyfully",
                   "答えます": "to answer (long form)",
                   "表して": "to express, to show (te form)",
                   "勇気": "courage", "雪": "snow"}

    generic_test(random_ten_with_prons, (1, 10, example), (ran_ex_pron,))
    generic_test(random_ten_with_means, (1, 10, example), (ran_ex_mean,))

    example.pop("果物じゃない")
    example.pop("楽しそうに")
    example.pop("答えます")
    example.pop("表して")
    example.pop("勇気")
    example.pop("雪")
    
    # word_remove unit tests
    word_remove("example_dict.csv", "怒った")
    example.pop("怒った")
    generic_test(csv_to_dict, ("example_dict.csv",), (example,))

    word_remove("example_dict.csv", "習慣じゃない")
    example.pop("習慣じゃない")
    generic_test(csv_to_dict, ("example_dict.csv",), (example,))

    word_remove("example_dict.csv", "練習します")
    example.pop("練習します")
    generic_test(csv_to_dict, ("example_dict.csv",), (example,))

    word_remove("example_dict.csv", "習って")
    example.pop("習って")
    generic_test(csv_to_dict, ("example_dict.csv",), (example,))

    # check if word_remove removes the words from kanji_history dictionary
    result = True
    for word in ["怒った", "習慣じゃない", "練習します", "習って"]:
        if word in kanji_history:
            result = False
    if result == True:
        print("All the three words have been successfully removed from kanji_history by function word_remove.")
    """
    
    # Start the whole program with the welcome interface
    welcome.tkraise()
    root.mainloop()
