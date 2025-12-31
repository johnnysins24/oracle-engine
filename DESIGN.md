# Oracle Engine - Design Principles

## Product Scope

**Oracle Engine เป็น Text-Only API**

### ✅ สิ่งที่ทำ
- คำนวณดวงชะตา (Tarot, Thai, Western)
- ส่งข้อมูลเป็น JSON
- AI ตีความเป็นข้อความ

### ❌ สิ่งที่ไม่ทำ
- **ไม่สร้างรูปภาพ** (No image generation)
- ไม่มี Tarot card images
- ไม่มี chart visualizations

### เหตุผล
1. ประหยัด API cost (Image gen แพง)
2. เรียบง่าย ไม่ซับซ้อน
3. ให้ลูกค้า customize UI เอง

---

## API Response Format

**ทุก endpoint ส่งกลับ JSON text เท่านั้น:**

```json
{
  "interpretation": "คำทำนาย...",
  "data": {
    "cards": [...],
    "year_animal": "...",
    "sun_sign": "..."
  }
}
```

**ไม่มี:**
- `image_url`
- `chart_svg`
- `base64_image`
