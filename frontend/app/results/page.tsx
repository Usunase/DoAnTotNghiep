"use client";

import { Suspense, useEffect, useState } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { motion } from "framer-motion";
import AuthGuard from "@/components/AuthGuard";
import PageTransition from "@/components/PageTransition";
import ResultGauge from "@/components/ResultGauge";
import ExplanationCard from "@/components/ExplanationCard";
import FeedbackSection from "@/components/FeedbackSection";
import { RESULT_STORAGE_KEY } from "@/lib/api";
import { fetchHistoryDetail } from "@/lib/history";
import type { AnalyzeResponse } from "@/lib/types";

function ResultsLoading() {
  return (
    <div className="flex min-h-[50vh] items-center justify-center">
      <div className="h-10 w-10 animate-spin rounded-full border-2 border-ocean/30 border-t-ocean" />
    </div>
  );
}

function ResultsPageContent() {
  const searchParams = useSearchParams();
  const historyId = searchParams.get("id");
  const [data, setData] = useState<AnalyzeResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;

    async function load() {
      setLoading(true);
      setError(null);

      if (historyId) {
        try {
          const res = await fetchHistoryDetail(Number(historyId));
          if (!cancelled) {
            if (res.status === "success") {
              setData(res);
            } else {
              setError(res.message || "Không tải được lịch sử.");
              setData(null);
            }
          }
        } catch {
          if (!cancelled) {
            setError("Không kết nối được máy chủ.");
            setData(null);
          }
        }
      } else {
        const raw = sessionStorage.getItem(RESULT_STORAGE_KEY);
        if (raw) {
          try {
            if (!cancelled) setData(JSON.parse(raw) as AnalyzeResponse);
          } catch {
            if (!cancelled) setData(null);
          }
        } else if (!cancelled) {
          setData(null);
        }
      }

      if (!cancelled) setLoading(false);
    }

    load();
    return () => {
      cancelled = true;
    };
  }, [historyId]);

  if (loading) {
    return <ResultsLoading />;
  }

  if (error || !data || data.status !== "success") {
    return (
      <PageTransition>
        <div className="container-main py-24 text-center">
          <h1 className="font-display text-2xl font-bold text-ink">
            {error || "Chưa có kết quả"}
          </h1>
          <p className="mt-3 text-slate-500">
            {error
              ? "Bản ghi có thể đã bị xóa hoặc không thuộc tài khoản của bạn."
              : "Hãy phân tích tin trước để xem kết quả tại đây."}
          </p>
          <div className="mt-8 flex flex-wrap justify-center gap-3">
            <Link href="/analyze" className="btn-primary inline-flex">
              Phân tích mới
            </Link>
            <Link href="/history" className="btn-secondary inline-flex">
              Xem lịch sử
            </Link>
          </div>
        </div>
      </PageTransition>
    );
  }

  const raw = data.raw_data;

  return (
    <PageTransition>
      <div className="bg-surface-soft py-12 sm:py-16">
        <div className="container-main">
          <div className="mb-8 flex flex-wrap gap-3">
            <Link href="/analyze" className="btn-secondary">
              ← Phân tích mới
            </Link>
            <Link href="/history" className="btn-secondary">
              Lịch sử
            </Link>
            <Link href="/" className="btn-secondary">
              Trang chủ
            </Link>
          </div>

          <motion.div
            initial={{ opacity: 0, y: 12 }}
            animate={{ opacity: 1, y: 0 }}
          >
            <h1 className="font-display text-3xl font-bold text-ink sm:text-4xl">
              Kết quả phân tích
            </h1>
            <p className="mt-2 text-slate-500">
              {historyId
                ? `Lịch sử #${historyId}${data.created_at ? ` · ${new Date(data.created_at).toLocaleString("vi-VN")}` : ""}`
                : "Xác suất tin giả và giải thích từ mô hình PhoBERT + MLP"}
            </p>
          </motion.div>

          <div className="mt-10 grid gap-8 lg:grid-cols-2">
            <ResultGauge data={data} />

            <motion.div
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.15 }}
              className="card-premium"
            >
              <h3 className="font-display text-lg font-semibold text-ink">
                Nội dung đã xử lý
              </h3>
              <p className="mt-4 text-sm">
                <span className="font-semibold text-slate-500">Tiêu đề: </span>
                {raw?.title || "—"}
              </p>
              {raw?.source_domain && (
                <p className="mt-2 text-sm text-slate-500">
                  Nguồn:{" "}
                  <code className="text-ocean-deep">{raw.source_domain}</code>
                </p>
              )}
              {raw?.original_url && (
                <a
                  href={raw.original_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="mt-4 inline-block text-sm font-semibold text-ocean-deep hover:underline"
                >
                  Mở bài gốc →
                </a>
              )}
              <details className="mt-6">
                <summary className="cursor-pointer text-sm font-semibold text-ocean-deep">
                  Xem toàn văn
                </summary>
                <p className="mt-3 max-h-48 overflow-y-auto rounded-lg bg-surface-soft p-4 text-sm leading-relaxed text-slate-600">
                  {raw?.content || ""}
                </p>
              </details>
            </motion.div>
          </div>

          <div className="mt-8">
            <ExplanationCard explanation={data.explanation} />

            {historyId && (
              <FeedbackSection
                historyId={Number(historyId)}
                initialFeedback={data.feedback}
              />
            )}
          </div>
        </div>
      </div>
    </PageTransition>
  );
}

export default function ResultsPage() {
  return (
    <AuthGuard>
      <Suspense fallback={<ResultsLoading />}>
        <ResultsPageContent />
      </Suspense>
    </AuthGuard>
  );
}
