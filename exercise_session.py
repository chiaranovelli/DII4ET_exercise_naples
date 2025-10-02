"""Exercise session management for POD classes."""

from datetime import datetime
from typing import List, Optional
from pod import POD


class ExerciseSession:
    """Manages an exercise session for POD (Problem of the Day) classes."""
    
    def __init__(self, session_name: str, description: str = ""):
        """
        Initialize an exercise session.
        
        Args:
            session_name: Name of the exercise session
            description: Description of the session
        """
        self.session_name = session_name
        self.description = description
        self.created_at = datetime.now()
        self.problems: List[POD] = []
        self.active = True
    
    def add_problem(self, problem: POD):
        """Add a problem to the session."""
        self.problems.append(problem)
    
    def remove_problem(self, problem_id: str) -> bool:
        """
        Remove a problem from the session by ID.
        
        Args:
            problem_id: ID of the problem to remove
            
        Returns:
            True if problem was removed, False if not found
        """
        for i, problem in enumerate(self.problems):
            if problem.problem_id == problem_id:
                self.problems.pop(i)
                return True
        return False
    
    def get_problem(self, problem_id: str) -> Optional[POD]:
        """Get a problem by ID."""
        for problem in self.problems:
            if problem.problem_id == problem_id:
                return problem
        return None
    
    def list_problems(self, show_completed: bool = True) -> List[POD]:
        """
        List all problems in the session.
        
        Args:
            show_completed: If False, only show incomplete problems
            
        Returns:
            List of problems
        """
        if show_completed:
            return self.problems
        return [p for p in self.problems if not p.completed]
    
    def get_progress(self) -> dict:
        """Get session progress statistics."""
        total = len(self.problems)
        completed = sum(1 for p in self.problems if p.completed)
        
        return {
            "total_problems": total,
            "completed": completed,
            "remaining": total - completed,
            "completion_rate": (completed / total * 100) if total > 0 else 0
        }
    
    def end_session(self):
        """Mark the session as ended."""
        self.active = False
    
    def __str__(self):
        status = "Active" if self.active else "Ended"
        progress = self.get_progress()
        return (f"Exercise Session: {self.session_name} ({status})\n"
                f"Problems: {progress['completed']}/{progress['total_problems']} completed "
                f"({progress['completion_rate']:.1f}%)")
    
    def __repr__(self):
        return f"ExerciseSession(session_name='{self.session_name}', problems={len(self.problems)})"
