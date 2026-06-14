"use client";

import { motion } from "framer-motion";
import type { AnalyzeResponse } from "@/lib/types";
import { verdictFromProb } from "@/lib/types";

interface Props {
  data: AnalyzeResponse;
}

const toneStyles = {
  safe: "from-emerald-500 to-emerald-600 border-emerald-400/30",
  warn: "from-amber-500 to-orange-500 border-amber-400/30",
  danger: "from-red-500 to-rose-600 border-red-400/30",
};

export default function ResultGauge({ data }: Props) {
  const prob = data.fake_prob ?? 0;
  const v = verdictFromProb(prob);
  const circumference = 2 * Math.PI * 45;
  const offset = circumference - (prob / 100) * circumference;

  const strokeColor =
    v.tone === "danger"
      ? "#ef4444"
      : v.tone === "warn"
        ? "#f59e0b"
        : "#10b981";

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      className="card-premium flex flex-col items-center text-center"
    >
      <div className="relative h-44 w-44">
        <svg className="h-full w-full" viewBox="0 0 100 100">
          <circle
            cx="50"
            cy="50"
            r="45"
            fill="none"
            stroke="#e2e8f0"
            strokeWidth="8"
          />
          <motion.circle
            cx="50"
            cy="50"
            r="45"
            fill="none"
            stroke={strokeColor}
            strokeWidth="8"
            strokeLinecap="round"
            className="gauge-ring"
            strokeDasharray={circumference}
            initial={{ strokeDashoffset: circumference }}
            animate={{ strokeDashoffset: offset }}
            transition={{ duration: 1.2, ease: [0.22, 1, 0.36, 1] }}
          />
        </svg>
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <motion.span
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.4 }}
            className="font-display text-4xl font-bold text-ink"
          >
            {prob.toFixed(0)}%
          </motion.span>
          <span className="text-xs font-semibold uppercase tracking-widest text-slate-400">
            Tin giả
          </span>
        </div>
      </div>

      <motion.div
        initial={{ opacity: 0, y: 12 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.5 }}
        className={`mt-8 w-full rounded-2xl border bg-gradient-to-br px-6 py-5 text-white ${toneStyles[v.tone]}`}
      >
        <p className="font-display text-xl font-bold">{v.label}</p>
        <p className="mt-2 text-sm text-white/90">{v.advice}</p>
      </motion.div>
    </motion.div>
  );
}
