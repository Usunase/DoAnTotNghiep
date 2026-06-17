"use client";

import { useCallback, useEffect, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { motion } from "framer-motion";
import AuthGuard from "@/components/AuthGuard";
import PageTransition from "@/components/PageTransition";
import { deleteHistoryItem, fetchHistoryList } from "@/lib/history";
import { resolveVerdict, type Verdict } from "@/lib/types";
import type { HistorySummary } from "@/lib/types";

function formatDate(iso?: string | null) {
  if (!iso) return "—";
  try {
    return new Date(iso).toLocaleString("vi-VN");
  } catch {
    return iso;
  }
}

function toneClass(verdict: Verdict | string | null | undefined, fakeProb: number) {
  const { tone } = resolveVerdict({ verdict, fake_prob: fakeProb });
  if (tone === "danger") return "bg-red-100 text-red-800 ring-red-200";
  if (tone === "warn") return "bg-amber-100 text-amber-800 ring-amber-200";
  return "bg-emerald-100 text-emerald-800 ring-emerald-200";
}

export default function HistoryPage() {
  const router = useRouter();
  const [items, setItems] = useState<HistorySummary[]>([]);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const load = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetchHistoryList();
      if (res.status === "error") {
        setError(res.message || "Không tải được lịch sử.");
        return;
      }
      setItems(res.items ?? []);
      setTotal(res.total ?? 0);
    } catch {
      setError("Không kết nối được máy chủ.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    load();
  }, [load]);

  const handleDelete = async (id: number) => {
    if (!confirm("Xóa bản ghi này khỏi lịch sử?")) return;
    const res = await deleteHistoryItem(id);
    if (res.status === "success") {
      setItems((prev) => prev.filter((x) => x.id !== id));
      setTotal((t) => Math.max(0, t - 1));
    }
  };

  return (
    <AuthGuard>
      <PageTransition>
        <div className="bg-surface-soft py-12 sm:py-16">
          <div className="container-main">
            <motion.div
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: 1, y: 0 }}
              className="mb-8 flex flex-wrap items-end justify-between gap-4"
            >
              <div>
                <h1 className="font-display text-3xl font-bold text-ink sm:text-4xl">
                  Lịch sử phân tích
                </h1>
                <p className="mt-2 text-slate-500">
                  {total} bài đã phân tích — lưu trong cơ sở dữ liệu ShieldAI
                </p>
              </div>
              <Link href="/analyze" className="btn-primary !py-2.5 !px-5 !text-xs">
                Phân tích mới
              </Link>
            </motion.div>

            {loading && (
              <div className="flex min-h-[30vh] items-center justify-center">
                <div className="h-10 w-10 animate-spin rounded-full border-2 border-ocean/30 border-t-ocean" />
              </div>
            )}

            {error && (
              <p className="rounded-xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
                {error}
              </p>
            )}

            {!loading && !error && items.length === 0 && (
              <div className="card-premium text-center py-16">
                <p className="text-slate-500">Chưa có lịch sử phân tích.</p>
                <Link href="/analyze" className="btn-primary mt-6 inline-flex">
                  Phân tích bài đầu tiên
                </Link>
              </div>
            )}

            {!loading && items.length > 0 && (
              <div className="space-y-4">
                {items.map((item, i) => {
                  const verdict = resolveVerdict({
                    verdict: item.verdict,
                    fake_prob: item.fake_prob,
                  });
                  return (
                    <motion.article
                      key={item.id}
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: i * 0.04 }}
                      className="card-premium flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
                    >
                      <div className="min-w-0 flex-1">
                        <div className="mb-2 flex flex-wrap items-center gap-2">
                          <span
                            className={`inline-flex rounded-full px-2.5 py-0.5 text-xs font-semibold ring-1 ${toneClass(item.verdict, item.fake_prob)}`}
                          >
                            {verdict.label} · {item.fake_prob.toFixed(1)}%
                          </span>
                          <span className="text-xs text-slate-400">
                            {item.input_mode === "url" ? "URL" : "Văn bản"}
                          </span>
                          <span className="text-xs text-slate-400">
                            {formatDate(item.created_at)}
                          </span>
                        </div>
                        <h2 className="truncate font-display text-lg font-semibold text-ink">
                          {item.title}
                        </h2>
                        <p className="mt-1 line-clamp-2 text-sm text-slate-500">
                          {item.preview || "—"}
                        </p>
                        {item.source_domain && (
                          <p className="mt-1 text-xs text-slate-400">
                            Nguồn: {item.source_domain}
                          </p>
                        )}
                      </div>
                      <div className="flex shrink-0 gap-2">
                        <button
                          type="button"
                          onClick={() => router.push(`/results?id=${item.id}`)}
                          className="btn-secondary !py-2 !px-4 !text-xs"
                        >
                          Xem chi tiết
                        </button>
                        <button
                          type="button"
                          onClick={() => handleDelete(item.id)}
                          className="rounded-full border border-red-200 px-4 py-2 text-xs font-semibold text-red-600 transition hover:bg-red-50"
                        >
                          Xóa
                        </button>
                      </div>
                    </motion.article>
                  );
                })}
              </div>
            )}
          </div>
        </div>
      </PageTransition>
    </AuthGuard>
  );
}
