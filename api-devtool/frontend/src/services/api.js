import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/api";

export const analyzeAPI = async (data) => {
  const response = await axios.post(`${BASE_URL}/analyze-api`, data);
  return response.data;
};