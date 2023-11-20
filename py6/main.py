import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class QuizWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Викторина")
        self.setGeometry(100, 100, 800, 600)
        self.set_background_image("m.avif")
        self.set_stylesheet()

        self.question_label = QLabel(self)
        self.question_label.setGeometry(100, 100, 600, 200)
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setStyleSheet("font-weight: bold; color: white;")

        self.true_button = QPushButton("Да", self)
        self.true_button.setGeometry(200, 400, 150, 100)
        self.true_button.clicked.connect(lambda: self.check_answer(True))

        self.false_button = QPushButton("Нет", self)
        self.false_button.setGeometry(450, 400, 150, 100)
        self.false_button.clicked.connect(lambda: self.check_answer(False))

        self.current_question = 0
        self.correct_answers = 0  # Счетчик правильных ответов
        self.questions = self.load_questions_from_database()

        if len(self.questions) == 0:
            self.create_database()
            self.insert_questions_to_database()
            self.questions = self.load_questions_from_database()

        self.show_question()

    def set_background_image(self, image_path):
        background_label = QLabel(self)
        background_pixmap = QPixmap(image_path)
        background_label.setPixmap(background_pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        background_label.lower()

    def set_stylesheet(self):
        self.setStyleSheet("""
            QWidget {
                font-size: 24px;  
            }

            QPushButton {
                height: 80px;
                background-color: white;
                color: black;
                font-size: 24px;  
            }

            QLabel {
                margin-bottom: 40px;  
            }
        """)

    def create_database(self):
        try:
            connection = sqlite3.connect("quiz.db")
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS questions (question TEXT, answer TEXT)")
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print("Ошибка при создании базы данных:", error)

    def load_questions_from_database(self):
        try:
            connection = sqlite3.connect("quiz.db")
            cursor = connection.cursor()
            cursor.execute("SELECT question, answer FROM questions")
            questions = cursor.fetchall()
            connection.close()
            return questions
        except sqlite3.Error as error:
            print("Ошибка при загрузке вопросов из базы данных:", error)
            return []

    def insert_questions_to_database(self):
        try:
            connection = sqlite3.connect("quiz.db")
            cursor = connection.cursor()

            questions = [
                ("Арбуз это ягода?", "True"),
                ("У человека 5 пальцев на руке?", "True"),
                ("В високосном году 365 дней?", "False"),
                ("Кит это млекопитающее?", "True"),
                ("У человека 33 зуба?", "False")
            ]

            cursor.executemany("INSERT INTO questions (question, answer) VALUES (?, ?)", questions)
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print("Ошибка при добавлении вопросов в базу данных:", error)

    def show_question(self):
        if self.current_question < len(self.questions):
            question, _ = self.questions[self.current_question]
            self.question_label.setText(question)
        else:
            # Все вопросы отвечены
            self.question_label.setText("Молодец! Вы ответили правильно на {} вопрос(а/ов)".format(self.correct_answers))

    def check_answer(self, user_answer):
        _, correct_answer = self.questions[self.current_question]

        if user_answer == (correct_answer == "True"):
            QMessageBox.information(self, "Правильно!", "Ответ верный!")
            self.correct_answers += 1
        else:

            QMessageBox.information(self, "Неправильно!", "Ответ неверный!")

        self.current_question += 1
        self.show_question()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QuizWindow()
    window.show()
    sys.exit(app.exec_())