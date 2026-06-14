"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { motion } from "framer-motion";
import { useAuth } from "@/context/AuthContext";

const links = [
  { href: "/", label: "Trang chủ" },
  { href: "/analyze", label: "Phân tích" },
  { href: "/history", label: "Lịch sử" },
  { href: "/results", label: "Kết quả" },
];

export default function Navbar() {
  const pathname = usePathname();
  const router = useRouter();
  const { user, loading, logout } = useAuth();

  const handleLogout = async () => {
    await logout();
    router.push("/");
  };

  return (
    <motion.header
      initial={{ y: -20, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.5 }}
      className="sticky top-0 z-50 border-b border-white/10 bg-ink/80 backdrop-blur-xl"
    >
      <div className="container-main flex h-16 items-center justify-between sm:h-[4.5rem]">
        <Link href="/" className="flex items-center gap-2.5">
          <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-ocean-gradient text-lg shadow-glow">
            🛡️
          </span>
          <span className="font-display text-lg font-bold tracking-tight text-white">
            Shield<span className="text-ocean-glow">AI</span>
          </span>
        </Link>

        <nav className="hidden items-center gap-1 md:flex">
          {links.map((link) => {
            const active = pathname === link.href;
            return (
              <Link
                key={link.href}
                href={link.href}
                className={`relative rounded-full px-4 py-2 text-sm font-medium transition-colors ${
                  active ? "text-white" : "text-slate-400 hover:text-white"
                }`}
              >
                {active && (
                  <motion.span
                    layoutId="nav-pill"
                    className="absolute inset-0 rounded-full bg-ocean/20 ring-1 ring-ocean/40"
                    transition={{ type: "spring", stiffness: 380, damping: 30 }}
                  />
                )}
                <span className="relative z-10">{link.label}</span>
              </Link>
            );
          })}
        </nav>

        <div className="flex items-center gap-2 sm:gap-3">
          {!loading && user ? (
            <>
              <span className="hidden text-sm text-slate-300 sm:inline">
                Xin chào, <strong className="text-white">{user.username}</strong>
              </span>
              <button
                type="button"
                onClick={handleLogout}
                className="rounded-full border border-white/20 px-4 py-2 text-xs font-semibold text-white transition hover:bg-white/10"
              >
                Đăng xuất
              </button>
              <Link href="/analyze" className="btn-primary !py-2.5 !px-5 !text-xs">
                Phân tích
              </Link>
            </>
          ) : (
            <>
              <Link
                href="/login"
                className="hidden rounded-full border border-white/20 px-4 py-2 text-xs font-semibold text-white transition hover:bg-white/10 sm:inline-flex"
              >
                Đăng nhập
              </Link>
              <Link href="/register" className="btn-primary !py-2.5 !px-5 !text-xs">
                Đăng ký
              </Link>
            </>
          )}
        </div>
      </div>
    </motion.header>
  );
}
