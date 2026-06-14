import { getStoredToken } from "./auth";
import type { AnalyzeResponse, HistoryListResponse } from "./types";

function authHeaders(): HeadersInit {
  const token = getStoredToken();
  const headers: HeadersInit = { "Content-Type": "application/json" };
  if (token) headers.Authorization = `Bearer ${token}`;
  return headers;
}

export async function fetchHistoryList(): Promise<HistoryListResponse> {
  const res = await fetch("/api/history", { headers: authHeaders() });
  return (await res.json()) as HistoryListResponse;
}

export async function fetchHistoryDetail(
  id: number
): Promise<AnalyzeResponse> {
  const res = await fetch(`/api/history/${id}`, { headers: authHeaders() });
  return (await res.json()) as AnalyzeResponse;
}

export async function deleteHistoryItem(id: number): Promise<{ status: string; message?: string }> {
  const res = await fetch(`/api/history/${id}`, {
    method: "DELETE",
    headers: authHeaders(),
  });
  return (await res.json()) as { status: string; message?: string };
}

export async function submitHistoryFeedback(
  historyId: number,
  isCorrect: boolean,
  comment?: string
): Promise<{ status: string; action?: string; message?: string }> {
  const res = await fetch(`/api/history/${historyId}/feedback`, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify({ is_correct: isCorrect, comment }),
  });
  return (await res.json()) as { status: string; action?: string; message?: string };
}
