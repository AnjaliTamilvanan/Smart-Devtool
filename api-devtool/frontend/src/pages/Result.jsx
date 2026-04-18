import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import { analyzeAPI } from "../services/api";
import Loader from "../components/Loader";
import "../styles/main.css";

function Result() {
  const location = useLocation();
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(true);

  // ✅ NEW: copy state
  const [copiedField, setCopiedField] = useState("");

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

  // ✅ NEW: copy handler with tooltip
  const handleCopy = (text, field) => {
    navigator.clipboard.writeText(text);
    setCopiedField(field);

    setTimeout(() => {
      setCopiedField("");
    }, 1500);
  };

  if (loading) return <Loader />;
  if (!result) return <h2>No data received</h2>;

  const cleanedData =
    typeof result.structured_data === "string"
      ? result.structured_data.replace(/```json|```/g, "")
      : result.structured_data;

  let parsedData = null;
  try {
    parsedData =
      typeof cleanedData === "string"
        ? JSON.parse(cleanedData)
        : cleanedData;
  } catch (err) {
    console.error("JSON parse error:", err);
    parsedData = null;
  }

  let sdkSuggestion = "No SDK suggestion available";

  if (parsedData) {
    sdkSuggestion = parsedData.sdk_suggestion || "Use REST API";
  }

  return (
    <div className="container">
      <h2>Extracted API Info</h2>
      <pre className="box">
        {typeof cleanedData === "string"
          ? cleanedData
          : JSON.stringify(cleanedData, null, 2)}
      </pre>

      <h2>Endpoints</h2>

      {Array.isArray(parsedData?.endpoints) ? (
        parsedData.endpoints.map((ep, i) => (
          <div key={i} className="box" style={{ marginBottom: "10px" }}>
            <p><b>{ep.method}</b> - {ep.url}</p>
            <p>{ep.description}</p>
          </div>
        ))
      ) : (
        <p>No multiple endpoints found</p>
      )}

      {/* ✅ SAMPLE URL */}
      <h2>Sample API URL</h2>
      <div className="code-container">
        <button
          className="copy-icon"
          onClick={() => handleCopy(result.sample_url, "url")}
        >
          {copiedField === "url" ? "✓" : "⧉"}
        </button>

        {copiedField === "url" && (
          <span className="copy-tooltip">Copied!</span>
        )}

        <pre className="box">{result.sample_url}</pre>
      </div>

      <h2>SDK Suggestion</h2>
      <pre className="box">{sdkSuggestion}</pre>

      {/* ✅ GENERATED CODE */}
      <h2>Ready-to-Use API Code</h2>
      <div className="code-container">
        <button
          className="copy-icon"
          onClick={() => handleCopy(result.generated_code, "code")}
        >
          {copiedField === "code" ? "✓" : "⧉"}
        </button>

        {copiedField === "code" && (
          <span className="copy-tooltip">Copied!</span>
        )}

        <pre className="box">{result.generated_code}</pre>
      </div>
    </div>
  );
}

export default Result;