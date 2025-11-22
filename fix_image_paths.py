#!/usr/bin/env python3
"""
fix_image_paths.py

将 `I HATE CMS_FINAL.md` 中引用的绝对路径图片替换为相对路径 `typora-user-images/<filename>`。
用法:
    python3 fix_image_paths.py [path/to/markdown.md]

脚本行为:
- 备份原文件为 `<name>.bak`
- 支持常见 Markdown 图片语法: `![alt](path "title")`
- 支持 HTML 图片: `<img src="path">`
- 支持引用式链接定义: `[id]: path`
- 只有当 `typora-user-images/<basename>` 存在时才替换；否则报告未找到的文件
"""
import re
import sys
from pathlib import Path


def replace_paths(md_path: Path) -> int:
    if not md_path.exists():
        print(f"Error: file not found: {md_path}")
        return 0

    repo_dir = md_path.parent
    images_dir = repo_dir / 'typora-user-images'
    if not images_dir.is_dir():
        print(f"Warning: images directory not found: {images_dir}")

    text = md_path.read_text(encoding='utf-8')

    replaced = []
    not_found = []

    # 1) Markdown image syntax: ![alt](path "title") or ![alt](path)
    # Updated regex to handle paths with spaces (match everything until ) or optional "title")
    md_img_re = re.compile(r'!\[[^\]]*\]\(([^)]+?)\)')

    def md_img_sub(m):
        orig = m.group(0)
        full_path = m.group(1).strip()
        
        # Check if there's a title after the path (separated by space and quotes)
        # Format: path "title" or path 'title'
        title_match = re.search(r'^(.+?)\s+["\']([^"\']*)["\']$', full_path)
        if title_match:
            path_str = title_match.group(1).strip()
            title = title_match.group(2)
            has_title = True
        else:
            path_str = full_path
            title = None
            has_title = False
        
        if path_str.startswith(('http://', 'https://')):
            return orig
        # Check if it's already a relative path pointing to typora-user-images
        if path_str.startswith('typora-user-images/'):
            return orig
        # Extract filename from absolute or relative path
        name = Path(path_str).name
        candidate = images_dir / name
        if candidate.exists():
            new_path = f"typora-user-images/{name}"
            if has_title:
                new = orig.replace(full_path, f'{new_path} "{title}"')
            else:
                new = orig.replace(path_str, new_path)
            replaced.append((path_str, new_path))
            return new
        else:
            not_found.append(path_str)
            return orig

    text = md_img_re.sub(md_img_sub, text)

    # 2) HTML <img src="...">
    html_img_re = re.compile(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>')

    def html_img_sub(m):
        orig = m.group(0)
        path_str = m.group(1)
        if path_str.startswith(('http://', 'https://')):
            return orig
        if path_str.startswith('typora-user-images/'):
            return orig
        name = Path(path_str).name
        candidate = images_dir / name
        if candidate.exists():
            new = orig.replace(path_str, f"typora-user-images/{name}")
            replaced.append((path_str, f"Typora_Images/{name}"))
            return new
        else:
            not_found.append(path_str)
            return orig

    text = html_img_re.sub(html_img_sub, text)

    # 3) Reference-style link definitions: [id]: path
    ref_re = re.compile(r'^(\s*\[[^\]]+\]:\s*)(\S+)', re.MULTILINE)

    def ref_sub(m):
        prefix = m.group(1)
        path_str = m.group(2)
        if path_str.startswith(('http://', 'https://')):
            return m.group(0)
        if path_str.startswith('typora-user-images/'):
            return m.group(0)
        name = Path(path_str).name
        candidate = images_dir / name
        if candidate.exists():
            replaced.append((path_str, f"typora-user-images/{name}"))
            return prefix + f"typora-user-images/{name}"
        else:
            not_found.append(path_str)
            return m.group(0)

    text = ref_re.sub(ref_sub, text)

    # Backup original
    bak = md_path.with_suffix(md_path.suffix + '.bak')
    if not bak.exists():
        md_path.rename(bak)
        # write backup content (ensure encoding preserved)
        bak.write_text(bak.read_text(encoding='utf-8'), encoding='utf-8')
        original_content = bak.read_text(encoding='utf-8')
    else:
        original_content = bak.read_text(encoding='utf-8')

    # Save new content
    md_path.write_text(text, encoding='utf-8')

    # Report
    print(f"Processed: {md_path}")
    print(f"Images dir: {images_dir}")
    print(f"Replacements made: {len(replaced)}")
    for old, new in replaced:
        print(f" - {old} -> {new}")
    if not_found:
        print(f"Not found in {images_dir}: {len(not_found)} (listed below)")
        for p in sorted(set(not_found)):
            print(f" - {p}")

    return len(replaced)


def main(argv):
    md = Path(argv[1]) if len(argv) > 1 else Path('I HATE CMS_FINAL.md')
    replaced = replace_paths(md)
    if replaced > 0:
        print('Done.')
    else:
        print('No replacements made.')


if __name__ == '__main__':
    main(sys.argv)
