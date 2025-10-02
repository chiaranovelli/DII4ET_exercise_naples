"""POD (Problem of the Day) class for exercise sessions."""

from datetime import datetime
from typing import List, Optional


class POD:
    """Problem of the Day class representing a single exercise problem."""
    
    def __init__(self, problem_id: str, title: str, description: str, 
                 difficulty: str = "medium", tags: Optional[List[str]] = None):
        """
        Initialize a POD instance.
        
        Args:
            problem_id: Unique identifier for the problem
            title: Title of the problem
            description: Description of the problem
            difficulty: Difficulty level (easy, medium, hard)
            tags: List of tags/topics for the problem
        """
        self.problem_id = problem_id
        self.title = title
        self.description = description
        self.difficulty = difficulty
        self.tags = tags or []
        self.created_at = datetime.now()
        self.completed = False
        self.solution = None
    
    def mark_completed(self, solution: str = ""):
        """Mark the problem as completed with optional solution."""
        self.completed = True
        self.solution = solution
    
    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.problem_id}: {self.title} ({self.difficulty})"
    
    def __repr__(self):
        return f"POD(problem_id='{self.problem_id}', title='{self.title}', completed={self.completed})"
