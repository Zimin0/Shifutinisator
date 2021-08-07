from struct import calcsize
import ctypes
from time import sleep 
from os import  remove, getlogin, listdir
from pygame import mixer 
from tkinter import Tk, Frame, Button
from shutil import copyfile
from pathlib import Path

### This program can be compiled into one file to make it easier to joke with your friends :)

def search_copy(working_dir):
    """ searching for jpeg image of desktop wallpaper """
    USER = getlogin()
    PATH = "C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\CachedFiles".format(USER)

    files = listdir(path=PATH)
    for file in files:
        if file.startswith('CachedImage') and file.endswith('.jpg'):
            path = file

    new_file_dir = working_dir + "\\old_pic.jpg"
    path_to_pic =  PATH + '\\' + path
    copyfile(path_to_pic,new_file_dir)
    return new_file_dir 

def remover(song_name,pic_path, old_pic_path):
    """ delete other files """ 
    remove(song_name)
    remove(pic_path)

def _play_music(song_name):
    """ Setting for music"""
    mixer.init()
    mixer.music.load(song_name)
    mixer.music.set_volume(0.3)
    mixer.music.play()
    sleep(0) # delay before output on display

def window_2_septemb(song_name,pic_path):
    """ display the window with 3rd September """
    def dest():
        nonlocal root, song_name, pic_path
        root.destroy()
        #remover(song_name,pic_path)

    root = Tk()
    root.geometry("400x400")
    root.config(bg = 'orange')
    root.title('3 Сентября')
    app = Frame(root)
    bt1 = Button(root,text = 'Вернуться во 2 сентября?', command = dest, font = 'Broadway')
    bt1.grid(padx = 90, pady = 160)
    _play_music(song_name)
    root.mainloop()

def making_paths(work_dir):
    music_file = work_dir + '\\3sentyabrya.mp3'
    pic_file = work_dir + '\\shufutin.jpg'
    return music_file, pic_file

def is_64bit_windows():
    """Check if 64 bit Windows OS"""
    return calcsize('P') * 8 == 64

def changeBG(path):
    """Change background depending on bit size"""
    if is_64bit_windows():
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)
    else:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path, 3)

SPI_SETDESKWALLPAPER = 20


# main part

# get the directory name
working_dir = cript_dir = str(Path(__file__).parent) 

# file handling
song_name, pic_path = making_paths(working_dir)

# seaching and copying background image of user's desktop 
new_file_dir_pic = search_copy(working_dir)

# changing the background image to the shufut's image
changeBG(pic_path)

# display tkinter and play music
window_2_septemb(song_name,pic_path)

# change bg back
changeBG(new_file_dir_pic) 

<<<<<<< HEAD

# remover(song_name,pic_path, new_file_dir_pic)
=======
# подчищаем оснтавшиеся файлы
# remover(song_name,pic_path, new_file_dir_pic)
>>>>>>> 5287fee3c83c406bc71d2e1c99154d53aad6239d
