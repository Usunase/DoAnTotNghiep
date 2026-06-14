"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import { fadeUp, staggerContainer } from "@/lib/motion";

export default function HeroBanner() {
  return (
    <section className="relative overflow-hidden bg-hero-gradient pb-20 pt-16 sm:pb-28 sm:pt-24">
      <div className="pointer-events-none absolute inset-0 overflow-hidden">
        <motion.div
          animate={{ opacity: [0.3, 0.6, 0.3], scale: [1, 1.05, 1] }}
          transition={{ duration: 8, repeat: Infinity, ease: "easeInOut" }}
          className="absolute -right-32 -top-32 h-96 w-96 rounded-full bg-ocean/20 blur-3xl"
        />
        <motion.div
          animate={{ opacity: [0.2, 0.45, 0.2] }}
          transition={{ duration: 10, repeat: Infinity, ease: "easeInOut", delay: 1 }}
          className="absolute -bottom-24 -left-24 h-80 w-80 rounded-full bg-ocean-deep/25 blur-3xl"
        />
      </div>

      <motion.div
        variants={staggerContainer}
        initial="initial"
        animate="animate"
        className="container-main relative z-10"
      >
        <motion.p
          variants={fadeUp}
          className="mb-4 inline-flex items-center gap-2 rounded-full border border-ocean/30 bg-ocean/10 px-4 py-1.5 text-xs font-semibold uppercase tracking-widest text-ocean-glow"
        >
          <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-ocean-glow" />
          AI Verification Platform
        </motion.p>

        <motion.h1
          variants={fadeUp}
          className="max-w-3xl font-display text-4xl font-bold leading-[1.1] tracking-tight text-white sm:text-5xl lg:text-6xl"
        >
          Welcome to{" "}
          <span className="bg-gradient-to-r from-ocean-glow via-ocean to-ocean-deep bg-clip-text text-transparent">
            ShieldAI
          </span>
        </motion.h1>

        <motion.p
          variants={fadeUp}
          className="mt-6 max-w-xl text-lg text-slate-400 sm:text-xl"
        >
          Phân loại tin thật và tin giả tiếng Việt với mô hình hybrid PhoBERT +
          metadata — giao diện premium, kết quả minh bạch.
        </motion.p>

        <motion.div
          variants={fadeUp}
          className="mt-10 flex flex-col gap-4 sm:flex-row sm:items-center"
        >
          <Link href="/analyze" className="btn-primary text-center">
            Phân tích ngay
          </Link>
          <Link href="/results" className="btn-secondary border-white/20 bg-white/5 text-white hover:bg-white/10 hover:text-white">
            Xem kết quả mẫu
          </Link>
        </motion.div>

        <motion.div
          variants={fadeUp}
          className="mt-16 grid gap-4 sm:grid-cols-3"
        >
          {[
            { n: "768D", l: "PhoBERT embedding" },
            { n: "10+", l: "Tín hiệu metadata" },
            { n: "<3s", l: "Thời gian phản hồi" },
          ].map((stat) => (
            <div
              key={stat.l}
              className="rounded-2xl border border-white/10 bg-white/5 p-5 backdrop-blur-sm"
            >
              <p className="font-display text-2xl font-bold text-ocean-glow">
                {stat.n}
              </p>
              <p className="mt-1 text-sm text-slate-400">{stat.l}</p>
            </div>
          ))}
        </motion.div>
      </motion.div>
    </section>
  );
}
