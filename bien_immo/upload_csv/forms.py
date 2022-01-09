from django import forms
from os.path import join
"""
from bien_immo.settings import BASE_DIR
path = str(BASE_DIR)

def content_file_name(instance, filename):
    return '/'.join(['upload', instance.user.username, filename])
"""
class UploadFileForm(forms.Form):
    file = forms.FileField()