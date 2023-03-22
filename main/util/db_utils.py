from main import db


class DBUtils:
    @staticmethod
    def save_to_db(obj, multiple: bool=False):
        if multiple:
            db.session.add_all(obj)
        else:
            db.session.add(obj)
        db.session.commit()
