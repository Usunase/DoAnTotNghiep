import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        ink: {
          DEFAULT: "#0a0a0f",
          soft: "#111118",
          muted: "#1a1a24",
        },
        ocean: {
          DEFAULT: "#0ea5e9",
          deep: "#0284c7",
          dark: "#0369a1",
          glow: "#38bdf8",
        },
        surface: {
          DEFAULT: "#ffffff",
          soft: "#f8fafc",
          border: "#e2e8f0",
        },
      },
      fontFamily: {
        sans: ["var(--font-inter)", "system-ui", "sans-serif"],
        display: ["var(--font-space)", "system-ui", "sans-serif"],
      },
      boxShadow: {
        premium: "0 24px 80px -24px rgba(14, 165, 233, 0.25)",
        card: "0 4px 24px -4px rgba(0, 0, 0, 0.08)",
        glow: "0 0 60px -12px rgba(14, 165, 233, 0.4)",
      },
      backgroundImage: {
        "hero-gradient":
          "radial-gradient(ellipse 80% 60% at 50% -20%, rgba(14, 165, 233, 0.18), transparent 60%), linear-gradient(180deg, #0a0a0f 0%, #111118 100%)",
        "ocean-gradient": "linear-gradient(135deg, #0ea5e9 0%, #0284c7 50%, #0369a1 100%)",
      },
      animation: {
        "fade-up": "fadeUp 0.6s ease-out forwards",
        float: "float 6s ease-in-out infinite",
      },
      keyframes: {
        fadeUp: {
          "0%": { opacity: "0", transform: "translateY(24px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        float: {
          "0%, 100%": { transform: "translateY(0)" },
          "50%": { transform: "translateY(-12px)" },
        },
      },
    },
  },
  plugins: [],
};

export default config;
