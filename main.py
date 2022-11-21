import os.path
import os
#os.system("pip.bat")
#import easyocr
import pytesseract
import PIL
from PIL import Image
#import Pillow
#import cv2
from pdf2image import convert_from_path



#pytesseract.pytesseract.tesseract_cmd = r"X:\neir\neir\ocr_exe\tesseract.exe"

#   функция для распознавания текста на изображении
def teseract_recognition(path_img):
    return pytesseract.image_to_string(Image.open(path_img), lang='eng', config=r'--oem 3 --psm 6')

#   путь к файлу
#def easyocr_recognition(path_img):
#    return easyocr.Reader(["ru"]).readtext(path_img, detail=0, paragraph=True, text_threshold=0.8)

#   функция сохранения текста в файл
def save_text(text, name):
    with open(f'{name}.txt', 'w', encoding='utf-8') as file:
        str(file.write)
        file.write(text)
    print(f'[+] Распознанный текст сохранен в файл: "{name}.txt"')
    main()
    return


#   функция main
def main():
    path_img = input('\n[+] Введите путь к картинке\n - Для выхода введите x\n   >>> ')
    if path_img == "x":
        exit(0)
    if not os.path.exists(path_img):
        print('[+] Картинки не существует')

    user_change = input('\n[+] Выберите библиотеку для распознавания текста:\n   [1] Tesseract OCR\n   '
                        '[2] EasyOCR\n   [3] Выход\n   >>> ')
    if user_change == "1":
        save_text(teseract_recognition(path_img), os.path.split(path_img)[1].split(".")[0])
    elif user_change == '2':
        #save_text(easyocr_recognition(path_img), os.path.split(path_img)[1].split(".")[0])
        print("я не работаю")
    elif user_change == "3":
        exit(0)
    else:
        print('[+] Неопознанный ввод. Повторите все сначала')
        main()

if __name__ == "__main__":
    main()





#mask_img = cv2.imread("images/1.jpg")
#print(mask_img)

