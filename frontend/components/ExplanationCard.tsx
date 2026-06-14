"use client";

import { motion } from "framer-motion";
import type { Explanation } from "@/lib/types";

interface Props {
  explanation?: Explanation;
}

const borderTone = {
  real: "border-t-emerald-500",
  fake: "border-t-red-500",
  suspicious: "border-t-amber-500",
};

export default function ExplanationCard({ explanation }: Props) {
  if (!explanation) return null;

  const tone = explanation.verdict || "suspicious";

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.2 }}
      className={`card-premium border-t-4 ${borderTone[tone]}`}
    >
      <h3 className="font-display text-xl font-semibold text-ink">
        💡 {explanation.headline}
      </h3>
      <p className="mt-3 text-slate-600 leading-relaxed">{explanation.summary}</p>

      {explanation.primary_reasons?.length > 0 && (
        <div className="mt-6">
          <p className="text-xs font-bold uppercase tracking-wider text-slate-400">
            Các lý do chính
          </p>
          <ul className="mt-3 space-y-2">
            {explanation.primary_reasons.map((r, i) => (
              <motion.li
                key={i}
                initial={{ opacity: 0, x: -12 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.3 + i * 0.08 }}
                className="flex gap-2 rounded-lg border border-surface-border bg-surface-soft px-4 py-3 text-sm text-ink"
              >
                <span className="text-ocean">▸</span>
                {r}
              </motion.li>
            ))}
          </ul>
        </div>
      )}

      {explanation.counter_points && explanation.counter_points.length > 0 && (
        <div className="mt-6">
          <p className="text-xs font-bold uppercase tracking-wider text-slate-400">
            {explanation.counter_label || "Lưu ý"}
          </p>
          <ul className="mt-3 space-y-2">
            {explanation.counter_points.map((c, i) => (
              <li
                key={i}
                className="rounded-lg border border-surface-border bg-white px-4 py-3 text-sm text-slate-600"
              >
                ○ {c}
              </li>
            ))}
          </ul>
        </div>
      )}
    </motion.div>
  );
}
