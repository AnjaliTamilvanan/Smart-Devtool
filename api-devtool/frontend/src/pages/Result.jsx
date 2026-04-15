import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import { analyzeAPI } from "../services/api";
import Loader from "../components/Loader";
import "../styles/main.css";

function Result() {
  const location = useLocation();
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    analyzeAPI(location.state)
      .then((res) => {
        setResult(res);
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  if (loading) return <Loader />;

  return (
    <div className="container">
      <h2>📊 Extracted API Info</h2>
      <pre className="box">
        {typeof result.structured_data === "string"
          ? result.structured_data.replace(/```json|```/g, "")
          : JSON.stringify(result.structured_data, null, 2)}
      </pre>

      <h2>📦 SDK Suggestion</h2>
      <pre className="box">
        {typeof result.structured_data === "string"
          ? result.structured_data
          : result.structured_data?.sdk_suggestion || "No SDK suggestion available"}
      </pre>

      <h2>💻 Generated Code</h2>
      <pre className="box">{result.generated_code}</pre>
    </div>
  );
}

export default Result;