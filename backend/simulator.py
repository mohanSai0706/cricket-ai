import random

BALL_OUTCOMES = [
    ("dot", 0),
    ("single", 1),
    ("double", 2),
    ("four", 4),
    ("six", 6),
    ("wicket", -1),
]


def simulate_ball(batting_strength, bowling_strength):

    wicket_prob = bowling_strength / (batting_strength + bowling_strength)

    r = random.random()

    if r < wicket_prob * 0.15:
        return "wicket", -1

    return random.choice(BALL_OUTCOMES[:-1])


# ✅ THIS FUNCTION MUST EXIST
def run_match_simulation(state):

    runs_needed = state["runs_required"]
    balls = state["balls_remaining"]
    wickets = state["wickets_left"]

    batting = state["batting_rating"]
    bowling = state["bowling_rating"]

    while balls > 0 and wickets > 0 and runs_needed > 0:

        outcome, runs = simulate_ball(batting, bowling)

        if outcome == "wicket":
            wickets -= 1
        else:
            runs_needed -= runs

        balls -= 1

    return runs_needed <= 0