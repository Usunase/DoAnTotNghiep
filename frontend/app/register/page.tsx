"use client";

import { useRouter } from "next/navigation";
import AuthForm from "@/components/AuthForm";
import { useAuth } from "@/context/AuthContext";

export default function RegisterPage() {
  const router = useRouter();
  const { register } = useAuth();

  return (
    <AuthForm
      title="Đăng ký tài khoản"
      subtitle="Tạo tài khoản miễn phí để sử dụng ShieldAI"
      fields={[
        {
          name: "username",
          label: "Tên đăng nhập",
          type: "text",
          placeholder: "ten_cua_ban",
          autoComplete: "username",
        },
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
          placeholder: "Tối thiểu 6 ký tự",
          autoComplete: "new-password",
        },
      ]}
      submitLabel="Đăng ký"
      alternateLabel="Đã có tài khoản? Đăng nhập"
      alternateHref="/login"
      onSubmit={async (values) =>
        register({
          username: values.username,
          email: values.email,
          password: values.password,
        })
      }
      onSuccess={() => router.push("/analyze")}
    />
  );
}
