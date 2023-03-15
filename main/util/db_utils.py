from main import db


class DBUtils:
    @staticmethod
    def save_to_db(obj):
        db.session.add(obj)
        db.session.commit()
