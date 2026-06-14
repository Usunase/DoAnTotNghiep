import { NextRequest, NextResponse } from "next/server";

const BACKEND = process.env.SHIELD_API_URL || "http://127.0.0.1:8000";

export async function GET(
  req: NextRequest,
  { params }: { params: { id: string } }
) {
  try {
    const auth = req.headers.get("authorization");
    if (!auth) {
      return NextResponse.json(
        { status: "error", message: "Chưa đăng nhập." },
        { status: 401 }
      );
    }

    const res = await fetch(`${BACKEND}/api/history/${params.id}`, {
      headers: { Authorization: auth },
    });
    const data = await res.json();
    return NextResponse.json(data, { status: res.status });
  } catch {
    return NextResponse.json(
      { status: "error", message: "Không kết nối được máy chủ." },
      { status: 503 }
    );
  }
}

export async function DELETE(
  req: NextRequest,
  { params }: { params: { id: string } }
) {
  try {
    const auth = req.headers.get("authorization");
    if (!auth) {
      return NextResponse.json(
        { status: "error", message: "Chưa đăng nhập." },
        { status: 401 }
      );
    }

    const res = await fetch(`${BACKEND}/api/history/${params.id}`, {
      method: "DELETE",
      headers: { Authorization: auth },
    });
    const data = await res.json();
    return NextResponse.json(data, { status: res.status });
  } catch {
    return NextResponse.json(
      { status: "error", message: "Không kết nối được máy chủ." },
      { status: 503 }
    );
  }
}
