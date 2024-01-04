from flask import Flask, render_template, redirect, request , jsonify
from func import format_message, load_messages, save_messages


app = Flask(__name__)


@app.route('/')
def get_static():
    return render_template('index.html')


@app.route('/<room>')
def get_static_html(room):
    return render_template('index.html')


@app.route('/api/chat/<room>', methods=['GET','POST'])
def get_full_chat(room):
    if request.method == 'GET':
        messages = load_messages()
        room_found = messages.get(room)
        messages = load_messages()

        if room_found is None:
            return jsonify({"message": "Room not found"}), 404

        return '\n'.join(room_found)


    else:
        username = request.form.get('username')
        message = request.form.get('msg')

        if not username or not message:
            return jsonify({"message": "Username and message are required"}), 400

        messages = load_messages()

        if room not in messages:
            messages[room] = []

        new_message = format_message(username, message)
        messages[room].append(new_message)

        save_messages(messages)

        return jsonify({'status': 'success'}), 201






if __name__ == '__main__':
    app.run(debug=True)
