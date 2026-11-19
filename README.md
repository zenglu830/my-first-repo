# my-first-repo

我的第一个 GitHub 仓库，也是 Git 工作流的练手模板。

## 目录结构

```
my-first-repo/
├── README.md          # 仓库首页说明（现在看的这份）
├── .gitignore         # 告诉 Git 哪些文件不要提交
├── docs/              # 文档、笔记、说明类文件
│   └── 使用说明.md
└── src/               # 代码、脚本
    └── hello.py
```

## 常用命令

```bash
git status           # 查看当前有哪些改动
git add .            # 把所有改动放进待提交区
git commit -m "说明"   # 打包成一个版本
git push             # 上传到 GitHub
git log --oneline    # 查看提交历史
```

## 三个容易搞混的概念

| 概念 | 含义 |
|---|---|
| 工作区 | 你电脑上实际的文件 |
| 暂存区 | `git add` 之后、`commit` 之前的中间状态 |
| 版本库 | `commit` 之后留下的历史快照 |

- 创建时间：2026-11-19