#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Убираем информацию об организации, оставляем только заголовок и автора

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Заменяем футер
old_footer = """    <!-- FOOTER -->
    <footer class="footer">
        <div class="container">
            <p style="font-size: 1.1rem; margin-bottom: 1.5rem;">
                Всероссийский конкурс по региональной лексикографии<br>
                «Мне всё родное в этом слове»
            </p>
            <p class="en-text" style="opacity: 1;">
                All-Russian Competition in Regional Lexicography<br>
                "Everything Native to Me in This Word"
            </p>
            <div class="divider" style="background: rgba(255,255,255,0.3);"></div>
            <p>Астраханский государственный университет им. В.Н. Татищева</p>
            <p class="en-text" style="opacity: 1;">Astrakhan State University named after V.N. Tatishchev</p>
            <p>Свердловская область • 2025</p>
            <p class="en-text" style="opacity: 1;">Sverdlovsk Oblast • 2025</p>
            <div class="divider" style="background: rgba(255,255,255,0.3); margin: 2rem auto;"></div>
            <p style="font-size: 0.95rem; color: rgba(255,255,255,0.9); margin-top: 1.5rem;">
                Работа выполнена Агафоновой Дарьей
            </p>
            <p class="en-text" style="opacity: 0.9; font-size: 0.9rem;">
                Created by Daria Agafonova
            </p>
        </div>
    </footer>"""

new_footer = """    <!-- FOOTER -->
    <footer class="footer">
        <div class="container">
            <p style="font-size: 1.3rem; margin-bottom: 1rem; font-weight: 600;">
                Региональный словарь Свердловской области
            </p>
            <p class="en-text" style="opacity: 1; font-size: 1.1rem;">
                Regional Vocabulary of Sverdlovsk Oblast
            </p>
            <div class="divider" style="background: rgba(255,255,255,0.3); margin: 2rem auto;"></div>
            <p style="font-size: 1.1rem; color: rgba(255,255,255,0.95);">
                Агафонова Дарья
            </p>
            <p class="en-text" style="opacity: 0.9;">
                Daria Agafonova
            </p>
            <p style="margin-top: 1.5rem; font-size: 0.95rem;">Свердловская область • 2025</p>
            <p class="en-text" style="opacity: 0.8; font-size: 0.9rem;">Sverdlovsk Oblast • 2025</p>
        </div>
    </footer>"""

content = content.replace(old_footer, new_footer)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK: Footer updated - removed organization info")
