import pyautogui
import time

pyautogui.PAUSE = 0

screenWidth, screenHeight = pyautogui.size()
scanHeight = 320
step = 20
lMargin = 800
tick = 0.05
scanWidth = screenWidth - lMargin
scanSteps = int(scanWidth / step)
targetOffset = 250
deadzone = 5

def main():
    index = 0
    time.sleep(0.5)
    # resetCamera()
    difference = 0
    ticksSinceYellow = 0
    while True:
        ticksSinceYellow += 1
        offset = targetOffset
        im = pyautogui.screenshot(region=(lMargin, scanHeight, screenWidth, 1))
        for i in range(scanSteps):
            px = im.getpixel((i * step, 0))
            if pixelIsYellow(px):
                ticksSinceYellow = 1
                offset = (i * step) - scanWidth / 2
                break

        lastDifference = difference
        difference = targetOffset - offset
        differenceRate = (difference - lastDifference) / ticksSinceYellow
        correction = max(min(0 - (0.6 * difference + 2 * differenceRate), 800), -800)
        if correction > 0:
            correction = correction ** 0.5
        else:
            correction = 0 - ((0 - correction) ** 0.5)


        print(index)
        index += 1
        print("detected " + str(ticksSinceYellow) + " ticks ago")
        print("difference: " + str(difference))
        print("correction: " + str(correction))
        
        if abs(correction) > deadzone:
            applyCorrection(correction)
            
        time.sleep(tick)


def resetCamera():
    for i in range(10):
        pyautogui.scroll(10)
    time.sleep(1.5)
    for i in range(2):
        pyautogui.scroll(-5)
    time.sleep(1.5)
    pyautogui.mouseDown(button='right')
    pyautogui.moveRel(0, -1000)
    time.sleep(0.1)
    pyautogui.moveRel(0, 10)
    pyautogui.mouseUp(button='right')
    time.sleep(1)

def pixelIsYellow(px):
    if (px[0] + px[1] > 480 and px[0] > (px[2] * 2)) or (px[0] > 40 and px[0] > px[2] * 3 and px[0] > px[1] + 30):
        return True
    else:
        return False

def applyCorrection(correction):
    dampening = 200
    if correction < 0:
        pyautogui.keyDown('a')
        time.sleep(abs(correction / dampening))
        pyautogui.keyUp('a')
    else:
        pyautogui.keyDown('d')
        time.sleep(abs(correction / dampening))
        pyautogui.keyUp('d')

if __name__ == "__main__":
    main()
