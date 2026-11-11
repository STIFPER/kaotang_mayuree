# CLAUDE.md

กติกาเต็มอยู่ที่ **`AGENTS.md`** — ไฟล์นั้นเป็นฉบับหลักของทุกเอเจนต์ (Claude Code, Codex, ChatGPT)
ถ้าสองไฟล์ขัดกัน ให้ยึด `AGENTS.md`

@AGENTS.md

## สรุปสั้น — สิ่งที่ผิดพลาดบ่อยที่สุด

1. **ห้ามแก้ `.html` ตรง ๆ** — แก้ `_build/` แล้วรัน `sh _build/build.sh`
2. **เริ่มงานด้วย `git status --short`** — มีงานค้างของคนอื่นอยู่เสมอ ห้าม `checkout -- .` / `reset --hard` / `stash` / commit แทนคนอื่น
3. **เพิ่มข้อความไทย = ต้องเพิ่มคีย์ในพจนานุกรม `EN`** ท้าย `_build/master.html` ไม่งั้นโหมด EN โชว์ไทย
4. **ห้ามแตะ** `assets/flavor-*.svg`, `assets/pack-*.png`, `assets/package-graphics.css` (ของอีกคน)
5. **อย่าเพิ่ม dependency** — build ใช้ `python3 -I` ใช้ได้แค่ stdlib
6. **ก่อนบอกว่าเสร็จ**: build ผ่าน, ทุกหน้า 200, สลับ EN แล้วไม่มีไทยค้าง, ไม่ล้นที่ 375px
7. **commit เมื่อได้รับอนุญาตเท่านั้น**

พรีวิว: `python3 -m http.server 5173` → http://localhost:5173
