from flask import Flask, render_template, url_for, request, jsonify, make_response
from util import json_response

import data_handler
import data_manager as dm

app = Flask(__name__)


@app.route("/")
def index():
    """
    This is a one-pager which shows all the boards and cards
    """
    return render_template('index.html')


@app.route("/get-boards")
@json_response
def get_boards():
    """
    All the boards
    """
    return data_handler.get_boards()


@app.route("/get-cards")
@json_response
def get_cards():
    """
    All the boards
    """
    return data_handler.get_cards()


@app.route("/get-statuses")
@json_response
def get_statuses():
    """
    All the boards
    """
    return data_handler.get_statuses()


@app.route("/get-cards/<int:board_id>")
@json_response
def get_cards_for_board(board_id: int):
    """
    All cards that belongs to a board
    :param board_id: id of the parent board
    """
    return data_handler.get_cards_for_board(board_id)


@app.route("/new-board/<board_name>", methods=['GET', 'POST'])
@json_response
def create_new_board(board_name: str):
    """
    Create new board
    """
    try:
        new_board = request.get_json()
        response = make_response(jsonify({"message": "JSON received"}), 200)
        dm.write_boards(new_board['name'])
        board_id = dm.get_last_board_id()
        card_name = 'new card'
        status_id = '0'
        order = '0'
        dm.write_cards(board_id['max'], card_name, status_id, order)
        return board_name
    except:
        return "An error has occurred"


@app.route("/new-card/<board_id>", methods=['GET', 'POST'])
@json_response
def create_new_card(board_id):
    """
    Create new card
    """
    try:
        board_id_obj = request.get_json()
        response = make_response(jsonify({"message": "JSON received"}), 200)
        target_board_id = board_id_obj['name']
        card_name = 'new card'
        status_id = str(0)
        max_order = dm.get_cards_order(target_board_id)
        order = str(int(max_order['max']) + 1)
        dm.write_cards(target_board_id, card_name, status_id, order)
        return "create new card successful"
    except:
        return "An error has occurred"


@app.route("/delete-card/<object>", methods=['GET', 'POST'])
@json_response
def delete_card(object):
    try:
        data = request.get_json()['name']# de transformat in dict
        data = data[1:-1]
        response = make_response(jsonify({"message": "JSON received"}), 200)
        data_list = data.split(',')
        board_id = data_list[0]
        status_id = data_list[1]
        card_order = data_list[2]
        dm.delete_card(board_id, status_id, card_order)
        return "create new card successful"
    except:
        return "An error has occurred"



def main():
    app.run(debug=True,
            port=5001)

    # Serving the favicon
    with app.app_context():
        app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()
