import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_file(file_obj, upload_folder):
    filename = secure_filename(file_obj.filename)
    save_path = os.path.join(upload_folder, filename)
    file_obj.save(save_path)
    return filename


def list_uploaded_files(upload_folder):
    return os.listdir(upload_folder)
