# GUI structure and window locking technique based on tutorials from RealPython and the official PyQt6 documentation.
# and the official PyQt6 documentation (doc.qt.io/qtforpython).

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

class VotingApp(QWidget):
    """
    A PyQt6 GUI application for voting between two candidates with ID validation.
    """

    def __init__(self, voting_system):
        super().__init__()
        
        # Load the GUI from gui.ui
        uic.loadUi("gui.ui", self)

        # Lock the window size
        self.setFixedSize(self.size())

        self.voting_system = voting_system

        # Connect buttons to functions
        self.voteButton.clicked.connect(self.vote_clicked)
        self.exitButton.clicked.connect(self.exit_clicked)
        
    def vote_clicked(self):
        """
        Handles the Vote button click: validates input, records vote, and updates GUI.
        """
        voter_id = self.idInput.text().strip()
        candidate = self.candidateDropdown.currentText()

        if not voter_id:
            self.resultLabel.setText("Error: ID is required!")
            self.resultLabel.setStyleSheet("color: red;")
            return

        if self.voting_system.has_voted(voter_id):
            self.resultLabel.setText("Error: You have already voted!")
            self.resultLabel.setStyleSheet("color: red;")
            return

        try:
            self.voting_system.vote(voter_id, candidate)
            self.voting_system.save_votes()
            self.resultLabel.setText(f"Success: Voted for {candidate}!")
            self.resultLabel.setStyleSheet("color: green;")
        except ValueError as e:
            self.resultLabel.setText(str(e))
            self.resultLabel.setStyleSheet("color: red;")

    def exit_clicked(self):
        """
        Handles the Exit button click: saves votes and closes the application.
        """
        self.voting_system.save_votes()
        self.close()
