#!usr/bin/python3
"""__int__ method for models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
