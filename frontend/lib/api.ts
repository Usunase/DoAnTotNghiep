import { getStoredToken } from "./auth";
import type { AnalyzeRequest, AnalyzeResponse } from "./types";

const API_BASE =
  typeof window !== "undefined"
    ? ""
    : process.env.SHIELD_API_URL || "http://127.0.0.1:8000";

export async function analyzeNews(
  payload: AnalyzeRequest
): Promise<AnalyzeResponse> {
  const headers: Record<string, string> = { "Content-Type": "application/json" };
  const token = getStoredToken();
  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  const res = await fetch(`${API_BASE}/api/analyze`, {
    method: "POST",
    headers,
    body: JSON.stringify(payload),
  });

  const data = (await res.json()) as AnalyzeResponse;
  if (!res.ok) {
    return {
      status: "error",
      message: data.message || "Không thể kết nối máy chủ phân tích.",
    };
  }
  return data;
}

export const RESULT_STORAGE_KEY = "shieldai_last_result";
