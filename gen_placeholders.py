#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成个人展示平台的本地 SVG 占位图（离线可见）。"""
import os

OUT = os.path.join(os.path.dirname(__file__), "assets", "img")
os.makedirs(OUT, exist_ok=True)


def gradient_svg(name, w, h, c1, c2, label, icon=None, kind="rect"):
    icon_mark = ""
    if icon:
        icon_mark = (
            f'<text x="{w/2}" y="{h/2 - 18}" font-size="{min(w,h)*0.22:.0f}" '
            f'text-anchor="middle" fill="rgba(255,255,255,0.92)">{icon}</text>'
        )
    label_mark = (
        f'<text x="{w/2}" y="{h/2 + min(w,h)*0.18:.0f}" font-size="{min(w,h)*0.10:.0f}" '
        f'font-family="sans-serif" font-weight="600" text-anchor="middle" '
        f'fill="rgba(255,255,255,0.95)">{label}</text>'
    )
    gid = f"g_{name}"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{c1}"/>
      <stop offset="1" stop-color="{c2}"/>
    </linearGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#{gid})"/>
  {icon_mark}
  {label_mark}
</svg>'''


def avatar_svg():
    w, h = 400, 500
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <linearGradient id="av" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#5b6cff"/>
      <stop offset="1" stop-color="#ff7a59"/>
    </linearGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#av)"/>
  <circle cx="{w/2}" cy="{h*0.40}" r="78" fill="rgba(255,255,255,0.92)"/>
  <path d="M70 {h} C70 {h*0.66} {w*0.30} {h*0.58} {w/2} {h*0.58} C{w*0.70} {h*0.58} {w-70} {h*0.66} {w-70} {h} Z" fill="rgba(255,255,255,0.92)"/>
  <text x="{w/2}" y="{h-26}" font-size="20" font-family="sans-serif" font-weight="700" text-anchor="middle" fill="rgba(255,255,255,0.95)">你的照片</text>
</svg>'''


# 照片占位（人像/风光/街拍 不同色调）
photos = [
    ("photo-1", 800, 800, "#7b8cff", "#5566dd", "人像 · 午后", "📷"),
    ("photo-2", 800, 800, "#46c2c6", "#2a8fb0", "风光 · 城市", "🌆"),
    ("photo-3", 800, 800, "#ff8a65", "#d9544d", "街拍 · 雨夜", "🌃"),
    ("photo-4", 800, 800, "#a78bfa", "#7c5cff", "人像 · 窗边", "📷"),
    ("photo-5", 800, 800, "#34d399", "#0e9488", "风光 · 海岸", "🌊"),
    ("photo-6", 800, 800, "#f472b6", "#be2fa0", "街拍 · 霓虹", "💡"),
]

# 舞蹈占位
dance = ("dance", 800, 600, "#8b5cf6", "#ec4899", "舞蹈展示", "💃")

# 项目缩略图
projects = [
    ("proj-1", 800, 450, "#5b6cff", "#3b4fd6", "项目一", "💻"),
    ("proj-2", 800, 450, "#0ea5e9", "#0369a1", "项目二", "📊"),
    ("proj-3", 800, 450, "#f59e0b", "#d97706", "项目三", "🗄"),
    ("proj-4", 800, 450, "#10b981", "#047857", "项目四", "📱"),
]

files = {}
files["avatar.svg"] = avatar_svg()
for name, w, h, c1, c2, label, icon in photos:
    files[f"{name}.svg"] = gradient_svg(name, w, h, c1, c2, label, icon)
files[f"{dance[0]}.svg"] = gradient_svg(*dance)
for name, w, h, c1, c2, label, icon in projects:
    files[f"{name}.svg"] = gradient_svg(name, w, h, c1, c2, label, icon)

for fname, content in files.items():
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(content)
    print("written:", fname)

print("total:", len(files))
