import { NextRequest, NextResponse } from "next/server";

const BACKEND = process.env.SHIELD_API_URL || "http://127.0.0.1:8000";

export async function POST(req: NextRequest) {
  try {
    const auth = req.headers.get("authorization");
    const headers: HeadersInit = { "Content-Type": "application/json" };
    if (auth) headers.Authorization = auth;

    const res = await fetch(`${BACKEND}/api/auth/logout`, {
      method: "POST",
      headers,
    });
    const data = await res.json();
    return NextResponse.json(data, { status: res.status });
  } catch {
    return NextResponse.json(
      { status: "success", message: "Đã đăng xuất." }
    );
  }
}
