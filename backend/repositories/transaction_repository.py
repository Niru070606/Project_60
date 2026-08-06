from database import db


def flush():
    db.session.flush()


def commit():
    db.session.commit()


def rollback():
    db.session.rollback()