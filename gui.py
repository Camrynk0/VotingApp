from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

class VotingApp(QWidget):
    """
    A PyQt6 GUI application for voting between two candidates.
    """

    def __init__(self, voting_system):
        """
        Initialize the VotingApp and load the GUI from the .ui file.

        Args:
            voting_system (VotingSystem): The voting system logic object.
        """
        super().__init__()
        uic.loadUi("gui.ui", self)

        self.voting_system = voting_system

        # Connect buttons
        self.voteButton.clicked.connect(self.vote_clicked)
        self.exitButton.clicked.connect(self.exit_clicked)

    def vote_clicked(self):
        """
        Handles the Vote button click: records the vote and updates the result label.
        """
        candidate = self.candidateDropdown.currentText()
        try:
            self.voting_system.vote(candidate)
            self.voting_system.save_votes()
            self.resultLabel.setText(f"Voted for {candidate}!\nTotal votes: {self.voting_system.total_votes()}")
        except ValueError as e:
            self.resultLabel.setText(str(e))

    def exit_clicked(self):
        """
        Handles the Exit button click: saves votes and closes the application.
        """
        self.voting_system.save_votes()
        self.close()
