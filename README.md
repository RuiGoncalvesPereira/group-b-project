
# Group B Project: Flashcard Quiz

## Project problem

Learners need a simple way to practise subjects with flashcards, check their answers, and track their progress. We propose a Python terminal application that loads flashcards from a file and allows learners to review their results.

The quiz uses short-answer questions with predefined correct answers. Answers are checked without considering capitalization or spaces at the beginning or end. Each quiz includes all questions from the selected chapter in a random order.

Possible app flow:

1. Show a menu to start a quiz, view past scores, manage flashcards, or quit.
2. Let the player choose a chapter and load its questions in a random order.
3. Show questions one at a time, check answers, and display the final score.
4. Allow the player to review or retry mistakes and view previous results.
5. Save quiz results to a file and handle invalid input or file errors.

## User stories

### Marisa

#### 1. Add flashcards

As a learner, I want to add flashcards so that I can expand my study material.

Acceptance criteria:

- Given I choose to add a flashcard, when I enter a chapter, question, and correct answer, then the flashcard is saved.
- Given I leave a required field empty, when I try to save, then the app displays an error.
- Given I add a flashcard, when I restart the app, then the flashcard is still available.

#### 2. Final score

As a learner, I want to see my final score so that I know how well I performed.

Acceptance criteria:

- Given I finish a quiz, when the results appear, then the app shows my correct and incorrect answers.
- Given I finish a quiz, when the score is calculated, then the app displays the percentage correct.
- Given I answer three out of five questions correctly, when the result appears, then the score is 60%.

#### 3. Review mistakes

As a learner, I want to review my incorrect answers so that I know what to study again.

Acceptance criteria:

- Given I made mistakes, when I choose to review them, then the app shows each question, my answer, and the correct answer.
- Given I made no mistakes, when I choose to review them, then the app displays "No mistakes to review."

### Dayhe

#### 1. Choose a chapter

As a learner, I want to choose a chapter so that I can focus on specific study material.

Acceptance criteria:

- Given chapters are available, when I start a quiz, then the app displays them in a numbered menu.
- Given I select a chapter, when the quiz starts, then only questions from that chapter are used.
- Given I enter an invalid selection, when the app checks my input, then it displays an error and lets me try again.
- Given no chapters are available, when I start a quiz, then the app displays an explanatory message.

#### 2. View quiz progress

As a learner, I want to see my quiz progress so that I know how many questions are left.

Acceptance criteria:

- Given I start a quiz, when a question appears, then the app displays the current question number and total questions.
- Given I answer a question, when the next question appears, then the question number increases.
- Given I answer the final question, when the answer is checked, then the quiz ends and displays my result.

#### 3. View past scores

As a learner, I want to view my past scores so that I can compare my performance over time.

Acceptance criteria:

- Given previous results exist, when I select "Past Scores," then the app displays them newest first.
- Given results are displayed, then each result shows the chapter, date/time, correct answers out of total questions, and percentage.
- Given no results exist, when I select "Past Scores," then the app displays "No previous results."

### Rui

#### 1. Check answers

As a learner, I want feedback after each answer so that I can learn from my mistakes.

Acceptance criteria:

- Given I submit a short answer, when the app compares it with the predefined answer, then it displays whether it is correct or incorrect.
- Given my answer differs only in capitalization or surrounding spaces, when it is checked, then it is accepted as correct.
- Given my answer is incorrect, when feedback appears, then the app displays the correct answer.
- Given I submit an empty answer, when the app checks my input, then it displays an error without moving to the next question.

#### 2. Edit flashcards

As a learner, I want to edit existing flashcards so that I can correct mistakes in my study material.

Acceptance criteria:

- Given flashcards exist, when I choose to edit one, then the app lets me select a flashcard.
- Given I select a flashcard, when I change its question or correct answer, then the changes are saved.
- Given I enter an empty question or answer, when I try to save, then the app displays an error.
- Given I edit a flashcard, when I restart the app, then the changes are still available.

#### 3. Filter past scores

As a learner, I want to filter past scores by chapter so that I can track my progress in a specific subject.

Acceptance criteria:

- Given past results exist, when I choose to filter them, then I can select a chapter or show all results.
- Given I select a chapter, when the results appear, then only matching results are displayed, newest first.
- Given I enter an invalid selection, when the app checks my input, then it displays an error and lets me try again.
- Given no results match, when the filter is applied, then the app displays an explanatory message.

### Amanuel

#### 1. Load flashcards

As a learner, I want flashcards loaded from a file so that study material can be updated without changing the code.

Acceptance criteria:

- Given a valid flashcard file exists, when the app starts, then it loads each flashcard's chapter, question, and correct answer.
- Given new flashcards are added to the file, when the app restarts, then they are available.
- Given the file is missing, unreadable, or incorrectly formatted, when the app loads it, then it displays an error without crashing or overwriting the file.
- Given the file is empty, when I start a quiz, then the app explains that no questions are available.

#### 2. Random questions

As a learner, I want questions in a random order so that I can practise without memorizing their sequence.

Acceptance criteria:

- Given I select a chapter, when the quiz starts, then all questions from that chapter are included.
- Given the quiz starts, when questions are displayed, then they appear in a randomized order.
- Given I complete a quiz, then no question has appeared more than once.

#### 3. Retry mistakes

As a learner, I want to retry questions I answered incorrectly so that I can practise difficult material.

Acceptance criteria:

- Given I made mistakes, when I choose "Retry Mistakes," then a new quiz starts with only those questions.
- Given I start a retry, when the questions appear, then the score starts at zero.
- Given I finish a retry, when the result is calculated, then it is saved as a separate attempt.
- Given I made no mistakes, when I choose to retry, then the app explains that there are no questions to retry.
