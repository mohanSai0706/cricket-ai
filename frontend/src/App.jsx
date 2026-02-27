import { useState } from "react";

export default function App() {

  const [form, setForm] = useState({
    runs_required: 30,
    balls_remaining: 18,
    wickets_left: 5,
    batting_rating: 8,
    bowling_rating: 7
  });

  const [probability, setProbability] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: Number(e.target.value)
    });
  };

  const runSimulation = async () => {

    setLoading(true);

    const response = await fetch(
      "https://cricket-ai.onrender.com/simulate",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(form)
      }
    );

    const data = await response.json();

    setProbability(data.win_probability);
    setLoading(false);
  };

  return (
    <div style={styles.container}>

      <h1>🏏 CricketIQ Simulation Dashboard</h1>

      <div style={styles.card}>

        <Input label="Runs Required" name="runs_required" value={form.runs_required} onChange={handleChange}/>
        <Input label="Balls Remaining" name="balls_remaining" value={form.balls_remaining} onChange={handleChange}/>
        <Input label="Wickets Left" name="wickets_left" value={form.wickets_left} onChange={handleChange}/>
        <Input label="Batting Rating (1-10)" name="batting_rating" value={form.batting_rating} onChange={handleChange}/>
        <Input label="Bowling Rating (1-10)" name="bowling_rating" value={form.bowling_rating} onChange={handleChange}/>

        <button style={styles.button} onClick={runSimulation}>
          {loading ? "Simulating..." : "Run AI Simulation"}
        </button>

      </div>

      {probability !== null && (
        <div style={styles.result}>
          Win Probability: {probability}%
        </div>
      )}

    </div>
  );
}

/* ---------- Reusable Input ---------- */

function Input({ label, name, value, onChange }) {
  return (
    <div style={{marginBottom:15}}>
      <label>{label}</label>
      <input
        type="number"
        name={name}
        value={value}
        onChange={onChange}
        style={styles.input}
      />
    </div>
  );
}

/* ---------- Styles ---------- */

const styles = {
  container: {
    padding:40,
    fontFamily:"Arial",
    color:"white",
    background:"#0f172a",
    minHeight:"100vh"
  },
  card:{
    background:"#1e293b",
    padding:25,
    width:350,
    borderRadius:12
  },
  input:{
    width:"100%",
    padding:8,
    marginTop:5,
    borderRadius:6,
    border:"none"
  },
  button:{
    marginTop:15,
    padding:10,
    width:"100%",
    background:"#22c55e",
    border:"none",
    color:"white",
    fontWeight:"bold",
    borderRadius:8,
    cursor:"pointer"
  },
  result:{
    marginTop:30,
    fontSize:28,
    fontWeight:"bold"
  }
};