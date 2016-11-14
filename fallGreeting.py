# Name: Eduardo R Abreu
# fallGreeting.py
#
# Problem: This program will output the total time of a CD.
#
# Certification of Authenticity:  
# I certify that this lab is entirely my own work.

from graphics import *
from time import *
from random import *

def fallGreeting():
    #Varibles and Constants.
    scrnWidth = 400
    scrnHeight = 500
    pumpkCenter = Point((scrnWidth / 2), (scrnHeight / 2))
    pumpkRadius = 50
    
    #Create window.
    win = GraphWin("Fall Greeting Card", scrnWidth, scrnHeight)
    win.setBackground(color_rgb(25, 0, 51))

    #Display greeting.
    greeting = "Happy Fall!"
    textAnchor = Point((scrnWidth / 2), (scrnHeight / 10))
    greetText = Text(textAnchor, greeting)
    greetText.setSize(18)
    greetText.setTextColor("white")
    greetText.draw(win)

    #Create the background.
    grass = Rectangle(Point(scrnWidth, 245), Point(0, scrnHeight))
    grass.setFill(color_rgb(0, 51, 0))
    grass.draw(win)

    #Map and draw the pumpkin.
    pumpkPoint = [
        Point(192, 140),
        Point(182, 139),
        Point(166, 145),
        Point(158, 141),
        Point(139, 150),
        Point(132, 155),
        Point(110, 164),
        Point(100, 174),
        Point(92, 188),
        Point(84, 204),
        Point(79, 227),
        Point(81, 246),
        Point(82, 264),
        Point(88, 282),
        Point(94, 298),
        Point(105, 314),
        Point(117, 329),
        Point(126, 334),
        Point(132, 335),
        Point(138, 340),
        Point(150, 348),
        Point(164, 350),
        Point(170, 350),
        Point(180, 353),
        Point(191, 348),
        Point(194, 347),
        Point(206, 351),
        Point(217, 352),
        Point(229, 348),
        Point(234, 343),
        Point(241, 347),
        Point(254, 343),
        Point(260, 338),
        Point(261, 335),
        Point(270, 338),
        Point(279, 333),
        Point(285, 329),
        Point(291, 319),
        Point(293, 314),
        Point(304, 305),
        Point(311, 291),
        Point(315, 266),
        Point(318, 247),
        Point(318, 227),
        Point(315, 204),
        Point(303, 183),
        Point(292, 168),
        Point(279, 158),
        Point(267, 155),
        Point(262, 155),
        Point(255, 148),
        Point(243, 147),
        Point(237, 147),
        Point(230, 147),
        Point(224, 140),
        Point(215, 139),
        Point(192, 140)
        ]
    pumpkin = Polygon(pumpkPoint)
    pumpkin.setFill("orangered")
    pumpkin.draw(win)

    #Map and draw leftEye.
    leftEyePoint = [
        Point(132, 211),
        Point(133, 218),
        Point(136, 225),
        Point(136, 230),
        Point(136, 234),
        Point(142, 235),
        Point(153, 236),
        Point(164, 236),
        Point(169, 236),
        Point(171, 235),
        Point(162, 231),
        Point(144, 217),
        Point(132, 211)
        ]

    leftEye = Polygon(leftEyePoint)
    leftEye.setFill("black")
    leftEye.setOutline("orangered")
    leftEye.draw(win)

    #Map and draw rightEye.
    rightEyePoint = [
        Point(226, 238),
        Point(236, 233),
        Point(246, 227),
        Point(252, 223),
        Point(260, 218),
        Point(266, 213),
        Point(270, 213),
        Point(270, 219),
        Point(269, 229),
        Point(267, 231),
        Point(263, 233),
        Point(226, 238)
        ]

    rightEye = Polygon(rightEyePoint)
    rightEye.setFill("black")
    rightEye.setOutline("orangered")
    rightEye.draw(win)

    #Map and draw nose.
    nosePoint = [
        Point(184, 241),
        Point(195, 243),
        Point(203, 242),
        Point(212, 241),
        Point(213, 241),
        Point(214, 241),
        Point(212, 246),
        Point(204, 250),
        Point(196, 252),
        Point(190, 248),
        Point(184, 241)
        ]

    nose = Polygon(nosePoint)
    nose.setFill("black")
    nose.setOutline("orangered")
    nose.draw(win)

    #Map and draw stem.
    stemPoint = [
        Point(180, 164),
        Point(183, 161),
        Point(186, 161),
        Point(188, 151),
        Point(193, 143),
        Point(193, 138),
        Point(198, 135),
        Point(201, 129),
        Point(206, 129),
        Point(210, 129),
        Point(214, 136),
        Point(216, 133),
        Point(215, 138),
        Point(213, 147),
        Point(211, 148),
        Point(211, 154),
        Point(213, 158),
        Point(216, 160),
        Point(220, 163),
        Point(223, 162),
        Point(223, 164),
        Point(219, 166),
        Point(213, 169),
        Point(204, 170),
        Point(197, 171),
        Point(191, 171),
        Point(187, 169),
        Point(179, 166),
        Point(180, 164)
        ]
    stem = Polygon(stemPoint)
    stem.setFill("brown")
    stem.setOutline("brown")
    stem.draw(win)

    #Map and draw the mouth.
    smilePoint = [
        Point(103, 207),
        Point(100, 216),
        Point(97, 234),
        Point(94, 257),
        Point(98, 274),
        Point(108, 292),
        Point(117, 306),
        Point(126, 314),
        Point(130, 317),
        Point(130, 312),
        Point(132, 302),
        Point(137, 310),
        Point(143, 316),
        Point(154, 323),
        Point(159, 326),
        Point(158, 313),
        Point(159, 307),
        Point(163, 302),
        Point(171, 319),
        Point(174, 314),
        Point(176, 307),
        Point(184, 318),
        Point(188, 325),
        Point(193, 332),
        Point(194, 335),
        Point(201, 331),
        Point(205, 326),
        Point(209, 318),
        Point(213, 307),
        Point(214, 323),
        Point(227, 312),
        Point(231, 326),
        Point(233, 324),
        Point(241, 312),
        Point(248, 303),
        Point(250, 300),
        Point(259, 322),
        Point(266, 312),
        Point(273, 301),
        Point(276, 290),
        Point(277, 284),
        Point(284, 293),
        Point(293, 273),
        Point(288, 300),
        Point(291, 301),
        Point(300, 286),
        Point(305, 270),
        Point(305, 252),
        Point(303, 231),
        Point(299, 218),
        Point(294, 210),
        Point(296, 225),
        Point(295, 236),
        Point(290, 244),
        Point(287, 254),
        Point(284, 255),
        Point(277, 251),
        Point(274, 252),
        Point(276, 267),
        Point(269, 279),
        Point(264, 286),
        Point(262, 289),
        Point(259, 293),
        Point(252, 263),
        Point(233, 285),
        Point(222, 271),
        Point(219, 268),
        Point(214, 275),
        Point(209, 287),
        Point(208, 290),
        Point(189, 269),
        Point(190, 284),
        Point(191, 295),
        Point(192, 298),
        Point(167, 267),
        Point(162, 282),
        Point(159, 285),
        Point(139, 256),
        Point(131, 279),
        Point(122, 264),
        Point(119, 234),
        Point(112, 251),
        Point(103, 231),
        Point(100, 216)
        ]
    smile = Polygon(smilePoint)
    smile.setFill("black")
    smile.setOutline("orangered")
    smile.draw(win)

    #Moon draw.
    blue = 255
    green = 255
    moonCenter = Point(14, 22)
    moon = Circle(moonCenter, 60)
    moon.setFill(color_rgb(255, blue, green))
    moon.draw(win)

    #Craters draw.
    blue2 = 235
    green2 = 235
    
    craCenter = Point(45, 24)
    crater = Circle(craCenter, 5)
    crater.setFill(color_rgb(255, blue2, green2))
    crater.draw(win)

    blue3 = 225
    green3 = 225
    craCenter2 = Point(17, 49)
    crater2 = Circle(craCenter2, 15)
    crater2.setFill(color_rgb(255, blue3, green3))
    crater2.draw(win)
  
    sleep(2)
    greetText.undraw()

    #For loop to flicker flame.
    for i in range(10):
        sleep(.35)
        star = Point(randint(5, scrnWidth), randint(5, scrnHeight - 400))
        star2 = Point(randint(5, scrnWidth), randint(5, scrnHeight - 400))
        star3 = Point(randint(5, scrnWidth), randint(5, scrnHeight - 400))
        star4 = Point(randint(5, scrnWidth), randint(5, scrnHeight - 400))
        star5 = Point(randint(5, scrnWidth), randint(5, scrnHeight - 400))
        star6 = Point(randint(5, scrnWidth), randint(5, scrnHeight - 400))
        star7 = Point(randint(5, scrnWidth), randint(5, scrnHeight - 400))
        star8 = Point(randint(5, scrnWidth), randint(5, scrnHeight - 400))
        star9 = Point(randint(5, scrnWidth), randint(5, scrnHeight - 400))
        star10 = Point(randint(5, scrnWidth), randint(5, scrnHeight - 400))
        star.setFill("white")
        star2.setFill("white")
        star3.setFill("white")
        star4.setFill("white")
        star5.setFill("white")
        star6.setFill("white")
        star7.setFill("white")
        star8.setFill("white")
        star9.setFill("white")
        star10.setFill("white")
        star.draw(win)
        star2.draw(win)
        star3.draw(win)
        star4.draw(win)
        star5.draw(win)
        star6.draw(win)
        star7.draw(win)
        star8.draw(win)
        star9.draw(win)
        star10.draw(win)
        
        blue = blue - 20
        green = green - 20
        moon.undraw()
        moon.setFill(color_rgb(255, blue, green))
        moon.draw(win)

        blue2 = blue - 20
        green2 = green - 20
        crater.undraw()
        crater.setFill(color_rgb(255, blue2, green2))
        crater.draw(win)

        blue3 = blue - 20
        green3 = green - 20
        crater2.undraw()
        crater2.setFill(color_rgb(255, blue3, green3))
        crater2.draw(win)
        
        nose.setFill("yellow")
        leftEye.setFill("yellow")
        rightEye.setFill("yellow")
        smile.setFill("yellow")
        sleep(.35)
        nose.setFill("black")
        leftEye.setFill("black")
        rightEye.setFill("black")
        smile.setFill("black")
        star.undraw()
        star2.undraw()
        star3.undraw()
        star4.undraw()
        star5.undraw()
        star6.undraw()
        star7.undraw()
        star8.undraw()
        star9.undraw()
        star10.undraw()

    nose.setFill("yellow")
    leftEye.setFill("yellow")
    rightEye.setFill("yellow")
    smile.setFill("yellow")
    greetText.draw(win)
  


    #Click to close.
    click = win.getMouse()
    win.close()
    



fallGreeting()
