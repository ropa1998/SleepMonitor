from python.Flask import db_manager


def check_report():
    db_manager.get_sleeping_range()