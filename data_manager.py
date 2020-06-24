import bcrypt
from psycopg2.extras import RealDictCursor
import os

import database_common


# @database_common.connection_handler
# def get_data_by_table(cursor: RealDictCursor, table: str) -> list:
#     """
#     :return:
#     all data from boards table
#     """
#     query = """
#         SELECT *
#         FROM %(table)s
#         """
#     args = {'table': table}
#     cursor.execute(query, args)
#     return cursor.fetchall()


@database_common.connection_handler
def get_data_boards(cursor: RealDictCursor) -> list:
    """
    :return:
    all data from boards table
    """
    query = """
        SELECT *
        FROM boards
        """
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_data_cards(cursor: RealDictCursor) -> list:
    """
    :return:
    all data from cards table
    """
    query = """
        SELECT *
        FROM cards
        """
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_data_statuses(cursor: RealDictCursor) -> list:
    """
    :return:
    all data from statuses table
    """
    query = """
        SELECT *
        FROM statuses
        """
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def write_boards(cursor: RealDictCursor, title: str) -> list:

    query = """
            INSERT INTO boards (title)
            VALUES (%(title)s)
            """
    args = {'title': title}
    cursor.execute(query, args)
    return query


@database_common.connection_handler
def write_statuses(cursor: RealDictCursor, title: str) -> list:

    query = """
            INSERT INTO statuses (title)
            VALUES (%(title)s)
            """
    args = {'title': title}
    cursor.execute(query, args)
    return ""


@database_common.connection_handler
def write_cards(cursor: RealDictCursor, boards_id: int, title: str, statuses_id: int, ordered: int) -> list:

    query = """
            INSERT INTO cards (boards_id, title, statuses_id, ordered)
            VALUES (%(boards_id)s, %(title)s, %(statuses_id)s, %(ordered)s)
            """
    args = {'boards_id': boards_id, 'title': title, 'statuses_id': statuses_id, 'ordered': ordered}
    cursor.execute(query, args)
    return ""


@database_common.connection_handler
def update_boards(cursor: RealDictCursor, id: int, title: str) -> list:

    query = """
            UPDATE boards
            SET title = %(title)s
            WHERE id = %(id)s
            """
    args = {'id': id, 'title': title}
    cursor.execute(query, args)
    updated_query = f"""
            SELECT *
            FROM boards
            WHERE id = %(id)s
            """
    args = {'id': id}
    cursor.execute(updated_query, args)
    return cursor.fetchall()


@database_common.connection_handler
def update_statuses(cursor: RealDictCursor, id: int, title: str) -> list:

    query = """
            UPDATE statuses
            SET title = %(title)s
            WHERE id = %(id)s
            """
    args = {'id': id, 'title': title}
    cursor.execute(query, args)
    updated_query = f"""
            SELECT *
            FROM statuses
            WHERE id = %(id)s
            """
    args = {'id': id}
    cursor.execute(updated_query, args)
    return cursor.fetchall()


@database_common.connection_handler
def update_cards(cursor: RealDictCursor, id: int, boards_id: int, title: str, statuses_id: int, ordered: int) -> list:

    query = """
            UPDATE cards
            SET boards_id = %(boards_id)s, title = %(title)s, statuses_id = %(statuses_id)s, ordered = %(ordered)s
            WHERE id = %(id)s
            """
    args = {'id': id, 'boards_id': boards_id, 'title': title, 'statuses_id': statuses_id, 'ordered': ordered}
    cursor.execute(query, args)
    updated_query = f"""
            SELECT *
            FROM cards
            WHERE id = %(id)s
            """
    args = {'id': id}
    cursor.execute(updated_query, args)
    return cursor.fetchall()


#
# @database_common.connection_handler
# def username_exists(cursor: RealDictCursor, username: str):
#     query = """
#         SELECT *
#         FROM users
#         WHERE username = %(username)s;
#          """
#     args = {'username': username}
#     cursor.execute(query, args)
#     return cursor.fetchone()
#
#
# @database_common.connection_handler
# def register_user(cursor: RealDictCursor, username: str, text_password: str, submission_time: int):
#     """
#     Checks for valid username.
#     If username is valid, inserts the new user into the database
#     """
#     if username_exists(username):
#         return False
#     query = """
#     INSERT INTO users (username,password,submission_time,count_questions,count_answers,count_comments,reputation)
#     VALUES (%(username)s,%(password)s,%(submission_time)s,0,0,0,0)
#            """
#     args = {"username": username, "password": encrypt_password(text_password), "submission_time": submission_time}
#     return cursor.execute(query, args)
#
#
# def encrypt_password(password):
#     # By using bcrypt, the salt is saved into the hash itself
#     hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
#     return hashed_pass.decode('utf-8')
#
#
# def verify_password(text_password, hashed_pass):
#     return bcrypt.checkpw(text_password.encode('utf-8'), hashed_pass.encode('utf-8'))
#