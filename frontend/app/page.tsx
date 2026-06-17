import HeroBanner from "@/components/HeroBanner";
import FeatureGrid from "@/components/FeatureGrid";
import PageTransition from "@/components/PageTransition";

export default function HomePage() {
  return (
    <PageTransition>
      <HeroBanner />
      <FeatureGrid />
      <section className="border-t border-surface-border bg-white py-16">
        <div className="container-main text-center">
          <h2 className="font-display text-2xl font-bold text-ink sm:text-3xl">
            Sẵn sàng kiểm tra tin tức?
          </h2>
          <p className="mx-auto mt-3 max-w-md text-slate-500">
            Nhập văn bản hoặc link báo — nhận xác suất tin giả và giải thích từ PhoBERT + MLP.
          </p>
          <a href="/analyze" className="btn-primary mt-8 inline-flex">
            Đến trang phân tích
          </a>
        </div>
      </section>
    </PageTransition>
  );
}
