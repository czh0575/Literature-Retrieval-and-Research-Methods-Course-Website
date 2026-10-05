# 文献检索与研究方法 - 课程网站

基于 [VitePress](https://vitepress.dev/) 搭建的课程教学网站。

## 环境要求

- Node.js ≥ 18.0.0
- npm ≥ 9.0.0(或 pnpm / yarn)

## 快速开始

```bash
# 1. 安装依赖(首次使用)
npm install

# 2. 启动本地开发服务器(默认 http://localhost:4321)
npm run docs:dev

# 3. 构建静态站点(输出到 docs/.vitepress/dist)
npm run docs:build

# 4. 本地预览构建结果(默认 http://localhost:4321)
npm run docs:preview
```

## 目录结构

```
web/
├── docs/                       # 网站源文件
│   ├── .vitepress/
│   │   └── config.mjs         # VitePress 配置（导航与侧边栏的唯一入口）
│   ├── index.md               # 首页（hero 主图见 public/logo.svg）
│   ├── course-outline.md      # 课程大纲
│   ├── course/                # 课程章节（第一部分至第七部分）
│   └── public/
│       ├── logo.svg           # 网站主图（首页 hero 图片）
│       ├── images/            # 讲义配图（cnki / foreign / zotero）
│       └── attachments/       # 教学文件
├── package.json
└── README.md
```

首页的 hero 图片由 `docs/public/logo.svg` 提供，在 `docs/index.md` 的 `hero.image.src` 中引用；
若要在顶栏也显示同名标识，可通过 `themeConfig.logo: '/logo.svg'` 启用。

## 添加新章节

1. 在 `docs/` 下创建新的 `.md` 文件(如 `docs/chapter-01/index.md`)
2. 在 `docs/.vitepress/config.mjs` 的 `sidebar` 中添加导航项
3. 保存后开发服务器会自动热更新

## 部署

构建后的静态文件位于 `docs/.vitepress/dist/`,可直接部署到:

- GitHub Pages
- Vercel / Netlify
- 任意静态网站托管服务

详细部署文档: <https://vitepress.dev/guide/deploy>
