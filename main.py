# Application launching structure based on PyQt6 official documentation.

import sys
from PyQt6.QtWidgets import QApplication
from voting_system import VotingSystem
from gui import VotingApp

def main() -> None:
    """
    Launches the VotingApp application.
    """
    app = QApplication(sys.argv)
    voting_system = VotingSystem()
    window = VotingApp(voting_system)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
