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

class SimulationResponse(BaseModel):
    win_probability: float
    simulations: int
    required_run_rate: float
    pressure_index: float

@app.get("/")
def home():
    return {"status": "Cricket AI Running"}


@app.post("/simulate", response_model=SimulationResponse)
def simulate(state: MatchState):

    wins = 0
    simulations = 500

    for _ in range(simulations):
        if run_match_simulation(state.dict()):
            wins += 1

    probability = round((wins / simulations) * 100, 2)

    # New Metrics
    required_run_rate = round(
        state.runs_required / (state.balls_remaining / 6), 2
    )

    pressure_index = round(
        (required_run_rate / state.batting_rating) * 10, 2
    )

    return {
        "win_probability": probability,
        "simulations": simulations,
        "required_run_rate": required_run_rate,
        "pressure_index": pressure_index
    }