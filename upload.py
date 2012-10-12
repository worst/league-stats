import os
from datetime import datetime


class Uploader():

    UPLOAD_FOLDER = 'static/replays'
    ALLOWED_EXTENSIONS = set(['lrf'])

    def __init__(self, app):
        self.app = app
        app.config['UPLOAD_FOLDER'] = self.UPLOAD_FOLDER

    def allowed_file(self, filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1] in self.ALLOWED_EXTENSIONS

    def upload_file(self, file):
            if file and self.allowed_file(file.filename):
                filename = datetime.today().strftime('%Y-%m-%d %H:%m.lrf')
                self.replay_path = os.path.join(
                                       self.app.config['UPLOAD_FOLDER'],
                                       filename
                                   )
                file.save(self.replay_path)
                return True

    def get_upload_path(self):
        return self.replay_path
