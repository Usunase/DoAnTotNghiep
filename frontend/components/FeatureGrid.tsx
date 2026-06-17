"use client";

import { motion } from "framer-motion";
import { fadeUp, staggerContainer } from "@/lib/motion";

const features = [
  {
    icon: "📝",
    title: "Nhập văn bản",
    desc: "Dán trực tiếp bài báo hoặc bài đăng cần kiểm tra độ tin cậy.",
  },
  {
    icon: "🔗",
    title: "Nhập link",
    desc: "Tự động crawl nội dung từ báo điện tử Việt Nam.",
  },
  {
    icon: "🧠",
    title: "PhoBERT + MLP",
    desc: "Phân tích ngữ nghĩa tiếng Việt bằng embedding sâu và bộ phân loại MLP.",
  },
  {
    icon: "💡",
    title: "Giải thích rõ",
    desc: "Trả về lý do phân loại để người dùng tự đánh giá.",
  },
];

export default function FeatureGrid() {
  return (
    <section className="py-20 sm:py-28">
      <div className="container-main">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center"
        >
          <h2 className="font-display text-3xl font-bold text-ink sm:text-4xl">
            Tính năng nổi bật
          </h2>
          <p className="mx-auto mt-4 max-w-lg text-slate-500">
            Thiết kế theo chuẩn ecommerce hiện đại — tối giản, rõ ràng, dễ thao tác.
          </p>
        </motion.div>

        <motion.div
          variants={staggerContainer}
          initial="initial"
          whileInView="animate"
          viewport={{ once: true, margin: "-80px" }}
          className="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-4"
        >
          {features.map((f, i) => (
            <motion.article
              key={f.title}
              variants={fadeUp}
              whileHover={{ y: -6, transition: { duration: 0.25 } }}
              className="card-premium group"
            >
              <span className="flex h-12 w-12 items-center justify-center rounded-xl bg-ocean/10 text-2xl transition-colors group-hover:bg-ocean/20">
                {f.icon}
              </span>
              <h3 className="mt-4 font-display text-lg font-semibold text-ink">
                {f.title}
              </h3>
              <p className="mt-2 text-sm leading-relaxed text-slate-500">
                {f.desc}
              </p>
            </motion.article>
          ))}
        </motion.div>
      </div>
    </section>
  );
}
