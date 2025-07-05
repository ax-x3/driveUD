# driveUD BETA

## Lane assist/self-driving designed for the Ultimate Driving game series.

This program is VERY simple and KINDA works. I've always wanted to make a self-driving script for UD, but I've since learned firsthand how hard that is.

This Python code scans portions of your screen, looking for lane markings in a range of weather conditions. It then calculates the optimal (not really optimal; I'm just using some magic constants here) PWM steering force to apply to correct for lane drift.

There is a 95% chance that this program will not work for you (sorry). This is caused by even the slightest differences in vehicle stats, screen resolution, computer, client, weather, etc. But if for some reason you really wanna see this crash and burn, here's what you'll need to do:

1. Install Python and the pyautogui package, then enable screen capture and keypress permissions.
2. Clone the driveUD repository to your computer.
3. In UD, drive onto a long road with no intersections and look straight down.
4. Run the Python code and quickly switch back to the Roblox window before the one-second countdown is up.
5. Slowly accelerate and maintain 30 to 50 MPH. You can use the Y key to turn on cruise control.
6. Watch as nothing works.

If all things go according to plan, you should see your car automatically steer to follow the curve of the road before losing control and crashing into the nearest tree. This is not an AFK grinding macro. It's a steering assist for low speeds.

> [!IMPORTANT]
> Since the creator of Ultimate Driving has decided to permanently end the game's development, this software may never leave beta. Sorry, but the game is dead.

> [!NOTE]
> I have another project called calculateUD, a web tool for easily calculating your progress to a credit or rank goal. Due to the release of bonuses, the calculator is not 100% accurate, but it will produce a good estimate.
