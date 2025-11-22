# 部署指南 🚀

本指南将帮助你将 MkDocs 文档站点部署到 GitHub Pages。

## 前提条件

- 已安装 Python 3.7+
- 已安装 Git
- 拥有 GitHub 账号
- 仓库已推送到 GitHub

## 快速部署

### 1. 确保虚拟环境已激活

```bash
cd "/Users/michael/Desktop/七德/QD G11/CS/I HATE CMS REPO"
source venv/bin/activate
```

### 2. 一键部署

```bash
mkdocs gh-deploy
```

这个命令会：
- 构建静态站点到 `site/` 目录
- 创建或更新 `gh-pages` 分支
- 将构建的站点推送到 GitHub
- 自动配置 GitHub Pages

### 3. 配置 GitHub Pages

部署后，访问你的 GitHub 仓库：

1. 进入 **Settings** → **Pages**
2. 在 **Source** 下，选择 `gh-pages` 分支
3. 点击 **Save**

几分钟后，你的站点就会在以下地址上线：
```
https://michaelmjhhhh.github.io/I-HATE-CMS/
```

## 本地预览

在部署前，建议先本地预览：

```bash
source venv/bin/activate
mkdocs serve
```

然后访问 http://127.0.0.1:8000/I-HATE-CMS/

## 更新站点

每次修改内容后，重新部署：

```bash
# 1. 提交更改到 main 分支
git add .
git commit -m "Update content"
git push origin main

# 2. 重新部署到 GitHub Pages
source venv/bin/activate
mkdocs gh-deploy
```

## 构建静态文件（可选）

如果只想生成静态文件而不部署：

```bash
mkdocs build
```

生成的文件将在 `site/` 目录中。

## 故障排除

### 问题：部署后 CSS/JS 文件 404

**解决方案**：检查 `mkdocs.yml` 中的 `site_url` 配置：

```yaml
site_url: "https://michaelmjhhhh.github.io/I-HATE-CMS/"
```

### 问题：图片无法显示

**解决方案**：确保图片路径是相对路径，且图片文件在 `docs/images/` 目录下。

### 问题：Mermaid 图表不渲染

**解决方案**：确保 `mkdocs.yml` 中包含 mermaid2 插件配置。

## 自定义域名（可选）

如果你有自定义域名：

1. 在 `docs/` 目录创建 `CNAME` 文件
2. 在文件中写入你的域名（如 `notes.example.com`）
3. 在域名提供商处配置 CNAME 记录指向 `michaelmjhhhh.github.io`

## 持续集成（可选）

使用 GitHub Actions 自动部署：

创建 `.github/workflows/deploy.yml`：

```yaml
name: Deploy MkDocs

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.x
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Deploy to GitHub Pages
        run: |
          mkdocs gh-deploy --force
```

这样每次推送到 main 分支时，站点会自动重新部署。

## 更多资源

- [MkDocs 官方文档](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [GitHub Pages 文档](https://docs.github.com/en/pages)

---

祝部署顺利！🎉
