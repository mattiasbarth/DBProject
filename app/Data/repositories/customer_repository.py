from Data.db import session


def save_changes(_):
    session.commit()