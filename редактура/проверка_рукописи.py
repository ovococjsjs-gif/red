#!/usr/bin/env python3
"""Поабзацная сверка DOCX/Markdown и техническая проверка последнего блока.

Запуск из любой папки: python3 редактура/проверка_рукописи.py
Литературные оценки (естественность диалога, мотивы, достоверность толкования)
этот скрипт не подменяет. Он проверяет воспроизводимые ограничения.
"""
from pathlib import Path
import json
import re
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / 'Хроники_Этериума_Осколки_Бездны_редакция.docx'
NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
LAST_EDITED = 25
LAST_BLOCK = range(21, 26)
SHADOW = {
    21: [11363, 11688, 11691, 11693, 11696, 11724],
    22: [11902, 11904, 11945, 12110, 12112, 12373],
    23: [12397, 12399, 12401, 12700, 12835, 12837, 12866, 12887, 12889],
    24: [12901, 12921, 12923, 12926, 13048, 13184, 13222, 13224,
         13411, 13413, 13474],
    25: [13489, 13491, 13666, 13668, 13671, 13691, 13785, 13788,
         13791, 13793, 13834, 13836, 13859, 13861, 13863, 13865,
         13869, 13874, 13876],
}
FORBIDDEN = re.compile(
    r'\b(?:эфирн\w*|сантиметр\w*|секунд\w*|покамест|дозвол\w*|'
    r'ретиров\w*|ежели|поутру|воссед\w*|осведом\w*)\b', re.I)
COUNTER_FORMULA = re.compile(r'\bне\b[^.!?…\n]*[,—–]\s*а\b', re.I)
PART_START = re.compile(
    r'^(?:[А-ЯЁ][а-яё]+(?:вшись|ившись|вши|ши)\b|'
    r'(?:Закрыв|Открыв|Прикрыв|Разжав|Сжав|Подняв|Опустив|Убрав|'
    r'Удерживая|Держа|Глядя|Лёжа|Лежа|Сидя|Стоя|Перехватив|'
    r'Прочитав|Повернув|Показав|Передав)\b)')


def indexed_source(chapter):
    result = {}
    for line in (ROOT / 'chapters' / f'ch_{chapter:02d}.txt').read_text().splitlines():
        match = re.match(r'^\[(\d+)\]\s*(.*)$', line)
        if match:
            result[int(match[1])] = match[2]
    return result


def verify():
    with zipfile.ZipFile(DOCX) as package:
        assert package.testzip() is None, 'Повреждён ZIP-контейнер DOCX'
        document = package.read('word/document.xml')
    root = ET.fromstring(document)
    paragraphs = [
        ''.join(t.text or '' for t in p.findall('.//w:t', NS))
        for p in root.findall('w:body/w:p', NS)
    ]
    assert len(paragraphs) == 20363, 'Изменилось число индексированных абзацев'
    starts = [
        (i, int(match[1])) for i, p in enumerate(paragraphs)
        if i >= 50 and (match := re.fullmatch(r'ГЛАВА (\d+)', p))
    ]
    assert [n for _, n in starts] == list(range(1, 39))
    ranges = {}
    for k, (a, n) in enumerate(starts):
        b = starts[k + 1][0] - 1 if k + 1 < len(starts) else len(paragraphs) - 1
        ranges[n] = (a, b)
        if n <= LAST_EDITED:
            md = (ROOT / f'Глава_{n:02d}_редакция.md').read_text().strip()
            md_paragraphs = re.split(r'\n\s*\n', md)
            md_paragraphs[0] = md_paragraphs[0].removeprefix('# ').strip()
            assert md_paragraphs == paragraphs[a:b + 1], f'DOCX/MD: глава {n}'
        else:
            original = indexed_source(n)
            assert all(paragraphs[i] == p for i, p in original.items()), (
                f'Затронута ещё не редактировавшаяся глава {n}')

    report = []
    for n in LAST_BLOCK:
        a, b = ranges[n]
        body = [(i, paragraphs[i]) for i in range(a + 1, b + 1)
                if paragraphs[i] != '· · ·']
        original = indexed_source(n)
        old_body = [p for i, p in original.items() if i > a and p != '· · ·']
        words = sum(len(p.split()) for _, p in body)
        old_words = sum(len(p.split()) for p in old_body)
        sentences = sum(len(re.findall(r'[.!?…]+', p)) for _, p in body)
        ya_starts = sum(p.startswith('Я ') for _, p in body)
        ya_pairs = [(i - 1, i) for i, p in body
                    if p.startswith('Я ') and paragraphs[i - 1].startswith('Я ')]
        assert not ya_pairs, (n, 'Повторные зачины Я', ya_pairs)
        assert 0.04 <= ya_starts / len(body) <= 0.08, (n, 'Доля зачинов Я')
        for i, p in body:
            assert ';' not in p, (i, 'Точка с запятой')
            assert not FORBIDDEN.search(p), (i, 'Запрещённая лексика')
            assert not COUNTER_FORMULA.search(p), (i, 'Шаблон не X, а Y')
            assert not PART_START.match(p), (i, 'Шаблонный деепричастный зачин')
            for sentence in re.split(r'(?<=[.!?…])\s+', p):
                assert len(sentence.split()) <= 28, (i, 'Предложение длиннее 28 слов')
        for i in SHADOW[n]:
            assert paragraphs[i].startswith('«') and '»' in paragraphs[i], (
                i, 'Не оформлена реплика Тени')
        report.append({
            'глава': n, 'диапазон': [a, b], 'индексированных_абзацев': b - a + 1,
            'абзацев_без_заголовка_и_разделителей': len(body),
            'слов_исходник': old_words, 'слов_редакция': words,
            'изменение_процентов': round((words / old_words - 1) * 100, 2),
            'среднее_слов_на_предложение': round(words / sentences, 2),
            'зачины_Я_процентов': round(100 * ya_starts / len(body), 2),
            'поабзацная_синхронизация': '100%',
        })
    # Earlier continuity repairs and the financial anchor at the end of the block.
    assert 'из моих восемнадцати' in paragraphs[7307]
    assert 'шестнадцать серебряных монет' in paragraphs[13828]
    assert 'пяти' in paragraphs[13829] and 'Эфир' in paragraphs[13829]
    assert 'Она не просила' in paragraphs[19998]
    assert 'Способностей Мизу у меня нет.' in paragraphs[20338]
    print('DOCX цел. Все 25 отредактированных глав синхронизированы с Markdown.')
    print('Главы 26–38 совпадают с исходными главами. Индексы сохранены.')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


if __name__ == '__main__':
    verify()
