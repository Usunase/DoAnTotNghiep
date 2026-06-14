"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import { submitHistoryFeedback } from "@/lib/history";

interface FeedbackSectionProps {
  historyId: number;
  initialFeedback?: {
    is_correct: boolean;
    comment?: string | null;
  } | null;
}

export default function FeedbackSection({ historyId, initialFeedback }: FeedbackSectionProps) {
  const [isCorrect, setIsCorrect] = useState<boolean | null>(
    initialFeedback ? initialFeedback.is_correct : null
  );
  const [comment, setComment] = useState(
    initialFeedback?.comment || ""
  );
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [status, setStatus] = useState<"idle" | "success" | "error">("idle");
  const [errorMessage, setErrorMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (isCorrect === null) return;

    setIsSubmitting(true);
    setStatus("idle");
    
    try {
      const res = await submitHistoryFeedback(historyId, isCorrect, comment);
      if (res.status === "success") {
        setStatus("success");
      } else {
        setStatus("error");
        setErrorMessage(res.message || "Đã xảy ra lỗi khi gửi phản hồi.");
      }
    } catch (err) {
      setStatus("error");
      setErrorMessage("Lỗi kết nối máy chủ.");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.3 }}
      className="card-premium mt-8"
    >
      <h3 className="font-display text-lg font-semibold text-ink">
        Đánh giá kết quả
      </h3>
      <p className="mt-2 text-sm text-slate-500">
        Bạn thấy kết quả phân tích này có chính xác không? Đánh giá của bạn giúp chúng tôi cải thiện hệ thống.
      </p>

      <form onSubmit={handleSubmit} className="mt-6 space-y-5">
        <div className="flex flex-wrap gap-4">
          <button
            type="button"
            onClick={() => setIsCorrect(true)}
            className={`flex items-center gap-2 rounded-xl px-5 py-3 text-sm font-semibold transition-all ${
              isCorrect === true
                ? "bg-ocean-deep text-white shadow-md shadow-ocean/30"
                : "bg-surface-soft text-slate-600 hover:bg-slate-100"
            }`}
          >
            👍 Mô hình đúng
          </button>
          <button
            type="button"
            onClick={() => setIsCorrect(false)}
            className={`flex items-center gap-2 rounded-xl px-5 py-3 text-sm font-semibold transition-all ${
              isCorrect === false
                ? "bg-danger text-white shadow-md shadow-danger/30"
                : "bg-surface-soft text-slate-600 hover:bg-slate-100"
            }`}
          >
            👎 Mô hình sai
          </button>
        </div>

        {isCorrect !== null && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
          >
            <label className="mb-2 block text-sm font-medium text-slate-700">
              Nhận xét thêm (Tùy chọn)
            </label>
            <textarea
              rows={3}
              className="input-field w-full"
              placeholder={
                isCorrect
                  ? "Ví dụ: Dự đoán rất chuẩn, đúng là tin giả."
                  : "Ví dụ: Nguồn tin này rất uy tín, không phải tin giả."
              }
              value={comment}
              onChange={(e) => setComment(e.target.value)}
            />
            
            <div className="mt-4 flex items-center justify-between">
              <button
                type="submit"
                disabled={isSubmitting}
                className="btn-primary"
              >
                {isSubmitting ? "Đang gửi..." : "Gửi phản hồi"}
              </button>

              {status === "success" && (
                <span className="text-sm font-medium text-ocean-deep">
                  ✅ Cảm ơn bạn đã phản hồi!
                </span>
              )}
              {status === "error" && (
                <span className="text-sm font-medium text-danger">
                  ❌ {errorMessage}
                </span>
              )}
            </div>
          </motion.div>
        )}
      </form>
    </motion.div>
  );
}
