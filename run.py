from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QDialog,
    QListView,
    QInputDialog,
)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QModelIndex, QDate, QStringListModel
import menu
import database as db
import helpers
import sys
from datetime import date
from gui.ui_main_window import Ui_MainWindow
from gui.create_modify_task_ui import Ui_Dialog as TaskDialog
from gui.edit_categories_ui import Ui_Dialog as CategoryDialog
from gui.change_skin_ui import Ui_Dialog as ChangeSkinDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_table_view_tasks()
        self.current_skin = db.DaoTasks.current_gui_skin
        self.path_skin = "gui/qss/" + self.current_skin + ".qss"
        self.load_style_sheet(self.path_skin)
        self.there_are_changes = False
        self.actionSave.setEnabled(False)

        # Signals
        self.pushButtonCreate.clicked.connect(self.create_task)
        self.pushButtonModify.clicked.connect(self.modify_task)
        self.pushButtonDelete.clicked.connect(self.delete_task)
        self.tableViewTasks.doubleClicked.connect(self.modify_task)
        self.checkBoxCompletedTasks.clicked.connect(self.load_table_view_tasks)
        self.actionSave.triggered.connect(self.save_state)
        self.actionChangeSkin.triggered.connect(self.change_skin)

        # TODO: Add change skin function (change skin action)

        # TODO: Add STATUS column in table view (COMPLETED, WIP, QUEUEUE, DUE)

        # TODO: Add Show Manual Action

        # TODO: Add About Action

    def change_skin(self):
        change_skin_dialog = DialogChangeSkin(self)
        change_skin_dialog.show()

    def edit_categories(self):
        pass

    def save_state(self):
        helpers.save_state()
        self.there_are_changes = False
        self.show_success_message(self, "All changes have been saved")
        self.actionSave.setEnabled(False)

    def closeEvent(self, event):
        if self.there_are_changes:
            if (
                self.show_confirmation_message(
                    self, "Confirmation", "Do you want to save changes before exit?"
                )
                == QMessageBox.Yes
            ):
                helpers.save_state()
        event.accept()

    def show_error_message(self, parent, message):
        QMessageBox.warning(parent, "Error", message)

    def show_success_message(self, parent, message):
        QMessageBox.information(parent, "Success", message)

    def show_confirmation_message(self, parent, title, message):
        msg_box = QMessageBox(parent)
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        return msg_box.exec()

    def load_style_sheet(self, file):
        path = helpers.get_abs_path(file)
        try:
            with open(path) as styles:
                self.setStyleSheet(styles.read())
        except:
            self.show_error_message(self, "Couldn't load the stylesheet")

    def load_table_view_tasks(self):
        show_completed = self.checkBoxCompletedTasks.isChecked()
        model = QStandardItemModel()
        model.setColumnCount(8)
        headers = [
            "ID",
            "NAME",
            "DESCRIPTION",
            "START DATE",
            "END DATE",
            "CATEGORY",
            "%",
            "OWNER",
        ]
        model.setHorizontalHeaderLabels(headers)
        if not show_completed:
            list_of_tasks = [
                task for task in db.DaoTasks.list_of_tasks if task.percentage != "100 %"]
        else:
            list_of_tasks = db.DaoTasks.list_of_tasks
        for row, task in enumerate(list_of_tasks):
            model.setItem(row, 0, QStandardItem(str(task.id)))
            model.setItem(row, 1, QStandardItem(
                helpers.get_substring(task.name, 30)))
            model.setItem(
                row, 2, QStandardItem(
                    helpers.get_substring(task.description, 70))
            )
            model.setItem(row, 3, QStandardItem(task.start_date))
            model.setItem(row, 4, QStandardItem(task.end_date))
            model.setItem(row, 5, QStandardItem(task.category))
            model.setItem(row, 6, QStandardItem(task.percentage))
            model.setItem(row, 7, QStandardItem(task.owner))

        # Center content of every cell
        for row in range(model.rowCount()):
            for column in range(model.columnCount()):
                item = model.item(row, column)
                if item:
                    item.setTextAlignment(Qt.AlignCenter)

        self.tableViewTasks.setModel(model)

        # Set columns size
        table_width = self.tableViewTasks.viewport().width()
        column_width_percentages = [5, 15, 27, 13, 13, 12, 5, 10]
        column_widths = [
            table_width * percentage / 100 for percentage in column_width_percentages
        ]
        for column, width in enumerate(column_widths):
            self.tableViewTasks.setColumnWidth(column, width)

    def create_task(self):
        dialog_create = DialogTask(self)
        dialog_create.setWindowTitle("Create a new task")
        dialog_create.dateEditStartDate.setDate(date.today())
        dialog_create.dateEditEndDate.setDate(date.today())
        dialog_create.save_mode = "create"
        dialog_create.lineEditName.setPlaceholderText("Enter 3-50 characters")
        dialog_create.textEditDescription.setPlaceholderText(
            "Enter 0-250 characters")
        dialog_create.comboBoxCategory.setCurrentIndex(0)
        dialog_create.comboBoxPercentage.setCurrentIndex(0)
        dialog_create.lineEditOwner.setPlaceholderText("Enter 3-30 characters")
        dialog_create.show()

    def modify_task(self):
        selected_row = self.get_selected_row()
        if selected_row is not None:
            id_task = int(self.get_cell_value(selected_row, 0))
            task = db.DaoTasks.search(id_task)
            dialog_modify = DialogTask(self)
            dialog_modify.setWindowTitle("Updating task")
            start_date = self.convert_to_qdate_format(task.start_date)
            end_date = self.convert_to_qdate_format(task.end_date)
            dialog_modify.dateEditStartDate.setDate(start_date)
            dialog_modify.dateEditEndDate.setDate(end_date)
            dialog_modify.save_mode = "modify"
            dialog_modify.lineEditName.setText(task.name)
            dialog_modify.textEditDescription.setText(task.description)
            dialog_modify.comboBoxCategory.setCurrentText(task.category)
            dialog_modify.comboBoxPercentage.setCurrentText(task.percentage)
            dialog_modify.lineEditOwner.setText(task.owner)
            dialog_modify.show()

    def delete_task(self):
        selected_row = self.get_selected_row()
        if selected_row is not None:
            if (
                self.show_confirmation_message(
                    self, "Confirmation", "Are you sure to delete the selected task?"
                )
                == QMessageBox.Yes
            ):
                id_task = int(self.get_cell_value(selected_row, 0))
                db.DaoTasks.delete(id_task)
                self.show_success_message(self, "Task deleted successfully!")
                self.load_table_view_tasks()
                self.there_are_changes = True
                self.actionSave.setEnabled(True)

    def get_selected_row(self):
        model = self.tableViewTasks.model()
        if model.rowCount():
            selection_model = self.tableViewTasks.selectionModel()
            index = selection_model.selectedIndexes()

            if index:
                return index[0].row()
            else:
                self.show_error_message(self, "First select a row")
                return None
        else:
            self.show_error_message(self, "There are not tasks")
            return None

    def get_cell_value(self, row, column):
        model = self.tableViewTasks.model()
        index = model.index(row, column, QModelIndex())
        return model.data(index)

    def convert_to_qdate_format(self, date_string):
        date_format = "dd-MM-yyyy"
        return QDate.fromString(date_string, date_format)


