import psycopg2
import sys
import datetime
import psycopg2

conn = psycopg2.connect(database="laba_7",
                        user="postgres",
                        password="raul2004",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                             QTableWidgetItem, QPushButton, QMessageBox)

zone = datetime.timezone(datetime.timedelta(hours=3))


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Расписание")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_shedule_tab()
        self._create_teachers_tab()
        self._create_subjects_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="bfi2203",
                        user="postgres",
                        password="password",
                        host="localhost",
                        port="5432")

        self.cursor = self.conn.cursor()

    def _create_teachers_tab(self):
        self.teachers_tab = QWidget()
        self.tabs.addTab(self.teachers_tab, "Преподаватели")

        self.teachers_gbox = QGroupBox("Преподаватели")

        self.svboxt = QVBoxLayout()
        self.shboxt1 = QHBoxLayout()
        self.shboxt2 = QHBoxLayout()
        self.shboxt3 = QHBoxLayout()

        self.svboxt.addLayout(self.shboxt1)
        self.svboxt.addLayout(self.shboxt2)
        self.svboxt.addLayout(self.shboxt3)

        self.shboxt1.addWidget(self.teachers_gbox)

        self._create_teachers_table()

        self.teachers_tab.setLayout(self.svboxt)

        self.new_teachers_button = QPushButton("Добавить строку")
        self.shboxt2.addWidget(self.new_teachers_button)
        self.new_teachers_button.clicked.connect(self._new_teachers_table)

        self.update_teachers_button = QPushButton("Обновить")
        self.shboxt3.addWidget(self.update_teachers_button)
        self.update_teachers_button.clicked.connect(self._update_teachers_table)

    def _create_subjects_tab(self):
        self.subjects_tab = QWidget()
        self.tabs.addTab(self.subjects_tab, "Предметы")

        self.subjects_gbox = QGroupBox("Предметы")

        self.svboxs = QVBoxLayout()
        self.shboxs1 = QHBoxLayout()
        self.shboxs2 = QHBoxLayout()
        self.shboxs3 = QHBoxLayout()

        self.svboxs.addLayout(self.shboxs1)
        self.svboxs.addLayout(self.shboxs2)
        self.svboxs.addLayout(self.shboxs3)

        self.shboxs1.addWidget(self.subjects_gbox)

        self._create_subjects_table()

        self.subjects_tab.setLayout(self.svboxs)

        self.new_subjects_button = QPushButton("Добавить строку")
        self.shboxs2.addWidget(self.new_subjects_button)
        self.new_subjects_button.clicked.connect(self._new_subjects_table)

        self.update_subjects_button = QPushButton("Обновить")
        self.shboxs3.addWidget(self.update_subjects_button)
        self.update_subjects_button.clicked.connect(self._update_subjects_table)

    def _create_shedule_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Расписание")

        self.monday_gbox = QGroupBox("Понедельник")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)

        self.shbox1.addWidget(self.monday_gbox)

        self._create_monday_table()

        self.tuesday_gbox = QGroupBox("Вторник")

        self.shbox3 = QHBoxLayout()
        self.shbox4 = QHBoxLayout()

        self.svbox.addLayout(self.shbox3)
        self.svbox.addLayout(self.shbox4)

        self.shbox1.addWidget(self.tuesday_gbox)

        self._create_tuesday_table()

        self.wednesday_gbox = QGroupBox("Среда")

        self.shbox5 = QHBoxLayout()
        self.shbox6 = QHBoxLayout()

        self.svbox.addLayout(self.shbox5)
        self.svbox.addLayout(self.shbox6)

        self.shbox1.addWidget(self.wednesday_gbox)

        self._create_wednesday_table()

        self.thursday_gbox = QGroupBox("Четверг")

        self.shbox7 = QHBoxLayout()
        self.shbox8 = QHBoxLayout()

        self.svbox.addLayout(self.shbox7)
        self.svbox.addLayout(self.shbox8)

        self.shbox2.addWidget(self.thursday_gbox)

        self._create_thursday_table()

        self.friday_gbox = QGroupBox("Пятница")

        self.shbox9 = QHBoxLayout()
        self.shbox10 = QHBoxLayout()

        self.svbox.addLayout(self.shbox9)
        self.svbox.addLayout(self.shbox10)

        self.shbox2.addWidget(self.friday_gbox)

        self._create_friday_table()

        self.saturday_gbox = QGroupBox("Суббота")

        self.shbox11 = QHBoxLayout()
        self.shbox12 = QHBoxLayout()

        self.svbox.addLayout(self.shbox11)
        self.svbox.addLayout(self.shbox12)

        self.shbox2.addWidget(self.saturday_gbox)

        self._create_saturday_table()

        self.update_shedule_button = QPushButton("Обновить")
        self.shbox6.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.shedule_tab.setLayout(self.svbox)

    def _create_monday_table(self):
        self.monday_table = QTableWidget()
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table.setColumnCount(4)
        self.monday_table.setHorizontalHeaderLabels(["Предмет", "Время", "Преподаватель", ""])

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _create_tuesday_table(self):
        self.tuesday_table = QTableWidget()
        self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_table.setColumnCount(4)
        self.tuesday_table.setHorizontalHeaderLabels(["Предмет", "Время", "Преподаватель", ""])

        self._update_tuesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.tuesday_table)
        self.tuesday_gbox.setLayout(self.mvbox)

    def _create_wednesday_table(self):
        self.wednesday_table = QTableWidget()
        self.wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday_table.setColumnCount(4)
        self.wednesday_table.setHorizontalHeaderLabels(["Предмет", "Время", "Преподаватель", ""])

        self._update_wednesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.wednesday_table)
        self.wednesday_gbox.setLayout(self.mvbox)

    def _create_thursday_table(self):
        self.thursday_table = QTableWidget()
        self.thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday_table.setColumnCount(4)
        self.thursday_table.setHorizontalHeaderLabels(["Предмет", "Время", "Преподаватель", ""])

        self._update_thursday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.thursday_table)
        self.thursday_gbox.setLayout(self.mvbox)

    def _create_friday_table(self):
        self.friday_table = QTableWidget()
        self.friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday_table.setColumnCount(4)
        self.friday_table.setHorizontalHeaderLabels(["Предмет", "Время", "Преподаватель", ""])

        self._update_friday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.friday_table)
        self.friday_gbox.setLayout(self.mvbox)

    def _create_saturday_table(self):
        self.saturday_table = QTableWidget()
        self.saturday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.saturday_table.setColumnCount(4)
        self.saturday_table.setHorizontalHeaderLabels(["Предмет", "Время", "Преподаватель", ""])

        self._update_saturday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.saturday_table)
        self.saturday_gbox.setLayout(self.mvbox)

    def _create_teachers_table(self):
        self.teachers_table = QTableWidget()
        self.teachers_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.teachers_table.setColumnCount(3)
        self.teachers_table.setHorizontalHeaderLabels(["Предмет", "Преподаватель", ""])

        self._update_teachers_table()

        self.mvboxt = QVBoxLayout()
        self.mvboxt.addWidget(self.teachers_table)
        self.teachers_gbox.setLayout(self.mvboxt)

    def _create_subjects_table(self):
        self.subjects_table = QTableWidget()
        self.subjects_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.subjects_table.setColumnCount(2)
        self.subjects_table.setHorizontalHeaderLabels(["Предметы", ""])

        self._update_subjects_table()

        self.mvboxs = QVBoxLayout()
        self.mvboxs.addWidget(self.subjects_table)
        self.subjects_gbox.setLayout(self.mvboxs)

    def _update_monday_table(self):
        time = datetime.datetime.now(zone)
        self.cursor.execute("SELECT * FROM timetable WHERE day='понедельник'"
                            "AND parity=%s", ((int(time.strftime('%W')) - 34) % 2,))
        records = list(self.cursor.fetchall())
        records.sort()
        self.monday_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Перезаписать")

            self.monday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[3])))
            self.monday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.monday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[-2])))
            self.monday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num, 'понедельник'))

        self.monday_table.resizeRowsToContents()

    def _update_tuesday_table(self):
        time = datetime.datetime.now(zone)
        self.cursor.execute("SELECT * FROM timetable WHERE day='вторник'"
                            "AND parity=%s", ((int(time.strftime('%W')) - 34) % 2,))
        records = list(self.cursor.fetchall())

        self.tuesday_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Перезаписать")

            self.tuesday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[3])))
            self.tuesday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.tuesday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[-2])))
            self.tuesday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num, 'вторник'))

        self.tuesday_table.resizeRowsToContents()

    def _update_wednesday_table(self):
        time = datetime.datetime.now(zone)
        self.cursor.execute("SELECT * FROM timetable WHERE day='среда'"
                            "AND parity=%s", ((int(time.strftime('%W')) - 34) % 2,))
        records = list(self.cursor.fetchall())
        records.sort()
        self.wednesday_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Перезаписать")

            self.wednesday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[3])))
            self.wednesday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.wednesday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[-2])))
            self.wednesday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num, 'среда'))

        self.wednesday_table.resizeRowsToContents()

    def _update_thursday_table(self):
        time = datetime.datetime.now(zone)
        self.cursor.execute("SELECT * FROM timetable WHERE day='четверг'"
                            "AND parity=%s", ((int(time.strftime('%W')) - 34) % 2,))
        records = list(self.cursor.fetchall())
        records.sort()
        self.thursday_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Перезаписать")

            self.thursday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[3])))
            self.thursday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.thursday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[-2])))
            self.thursday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num, 'четверг'))

        self.thursday_table.resizeRowsToContents()

    def _update_friday_table(self):
        time = datetime.datetime.now(zone)
        self.cursor.execute("SELECT * FROM timetable WHERE day='пятница'"
                            "AND parity=%s", ((int(time.strftime('%W')) - 34) % 2,))
        records = list(self.cursor.fetchall())
        records.sort()
        self.friday_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Перезаписать")

            self.friday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[3])))
            self.friday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.friday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[-2])))
            self.friday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num, 'пятница'))

        self.friday_table.resizeRowsToContents()


    def _update_saturday_table(self):
        time = datetime.datetime.now(zone)
        self.cursor.execute("SELECT * FROM timetable WHERE day='суббота'"
                            "AND parity=%s", ((int(time.strftime('%W')) - 34) % 2,))
        records = list(self.cursor.fetchall())
        records.sort()
        self.saturday_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Перезаписать")

            self.saturday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[3])))
            self.saturday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.saturday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[-2])))
            self.saturday_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num, 'суббота'))

        self.saturday_table.resizeRowsToContents()

    def _update_teachers_table(self):
        self.cursor.execute("SELECT * FROM teachers WHERE full_name <> ''")
        records = list(self.cursor.fetchall())
        self.teachers_table.setRowCount(len(records))
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Перезаписать")

            self.teachers_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.teachers_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[1])))
            self.teachers_table.setItem(i, 2,
                                        QTableWidgetItem(str(r[0])))
            self.teachers_table.setCellWidget(i, 2, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_teacher_from_table(num))
        self.teachers_table.resizeRowsToContents()

    def _update_subjects_table(self):
        self.cursor.execute("SELECT * FROM subjects WHERE name <> ''")
        records = list(self.cursor.fetchall())
        self.subjects_table.setRowCount(len(records))
        for i, r in enumerate(records):
            joinButton = QPushButton("Перезаписать")

            self.subjects_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[-1])))
            self.subjects_table.setItem(i, 1,
                                        QTableWidgetItem(str(r[0])))
            self.subjects_table.setCellWidget(i, 1, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_subject_from_table(num))
        self.subjects_table.resizeRowsToContents()


    def _change_day_from_table(self, rowNum, day):
        row = list()
        if day == 'понедельник':
            for i in range(self.monday_table.columnCount()):
                try:
                    row.append(self.monday_table.item(rowNum, i).text())
                except:
                    row.append(None)
            try:
                self.cursor.execute("UPDATE timetable SET subject=%s, teacher=%s WHERE day=%s AND time=%s",
                                    (row[0], row[2], day, row[1]))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")
        if day == 'вторник':
            for i in range(self.tuesday_table.columnCount()):
                try:
                    row.append(self.tuesday_table.item(rowNum, i).text())
                except:
                    row.append(None)
            try:
                self.cursor.execute("UPDATE timetable SET subject=%s, teacher=%s WHERE day=%s AND time=%s",
                                    (row[0], row[2], day, row[1]))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")
        if day == 'среда':
            for i in range(self.wednesday_table.columnCount()):
                try:
                    row.append(self.wednesday_table.item(rowNum, i).text())
                except:
                    row.append(None)
            try:
                self.cursor.execute("UPDATE timetable SET subject=%s, teacher=%s WHERE day=%s AND time=%s",
                                    (row[0], row[2], day, row[1]))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")

        if day == 'четверг':
            for i in range(self.thursday_table.columnCount()):
                try:
                    row.append(self.thursday_table.item(rowNum, i).text())
                except:
                    row.append(None)
            try:
                self.cursor.execute("UPDATE timetable SET subject=%s, teacher=%s WHERE day=%s AND time=%s",
                                    (row[0], row[2], day, row[1]))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")
        if day == 'пятница':
            for i in range(self.friday_table.columnCount()):
                try:
                    row.append(self.friday_table.item(rowNum, i).text())
                except:
                    row.append(None)
            try:
                self.cursor.execute("UPDATE timetable SET subject=%s, teacher=%s WHERE day=%s AND time=%s",
                                    (row[0], row[2], day, row[1]))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")
        if day == 'суббота':
            for i in range(self.saturday_table.columnCount()):
                try:
                    row.append(self.saturday_table.item(rowNum, i).text())
                except:
                    row.append(None)
            try:
                self.cursor.execute("UPDATE timetable SET subject=%s, teacher=%s WHERE day=%s AND time=%s",
                                    (row[0], row[2], day, row[1]))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _change_teacher_from_table(self, rowNum):
        row = list()
        for i in range(self.teachers_table.columnCount()):
            try:
                row.append(self.teachers_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("SELECT id FROM teachers")
            records = list(self.cursor.fetchall())
            mas = []
            for data in records:
                mas.append(data[0])
            if row[0] and row[1] and int(row[2]) in mas:
                self.cursor.execute("UPDATE teachers SET full_name=%s, subject=%s WHERE id=%s",
                                    (row[1], row[0], row[2]))
                self.conn.commit()
            elif not(row[0]) and not(row[1]) and int(row[2]) in mas:
                self.cursor.execute("DELETE FROM teachers WHERE id=%s",
                                    (row[2],))
                self.conn.commit()
            elif not(int(row[2]) in mas) and row[1] and row[0]:
                self.cursor.execute("INSERT INTO teachers (subject, full_name, id) VALUES (%s, %s, %s)",
                                        (row[0], row[1], row[2]))
                self.conn.commit()
            else:
                raise Exception
        except:
            QMessageBox.about(self, "Error", "Enter or delete all fields")

    def _change_subject_from_table(self, rowNum):
        row = list()
        for i in range(self.subjects_table.columnCount()):
            try:
                row.append(self.subjects_table.item(rowNum, i).text())
            except:
                row.append(None)
        if row[0]:
            self.cursor.execute("SELECT id FROM subjects")
            records = list(self.cursor.fetchall())
            mas = []
            for data in records:
                mas.append(data[0])
            if int(row[1]) in mas:
                self.cursor.execute("UPDATE subjects SET name=%s WHERE id=%s",
                                            (row[0], row[1]))
                self.conn.commit()
            else:
                self.cursor.execute("INSERT INTO subjects (name, id) VALUES (%s, %s)",
                                        (row[0], row[1]))
                self.conn.commit()
        elif not(row[0]):
            self.cursor.execute("DELETE FROM subjects WHERE id=%s",
                                    (row[1],))
            self.conn.commit()

    def _new_subjects_table(self):
        row = []
        for i in range(self.subjects_table.columnCount()):
            try:
                row.append(self.subjects_table.item(self.subjects_table.rowCount() - 1, i).text())
            except:
                row.append(None)
        if row[0]:
            self.cursor.execute("SELECT id FROM subjects")
            records = list(self.cursor.fetchall())
            index = -1
            for data in records:
                if data[0] > index:
                    index = data[0]
            index += 1
            self.subjects_table.setRowCount(self.subjects_table.rowCount() + 1)
            joinButton = QPushButton("Перезаписать")
            self.subjects_table.setItem(self.subjects_table.rowCount() - 1, 0,
                                            QTableWidgetItem(''))
            self.subjects_table.setItem(self.subjects_table.rowCount() - 1, 1,
                                            QTableWidgetItem(str(index)))
            self.subjects_table.setCellWidget(self.subjects_table.rowCount() - 1, 1, joinButton)
            joinButton.clicked.connect(lambda ch, num=self.subjects_table.rowCount() - 1: self._change_subject_from_table(num))

    def _new_teachers_table(self):
        row = []
        for i in range(self.teachers_table.columnCount()):
            try:
                row.append(self.teachers_table.item(self.teachers_table.rowCount() - 1, i).text())
            except:
                row.append(None)
        if row[0] and row[1]:
            self.cursor.execute("SELECT id FROM teachers")
            records = list(self.cursor.fetchall())
            index = -1
            for data in records:
                if data[0] > index:
                    index = data[0]
            index += 1
            self.teachers_table.setRowCount(self.teachers_table.rowCount() + 1)
            joinButton = QPushButton("Перезаписать")
            self.teachers_table.setItem(self.teachers_table.rowCount() - 1, 0,
                                            QTableWidgetItem(''))
            self.teachers_table.setItem(self.teachers_table.rowCount() - 1, 1,
                                            QTableWidgetItem(''))
            self.teachers_table.setItem(self.teachers_table.rowCount() - 1, 2,
                                            QTableWidgetItem(str(index)))
            self.teachers_table.setCellWidget(self.teachers_table.rowCount() - 1, 2, joinButton)
            joinButton.clicked.connect(lambda ch, num=self.teachers_table.rowCount() - 1:
                                       self._change_teacher_from_table(num))

    def _update_shedule(self):
        self._update_monday_table()
        self._update_tuesday_table()
        self._update_wednesday_table()
        self._update_thursday_table()
        self._update_friday_table()
        self._update_saturday_table()


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
