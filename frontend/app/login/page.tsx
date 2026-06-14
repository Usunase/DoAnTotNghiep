"use client";

import { useRouter } from "next/navigation";
import AuthForm from "@/components/AuthForm";
import { useAuth } from "@/context/AuthContext";

export default function LoginPage() {
  const router = useRouter();
  const { login } = useAuth();

  return (
    <AuthForm
      title="Đăng nhập"
      subtitle="Truy cập công cụ phân tích tin giả ShieldAI"
      fields={[
        {
          name: "email",
          label: "Email",
          type: "email",
          placeholder: "ban@example.com",
          autoComplete: "email",
        },
        {
          name: "password",
          label: "Mật khẩu",
          type: "password",
          placeholder: "••••••••",
          autoComplete: "current-password",
        },
      ]}
      submitLabel="Đăng nhập"
      alternateLabel="Chưa có tài khoản? Đăng ký"
      alternateHref="/register"
      onSubmit={async (values) =>
        login({ email: values.email, password: values.password })
      }
      onSuccess={() => router.push("/analyze")}
    />
  );
}
