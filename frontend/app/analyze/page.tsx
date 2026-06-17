"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { motion, AnimatePresence } from "framer-motion";
import AuthGuard from "@/components/AuthGuard";
import PageTransition from "@/components/PageTransition";
import { analyzeNews, RESULT_STORAGE_KEY } from "@/lib/api";

const SAMPLE_FAKE =
  "CẢNH BÁO KHẨN CẤP!!! Hàng ngàn người đang hoảng loạn tháo chạy vì vụ cháy quá lớn. Tin cực hot mọi người ơi chia sẻ gấp trước khi bị gỡ!!!!";
const SAMPLE_REAL =
  "Người bệnh cúm nên ăn thực phẩm giàu dinh dưỡng như thịt gà, thịt bò và uống đủ nước. Bác sĩ khuyến cáo tránh uống nhiều rượu bia.";

export default function AnalyzePage() {
  const router = useRouter();
  const [tab, setTab] = useState<"text" | "url">("text");
  const [title, setTitle] = useState("");
  const [text, setText] = useState("");
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleAnalyze = async () => {
    setError(null);
    if (tab === "text" && !text.trim()) {
      setError("Vui lòng nhập nội dung bài báo.");
      return;
    }
    if (tab === "url" && !url.trim()) {
      setError("Vui lòng nhập URL.");
      return;
    }

    setLoading(true);
    try {
      const res = await analyzeNews({
        mode: tab,
        text: tab === "text" ? text : undefined,
        title: tab === "text" ? title : undefined,
        url: tab === "url" ? url : undefined,
      });

      if (res.status === "error") {
        setError(res.message || "Phân tích thất bại.");
        return;
      }

      sessionStorage.setItem(RESULT_STORAGE_KEY, JSON.stringify(res));
      if (res.history_id) {
        router.push(`/results?id=${res.history_id}`);
      } else {
        router.push("/results");
      }
    } catch {
      setError("Không kết nối được API. Hãy chạy backend (port 8000).");
    } finally {
      setLoading(false);
    }
  };

  return (
    <AuthGuard>
    <PageTransition>
      <div className="bg-surface-soft py-12 sm:py-16">
        <div className="container-main">
          <motion.div
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            className="mb-10"
          >
            <h1 className="font-display text-3xl font-bold text-ink sm:text-4xl">
              Phân tích tin tức
            </h1>
            <p className="mt-2 text-slate-500">
              Nhập văn bản hoặc URL — mô hình PhoBERT + MLP sẽ phân loại và giải thích kết quả.
            </p>
          </motion.div>

          <div className="mx-auto max-w-3xl">
              <div className="card-premium">
                <div className="flex gap-2 rounded-xl bg-surface-soft p-1">
                  {(["text", "url"] as const).map((t) => (
                    <button
                      key={t}
                      type="button"
                      onClick={() => setTab(t)}
                      className={`flex-1 rounded-lg py-2.5 text-sm font-semibold transition-all ${
                        tab === t
                          ? "bg-ocean-gradient text-white shadow-md"
                          : "text-slate-600 hover:text-ink"
                      }`}
                    >
                      {t === "text" ? "📝 Nhập văn bản" : "🔗 Nhập link"}
                    </button>
                  ))}
                </div>

                <AnimatePresence mode="wait">
                  {tab === "text" ? (
                    <motion.div
                      key="text"
                      initial={{ opacity: 0, x: -12 }}
                      animate={{ opacity: 1, x: 0 }}
                      exit={{ opacity: 0, x: 12 }}
                      className="mt-6 space-y-4"
                    >
                      <div className="flex flex-wrap gap-2">
                        <button
                          type="button"
                          className="btn-secondary !py-2 !text-xs"
                          onClick={() => {
                            setText(SAMPLE_FAKE);
                            setTitle("Tin giật gân (mẫu)");
                          }}
                        >
                          Mẫu đáng ngờ
                        </button>
                        <button
                          type="button"
                          className="btn-secondary !py-2 !text-xs"
                          onClick={() => {
                            setText(SAMPLE_REAL);
                            setTitle("Tin y tế (mẫu)");
                          }}
                        >
                          Mẫu khách quan
                        </button>
                      </div>
                      <div>
                        <label className="label-field">Tiêu đề</label>
                        <input
                          className="input-field"
                          value={title}
                          onChange={(e) => setTitle(e.target.value)}
                          placeholder="Tiêu đề (tùy chọn)"
                        />
                      </div>
                      <div>
                        <label className="label-field">Nội dung</label>
                        <textarea
                          className="input-field min-h-[200px] resize-y"
                          value={text}
                          onChange={(e) => setText(e.target.value)}
                          placeholder="Dán toàn bộ nội dung cần kiểm tra..."
                        />
                      </div>
                    </motion.div>
                  ) : (
                    <motion.div
                      key="url"
                      initial={{ opacity: 0, x: 12 }}
                      animate={{ opacity: 1, x: 0 }}
                      exit={{ opacity: 0, x: -12 }}
                      className="mt-6"
                    >
                      <label className="label-field">URL bài báo</label>
                      <input
                        className="input-field"
                        value={url}
                        onChange={(e) => setUrl(e.target.value)}
                        placeholder="https://vnexpress.net/..."
                      />
                      <p className="mt-2 text-xs text-slate-500">
                        Hỗ trợ VnExpress, Tuổi Trẻ và các báo tương tự.
                      </p>
                    </motion.div>
                  )}
                </AnimatePresence>

                {error && (
                  <motion.p
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    className="mt-4 rounded-lg bg-red-50 px-4 py-3 text-sm text-red-700"
                  >
                    {error}
                  </motion.p>
                )}

                <button
                  type="button"
                  onClick={handleAnalyze}
                  disabled={loading}
                  className="btn-primary mt-8 w-full disabled:opacity-60"
                >
                  {loading ? (
                    <span className="flex items-center gap-2">
                      <span className="h-4 w-4 animate-spin rounded-full border-2 border-white/30 border-t-white" />
                      Đang phân tích...
                    </span>
                  ) : (
                    "🔍 Phân tích văn bản"
                  )}
                </button>
              </div>
          </div>
        </div>
      </div>
    </PageTransition>
    </AuthGuard>
  );
}
