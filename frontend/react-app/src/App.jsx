import React, { useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const [formData, setFormData] = useState({
    hscMarks: "", mhcetMarks: "", jeeMarks: "", preferredBranch: "", preferredState: ""
  });
  const [prediction, setPrediction] = useState([]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post("http://localhost:5000/api/predict", formData);
    setPrediction(response.data.prediction);
  };

  return (
    <div className="container mt-5">
      <h2>Option Form Prediction</h2>
      <form onSubmit={handleSubmit}>
        <input name="hscMarks" type="number" placeholder="HSC Marks" onChange={handleChange} required />
        <input name="mhcetMarks" type="number" placeholder="MhCET Marks" onChange={handleChange} required />
        <input name="jeeMarks" type="number" placeholder="JEE Marks" onChange={handleChange} required />
        <input name="preferredBranch" type="text" placeholder="Preferred Branch" onChange={handleChange} required />
        <input name="preferredState" type="text" placeholder="Preferred State" onChange={handleChange} required />
        <button type="submit">Predict</button>
      </form>
      <h3>Predicted Colleges</h3>
      <ul>
        {prediction.map((college, index) => (
          <li key={index}>{college.College} - {college.Branch}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
