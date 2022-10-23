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

    def get_user_class_by_id(self, user_id):
        db_request = self.cursor.execute("SELECT class FROM users WHERE user_id = ?", (user_id,))
        return db_request.fetchone()[0]

    def add_user(self, user_name, user_id, user_class=None):
        self.cursor.execute("INSERT INTO users (user_id, class,name) VALUES (?, ?, ?)",
                            (user_id, user_class, user_name))
        return self.connection.commit()

    def set_user_class(self, user_id, user_class):
        self.cursor.execute("UPDATE users SET class = ? WHERE user_id = ?", (user_class, user_id))
        return self.connection.commit()

    def set_user_name(self, user_id, user_name):
        self.cursor.execute("UPDATE users SET name = ? WHERE user_id = ?", (user_name, user_id))
        return self.connection.commit()

    def _close_db(self):
        self.connection.close()
