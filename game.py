import turtle
import random
import math
import drawer
import writer

class Game:
    def __init__(self, mode=0, **kwargs):
        self.mode = mode
        self.seed = kwargs.get("seed",50)
        random.seed(self.seed)
        if self.mode in (0, 1):
            self.goalsNum = random.randint(3,10)

        self.width = kwargs.get("width", 300)
        self.height = kwargs.get("height", 300)
        self.screen = turtle.Screen()
        self.screen.setup(width=self.width * 2, height=self.height * 2)
        self.screen.bgcolor("black") 

        self.scale = kwargs.get("size",1)
        self.goalSize = self.width * kwargs.get("goalSize",0.025)
        self.goalLocations = []
        self.goalTurtles = []
        self.score = 0
        self.passed_goals = set()

        self.scoreKeeper = writer.Writer()


    def draw(self):
        if self.mode == 0:
            for goal in range(self.goalsNum):
                overlap = True
                attempts = 0
                while overlap:
                    x = random.randint(
                        int(self.goalSize - self.width), int(self.width - self.goalSize)
                    )
                    # Reduce the max height so it doesnt overlap the score
                    y = random.randint(
                        int(self.goalSize - self.height + 75), int(self.height - self.goalSize *2)
                    )
                    candidate = (x, y)
                    candidate_center = (x, y + self.goalSize)
                    attempts += 1

                    overlap = any(
                        math.dist(candidate_center, (old_x, old_y + self.goalSize)) < self.goalSize * 2
                        for old_x, old_y in self.goalLocations
                    )

                    if attempts >= 1000:
                        raise RuntimeError("Could not place all circles without overlap")
                self.goalLocations.append(candidate) #type: ignore
        elif self.mode == 1:
            self.create_shape(self.goalsNum)
        elif self.mode ==2:
            bottom_width = self.width * 0.5
            top_width = self.width * 0.9 
            bottom_y = -self.height * 0.15
            top_y = self.height * 0.2

            bottom_count = 5
            top_count = 7
            left_count = 3
            right_count = 3

            # Arrays just to reverse the order to make drawing look good
            bottom = []
            top = []
            right = []
            left = []

            for i in range(bottom_count):
                t = i / (bottom_count - 1)
                x = - bottom_width / 2 + t * bottom_width
                bottom.append((x, bottom_y))
            
            for i in range(right_count):
                t = i / (right_count - 1)
                x = bottom_width/2 + (self.goalSize) + i * ((top_width - bottom_width)/4 - self.goalSize)
                y = bottom_y + (self.goalSize*2) + i * ((top_y - bottom_y)/2 - self.goalSize*2)
                right.append((x,y))

            for i in range(top_count):
                t = i / (top_count - 1)
                x = - top_width / 2 + t * top_width
                top.append((x, top_y))

            for i in range(left_count):
                t = i / (left_count - 1)
                x = - bottom_width/2 - (self.goalSize) - i * ((top_width - bottom_width)/4 - self.goalSize)
                y = bottom_y + (self.goalSize*2) + i * ((top_y - bottom_y)/2 - self.goalSize*2)
                left.append((x,y))

            self.goalLocations = bottom + right + top[::-1] + left[::-1]

        else:
            self.create_shape(self.mode)
        
            

        for goal in self.goalLocations:
            goal = tuple(x * self.scale for x in goal)
            goalie = drawer.Drawer(goal)
            goalie.drawCircle(self.goalSize)
            self.goalTurtles.append(goalie)

        self.scoreKeeper.turtle.goto(-self.width + 10, self.height - 30)
        self.scoreKeeper.writeScore(self.score)
        
    def start_game(self):         
        self.screen.ontimer(self._check_collisions, 25)

    def _check_collisions(self):
        players = []
        for turtle in self.screen.turtles():
            if turtle is self.scoreKeeper.turtle:
                continue

            is_goal = False
            for goal in self.goalTurtles:
                if turtle is goal.turtle:
                    is_goal = True
                    break

            if not is_goal:
                players.append(turtle)

        for goal_index, goal in enumerate(self.goalTurtles):
            if goal_index in self.passed_goals:
                continue

            goal_x = goal.x
            goal_y = goal.y + self.goalSize
            if any(player.distance(goal_x, goal_y) <= self.goalSize + 5 for player in players):
                self.passed_goals.add(goal_index)
                self.score += 1
                self.scoreKeeper.writeScore(self.score)

        self.screen.ontimer(self._check_collisions, 25)

    def create_shape(self, sides):
        polygon_side_length = self.goalSize * 8 * self.scale
        radius = polygon_side_length / (
            2 * math.sin(math.pi / sides)
        )

        for index in range(sides):
            angle = (2 * math.pi * index / sides) - math.pi / 2
            x = radius * math.cos(angle)
            y = radius * math.sin(angle) - self.goalSize
            self.goalLocations.append((x, y))