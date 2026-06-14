export default function Footer() {
  return (
    <footer className="border-t border-surface-border bg-white py-10">
      <div className="container-main flex flex-col items-center justify-between gap-4 text-center sm:flex-row sm:text-left">
        <div>
          <p className="font-display text-sm font-bold text-ink">ShieldAI</p>
          <p className="mt-1 text-sm text-slate-500">
            PhoBERT + Hybrid MLP · Phát hiện tin giả tiếng Việt
          </p>
        </div>
        <p className="text-xs text-slate-400">
          Chỉ mang tính hỗ trợ tham khảo — luôn kiểm chứng từ nguồn chính thống.
        </p>
      </div>
    </footer>
  );
}
