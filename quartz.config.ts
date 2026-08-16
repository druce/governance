import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 config for the AI Governance & Security Vendor Wiki.
 * This file is copied over the cloned Quartz tree by .github/workflows/deploy-quartz.yml.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "AI Governance & Security Vendor Wiki",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: "druce.ai/governance",
    ignorePatterns: ["private", "templates", ".obsidian", "raw", "tasks"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      // Field-guide theme, matched to https://druce.ai/governance_wiki/ so the two
      // sites read as one publication. Display serif (Fraunces) + reading serif
      // (Source Serif 4) + mono chrome (JetBrains Mono); warm paper light, deep ink
      // dark, one amber accent. custom.scss consumes these variables — keep the two
      // in sync, and see .github/workflows/deploy-quartz.yml, which copies
      // custom.scss into quartz/styles/ at build time.
      // Weights are explicit because custom.scss leans on 500/600, which Quartz
      // does not request by default — without these the browser would synthesise
      // them and headings would render heavier than the reference site.
      typography: {
        header: { name: "Fraunces", weights: [400, 500, 600, 700] },
        body: "Source Serif 4",
        code: { name: "JetBrains Mono", weights: [400, 500, 600] },
      },
      colors: {
        lightMode: {
          light: "#f7f3ea",
          lightgray: "#e2dac9",
          gray: "#8c8678",
          darkgray: "#33302a",
          dark: "#211f1a",
          secondary: "#9a5d12",
          tertiary: "#b3701a",
          highlight: "#b3701a1a",
          textHighlight: "#b3701a47",
        },
        darkMode: {
          light: "#15151a",
          lightgray: "#2c2c35",
          gray: "#837e74",
          darkgray: "#ded8ca",
          dark: "#ece6d8",
          secondary: "#d8a14a",
          tertiary: "#f0b657",
          highlight: "#e0a23e21",
          textHighlight: "#e0a23e4d",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: { light: "github-light", dark: "github-dark" },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "relative" }),
      Plugin.Description(),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({ enableSiteMap: true, enableRSS: true }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // CustomOgImages omitted intentionally — avoids the satori/og-image build step.
    ],
  },
}

export default config
