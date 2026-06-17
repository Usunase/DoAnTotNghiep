export type Verdict = "real" | "fake" | "suspicious";

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

export interface AnalyzeRequest {
  mode: "text" | "url";
  text?: string;
  title?: string;
  url?: string;
}

export interface Explanation {
  verdict: "real" | "fake" | "suspicious";
  headline: string;
  summary: string;
  primary_reasons: string[];
  counter_points?: string[];
  counter_label?: string;
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
  verdict?: Verdict;
  fake_prob?: number;
  created_at?: string;
  raw_data?: {
    title?: string;
    content?: string;
    source_domain?: string;
    original_url?: string;
  };
  explanation?: Explanation;
  feedback?: {
    is_correct: boolean;
    comment?: string | null;
  } | null;
}

export function verdictToDisplay(verdict: Verdict): {
  label: string;
  tone: "safe" | "warn" | "danger";
  advice: string;
} {
  if (verdict === "fake") {
    return {
      label: "TIN GIẢ",
      tone: "danger",
      advice: "Rủi ro rất cao — đối chiếu nguồn chính thống trước khi chia sẻ.",
    };
  }
  if (verdict === "suspicious") {
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

export function resolveVerdict(data: {
  verdict?: Verdict | string | null;
  explanation?: Explanation;
  fake_prob?: number;
}): {
  label: string;
  tone: "safe" | "warn" | "danger";
  advice: string;
} {
  const fromApi = data.verdict ?? data.explanation?.verdict;
  if (fromApi === "fake" || fromApi === "suspicious" || fromApi === "real") {
    return verdictToDisplay(fromApi);
  }
  return verdictFromProb(data.fake_prob ?? 0);
}

export function verdictFromProb(prob: number): {
  label: string;
  tone: "safe" | "warn" | "danger";
  advice: string;
} {
  if (prob >= 75) {
    return verdictToDisplay("fake");
  }
  if (prob >= 35) {
    return verdictToDisplay("suspicious");
  }
  return verdictToDisplay("real");
}
