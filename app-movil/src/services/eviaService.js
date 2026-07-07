// src/services/eviaService.js
import { API_BASE_URL, DEMO_EMAIL } from "../config/api";

async function readResponse(response) {
  const body = await response.json();
  if (!response.ok || body.ok === false) {
    throw new Error(body.message || "Error en la API");
  }
  return body;
}

export async function loginUser(email = DEMO_EMAIL) {
  const response = await fetch(`${API_BASE_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email }),
  });
  const body = await readResponse(response);
  return body.data;
}

export async function getProducts() {
  const { apiKey } = await loginUser();
  const response = await fetch(`${API_BASE_URL}/products`, {
    headers: { "x-api-key": apiKey },
  });
  const body = await readResponse(response);
  return body.data;
}