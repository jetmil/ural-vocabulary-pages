#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Убираем черную полосу на картинках и исправляем имя файла

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Удаляем CSS для черной полосы (.word-image::after)
old_css = """        .word-image::after {
            content: attr(data-instruction);
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 90%;
            text-align: center;
            background: rgba(0,0,0,0.8);
            color: white;
            padding: 2rem;
            font-size: 0.9rem;
            line-height: 1.6;
            border-radius: 4px;
        }

        """

content = content.replace(old_css, "")

# 2. Исправляем имя файла с украинской буквой на английскую
content = content.replace('khrenovіna', 'khrenovina')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK: Black bar removed, filename fixed")
