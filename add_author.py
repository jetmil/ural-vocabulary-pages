#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Добавление подписи автора в footer

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Проверяем, не добавлена ли уже подпись
if 'Created by Daria Agafonova' in content:
    print("Signature already exists")
else:
    lines = content.split('\n')

    # Находим строку "Sverdlovsk Oblast • 2025" и вставляем после нее подпись
    new_lines = []
    for line in lines:
        new_lines.append(line)
        if 'Sverdlovsk Oblast • 2025</p>' in line:
            # Вставляем подпись автора
            new_lines.append('            <div class="divider" style="background: rgba(255,255,255,0.3); margin: 2rem auto;"></div>')
            new_lines.append('            <p style="font-size: 0.95rem; color: rgba(255,255,255,0.9); margin-top: 1.5rem;">')
            new_lines.append('                Работа выполнена Агафоновой Дарьей')
            new_lines.append('            </p>')
            new_lines.append('            <p class="en-text" style="opacity: 0.9; font-size: 0.9rem;">')
            new_lines.append('                Created by Daria Agafonova')
            new_lines.append('            </p>')

    # Записываем обратно
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))

    print("OK: Signature added!")
