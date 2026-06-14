"use client";

import Link from "next/link";
import { useState } from "react";
import { motion } from "framer-motion";
import PageTransition from "@/components/PageTransition";

interface Field {
  name: string;
  label: string;
  type: "text" | "email" | "password";
  placeholder: string;
  autoComplete?: string;
}

interface AuthFormProps {
  title: string;
  subtitle: string;
  fields: Field[];
  submitLabel: string;
  alternateLabel: string;
  alternateHref: string;
  onSubmit: (values: Record<string, string>) => Promise<string | null>;
  onSuccess: () => void;
}

export default function AuthForm({
  title,
  subtitle,
  fields,
  submitLabel,
  alternateLabel,
  alternateHref,
  onSubmit,
  onSuccess,
}: AuthFormProps) {
  const [values, setValues] = useState<Record<string, string>>(() =>
    Object.fromEntries(fields.map((f) => [f.name, ""]))
  );
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      const err = await onSubmit(values);
      if (err) {
        setError(err);
        return;
      }
      onSuccess();
    } catch {
      setError("Không kết nối được máy chủ. Hãy chạy backend (port 8000).");
    } finally {
      setLoading(false);
    }
  };

  return (
    <PageTransition>
      <section className="container-main flex min-h-[calc(100vh-12rem)] items-center justify-center py-12">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="card-premium w-full max-w-md"
        >
          <div className="mb-8 text-center">
            <span className="mb-3 inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-ocean-gradient text-2xl shadow-glow">
              🛡️
            </span>
            <h1 className="font-display text-2xl font-bold text-ink">{title}</h1>
            <p className="mt-2 text-sm text-slate-500">{subtitle}</p>
          </div>

          <form onSubmit={handleSubmit} className="space-y-5">
            {fields.map((field) => (
              <div key={field.name}>
                <label htmlFor={field.name} className="label-field">
                  {field.label}
                </label>
                <input
                  id={field.name}
                  type={field.type}
                  className="input-field"
                  placeholder={field.placeholder}
                  autoComplete={field.autoComplete}
                  required
                  value={values[field.name]}
                  onChange={(e) =>
                    setValues((prev) => ({
                      ...prev,
                      [field.name]: e.target.value,
                    }))
                  }
                />
              </div>
            ))}

            {error && (
              <p className="rounded-xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
                {error}
              </p>
            )}

            <button
              type="submit"
              disabled={loading}
              className="btn-primary w-full disabled:opacity-60"
            >
              {loading ? "Đang xử lý…" : submitLabel}
            </button>
          </form>

          <p className="mt-6 text-center text-sm text-slate-500">
            {alternateLabel}{" "}
            <Link
              href={alternateHref}
              className="font-semibold text-ocean-deep hover:underline"
            >
              tại đây
            </Link>
          </p>
        </motion.div>
      </section>
    </PageTransition>
  );
}
