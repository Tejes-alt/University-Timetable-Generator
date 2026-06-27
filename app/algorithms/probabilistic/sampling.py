import random


class Sampling:

    @staticmethod
    def monte_carlo_sampling(
        probabilities,
        iterations=1000
    ):

        success = 0

        for _ in range(iterations):

            value = random.choice(
                probabilities
            )

            if value > 0.5:
                success += 1

        return {
            "estimated_probability":
                success / iterations,
            "samples": iterations
        }