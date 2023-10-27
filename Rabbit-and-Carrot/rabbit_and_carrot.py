import cv2
import time
import numpy as np 
from random import randint

SCORE = 0
WINDOW_HEIGHT = 480
WINDOW_WIDTH = 480
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

TIME_LIMIT = 60
start_time = time.time()

def initialize_rabbit_and_carrot(height, width):
    """
    This function initializes the rabbit and carrots in a window of given height and width
    """
    return (np.array([randint(0, height), randint(0, width)]), np.array([randint(0, height), randint(0, width)]))

def get_cursor_moves(event, x, y, flags, param):
    """
    Get cursor position over window and 
    ensure cursor inside the window borders.
    """
    global rabbit
    x = max(0, min(x, WINDOW_WIDTH - 1))
    y = max(0, min(y, WINDOW_HEIGHT - 1))
    
    rabbit = np.array([x, y])

def generate_new_carrot_position():
    """
    Generate a new carrot position with the following rules
    """
    return np.array([randint(0, WINDOW_HEIGHT), randint(0, WINDOW_WIDTH)])

def display_text(text, position, size=1):
    """
    Displays text on screen at given coordinates and font size
    """
    cv2.putText(background, text, position, cv2.FONT_HERSHEY_DUPLEX, size, BLUE, 1)

rabbit, carrot = initialize_rabbit_and_carrot(WINDOW_HEIGHT, WINDOW_WIDTH)
carrot_speed = np.array([randint(1, 5), randint(1, 5)])

background = np.zeros((WINDOW_HEIGHT, WINDOW_WIDTH, 3), dtype=np.uint8)
cv2.namedWindow("Rabbit and Carrot")
cv2.setMouseCallback("Rabbit and Carrot", get_cursor_moves)

while True:
    background.fill(0)
    carrot += carrot_speed
     
    if carrot[0] < 0 or carrot[0] > WINDOW_HEIGHT:
        carrot_speed[0] *= -1
    if carrot[1] < 0 or carrot[1] > WINDOW_WIDTH:
        carrot_speed[1] *= -1

    cv2.circle(background, tuple(carrot), 5, GREEN, -1)

    current_time = int(time.time() - start_time)
    remaining_time = max(0, TIME_LIMIT - current_time)

    display_text(f"Score: {SCORE}", (0, 26))
    display_text(f"Time: {remaining_time} s", (WINDOW_WIDTH - 150, 30))

    if remaining_time == 0:
        print(f"Game Over! Your  score:{SCORE}")
        break

    distance = np.sqrt(np.sum((rabbit - carrot) ** 2))
    if distance < 5:
        SCORE += 1
        print(f"Score: {SCORE}")
        carrot = generate_new_carrot_position()
        carrot_speed = np.array([randint(1, 5), randint(1, 5)])

    cv2.circle(background, tuple(rabbit), 5, RED, -1)
    cv2.imshow("Rabbit and Carrot", background)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()
