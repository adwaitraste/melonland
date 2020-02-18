# Global config file


class GlobalSettings():
    def __init__(self):
        self.title = "MelonLand"
        self.noOfLvls = 5
        self.xFactor = 80
        self.yFactor = 80
        self.rows = 10
        self.cols = 10
        self.screenWidth = (self.cols+1) * self.xFactor
        self.screenHeight = (self.rows+2) * self.yFactor
        self.font = "./Fonts/zorque.ttf"
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.p1Image = "./Images/Player1.png"
        self.p2Image = "./Images/Player2.png"
        self.groundImage = "./Images/Ground.png"
        self.waterImage = "./Images/Water.png"
        self.voidImage = "./Images/Void.png"
        self.knifeRightImage = "./Images/KnifeRight.png"
        self.fobsScore = 5
        self.mobsScore = 10
        self.completeScore = 25
        self.timePenalty = 2
        self.dyingPenalty = 50
        self.startScreenMsg1 = self.title
        self.startScreenMsg2 = "Press Space to play"
        self.startScreenMsg3 = "Use arrow keys to move"
        self.startScreenMsg4 = "Don't hit the knives or fall into the void"
        self.startScreenMsg5 = "Every second spent deducts 2 points"
        self.endScreenMsg1 = "Game Over"
        self.endScreenMsg2 = "Press Space to exit"
        self.collidedMsg = "You crashed into an obstacle!"
        self.successMsg = "You successfully reached the end!"
        self.switchPlayerMsg = "Switch Players"
