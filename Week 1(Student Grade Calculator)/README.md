# Student Grade Calculator

A simple Command-Line Interface (CLI) application built using Python to calculate a student's total marks, average, grade, and pass/fail result.

## Features

- Accepts student name
- Accepts multiple subjects
- Accepts marks for each subject
- Validates marks between 0 and 100
- Calculates total marks
- Calculates average percentage
- Assigns a grade based on the average
- Determines Pass/Fail status
- Displays subject-wise marks
- Handles invalid user input

## Grade Criteria

| Average | Grade |
|--------:|:------|
| 90 - 100 | A+ |
| 80 - 89 | A |
| 70 - 79 | B |
| 60 - 69 | C |
| 50 - 59 | D |
| Below 50 | F |

### Pass Criteria

A student is considered **PASS** if the average marks are 40 or above.

## Technologies Used

- Python 3
- Command-Line Interface (CLI)

## Project Structure

```text
Student-Grade-Calculator/
│
├── main.py
└── README.md