from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

# First layer
@app.route('/')
def first_layer():
    return render_template('first_layer.html')

# Second layer
@app.route('/image_hub')
def second_layer():
    return render_template('second_layer.html')

# Third layer
@app.route('/image_hub/<folder_name>')
def third_layer(folder_name):
    image_folder = os.path.join('meng_images', folder_name)
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('png', 'jpg', 'jpeg', 'gif','JPG','PNG','JPEG','GIF'))]
    return render_template('third_layer.html', folder_name=folder_name, image_files=image_files)

# Display image
@app.route('/image_hub/<folder_name>/<image_name>')
def image_display(folder_name, image_name):
    image_path = os.path.join('meng_images', folder_name, image_name)
    return send_file(image_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
