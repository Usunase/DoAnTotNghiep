import type { AuthResponse, LoginRequest, RegisterRequest, User } from "./types";

const TOKEN_KEY = "shieldai_token";

export function getStoredToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem(TOKEN_KEY);
}

export function setStoredToken(token: string): void {
  localStorage.setItem(TOKEN_KEY, token);
}

export function clearStoredToken(): void {
  localStorage.removeItem(TOKEN_KEY);
}

function authHeaders(): HeadersInit {
  const token = getStoredToken();
  const headers: HeadersInit = { "Content-Type": "application/json" };
  if (token) {
    headers.Authorization = `Bearer ${token}`;
  }
  return headers;
}

async function parseAuthResponse(res: Response): Promise<AuthResponse> {
  const data = (await res.json()) as AuthResponse;
  if (data.status === "success" && data.token) {
    setStoredToken(data.token);
  }
  return data;
}

export async function registerUser(
  payload: RegisterRequest
): Promise<AuthResponse> {
  const res = await fetch("/api/auth/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return parseAuthResponse(res);
}

export async function loginUser(payload: LoginRequest): Promise<AuthResponse> {
  const res = await fetch("/api/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return parseAuthResponse(res);
}

export async function logoutUser(): Promise<void> {
  try {
    await fetch("/api/auth/logout", {
      method: "POST",
      headers: authHeaders(),
    });
  } finally {
    clearStoredToken();
  }
}

export async function fetchCurrentUser(): Promise<User | null> {
  const token = getStoredToken();
  if (!token) return null;

  const res = await fetch("/api/auth/me", {
    headers: { Authorization: `Bearer ${token}` },
  });
  const data = (await res.json()) as AuthResponse;
  if (data.status === "success" && data.user) {
    return data.user;
  }
  clearStoredToken();
  return null;
}
