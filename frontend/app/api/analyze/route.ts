import { NextRequest, NextResponse } from "next/server";

const BACKEND =
  process.env.SHIELD_API_URL || "http://127.0.0.1:8000";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const headers: Record<string, string> = { "Content-Type": "application/json" };
    const auth = req.headers.get("authorization");
    if (auth) headers["Authorization"] = auth;

    const res = await fetch(`${BACKEND}/api/analyze`, {
      method: "POST",
      headers,
      body: JSON.stringify(body),
    });

    const data = await res.json();
    return NextResponse.json(data, { status: res.status });
  } catch {
    return NextResponse.json(
      {
        status: "error",
        message:
          "Không kết nối được backend Python. Chạy: uvicorn backend.api.main:app --reload --port 8000",
      },
      { status: 503 }
    );
  }
}