class DialogTask(QDialog, TaskDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.save_mode = ""
        self.load_categories_on_combobox()

        # Signals
        self.pushButtonCancel.clicked.connect(self.cancel_dialog)
        self.pushButtonSave.clicked.connect(self.save_task)
        self.pushButtonManageCategories.clicked.connect(self.manage_categories)

    def load_categories_on_combobox(self):
        self.comboBoxCategory.clear()
        self.comboBoxCategory.addItems(db.DaoTasks.list_of_categories)

    def cancel_dialog(self):
        self.close()

    def save_task(self):
        name = self.lineEditName.text()
        description = self.textEditDescription.toPlainText()
        start_date = self.dateEditStartDate.text()
        end_date = self.dateEditEndDate.text()
        category = self.comboBoxCategory.currentText()
        percentage = self.comboBoxPercentage.currentText()
        owner = self.lineEditOwner.text()

        if self.validate_data(name, description, start_date, end_date, owner):
            if self.save_mode == "create":
                self.create_task(
                    name, description, start_date, end_date, category, percentage, owner
                )
            elif self.save_mode == "modify":
                self.modify_task(
                    name, description, start_date, end_date, category, percentage, owner
                )

    def create_task(
        self, name, description, start_date, end_date, category, percentage, owner
    ):
        db.DaoTasks.add(
            name, description, start_date, end_date, category, percentage, owner
        )
        window.show_success_message(self, "Task created successfully!")
        window.load_table_view_tasks()
        window.there_are_changes = True
        window.actionSave.setEnabled(True)

    def modify_task(
        self, name, description, start_date, end_date, category, percentage, owner
    ):
        selected_row = window.get_selected_row()
        id_task = int(window.get_cell_value(selected_row, 0))
        db.DaoTasks.update(
            id_task,
            name,
            description,
            start_date,
            end_date,
            category,
            percentage,
            owner,
        )
        window.show_success_message(self, "Task updated successfully...")
        window.load_table_view_tasks()
        window.there_are_changes = True
        window.actionSave.setEnabled(True)
        self.close()

    def validate_data(self, name, description, start_date, end_date, owner):
        if not (helpers.validate_text_length(name, 3, 50)):
            window.show_error_message(self, "Name has an incorrect format")
            return False
        if not (helpers.validate_text_length(description, 0, 250)):
            window.show_error_message(
                self, "Description has more than 250 characters")
            return False
        if not helpers.validate_date_format(start_date):
            window.show_error_message(
                self, "Start Date has an incorrect format")
            return False
        if not helpers.validate_date_format(end_date):
            window.show_error_message(self, "End Date has an incorrect format")
        if not helpers.validate_correct_range_date(start_date, end_date):
            window.show_error_message(
                self, "End Date must be greater or equal than Start Date"
            )
            return False
        if not (helpers.validate_text_length(owner, 3, 30)):
            window.show_error_message(self, "Owner has an incorrect format")
            return False
        return True

    def manage_categories(self):
        dialog = DialogCategory(self)
        dialog.show()


class DialogCategory(QDialog, CategoryDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Manage categories")
        self.setModal(True)
        self.load_categories_on_list_view()
        self.dialog = parent

        # Signals
        self.pushButtonDeleteCategory.clicked.connect(self.delete_category)
        self.pushButtonModifyCategory.clicked.connect(self.modify_category)
        self.pushButtonCancel.clicked.connect(self.cancel_dialog)
        self.lineEditCategoryName.returnPressed.connect(self.save_category)
        self.pushButtonCreateCategory.clicked.connect(self.save_category)

    def load_categories_on_list_view(self):
        model = QStringListModel()
        model.setStringList(db.DaoTasks.list_of_categories)
        self.listViewCategories.setModel(model)
        self.listViewCategories.setCurrentIndex(model.index(0, 0))

    def delete_category(self):
        if len(db.DaoTasks.list_of_categories):
            if (
                window.show_confirmation_message(
                    self, "Confirmation", "Are you sure to delete the selected category?"
                )
                == QMessageBox.Yes
            ):
                index = self.listViewCategories.currentIndex()
                if index.isValid():
                    category = self.listViewCategories.model().data(index)
                    db.DaoTasks.list_of_categories.remove(category)
                    window.show_success_message(
                        self, "Category deleted successfully!")

                    self.load_categories_on_list_view()
                    window.there_are_changes = True
                    window.actionSave.setEnabled(True)
                    self.dialog.load_categories_on_combobox()
                    self.dialog.update()

        else:
            window.show_error_message(self, "There are not categories")

    def modify_category(self):
        selected_row = self.listViewCategories.currentIndex()
        if selected_row.isValid():
            new_text, result = QInputDialog.getText(
                self, "Modify category", "Enter new name")
            if result:
                new_text = new_text.strip()
                if helpers.validate_text_length(new_text, 3, 25):
                    index = self.listViewCategories.currentIndex()
                    category = self.listViewCategories.model().data(index)
                    db.DaoTasks.list_of_categories[
                        db.DaoTasks.list_of_categories.index(category)
                    ] = new_text
                    self.load_categories_on_list_view()
                    window.there_are_changes = True
                    window.actionSave.setEnabled(True)
                    self.dialog.load_categories_on_combobox()
                    self.dialog.update()
                else:
                    window.show_error_message(
                        self, "Category name cannot be empty or greater than 25 characters")

    def cancel_dialog(self):
        self.close()

    def save_category(self):
        new_category = self.lineEditCategoryName.text()
        if helpers.validate_text_length(new_category, 3, 25):
            if new_category not in db.DaoTasks.list_of_categories:
                db.DaoTasks.list_of_categories.append(new_category)
                window.show_success_message(
                    self, "Category created successfully!")
                self.load_categories_on_list_view()
                window.there_are_changes = True
                window.actionSave.setEnabled(True)
                self.dialog.load_categories_on_combobox()
                self.dialog.update()
            else:
                window.show_error_message(self, "Category already exists")
        else:
            window.show_error_message(
                self, "Category name cannot be empty or greater than 25 characters")


class DialogChangeSkin(QDialog, ChangeSkinDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Change Skin")
        self.setModal(True)
        self.load_list_of_skins()
        self.temp_skin = window.current_skin
        self.skin_changed = False
        self.accept_change = False

        # Signals
        self.pushButtonApply.clicked.connect(self.apply_skin)
        self.pushButtonCancel.clicked.connect(self.cancel_dialog)
        self.pushButtonAccept.clicked.connect(self.accept)

    def load_list_of_skins(self):
        list_of_files = helpers.get_qss_files("gui/qss/", "qss")
        list_of_names = [name.split(".")[0] for name in list_of_files]
        model = QStringListModel()
        model.setStringList(list_of_names)
        self.listViewSkins.setModel(model)
        self.listViewSkins.setCurrentIndex(model.index(0, 0))

    def apply_skin(self):
        selected_row = self.listViewSkins.currentIndex()
        if selected_row.isValid():
            new_skin = self.listViewSkins.model().data(selected_row)
            if new_skin != self.temp_skin:
                self.temp_skin = new_skin
                self.skin_changed = True
                new_skin = "gui/qss/" + new_skin + ".qss"
                window.load_style_sheet(new_skin)
                window.update()
            else:
                window.show_error_message(
                    self, "The selected skin is the same as the current one")
        else:
            window.show_error_message(self, "There are not skins")

    def cancel_dialog(self):
        self.close()

    def accept(self):
        window.current_skin = self.temp_skin
        db.DaoTasks.current_gui_skin = window.current_skin
        window.there_are_changes = True
        self.accept_change = True
        self.close()

    def closeEvent(self, event):
        if not self.accept_change:
            if self.skin_changed:
                if (
                    window.show_confirmation_message(
                        self, "Confirmation", "Do you want to close and cancel skin changes?"
                    )
                    == QMessageBox.Yes
                ):
                    skin = "gui/qss/" + window.current_skin + ".qss"
                    window.load_style_sheet(skin)
                    window.update()
                    self.skin_changed = False
                else:
                    event.ignore()
        event.accept()


if __name__ == "__main__":
    helpers.load_state()
    # menu.start()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
