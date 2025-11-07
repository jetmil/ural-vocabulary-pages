#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Исправляем путь к hero и убираем надпись "Замените на фото"

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Исправляем путь к hero-ural-mountains.jpg
content = content.replace(
    "url('hero-ural-mountains.jpg')",
    "url('images/hero-ural-mountains.jpg')"
)

# 2. Убираем .hero::before с надписью "Замените на фото"
old_hero_before = """        .hero::before {
            content: 'Замените на фото: Уральские горы, панорама, золотой час';
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 0.5rem 1rem;
            font-size: 0.8rem;
            border-radius: 4px;
            z-index: 10;
        }

        """

content = content.replace(old_hero_before, "")

# 3. Исправляем в @media print - убираем упоминание .hero::before
content = content.replace(
    ".hero::before, .word-image::after { display: none; }",
    ".word-image::after { display: none; }"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK: Hero image path fixed and placeholder text removed")
