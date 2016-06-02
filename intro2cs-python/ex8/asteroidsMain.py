from torpedo import *
from asteroid import *
from spaceship import *
from gameMaster import *
import math

SMALL_ASTEROID = 1
MED_ASTEROID = 2
BIG_ASTEROID = 3
LOW_POINTS = 20
MID_POINTS = 50
MOST_POINTS = 100
ANGLE_MULTI = 2
HALF_CIRCLE = 180


class GameRunner:
    def __init__(self, amnt=3):

        self.game = GameMaster()
        self.screenMaxX = self.game.get_screen_max_x()
        self.screenMaxY = self.game.get_screen_max_y()
        self.screenMinX = self.game.get_screen_min_x()
        self.screenMinY = self.game.get_screen_min_y()
        shipStartX = (self.screenMaxX - self.screenMinX) / 2 + self.screenMinX
        shipStartY = (self.screenMaxY - self.screenMinY) / 2 + self.screenMinY
        self.game.set_initial_ship_cords(shipStartX, shipStartY)
        self.game.add_initial_astroids(amnt)

    def run(self):
        self._do_loop()
        self.game.start_game()

    def _do_loop(self):
        self.game.update_screen()
        self.game_loop()
        # Set the timer to go off again
        self.game.ontimer(self._do_loop, 5)

    def game_loop(self):
        """
        this method is a one turn of events in the game.
        this method will check the status of all objects in the game and will
        then determine what will happen in the next round - the ship movement,
        the asteroids movement and explosions, the torpedo movement, the score,
        and check if the game should end or not
        """
        # the method which controls the ships movement
        self.move_ship(self.game.get_ship())
        # move each asteroid and check collision with the ship
        for asteroid in self.game.get_asteroids():
            self.move_object(asteroid)
            if self.game.intersect(self.game.get_ship(), asteroid):
                self.ship_collision(asteroid)
        # fire a torpedo
        if self.game.is_fire_pressed():
            self.move_torpedo(self.game.get_ship())
        # keep track on the torpedo shots
        for torpedo in self.game.get_torpedos():
            self.move_object(torpedo)  # move this torpedo
            dead_torpedo = []  # initiate the dead torpedo list
            # add the torpedo to the dead list if the life time of it is over
            if torpedo.get_life_span() <= 0:
                dead_torpedo.append(torpedo)
            # check for collision between torpedo and asteroids
            for asteroid in self.game.get_asteroids():
                if self.game.intersect(torpedo, asteroid):
                    self.asteroid_explode(asteroid, torpedo)
                    dead_torpedo.append(torpedo)
            # remove all the dead torpedo from the game
            self.game.remove_torpedos(dead_torpedo)
        # check if the game should end this turn
        self.check_end_game()

    def delta_axis_x(self):
        """
        :return: the difference between the max and min coordination of
        the "X" axis
        """
        return self.screenMaxX - self.screenMinX

    def delta_axis_y(self):
        """
        :return: the difference between the max and min coordination of
        the "Y" axis
        """
        return self.game.get_screen_max_y() - self.game.get_screen_min_y()

    def move_object(self, object_o):
        """
        this method changes the given object location according to its current
        speed and previous location. it uses the delta methods and move method
        :param object_o: the object to move
        """
        object_o.move((object_o.get_speed_x() + object_o.get_x_cor() -
                       self.screenMinX) % self.delta_axis_x() + self.screenMinX,
                      (object_o.get_speed_y() + object_o.get_y_cor() -
                       self.screenMinY) % self.delta_axis_y() + self.screenMinY)

    def move_ship(self, ship):
        """
        this method will change the ships angle and speed on both axis
        :param ship: the ship is the object to move
        """
        # if the right key was pressed turn the ship to the right by decreasing
        # its angle
        if self.game.is_right_pressed():
            ship.decrease_angle()
        # if the left key was pressed turn the ship to the left by increasing
        # its angle
        elif self.game.is_left_pressed():
            ship.increase_angle()
        # if the up key was pressed change the ship speed on both axis,
        # by adding to the old speed for each axis
        elif self.game.is_up_pressed():
            ship.set_speed_x(ship.get_speed_x() + math.cos
            (_convert_degrees_to_radians(ship.get_angle())))
            ship.set_speed_y(ship.get_speed_y() + math.sin
            (_convert_degrees_to_radians(ship.get_angle())))
        # move the ship on the game board by the new settings
        self.move_object(ship)

    def move_torpedo(self, ship):
        """
        this method adds a new torpedo to the game by taking the ships
        parameters - location, speed and angle
        :param ship: the ship object, for its current state in the game
        """

        self.game.add_torpedo(ship.get_x_cor(), ship.get_y_cor(),
                              ship.get_speed_x() + ANGLE_MULTI * math.cos \
                                  (_convert_degrees_to_radians(
                                      ship.get_angle())),
                              ship.get_speed_y() + ANGLE_MULTI * math.sin \
                                  (_convert_degrees_to_radians(
                                      ship.get_angle())),
                              ship.get_angle())

    def asteroid_explode(self, asteroid, torpedo):
        """
        this method is in charge of the asteroids splitting and the score of
        splitting them
        :param asteroid: the asteroid object
        :param torpedo: the torpedo object
        """
        # the new speed of the asteroid on "X" axis after splitting
        __new_x_speed = self.new_asteroid_speed(torpedo.get_speed_x(),
                                                asteroid.get_speed_x(),
                                                asteroid.get_speed_x(),
                                                asteroid.get_speed_y())
        # the new speed of the asteroid on "Y" axis after splitting
        __new_y_speed = self.new_asteroid_speed(torpedo.get_speed_y(),
                                                asteroid.get_speed_y(),
                                                asteroid.get_speed_x(),
                                                asteroid.get_speed_y())

        # if the asteroid is the smallest size
        if asteroid.get_size() == SMALL_ASTEROID:
            self.game.add_to_score(MOST_POINTS)  # add to the score 100 points
            self.game.remove_asteroid(asteroid)  # remove this asteroid

        # if the asteroid is the medium size
        elif asteroid.get_size() == MED_ASTEROID:
            self.game.add_to_score(MID_POINTS)  # add to the score 50 points
            self.game.remove_asteroid(asteroid)  # remove this asteroid

            # add to the game two smallest size asteroids with new speeds of
            # the older asteroid in counter directions from each other
            self.game.add_asteroid(asteroid.get_x_cor(), asteroid.get_y_cor(),
                                   __new_x_speed, __new_y_speed, 1)
            self.game.add_asteroid(asteroid.get_x_cor(), asteroid.get_y_cor(),
                                   -__new_x_speed, -__new_y_speed, 1)
        # if the asteroid is the large size
        elif asteroid.get_size() == BIG_ASTEROID:
            self.game.add_to_score(LOW_POINTS)  # add to the score 20 points
            self.game.remove_asteroid(asteroid)  # remove this asteroid

            # add to the game two medium size asteroids with new speeds of
            # the older asteroid in counter directions from each other
            self.game.add_asteroid(asteroid.get_x_cor(), asteroid.get_y_cor(),
                                   __new_x_speed, __new_y_speed, 2)
            self.game.add_asteroid(asteroid.get_x_cor(), asteroid.get_y_cor(),
                                   -__new_x_speed, -__new_y_speed, 2)

    def new_asteroid_speed(self, torpedo_speed, current_speed, speed_x,
                           speed_y):
        """
        this method changes changes the asteroid speed with consideration of
        the torpedo speed that hit it
        :param torpedo_speed: the torpedo speed on either "X" or "Y" axis
        :param current_speed: the asteroid speed on either "X" or "Y" axis
        :param speed_x: the asteroid current x speed
        :param speed_y: the asteroid current y speed
        :return: the new asteroid speed on one axis
        """
        return (torpedo_speed + current_speed) / math.sqrt(
            speed_x ** 2 + speed_y ** 2)

    def ship_collision(self, asteroid):
        """
        this method tells if the ship collided with an asteroid and prompts
        to the user that he got hit and shows the remaining lives he has
        it also removes lives from the live lives list and the asteroid that
        hit the ship
        :param asteroid: the asteroid that hit the ship
        """
        # take on life off the lives list
        self.game.ship_down()

        # if player has more than one life left
        if self.game.get_num_lives() >= 1:
            # prompt a message letting him know he got hit
            self.game.show_message("CAPTAIN, WATCH OUT!",
                                   "Captain you just got hit!")
            self.game.remove_asteroid(asteroid)  # remove this asteroid

        # if no more lives are available - end the game
        elif self.game.get_num_lives() == 0:
            self.check_end_game()

    def check_end_game(self):
        """
        this method checks how to end the game:
        1. by blowing up all the asteroids
        2. having no more lives
        3. hitting the quit button or "q" key
        if one of these occur a message will be prompt to the user
        """
        # in case no more lives are available
        if self.game.get_num_lives() == 0:
            self.game.show_message("Too Bad",
                                   "You just crashed your last ship")
            self.game.end_game()

        # in case all asteroids were blown
        elif self.game.get_asteroids() == 0:
            self.game.show_message("Congratulations, You Won!",
                                   "You just blew up all the asteroids")
            self.game.end_game()

        # in case "q" or quit were pressed
        elif self.game.should_end():
            self.game.show_message("Exit program",
                                   "You just quit the game. oh well...")
            self.game.end_game()


def _convert_degrees_to_radians(degree):
    """
    this method converts degrees to radians
    :param degree: the value of the degree to convert
    :return: the radian form of the degree
    """
    return degree * math.pi / HALF_CIRCLE


def main():
    runner = GameRunner()
    runner.run()


if __name__ == "__main__":
    main()
