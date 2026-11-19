"""ลดงานตอนโหลดหน้า (ไม่เปลี่ยนหน้าตา/ข้อความ): รูปที่ไม่ได้อยู่ในจอแรกให้โหลดทีหลัง
เพื่อไม่ให้แย่งแบนด์วิดท์กับสคริปต์และรูปสินค้าหลัก ใช้เฉพาะ standard library"""
import re

_IMG = re.compile(r'<img\b[^>]*>')

def lazyfy(html):
    def add(m):
        tag = m.group(0)
        if 'loading=' in tag or 'fetchpriority' in tag:
            return tag
        end = '/>' if tag.endswith('/>') else '>'
        extra = ' loading="lazy"' + ('' if 'decoding=' in tag else ' decoding="async"')
        return tag[:-len(end)].rstrip() + extra + end
    return _IMG.sub(add, html)
