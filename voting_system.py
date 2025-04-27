import csv
from typing import Dict

class VotingSystem:
    """
    A class to manage the voting system logic for two candidates.
    """

    def __init__(self) -> None:
        """
        Initialize the VotingSystem with zero votes for each candidate.
        """
        self.votes: Dict[str, int] = {"John": 0, "Jane": 0}

    def vote(self, candidate: str) -> None:
        """
        Increments the vote count for the specified candidate.
        
        Args:
            candidate (str): The name of the candidate ("John" or "Jane").
        
        Raises:
            ValueError: If the candidate name is invalid.
        """
        if candidate in self.votes:
            self.votes[candidate] += 1
        else:
            raise ValueError(f"Invalid candidate: {candidate}")

    def save_votes(self, filename: str = "data/votes.csv") -> None:
        """
        Saves the current vote totals to a CSV file.

        Args:
            filename (str): The file path where votes should be saved.
        """
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Candidate", "Votes"])
                for candidate, votes in self.votes.items():
                    writer.writerow([candidate, votes])
        except Exception as e:
            print(f"Error saving votes: {e}")

    def total_votes(self) -> int:
        """
        Returns the total number of votes cast.

        Returns:
            int: Total votes for all candidates combined.
        """
        return sum(self.votes.values())
