# เว็บไซต์ มยุรี ข้าวตังทรงเครื่อง

เว็บสแตติก (HTML/CSS/JS ล้วน ไม่ต้องติดตั้งอะไร) ภาษาไทย/อังกฤษ ฟอนต์ Thonglor Soi 4 จาก Adobe Fonts

## ดูตัวอย่างในเครื่อง

```bash
python3 -m http.server 5173
```

แล้วเปิด http://localhost:5173

## โครงสร้าง

| ที่ | คืออะไร |
|---|---|
| `index.html` `shop.html` `story.html` `craft.html` `gift.html` `visit.html` `corporate.html` `404.html` | หน้าเว็บ **สร้างอัตโนมัติจาก `_build/`** อย่าแก้ตรงนี้ |
| `_build/` | ต้นฉบับของทุกหน้า (แก้ที่นี่ แล้วรัน `_build/build.sh`) **ไม่ต้องอัปขึ้นเว็บ** |
| `assets/photos/` | รูปถ่าย ตั้งชื่อตามเนื้อหา (ดูด้านล่าง) |
| `assets/video/` | วิดีโอ hero และเตาถ่าน |
| `assets/icons/` | ไอคอนเว็บ / แอปบนมือถือ |
| `assets/lineart-*.png` | ภาพลายเส้น |
| `assets/presentation.*` `assets/mobile.*` | สไตล์และสคริปต์ของหน้าเว็บ (ส่วนมือถือและการแสดงผล) |
| `assets/flavor-*.svg` `assets/pack-*.png` `assets/package-graphics.css` | กราฟิกแพ็กเกจ **ดูแลโดยอีกคน** อย่าแก้หรือย้อนกลับ |
| `site.webmanifest` `robots.txt` `favicon.ico` | ไฟล์ประกอบเว็บ |

โฟลเดอร์ `web-มยุรี-ไม่ได้ใช้` (อยู่ข้างๆ โฟลเดอร์นี้) เก็บไฟล์ที่เลิกใช้แล้ว เผื่อกลับมาใช้ ไม่ได้ลบทิ้ง

## วิธีแก้ไข

1. แก้ข้อความ/โครงสร้างที่ `_build/master.html` (ทุกหน้าที่ใช้ร่วมกัน) หรือ `_build/build_home.py` (หน้าแรก) หรือ `_build/build_pages.py` (หน้าอื่น)
2. ข้อความภาษาอังกฤษอยู่ในพจนานุกรม `EN` ท้ายไฟล์ `_build/master.html` (และ `_build/build_home.py` สำหรับหน้าแรก) เพิ่มคู่ไทย → อังกฤษที่นั่น
3. ชื่อหน้า/คำอธิบายสำหรับ Google และการแชร์: `_build/pagemeta.json`
4. รัน `_build/build.sh` แล้วรีเฟรชหน้าเว็บ

ถ้าแก้ไฟล์ `.html` ตรงๆ แล้วรัน build ทีหลัง สิ่งที่แก้จะหาย

## ตั้งชื่อรูป

`หมวด-อธิบายสั้นๆ.jpg` ตัวพิมพ์เล็ก ใช้ขีดกลาง ไม่มีช่องว่างหรือเลขรหัสกล้อง

| หมวด | ใช้กับ |
|---|---|
| `product-` | สินค้า ชาม กล่อง |
| `mini-` | กล่อง Mini 95 g |
| `gift-` | ชุดของขวัญ |
| `store-` | หน้าร้านและภายใน |
| `story-` | เรื่องราวของแบรนด์ |
| `process-` | ขั้นตอนทำข้าวตัง |
| `quality-` | แถว "กรอบ หอม กลมกล่อม" |
| `lifestyle-` | ภาพบรรยากาศ |

เปลี่ยนชื่อรูปแล้วต้องแก้ทุกที่ที่อ้างถึง ค้นชื่อเดิมทั้งใน `_build/` และ `assets/*.js` `assets/*.css` แล้วรัน build

## ฟอนต์

Thonglor Soi 4 โหลดจาก Adobe Fonts โปรเจกต์ `mayuree-web` (บรรทัด `use.typekit.net` ในหัวทุกหน้า) ไม่ต้องวางไฟล์ฟอนต์ในโฟลเดอร์นี้ ถ้าต้องการน้ำหนักเพิ่ม (Regular / SemiBold / ExtraBold) ให้เพิ่มในโปรเจกต์ Adobe แล้วกดเผยแพร่

## ที่เก็บบน GitHub และการขึ้นเว็บ

- repo: https://github.com/STIFPER/kaotang_mayuree (เว็บตัวอย่าง: https://stifper.github.io/kaotang_mayuree/)
- repo นี้มีทั้งไฟล์เว็บและต้นฉบับใน `_build/` เพื่อให้คนอื่นแก้ต่อได้ แก้ที่ `_build/` แล้วรัน `_build/build.sh` แล้ว commit ทั้งหมด
- ถ้าจะอัปขึ้นโฮสต์ที่ไม่ใช่ GitHub Pages อัปเฉพาะ: ไฟล์ `.html`, `assets/`, `site.webmanifest`, `robots.txt`, `favicon.ico` (ไม่ต้องอัป `_build/` และ `README.md`)

## ฟอนต์และใบอนุญาต

เว็บนี้โหลด Thonglor Soi 4 จากโปรเจกต์ Adobe Fonts `mayuree-web` (ID `csi6fno`) ซึ่งตอนนี้อยู่ในบัญชี Adobe ของผู้ทำเว็บ ข้อกำหนดของ Adobe ระบุว่าเว็บของลูกค้าควรโหลดฟอนต์ผ่านบัญชี Creative Cloud ของเจ้าของธุรกิจเอง ผู้ดูแลต่อควรโอนโปรเจกต์ไปบัญชีเจ้าของร้าน (Adobe Fonts > Web Projects) หรือซื้อสิทธิ์โฮสต์ฟอนต์จาก Cadson Demak ห้ามนำไฟล์ฟอนต์มาวางในโฟลเดอร์เว็บเอง

โปรเจกต์ต้องตั้งชุดตัวอักษรเป็น "All Characters" ไม่เช่นนั้นตัวไทยของน้ำหนักบางตัวจะตกไปใช้ฟอนต์สำรอง

## ก่อนขึ้นโดเมนจริง

- ใส่โดเมนจริงใน `og:image` / `og:url` ของทุกหน้า (ตอนนี้เป็น `assets/og-image.jpg` แบบไม่มีโดเมน บางแอปแชร์ลิงก์ต้องการ URL เต็ม) และเพิ่ม `sitemap.xml` กับบรรทัด `Sitemap:` ใน `robots.txt`
