import { useState } from "react";

function InputForm({ onSubmit }) {
  const [url, setUrl] = useState("");
  const [useCase, setUseCase] = useState("");
  const [language, setLanguage] = useState("python");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ url, use_case: useCase, language });
  };

  return (
    <form onSubmit={handleSubmit} className="form">
      <h2>Enter API Details</h2>

      <input
        type="text"
        placeholder="API Documentation URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />

      <input
        type="text"
        placeholder="Use Case (e.g. get weather data)"
        value={useCase}
        onChange={(e) => setUseCase(e.target.value)}
      />

      <select value={language} onChange={(e) => setLanguage(e.target.value)}>
        <option value="python">Python</option>
        <option value="javascript">JavaScript</option>
      </select>

      <button type="submit">Analyze API</button>
    </form>
  );
}

export default InputForm;