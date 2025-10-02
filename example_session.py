"""Example usage of the POD Exercise Session system."""

from pod import POD
from exercise_session import ExerciseSession


def main():
    """Demonstrate the POD exercise session functionality."""
    
    # Create a new exercise session
    print("Creating a new exercise session for POD class...")
    session = ExerciseSession(
        session_name="Naples Python Workshop - Day 1",
        description="Introduction to Python fundamentals"
    )
    print(f"\n{session}\n")
    
    # Create and add problems to the session
    print("Adding problems to the session...")
    
    problem1 = POD(
        problem_id="POD-001",
        title="Hello World",
        description="Write a program that prints 'Hello, World!' to the console.",
        difficulty="easy",
        tags=["basics", "introduction"]
    )
    
    problem2 = POD(
        problem_id="POD-002",
        title="FizzBuzz",
        description="Print numbers 1-100, but for multiples of 3 print 'Fizz', for multiples of 5 print 'Buzz', and for multiples of both print 'FizzBuzz'.",
        difficulty="medium",
        tags=["loops", "conditionals"]
    )
    
    problem3 = POD(
        problem_id="POD-003",
        title="Fibonacci Sequence",
        description="Generate the first n numbers in the Fibonacci sequence.",
        difficulty="medium",
        tags=["recursion", "algorithms"]
    )
    
    problem4 = POD(
        problem_id="POD-004",
        title="Prime Number Checker",
        description="Write a function to check if a number is prime.",
        difficulty="hard",
        tags=["algorithms", "mathematics"]
    )
    
    session.add_problem(problem1)
    session.add_problem(problem2)
    session.add_problem(problem3)
    session.add_problem(problem4)
    
    # List all problems
    print("\nAll problems in the session:")
    for problem in session.list_problems():
        print(f"  {problem}")
    
    # Mark some problems as completed
    print("\n\nCompleting some problems...")
    problem1.mark_completed("print('Hello, World!')")
    problem2.mark_completed("for i in range(1, 101): print('FizzBuzz' if i%15==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else i)")
    
    # Show progress
    print(f"\n{session}")
    progress = session.get_progress()
    print(f"\nDetailed progress:")
    print(f"  Total problems: {progress['total_problems']}")
    print(f"  Completed: {progress['completed']}")
    print(f"  Remaining: {progress['remaining']}")
    print(f"  Completion rate: {progress['completion_rate']:.1f}%")
    
    # List only incomplete problems
    print("\n\nRemaining problems to solve:")
    for problem in session.list_problems(show_completed=False):
        print(f"  {problem}")
    
    # Get a specific problem
    print("\n\nRetrieving specific problem:")
    specific_problem = session.get_problem("POD-003")
    if specific_problem:
        print(f"  {specific_problem}")
        print(f"  Description: {specific_problem.description}")
    
    # End the session
    print("\n\nEnding the session...")
    session.end_session()
    print(f"{session}")


if __name__ == "__main__":
    main()
