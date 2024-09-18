import yaml
import glob
import pickle
import os
import socket

def get_file_path(file_path):
    # Bypassing hostname check and returning the original file path
    cwd = os.getcwd()  # Keeping the current working directory
    print(f"Using file path: {file_path}")
    return os.path.join(cwd, file_path)  # Join the provided file path with the current working directory

def load_yaml(file_path):
    file_path = get_file_path(file_path)
    files = glob.glob(file_path, recursive=True)
    print(file_path)
    assert(len(files) == 1)
    cfg = yaml.safe_load(open(files[0], 'r'))
    return cfg

def load_pickle(file_path):
    file_path = get_file_path(file_path)
    files = glob.glob(file_path, recursive=True)
    assert(len(files) == 1)
    data = pickle.load(open(files[0], 'rb'))
    return data
