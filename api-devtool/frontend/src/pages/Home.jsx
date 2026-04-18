import { useNavigate } from "react-router-dom";
import { useState } from "react";
import InputForm from "../components/InputForm";
import "../styles/main.css";

function Home() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [step, setStep] = useState("");

  const handleSubmit = async (data) => {
    setLoading(true);

    setStep("Scraping API docs...");
    await new Promise((r) => setTimeout(r, 600));

    setStep("Parsing with AI...");
    await new Promise((r) => setTimeout(r, 600));

    setStep("Generating code...");
    await new Promise((r) => setTimeout(r, 600));

    setLoading(false);
    navigate("/result", { state: data });
  };

  return (
    <div className="container">
      <h1>Smart API DevTool</h1>
      <InputForm onSubmit={handleSubmit} />

      {loading && (
        <div className="loader-container">
          <p className="loading-text">{step}</p>
        </div>
      )}
    </div>
  );
}

export default Home;