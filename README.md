# Group B Project: Flashcard Quiz

## Project problem

Learners need a simple way to practise subjects with flashcards, check their answers, and see their scores. We propose a Python terminal application that loads questions from a file and lets players review past results. We will clarify the final scope with the teacher.

Possible app flow:

1. Show a menu; let the player choose a topic; let the player quit
2. Load questions from a file; select five at random; show each question
3. Check answers; keep score; show the final result
4. Save results to a file; show previous results; handle invalid input or missing files

## User stories

### Marisa

#### 1. Main menu

As a learner, I want a terminal menu so that I can choose what to do.

Acceptance criteria:

- The menu offers “Start Quiz,” “Past Scores,” and “Quit.”
- Invalid input displays an error and lets me try again.
- Selecting “Quit” closes the application.

#### 2. Final score

As a learner, I want to see my final score so that I know how well I performed.

Acceptance criteria:

- After the quiz, the app shows the number of correct and incorrect answers.
- It also shows the percentage correct.
- Three correct answers out of five produce a score of 60%.

#### 3. Review mistakes

As a learner, I want to review my incorrect answers so that I know what to study again.

Acceptance criteria:

- After the quiz, I can choose to review mistakes.
- The app shows each incorrect question, my answer, and the correct answer.
- If I made no mistakes, it displays “No mistakes to review.”

### Dayhe

#### 1. Choose a chapter

As a learner, I want to choose a chapter so that I can focus on the material I need to study.

Acceptance criteria:

- The app displays the available chapters in a numbered terminal menu.
- My selection determines which chapter the quiz uses.
- Invalid selections display an error and let me try again.
- If no chapters are available, the app displays an explanatory message.

#### 2. Choose the number of questions

As a learner, I want to choose how many questions to answer so that I can control the length of my quiz.

Acceptance criteria:

- The app shows how many questions are available in the selected chapter.
- I can enter a whole number between one and the available question count.
- Invalid input displays an error and lets me try again.

#### 3. View past scores

As a learner, I want to view my past scores so that I can compare my performance over time.

Acceptance criteria:

- “Past Scores” displays saved results, newest first.
- Each result shows the chapter, date/time, correct answers out of total questions, and percentage.
- If no results exist, the app displays “No previous results.”

### Rui

#### 1. Check answers

As a learner, I want feedback after each answer so that I can learn from mistakes.

Acceptance criteria:

- The app displays whether my answer is correct or incorrect.
- Capitalization and spaces at the beginning or end do not affect the comparison.
- Incorrect answers reveal the correct answer.
- Empty answers are rejected without advancing the quiz.

#### 2. Save results

As a learner, I want my quiz results saved so that I can review them later.

Acceptance criteria:

- Completed quizzes are saved with their chapter, date/time, total questions, correct answers, and percentage.
- New results preserve previous results.
- Saved results remain available after restarting the app.
- If saving fails, the app displays an error instead of a success message.

#### 3. Filter past scores

As a learner, I want to filter past scores by chapter so that I can track my progress in a particular subject.

Acceptance criteria:

- I can select a chapter or choose to show all results.
- Matching results appear newest first.
- Invalid selections display an error and let me try again.
- If no results match, the app displays an explanatory message.

### Amanuel

#### 1. Load flashcards

As a learner, I want flashcards loaded from a file so that study material can be updated without changing the code.

Acceptance criteria:

- The app reads each flashcard’s chapter, question, and correct answer.
- Valid flashcards added to the file are available when the app starts again.
- Missing, unreadable, or incorrectly formatted files produce an error without crashing or overwriting the file.
- An empty file produces a message explaining that no quiz is available.

#### 2. Random questions

As a learner, I want randomly selected questions so that I can practise different parts of a chapter.

Acceptance criteria:

- The quiz contains the requested number of questions from the selected chapter.
- No flashcard appears twice within the same quiz.
- Questions appear one at a time in a randomized order.

#### 3. Retry mistakes

As a learner, I want to retry questions I answered incorrectly so that I can practise difficult material.

Acceptance criteria:

- After a quiz, I can retry only the questions I answered incorrectly.
- The retry starts with a new score and is saved as a separate attempt.
- If I answered everything correctly, the app explains that there are no questions to retry.
