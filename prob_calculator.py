import copy
import random

# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        # Initialize the Hat object with a list of colored balls based on the provided counts.
        self.contents = []
        for color, count in kwargs.items():
            for _ in range(count):
                self.contents.append(color)

    def draw(self, num):
        # Draw a specified number of balls randomly from the hat.
        # If the requested number is greater than the total number of balls, return all the balls.
        if num > len(self.contents):
            return self.contents
        else:
            drawn_balls = random.sample(self.contents, num)
            for ball in drawn_balls:
                self.contents.remove(ball)  # Remove the drawn balls from the hat.
            return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    # Run a specified number of experiments.
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)  # Create a deep copy of the hat for each experiment.
        drawn_balls = hat_copy.draw(num_balls_drawn)
        print(drawn_balls)

        color_counts = {}
        # Count the occurrences of each color in the drawn balls.
        for color in drawn_balls:
            color_counts[color] = color_counts.get(color, 0) + 1

        experiment_success = True
        # Check if the drawn balls match the expected counts for each color.
        for color, count in expected_balls.items():
            try:
                if color_counts[color] < count:
                    experiment_success = False
                    break
            except KeyError:
                # Handle the case where the expected color is not present in the drawn balls.
                experiment_success = False
                break

        if experiment_success:
            success += 1

    return success / num_experiments
