from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MongoDB connection
client = MongoClient('localhost', 27017)
db = client.db_penginapan
rooms_collection = db.rooms

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def rooms():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/rooms')
def frontend():
    # Get the selected room type from the query string
    room_type = request.args.get('room_type')
    
    # If a room type is provided, filter by that type; otherwise, get all rooms
    if room_type:
        # Ensure case-insensitive matching (e.g., 'single', 'Single', 'SINGLE' will all work)
        rooms = list(rooms_collection.find({'type': {'$regex': f'^{room_type}$', '$options': 'i'}}))
    else:
        rooms = list(rooms_collection.find())

    return render_template('rooms.html', rooms=rooms)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect('/admin')
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect('/login')

    if request.method == 'POST':
        room_id = request.form.get('id')
        name = request.form['name']
        description = request.form['description']
        detail = request.form['detail']
        room_type = request.form['type']
        price = request.form['price']

        # Handle file upload
        photo = request.files['photo']
        photo_path = None
        if photo and photo.filename != '':
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
            photo.save(photo_path)

        if room_id:  # Update existing room
            update_data = {
                'name': name,
                'description': description,
                'detail': detail,
                'type': room_type,
                'price': price
            }
            if photo_path:
                update_data['photo'] = photo_path

            rooms_collection.update_one({'_id': ObjectId(room_id)}, {'$set': update_data})
        else:  # Add new room
            new_room = {
                'name': name,
                'description': description,
                'detail': detail,
                'type': room_type,
                'price': price,
                'photo': photo_path
            }
            rooms_collection.insert_one(new_room)

        return redirect('/admin')

    edit_id = request.args.get('edit_id')
    room_to_edit = None
    if edit_id:
        room_to_edit = rooms_collection.find_one({'_id': ObjectId(edit_id)})

    rooms = list(rooms_collection.find())
    
    return render_template('backend.html', rooms=rooms, room_to_edit=room_to_edit)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Hapus status login dari sesi
    return redirect('/login')  # Arahkan kembali ke halaman login

@app.route('/delete/<room_id>')
def delete_room(room_id):
    if not session.get('logged_in'):
        return redirect('/login')

    rooms_collection.delete_one({'_id': ObjectId(room_id)})
    return redirect('/admin')

if __name__ == '__main__':
    app.run(debug=True)