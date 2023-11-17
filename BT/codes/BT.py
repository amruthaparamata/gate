import random

def simulate_probability(num_simulations=100000):
    favorable_outcomes = 0

    for _ in range(num_simulations):
        first_draw = random.randint(1, 10)
        second_draw = random.randint(1, 10)

        if second_draw > first_draw:
            favorable_outcomes += 1

    overall_probability = favorable_outcomes / num_simulations
    return round(overall_probability, 2)

result = simulate_probability()
print(f"Simulated probability that the number on the second draw is greater than the number on the first draw is: {result}")
