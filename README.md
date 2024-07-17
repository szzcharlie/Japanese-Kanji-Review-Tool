# Japanese-Kanji-Review-Tool
A tool to help you review the kanji vocabulary you have learnt, features include quiz, game and sort
Designed by Charlie Shao

Before running the program:

1. Download 'unit_test.py' to the same directory so that the unit tests of the functions can be run.

2. Download font file 'f910-shin-comic-2.01.otf' to the same directory so that the Japanese characters can be displayed onto the game interface.

3. Please have at least 10 words in the learning history before you try on the quiz and game feature.

4. If you do not want to create your own csv file which records your learning history, download csv file 'kanji_dict.csv' to the same directory so that you can directly use it. There are already 12 words inside this csv file.

Now, you can open the file 'final_project.py' in python and run it, to start the program.

Here are the listed proposed features of the program along with its instructions:

1. A clear user interface which guides the user to different features of the program.

Once you start the program, you will see a main menu listing all the features of this program.

2. Ask the user to add the kanji vocabulary they have learnt to the database by themselves, which can be a really good review process for the user. When adding each vocabulary, the pronunciation written in Japanese phonetic letters for every character is required for the user to fill in, along with its english meaning.

By pressing the first button in the main menu, you can go to the 'add' feature. You will see an interface telling you what to fill in in each text bar, after you finished, hit the button 'Add'. If you want to add a word that already exists in the learning history, the program will ask you whether you want to update its information.

3. Store every vocabulary the user has added in a file so as to read and edit it any time, even if the user exits the program.

Once you have added one word, you will see a csv file 'kanji_dict.csv' in the same directory. This file records all of your learning history. If you want to add or edit the word in this file, press the first button in the main menu. If you want to remove a word, press the second button and type the word you want to remove. The program will tell you either the word has been removed, or the word does not exist in the learning history at all.

You can also press the sixth button 'Show the entire kanji learning history' to directly get a view of all the words inside the csv file.

4. Allow the user to look up the pronunciation and meaning of a word they have entered.

In the main menu, you will see the third button 'Look up the pronunciation and meaning' with a text bar placed above it. In this text bar, you can type one single vocabulary written in kanji, and then hit the button to look up the pronunciation and meaning. The interface will either show you the pronunciation and English meaning, or tell you that the word is not found in the learning history.

5. Allow the user to look up all the possible pronunciations of a single kanji character, along with all the examples the database file has.

In the main menu, you will see the fourth button 'Search for all pronunciations with examples' with a text bar placed above it. In this text bar, you can type one single kanji character, and then hit the button to look for all the possible pronunciations of this character. If the length of the string you enter is not 1, it will be identified and then you will be asked to put in only one character. If you enter hiragana (Japanese phonetic letters) instead of kanji characters, it will also be identified and you will be asked to enter kanji character. If you type in one kanji character, it will either show the pronunciation and word examples you have learnt, or just tell you nothing is found in the learning history.

6. Generate two types of quizzes for the user to review, pronunciation quiz which requires the user to fill in the pronunciation of kanji vocabularies, and tranlstion quiz which requires the user to fill in the original kanji vocabularies according to the English meanings provided. Also allow the user to check their answers and view their score. (Please learn at least 10 words before using this feature.)

In the main menu, you will see the button 'Quiz and Game', this is the place to test yourself whether you have memorized the vocabulary. After you press the button, you will see an interface asking you a number range. The quiz or the game will randomly select 10 words in this range, therefore this range must include at least 10 numbers. You can go back to main menu and press the button 'Show the entire kanji learning history', and then you will see each word is assigned a number. If you only want the words with number 1 to 10 appear in the quiz, then you enter 1 and 10 to the text bar. After you enter a range, if you are not sure whether it is a valid range, you can hit the button 'Okay' to check the validity, the program will tell you whether this is a valid range. If you are confident that the range you entered is valid, you can hit any of the three button below, which are the two kinds of quizzes and the game. If your range happens to be invalid because you haven't checked range, or you haven't typed anything in the text bar, the program will just randomly select 10 words from all the words in the learning history when starting a quiz.

After you start the quiz and finish all ten questions, you can hit button 'Submit' to check whether you get them right and also have a quiz score. If there is any word you get wrong, you can corrct them and reclick the button 'Submit' to check. If you are completely confused and are unable to get a word right, you can hit button 'Check the solution' to view the correct answer.

7. A pair-matching memory game which can make the user have some fun while learning. In this game, the user will constantly flip cards, remember what they already flipped, and try to match pairs of kanji words and its corresponding kanji pronunciation. (Please learn at least 10 words before using this feature.)

Again hit the button 'Quiz and Game' in the main menu, and type in a valid range as mentioned above. Now you can hit the very last button, which is 'Play memory matching game'. If you do not enter a valid range, it will also just randomly select 10 words from all the words in the dictionary.

In the game, you can only flip two cards at one time, and you are trying to flip the two cards which are a pair of kanji word and its pronunciation so as to make a match. If the two cards do not match, they will be flipped back. Therefore you have to try your best to memorize the card you have already flipped. Your score of the game will be shown at the right bottom. If you make a match, your score will not be deducted. And the first 5 wrong match will not cause score to be deducted either. However, starting from the 6th wrong match, 2 points will be deducted each time you flip the cards and fail to make a match. Starting from the 11th wrong match, 3 points will be deducted each time you fail to make a match. After you finish the game, or you feel like you do not want to play it any more at any point, you can just close the game interface and go back to the program interface.
