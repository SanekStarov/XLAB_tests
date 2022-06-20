import os
from params import path_to_waiting_screenshot
from params import path_to_acceptance_screenshot

def remove_png():
    if os.path.isfile(path_to_waiting_screenshot):
        os.remove(path_to_waiting_screenshot)
        print("Waiting.png успешно удалено")
        if os.path.isfile(path_to_acceptance_screenshot):
            os.remove(path_to_acceptance_screenshot)
            print("Acceptance.png успешно удалено")
        else:
            print("Файла не существует!")
    else:
        print("Файла не существует!")

if __name__=='__main__':
    remove_png()