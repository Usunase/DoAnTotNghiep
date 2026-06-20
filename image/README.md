# Sơ đồ kiến trúc (Mermaid)

| File | Nội dung |
|------|----------|
| `mermaid_1.mmd` | Kiến trúc 3 tầng — PhoBERT text-only + MLP |
| `mermaid_2.mmd` | ERD SQLite (users, history) |
| `mermaid_3.mmd` | Lưu đồ suy luận + verdict 3 mức |

Sau khi sửa `.mmd`, tái tạo PNG:

```bash
cd image
npx @mermaid-js/mermaid-cli -i mermaid_1.mmd -o mermaid_1.png -b white
npx @mermaid-js/mermaid-cli -i mermaid_3.mmd -o mermaid_3.png -b white
```

Hoặc dán nội dung `.mmd` vào https://mermaid.live để export PNG.
