# voting_system.py
import csv
from typing import Dict

class VotingSystem:
    def __init__(self) -> None:
        self.votes: Dict[str, int] = {"John": 0, "Jane": 0}

    def vote(self, candidate: str) -> None:
        if candidate in self.votes:
            self.votes[candidate] += 1
        else:
            raise ValueError(f"Invalid candidate: {candidate}")

    def save_votes(self, filename: str = "data/votes.csv") -> None:
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Candidate", "Votes"])
                for candidate, votes in self.votes.items():
                    writer.writerow([candidate, votes])
        except Exception as e:
            print(f"Error saving votes: {e}")

    def total_votes(self) -> int:
        return sum(self.votes.values())
