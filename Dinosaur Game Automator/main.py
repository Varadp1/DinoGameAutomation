import pyautogui
import PIL
import time

#Colors in Dino game :- (83, 83, 83)
#Rectangle1 = (300, 600, 350, 700)
#Rectangle2 = (300, 500, 350, 600)

time.sleep(3)

while True:
    image = pyautogui.screenshot()
    image.save("image.jpg")

    GrayImg = PIL.Image.open('image.jpg').convert('L')
    GrayImg.save("image.jpg")
    

    for i in range(320,370):
        for j in range(680, 700):
            if GrayImg.load()[i, j] <= 83:
                pyautogui.press("up")
                break
        else:
            continue  # only executed if the inner loop did NOT break
        break
    
    else:
        for i in range(320,370):
            for j in range(550, 650):
                if GrayImg.load()[i, j] <= 83:
                    pyautogui.keyDown("down")
                    break
            else:
                continue
            time.sleep(0.5)
            pyautogui.keyUp("down")
              # only executed if the inner loop did NOT break
            break
            

# image = pyautogui.screenshot()
# image.save("image.jpg")

# GrayImg = PIL.Image.open('image.jpg').convert('L')
# GrayImg.save("image.jpg")
# PIL.ImageDraw.Draw(image).rectangle(((320, 700), (370, 720)), fill="black")   
# PIL.ImageDraw.Draw(image).rectangle(((320, 550), (370, 650)), fill="gray")
# # PIL.ImageDraw.Draw(image).rectangle(((320, 370), (550, 650)), fill="gray")
# image.show()        