export interface User {
  id: number;
  email: string;
  username: string;
}

export interface RegisterRequest {
  email: string;
  username: string;
  password: string;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface AuthResponse {
  status: "success" | "error";
  message?: string;
  token?: string;
  user?: User;
}

export interface MetaInput {
  account_age_days: number;
  followers: number;
  is_verified: number;
  share_speed: number;
  angry_ratio: number;
}

export interface AnalyzeRequest {
  mode: "text" | "url";
  text?: string;
  title?: string;
  url?: string;
  meta: MetaInput;
}

export interface Explanation {
  verdict: "real" | "fake" | "suspicious";
  headline: string;
  summary: string;
  primary_reasons: string[];
  counter_points?: string[];
  counter_label?: string;
  meta_breakdown?: { label: string; value: number | string }[];
}

export interface HistorySummary {
  id: number;
  input_mode: "text" | "url";
  title: string;
  preview: string;
  source_url?: string | null;
  source_domain?: string | null;
  result_label: string;
  fake_prob: number;
  verdict?: string | null;
  created_at?: string | null;
}

export interface HistoryListResponse {
  status: "success" | "error";
  message?: string;
  items?: HistorySummary[];
  total?: number;
}

export interface AnalyzeResponse {
  status: "success" | "error";
  message?: string;
  history_id?: number;
  result?: string;
  fake_prob?: number;
  created_at?: string;
  raw_data?: {
    title?: string;
    content?: string;
    source_domain?: string;
    original_url?: string;
  };
  explanation?: Explanation;
  meta_vector?: number[];
  feedback?: {
    is_correct: boolean;
    comment?: string | null;
  } | null;
}

export const DEFAULT_META: MetaInput = {
  account_age_days: 0,
  followers: 0,
  is_verified: 0,
  share_speed: 0,
  angry_ratio: 0,
};

export function verdictFromProb(prob: number): {
  label: string;
  tone: "safe" | "warn" | "danger";
  advice: string;
} {
  if (prob >= 75) {
    return {
      label: "TIN GIẢ",
      tone: "danger",
      advice: "Rủi ro rất cao — đối chiếu nguồn chính thống trước khi chia sẻ.",
    };
  }
  if (prob >= 35) {
    return {
      label: "ĐÁNG NGỜ",
      tone: "warn",
      advice: "Có dấu hiệu giật tít hoặc thiếu kiểm chứng — cần xác minh thêm.",
    };
  }
  return {
    label: "TIN THẬT",
    tone: "safe",
    advice: "Nội dung được mô hình đánh giá tương đối đáng tin.",
  };
}
