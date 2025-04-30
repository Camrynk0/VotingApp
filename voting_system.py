# CSV file saving based on official Python csv module documentation (docs.python.org/csv).

import csv
import os
from datetime import datetime
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

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._save_vote(voter_id, candidate, timestamp)

    def _save_vote(self, voter_id: str, candidate: str, timestamp: str, filename: str = "data/votes.csv") -> None:
        """
        Saves the vote records to a CSV file.

        Args:
            filename (str): The output CSV file name.
        """
        # Append the new vote
        file_exists = os.path.isfile(filename)
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Voter ID", "Candidate", "Timestamp"])
            writer.writerow([voter_id, candidate, timestamp])

        # Read existing votes to calculate totals
        vote_counts = {}
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cand = row["Candidate"]
                if cand in self.votes:
                    vote_counts[cand] = vote_counts.get(cand, 0) + 1

        # Remove existing summary rows
        lines = []
        with open(filename, mode='r', newline='') as file:
            lines = [line for line in file if not line.startswith("Total Votes")]

        with open(filename, mode='w', newline='') as file:
            file.writelines(lines)

        # Append the summary row
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            summary = ["Total Votes"]
            for candidate in self.votes:
                summary.append(f"{candidate}: {vote_counts.get(candidate, 0)}")
            writer.writerow(summary)

    def total_votes(self) -> int:
        """
        Returns the total number of votes.

        Returns:
            int: The number of total votes.
        """
        return sum(self.votes.values())
