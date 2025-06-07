RENISH GAMES - HANGMAN
========================

A classic Hangman game with a modern, responsive design and engaging sound effects! Guess the hidden word before you run out of lives (represented by hearts!).

FEATURES
----------
* Classic Hangman Gameplay: Guess letters to reveal the hidden word.
* Difficulty Levels: Choose between Easy (10 mistakes), Medium (6 mistakes), and Hard (4 mistakes).
* Multiple Categories: Play with words from Programming, Animals, Countries, or Fruits.
* Player Name Input: Personalize your game experience.
* Interactive Lives System: Hearts visually represent your remaining guesses.
* Timer: A 3-minute timer adds an extra layer of challenge.
* Responsive Design: Plays well on various screen sizes (desktops, tablets, phones).
* Engaging Audio:
    * Background music (starts on game initiation).
    * Sound effect for correct guesses.
    * Sound effect for incorrect guesses.
* Restart/New Word Options: Easily restart the current game or start a new word in the same category.

HOW TO PLAY
-------------
1.  Open index.html: Simply open the index.html file in your web browser.
2.  Start Game: Click the "Start Game" button on the splash screen. The background music will begin.
3.  Enter Details: Provide your name, select a difficulty level, and choose a word category.
4.  Begin Game: Click "Begin Game."
5.  Guess Letters: Use the on-screen keyboard to guess letters.
    * If correct, the letter will appear in the word placeholder, and a "correct" sound will play.
    * If incorrect, a heart will turn gray, and a "wrong" sound will play.
6.  Win Condition: Guess all the letters in the word before all your hearts turn gray and the timer runs out.
7.  Lose Condition: If all your hearts turn gray, or the timer reaches zero, the game ends, and the correct word is revealed.
8.  Restart/New Word: Use the "Restart Game" button to reload the page and start fresh, or "New Word" to get a new word in the current category.

PROJECT STRUCTURE
-------------------
.
├── index.html
├── vgm.mp3         (Background music)
├── right.mp3       (Sound for correct guess)
├── wrong.mp3       (Sound for wrong guess)
└── README.txt      (This file)


TECHNOLOGIES USED
-------------------
* HTML5: Structure of the game.
* CSS3: Styling and responsive layout.
* JavaScript (ES6+): Game logic, interaction, and audio control.
* SVG: For the heart icons.