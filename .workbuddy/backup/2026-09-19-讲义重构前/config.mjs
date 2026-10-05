import { defineConfig } from 'vitepress'

export default defineConfig({
  title: '文献检索与研究方法',
  description: '高校《文献检索与研究方法》课程教学网站',
  lang: 'zh-CN',

  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '课程介绍', link: '/about/' },
      { text: '课程指南', link: '/guide/' },
      {
        text: '课程章节',
        items: [
          { text: '课程大纲', link: '/course-outline' },
          { text: '课程简介', link: '/course/01-course-introduction/why-thesis' },
          { text: '学术道德', link: '/course/02-academic-ethics/misconduct' },
          { text: '论文选题', link: '/course/03-topic-selection/principles' },
          { text: '知网文献检索', link: '/course/05-cnki-retrieval/keyword-system' },
          { text: 'Zotero 文献管理', link: '/course/06-zotero/setup-and-library' },
          { text: '文献综述', link: '/course/07-literature-review/purpose-and-scope' },
        ],
      },
    ],

    sidebar: {
      '/course/': [
        {
          text: '第一部分 课程简介',
          items: [
            { text: '为什么要写毕业论文', link: '/course/01-course-introduction/why-thesis' },
            { text: '课程目标与考核办法', link: '/course/01-course-introduction/objectives-and-assessment' },
            { text: '课堂流程与学习要求', link: '/course/01-course-introduction/workflow-and-expectations' },
          ],
        },
        {
          text: '第二部分 学术道德',
          items: [
            { text: '学术不端的类型与边界', link: '/course/02-academic-ethics/misconduct' },
            { text: '引用、转述与证据使用', link: '/course/02-academic-ethics/citation-and-evidence' },
            { text: '人工智能与研究诚信', link: '/course/02-academic-ethics/ai-and-integrity' },
            { text: '案例分析与自查', link: '/course/02-academic-ethics/cases' },
          ],
        },
        {
          text: '第三部分 关于论文选题',
          items: [
            { text: '选题的四项原则', link: '/course/03-topic-selection/principles' },
            { text: '税收学选题方向', link: '/course/03-topic-selection/tax-directions' },
            { text: '实证选题与变量设计', link: '/course/03-topic-selection/empirical-topic' },
            { text: '从兴趣到选题说明', link: '/course/03-topic-selection/workflow-and-feasibility' },
          ],
        },
        {
          text: '配套环节 开题报告',
          items: [
            { text: '开题报告的结构', link: '/course/04-opening-report/structure' },
            { text: '背景、意义与研究问题', link: '/course/04-opening-report/background-and-significance' },
            { text: '研究内容、方法与技术路线', link: '/course/04-opening-report/methods-and-roadmap' },
            { text: '进度安排与提交前检查', link: '/course/04-opening-report/checklist' },
          ],
        },
        {
          text: '第四部分 知网文献检索',
          items: [
            { text: '关键词体系与检索准备', link: '/course/05-cnki-retrieval/keyword-system' },
            { text: '检索式与筛选策略', link: '/course/05-cnki-retrieval/search-strategy' },
            { text: '结果判断与题录导出', link: '/course/05-cnki-retrieval/screening-and-export' },
            { text: '检索日志与研究脉络', link: '/course/05-cnki-retrieval/retrieval-log' },
          ],
        },
        {
          text: '第五部分 Zotero 文献管理',
          items: [
            { text: '安装、资料库与目录结构', link: '/course/06-zotero/setup-and-library' },
            { text: '题录、附件与阅读笔记', link: '/course/06-zotero/metadata-and-reading' },
            { text: 'Word 引用与参考文献表', link: '/course/06-zotero/citation-and-bibliography' },
            { text: '备份与完整工作流', link: '/course/06-zotero/backup-and-workflow' },
          ],
        },
        {
          text: '第六部分 撰写文献综述',
          items: [
            { text: '文献综述的任务与范围', link: '/course/07-literature-review/purpose-and-scope' },
            { text: '专题组织与段落结构', link: '/course/07-literature-review/organization' },
            { text: '归纳、比较与文献评述', link: '/course/07-literature-review/synthesis-and-critique' },
            { text: '从阅读卡片到综述初稿', link: '/course/07-literature-review/writing-practice' },
          ],
        },
      ],
      '/guide/': [
        {
          text: '课程指南',
          items: [{ text: '学习指南', link: '/guide/' }],
        },
      ],
      '/about/': [
        {
          text: '课程资源',
          items: [
            { text: '关于本课程', link: '/about/' },
            { text: '课程大纲', link: '/course-outline' },
          ],
        },
      ],
    },

    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: '搜索文档',
            buttonAriaLabel: '搜索文档',
          },
          modal: {
            displayDetails: '显示详细结果',
            resetButtonTitle: '清除搜索',
            backButtonTitle: '返回搜索',
            noResultsText: '无法找到相关结果',
            footer: {
              selectText: '选择',
              navigateText: '导航',
              closeText: '关闭',
            },
          },
        },
      },
    },

    outline: {
      level: [2, 3],
      label: '本页目录',
    },

    docFooter: {
      prev: '上一篇',
      next: '下一篇',
    },

    lastUpdatedText: '最后更新于',
    lastUpdatedAriaLabel: '最后更新于',
    returnToTopLabel: '返回顶部',
    sidebarMenuLabel: '目录菜单',
    skipToContentLabel: '跳转到主要内容',
    searchLabel: '搜索',
    darkModeSwitchLabel: '切换深色模式',
    lightModeSwitchTitle: '切换浅色模式',
    darkModeSwitchTitle: '切换深色模式',

    footer: {
      message: '基于 VitePress 构建',
      copyright: '© 课程教学团队',
    },
  },

  markdown: {
    config: () => {
      // 预留 Markdown 插件扩展位置
    },
  },

  ignoreDeadLinks: true,
})
