# gui.py
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

class VotingApp(QWidget):
    def __init__(self, voting_system):
        super().__init__()
        uic.loadUi("gui.ui", self)

        self.voting_system = voting_system

        # Connect buttons
        self.voteButton.clicked.connect(self.vote_clicked)
        self.exitButton.clicked.connect(self.exit_clicked)

    def vote_clicked(self):
        candidate = self.candidateDropdown.currentText()
        try:
            self.voting_system.vote(candidate)
            self.voting_system.save_votes()
            self.resultLabel.setText(f"Voted for {candidate}!\nTotal votes: {self.voting_system.total_votes()}")
        except ValueError as e:
            self.resultLabel.setText(str(e))

    def exit_clicked(self):
        self.voting_system.save_votes()
        self.close()
