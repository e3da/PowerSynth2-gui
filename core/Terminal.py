#From https://www.pythonguis.com/tutorials/qprocess-external-programs/

from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                                QVBoxLayout, QWidget, QProgressBar)
from PySide6.QtCore import QProcess
import sys

class SubProcessWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.p = None

        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        l = QVBoxLayout()
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

        self.before_start=None
        self.after_start=None
        self.after_finish=None

    def set_cbfunc(self, before_start=None,after_start=None,after_finish=None):
        self.before_start=before_start
        self.after_start=after_start
        self.after_finish=after_finish

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process(self,cmd="python",args=[]):
        if self.before_start:
            self.before_start()
        if self.p is None:  # No process running.
            self.message("Starting Process.")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start(cmd, args)

            if self.after_start:
                self.after_start()

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def process_finished(self):
        self.message("Process finished.")
        self.p = None
        if self.after_finish:
            self.after_finish()

