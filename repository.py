import sqlite3


class TGBotUserRepository:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def is_user_exists(self, user_id):
        db_request = self.cursor.execute("SELECT name FROM users WHERE user_id = ?", (user_id,))
        return bool(len(db_request.fetchall()))

    def get_user_name_by_id(self, user_id):
        db_request = self.cursor.execute("SELECT name FROM users WHERE user_id = ?", (user_id,))
        return db_request.fetchone()[0]

    def get_user_class_id_by_id(self, user_id):
        db_request = self.cursor.execute("SELECT class_id FROM users WHERE user_id = ?", (user_id,))
        return db_request.fetchone()[0]

    def get_user_school_id_by_id(self, user_id):
        db_request = self.cursor.execute("SELECT school_id FROM users WHERE user_id = ?", (user_id,))
        return db_request.fetchone()[0]

    def add_user(self, user_name, user_id, user_class_id=None, user_school_id=None):
        self.cursor.execute("INSERT INTO users (user_id, name, class_id,  school_id) VALUES (?, ?, ?, ?)",
                            (user_id, user_name, user_class_id, user_school_id))
        return self.connection.commit()

    def set_user_school(self, user_id, user_school_id):
        self.cursor.execute("UPDATE users SET school_id = ? WHERE user_id = ?", (user_school_id, user_id))
        return self.connection.commit()

    def set_user_class(self, user_id, user_class_id):
        self.cursor.execute("UPDATE users SET class_id = ? WHERE user_id = ?", (user_class_id, user_id))
        return self.connection.commit()

    def set_user_name(self, user_id, user_name):
        self.cursor.execute("UPDATE users SET name = ? WHERE user_id = ?", (user_name, user_id))
        return self.connection.commit()

    def _close_db(self):
        self.connection.close()
