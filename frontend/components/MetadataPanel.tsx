"use client";

import type { MetaInput } from "@/lib/types";

interface Props {
  meta: MetaInput;
  onChange: (meta: MetaInput) => void;
}

export default function MetadataPanel({ meta, onChange }: Props) {
  const set = <K extends keyof MetaInput>(key: K, value: MetaInput[K]) => {
    onChange({ ...meta, [key]: value });
  };

  return (
    <div className="card-premium">
      <h3 className="font-display text-lg font-semibold text-ink">
        Cấu hình nguồn phát
      </h3>
      <p className="mt-1 text-sm text-slate-500">
        Mặc định 0 — chỉ nhập khi bài có metadata mạng xã hội.
      </p>

      <div className="mt-6 grid gap-5 sm:grid-cols-2">
        <div>
          <label className="label-field">Tuổi tài khoản (ngày)</label>
          <input
            type="number"
            min={0}
            className="input-field"
            value={meta.account_age_days}
            onChange={(e) =>
              set("account_age_days", Number(e.target.value) || 0)
            }
          />
        </div>
        <div>
          <label className="label-field">Follower</label>
          <input
            type="number"
            min={0}
            className="input-field"
            value={meta.followers}
            onChange={(e) => set("followers", Number(e.target.value) || 0)}
          />
        </div>
        <div>
          <label className="label-field">Tốc độ share / phút</label>
          <input
            type="number"
            min={0}
            step={0.1}
            className="input-field"
            value={meta.share_speed}
            onChange={(e) => set("share_speed", Number(e.target.value) || 0)}
          />
        </div>
        <div>
          <label className="label-field">Tỷ lệ phẫn nộ (%)</label>
          <input
            type="range"
            min={0}
            max={100}
            className="mt-2 w-full accent-ocean"
            value={Math.round(meta.angry_ratio * 100)}
            onChange={(e) =>
              set("angry_ratio", Number(e.target.value) / 100)
            }
          />
          <span className="text-sm font-medium text-ocean-deep">
            {Math.round(meta.angry_ratio * 100)}%
          </span>
        </div>
        <div className="sm:col-span-2">
          <label className="flex cursor-pointer items-center gap-3">
            <input
              type="checkbox"
              checked={meta.is_verified === 1}
              onChange={(e) => set("is_verified", e.target.checked ? 1 : 0)}
              className="h-5 w-5 rounded border-surface-border accent-ocean"
            />
            <span className="text-sm font-semibold text-ink">Tích xanh (verified)</span>
          </label>
        </div>
      </div>
    </div>
  );
}
