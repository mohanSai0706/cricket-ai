from fastapi import FastAPI
from pydantic import BaseModel
from simulator import run_match_simulation
from fastapi.middleware.cors import CORSMiddleware

# ✅ FastAPI instance
app = FastAPI()

# ✅ Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class MatchState(BaseModel):
    runs_required: int
    balls_remaining: int
    wickets_left: int
    batting_rating: float
    bowling_rating: float


@app.get("/")
def home():
    return {"status": "Cricket AI Running"}


@app.post("/simulate")
def simulate(state: MatchState):

    wins = 0
    simulations = 500

    for _ in range(simulations):
        if run_match_simulation(state.dict()):
            wins += 1

    probability = round((wins / simulations) * 100, 2)

    return {
        "win_probability": probability,
        "simulations": simulations
    }