import os
from flask import Flask, jsonify, render_template, request
from utils import *
import cv2
import random

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
PNG = '.png'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/encrypt_image')
def encrypt_image():
    return render_template('encrypt-image.html')


@app.route('/decrypt_image')
def decrypt_image():
    return render_template('decrypt-image.html')


def random_string(length=10):
    result = ''
    for i in range(length):
        result += chr(random.randint(97, 122))
    return result


@app.route('/lsb_image_encrypt', methods=['POST'])
def lsb_image_encrypt():
    target = os.path.join(APP_ROOT, 'static')
    if not os.path.isdir(target):
        os.mkdir(target)

    file = request.files.getlist('file')[0]
    file_name, file_extension = os.path.splitext(file.filename)
    final_file_name = file_name + random_string() + PNG
    initial_file_destination = os.path.join(target, final_file_name)
    final_file_destination = os.path.join(target, final_file_name)
    final_path = os.path.join(target, final_file_name)

    # saving the obtained file to load image matrix
    file.save(initial_file_destination)
    I = cv2.imread(initial_file_destination)
    os.remove(initial_file_destination)

    # saving this image as png and loading png matrix
    cv2.imwrite(final_file_destination, I)
    I = cv2.imread(final_file_destination)

    # extracting message and creating encrypted image
    message = request.form['message']
    J = lsb_encrypt(I, message)

    # saving encrypted image in the static directory
    cv2.imwrite(final_path, J)

    return render_template('encrypted-image.html', encrypted_image=final_file_name, original_image=final_file_name)


@app.route('/lsb_image_decrypt', methods=['POST'])
def lsb_image_decrypt():
    file = request.files.getlist('file')[0]
    file_name = file.filename
    target = os.path.join(APP_ROOT, 'image')
    destination = os.path.join(target, file_name)

    if not os.path.isdir(target):
        os.mkdir(target)

    file.save(destination)
    I = cv2.imread(destination)
    return render_template('decrypted-image.html', image_name=file_name, message=lsb_decrypt(I))


if __name__ == '__main__':
    app.run()
