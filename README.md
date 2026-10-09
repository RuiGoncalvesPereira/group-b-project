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

As a fashion icon,
I want to impact global fashion trends,
so that I can become an influential individual in the fashion world.

As a tiered long-serving soldier,
I want to life the rest of my life in peace and retire,
so that i can spent more time on myself and rest.

As an employee of a call center,
i want to prioretize the feelings of the customer and listen to them carfully,
so that I can communicate with them better and help them.

### Dayhe

User Story 1

As a learner, I want to be able to choose which chapters to study, so that, I can focus on the parts I want to learn.

Acceptance criteria

-The flashcard database is organized by chapter.
-The system displays a menu organized by chapter.

User Story 2

As a learner, I want to study using quizzes that provide questions and answers, so that, I can assess my current level of understanding through a score.

Acceptance criteria

-When a learner select a chapter, the system randomly displays questions from a set of flashcards.
-When a learner enter an answer, the system dispalys whether it’s correct or incorrect and the correct answer.

User Story 3

As a learner, I want to save my past scores, so that I can track my progress.

Acceptance criteria

-Once the test is complete, the system saves the results along with the corresponding date and time.
-The system displays past test scores in the “Past Scores” menu, sorted by date and time.

### Rui

As a player, I want to be told whether each answer is correct so that I can learn from mistakes.

As a player, I want to see my number of correct and incorrect answers at the end so that I know how I performed.

As a player, I want my result saved to a file so that I can look back at previous attempts.

### Amanuel

As a player, I want to choose a quiz topic from a terminal menu so that I can practise a subject I’m studying.

As a player, I want the quiz to load questions from a file so that questions can be added without changing the Python code.

As a player, I want questions to appear in random order so that each attempt feels different.
