#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
移除文件中的 emoji 脚本

使用方法:
    python remove_emoji.py <文件路径>
    python remove_emoji.py <文件路径> --output <输出文件路径>
    python remove_emoji.py <文件路径> --inplace  # 直接修改原文件
"""

import re
import sys
import argparse
from pathlib import Path


def remove_emoji(text):
    """
    移除文本中的 emoji 字符

    使用安全的方式，只删除明确的 emoji 范围，避免误删中文等正常文字

    Args:
        text: 输入文本

    Returns:
        移除 emoji 后的文本
    """
    # 使用精确且安全的 emoji Unicode 范围
    # 避免包含中文字符范围 (CJK: \u4e00-\u9fff)
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # 表情符号 (Emoticons)
        "\U0001F300-\U0001F5FF"  # 符号和象形文字 (Miscellaneous Symbols and Pictographs)
        "\U0001F680-\U0001F6FF"  # 交通和地图符号 (Transport and Map Symbols)
        "\U0001F1E0-\U0001F1FF"  # 旗帜 (Flags)
        "\U0001F900-\U0001F9FF"  # 补充符号和象形文字 (Supplemental Symbols and Pictographs)
        "\U0001FA00-\U0001FA6F"  # 扩展-A (Extended-A)
        "\U0001FA70-\U0001FAFF"  # 扩展-B (Extended-B)
        "]+",
        flags=re.UNICODE
    )

    # 移除 emoji
    cleaned = emoji_pattern.sub('', text)

    # 额外处理：移除一些常见的单个特殊符号 emoji
    # 这些符号通常用作装饰，不是文档的核心内容
    # 注意：这里只删除明确的 emoji，不删除普通符号
    common_emojis = [
        # 常见的勾选和标记
        '✅', '❌', '⚠️', '⚠', '✓', '✔️', '✔', '✗', '✘',
        # 新增和循环标记
        '🆕', '🔄', '🔃', '🔁',
        # 其他常见装饰 emoji
        '🎯', '💡', '📝', '🚀', '⚡', '🔥', '💻', '📱', '🌟', '⚙️',
        '⭐', '🌠', '💫', '✨', '🎉', '🎊', '🎈',
        # 箭头和指示
        '➡️', '⬅️', '⬆️', '⬇️', '↗️', '↘️', '↙️', '↖️',
        '▶️', '◀️', '🔼', '🔽',
    ]

    for emoji in common_emojis:
        # 删除 emoji 及其后面紧跟的一个空格（如果有）
        cleaned = cleaned.replace(emoji + ' ', '')
        # 再删除没有空格的 emoji
        cleaned = cleaned.replace(emoji, '')

    return cleaned


def process_file(input_path, output_path=None, inplace=False):
    """
    处理文件，移除其中的 emoji

    Args:
        input_path: 输入文件路径
        output_path: 输出文件路径（可选）
        inplace: 是否直接修改原文件
    """
    input_path = Path(input_path)

    if not input_path.exists():
        print(f"错误: 文件不存在: {input_path}")
        sys.exit(1)

    # 读取文件
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"错误: 无法读取文件: {e}")
        sys.exit(1)

    # 移除 emoji
    original_length = len(content)
    cleaned_content = remove_emoji(content)
    removed_count = original_length - len(cleaned_content)

    # 确定输出路径
    if inplace:
        output_path = input_path
    elif output_path is None:
        # 默认输出到 原文件名_no_emoji.扩展名
        stem = input_path.stem
        suffix = input_path.suffix
        output_path = input_path.parent / f"{stem}_no_emoji{suffix}"
    else:
        output_path = Path(output_path)

    # 写入文件
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)

        print(f"✓ 处理完成!")
        print(f"  输入文件: {input_path}")
        print(f"  输出文件: {output_path}")
        print(f"  移除字符数: {removed_count}")

    except Exception as e:
        print(f"错误: 无法写入文件: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='移除文件中的 emoji 字符',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 输出到新文件（默认添加 _no_emoji 后缀）
  python remove_emoji.py document.md

  # 指定输出文件
  python remove_emoji.py document.md --output clean_document.md

  # 直接修改原文件
  python remove_emoji.py document.md --inplace
        """
    )

    parser.add_argument('input', help='输入文件路径')
    parser.add_argument('-o', '--output', help='输出文件路径（可选）')
    parser.add_argument('-i', '--inplace', action='store_true',
                       help='直接修改原文件')

    args = parser.parse_args()

    process_file(args.input, args.output, args.inplace)


if __name__ == '__main__':
    main()

