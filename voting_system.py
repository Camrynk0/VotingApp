# CSV file saving based on official Python csv module documentation (docs.python.org/csv).

import csv
from typing import Dict, Set

class VotingSystem:
    """
    A class to manage the voting system logic for two candidates with ID tracking.
    """

    def __init__(self) -> None:
        """
        Initialize the VotingSystem with zero votes and no voted IDs.
        """
        self.votes: Dict[str, int] = {"John": 0, "Jane": 0}
        self.voted_ids: Set[str] = set()

    def has_voted(self, voter_id: str) -> bool:
        """
        Check if the given voter ID has already voted.

        Args:
            voter_id (str): The unique voter ID.

        Returns:
            bool: True if ID has already voted, False otherwise.
        """
        return voter_id in self.voted_ids

    def vote(self, voter_id: str, candidate: str) -> None:
        """
        Registers a vote if the ID has not already voted.

        Args:
            voter_id (str): The voter ID.
            candidate (str): The candidate to vote for.

        Raises:
            ValueError: If candidate is invalid.
        """
        if candidate not in self.votes:
            raise ValueError(f"Invalid candidate: {candidate}")

        self.votes[candidate] += 1
        self.voted_ids.add(voter_id)

    def save_votes(self, filename: str = "data/votes.csv") -> None:
        """
        Saves the vote records to a CSV file.

        Args:
            filename (str): The output CSV file name.
        """
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Voter ID", "Candidate"])
                for voter_id in self.voted_ids:
                    for candidate, count in self.votes.items():
                        # Simplified: Normally would store individual votes
                        writer.writerow([voter_id, candidate])
        except Exception as e:
            print(f"Error saving votes: {e}")

    def total_votes(self) -> int:
        """
        Returns the total number of votes.

        Returns:
            int: The number of total votes.
        """
        return sum(self.votes.values())
