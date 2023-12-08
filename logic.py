from PyQt6.QtWidgets import *
from gui import *
import csv


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        '''
        This function initializes the screen to allow
        for all the questions needing to be answered
        before submission.
        '''
        super().__init__()
        self.setupUi(self)
        self.radio_public.setChecked(True)
        self.radio_2years.setChecked(True)
        self.push_schools.clicked.connect(lambda : self.schools())
        self.push_submit.clicked.connect(lambda : self.submit())
        self.push_clear.clicked.connect(lambda: self.clear())

    def schools(self) -> None:
        '''
        This function will provide a drop-down menu
        of all the schools that fit the school type and
        number of years attending.
        '''
        self.combo_available.clear()
        with open('Final.Project.csv', newline='') as csvfile:
            schools = csv.reader(csvfile, delimiter=',', quotechar='|')
            if self.radio_public.isChecked() and self.radio_2years.isChecked():
                for row in schools:
                    if row[1] == 'Yes' and row[4] == 'Yes':
                        self.combo_available.addItem(row[0])
            elif self.radio_public.isChecked() and self.radio_4years.isChecked():
                for row in schools:
                    if row[1] == 'Yes' and row[3] == 'Yes':
                        self.combo_available.addItem(row[0])
            elif self.radio_private.isChecked() and self.radio_2years.isChecked():
                for row in schools:
                    if row[2] == 'Yes' and row[4] == 'Yes':
                        self.combo_available.addItem(row[0])
            elif self.radio_private.isChecked() and self.radio_4years.isChecked():
                for row in schools:
                    if row[2] == 'Yes' and row[3] == 'Yes':
                        self.combo_available.addItem(row[0])
        self.label_match.setText("The following schools are a match.")

    def submit(self) -> None:
        '''
        This function will check if a school has been selected, and
        if a correct value has been entered for the known scholarships.
        It will then go to the csv file and show the estimated cost of
        tuition based on the entered scholarship value and school selected.
        '''
        try:
            scholarships = float(self.input_scholarship.text())
            if scholarships < 0:
                raise ValueError
            self.label_error.setText(f"Entered Scholarship Amount: ${scholarships:.2f}")
            selected_school = self.combo_available.currentText()
            if selected_school == '':
                raise RuntimeError
            with open('Final.Project.csv', newline='') as csvfile:
                schools = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in schools:
                    if row[0] == selected_school:
                        tuition = float(row[5]) - scholarships
            self.label_tuition.setText("Estimated Cost Of Tuition:")
            if tuition > 0:
                self.label_cost.setText(f"${tuition:.2f}")
            else:
                self.label_cost.setText(f"$0.00")
        except ValueError:
            self.label_error.setText("Invalid input. Value must be numeric and positive.")
        except RuntimeError:
            self.label_error.setText("Please select a school.")


    def clear(self) -> None:
        '''
        This function will clear all of the selected
        options and will allow for the next user.
        '''
        self.label_error.setText('')
        self.input_scholarship.setText('')
        self.label_match.setText('')
        self.label_tuition.setText('')
        self.label_cost.setText('')
        self.radio_public.setChecked(True)
        self.radio_2years.setChecked(True)
        self.combo_available.clear()





