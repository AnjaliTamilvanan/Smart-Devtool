import { useNavigate } from "react-router-dom";
import InputForm from "../components/InputForm";
import "../styles/main.css";

function Home() {
  const navigate = useNavigate();

  const handleSubmit = (data) => {
    navigate("/result", { state: data });
  };

  return (
    <div className="container">
      <h1>🚀 Smart API DevTool</h1>
      <InputForm onSubmit={handleSubmit} />
    </div>
  );
}

export default Home;