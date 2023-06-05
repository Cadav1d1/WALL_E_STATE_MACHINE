from Robot import Robot
from RobotUI import RobotUI

from tkinter import messagebox

if __name__ == "__main__":
    robot = Robot()
    app = RobotUI(robot)
    app.mainloop()
