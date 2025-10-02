# DII4ET_exercise_naples

A Python-based exercise session management system for POD (Problem of the Day) classes.

## Features

- **POD Class**: Represents individual problems with metadata (title, description, difficulty, tags)
- **Exercise Session Management**: Create and manage exercise sessions with multiple problems
- **Progress Tracking**: Monitor completion status and statistics
- **Simple API**: Easy-to-use interface for educational settings

## Quick Start

### Running the Example

```bash
python example_session.py
```

This will demonstrate the complete functionality of the system including:
- Creating an exercise session
- Adding problems to the session
- Marking problems as completed
- Tracking progress
- Listing remaining problems

### Basic Usage

```python
from pod import POD
from exercise_session import ExerciseSession

# Create a session
session = ExerciseSession(
    session_name="My Exercise Session",
    description="Practice problems for today"
)

# Create a problem
problem = POD(
    problem_id="POD-001",
    title="Hello World",
    description="Write a program that prints 'Hello, World!'",
    difficulty="easy",
    tags=["basics"]
)

# Add problem to session
session.add_problem(problem)

# Mark problem as completed
problem.mark_completed("print('Hello, World!')")

# Check progress
progress = session.get_progress()
print(f"Completed: {progress['completed']}/{progress['total_problems']}")
```

## Classes

### POD (Problem of the Day)

Represents a single exercise problem with:
- `problem_id`: Unique identifier
- `title`: Problem title
- `description`: Detailed description
- `difficulty`: Difficulty level (easy, medium, hard)
- `tags`: List of topic tags
- `completed`: Completion status
- `solution`: Optional solution text

### ExerciseSession

Manages a collection of POD problems:
- `session_name`: Name of the session
- `description`: Session description
- `problems`: List of POD instances
- `active`: Session status

Key methods:
- `add_problem(problem)`: Add a POD to the session
- `remove_problem(problem_id)`: Remove a POD by ID
- `get_problem(problem_id)`: Retrieve a specific POD
- `list_problems(show_completed)`: List all or incomplete problems
- `get_progress()`: Get completion statistics
- `end_session()`: Mark session as ended

## Project Structure

```
DII4ET_exercise_naples/
├── README.md                 # This file
├── pod.py                    # POD class definition
├── exercise_session.py       # ExerciseSession class
└── example_session.py        # Example usage demonstration
```

## License

This project is part of the DII4ET exercise series for Naples workshops.