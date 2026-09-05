// The chrome every page shares: the document shell, the top bar, and the tag colors.

import type { Database } from "../models.ts";

const GITHUB_REPOSITORY_URL = "https://github.com/CodyCBakerPhD/como_recipes";

// The GitHub "mark" octicon, inlined so pages have no external image dependencies
const GITHUB_ICON_PATH =
  "M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49" +
  "-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58" +
  " 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59" +
  ".82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27" +
  " 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65" +
  " 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8" +
  "c0-4.42-3.58-8-8-8z";

const GITHUB_LINK_HTML =
  `<a class="icon-link" href="${GITHUB_REPOSITORY_URL}" aria-label="View source on GitHub">` +
  `<svg viewBox="0 0 16 16" aria-hidden="true"><path d="${GITHUB_ICON_PATH}"/></svg></a>`;

const THEME_TOGGLE_HTML =
  '<button class="theme-toggle" type="button" onclick="comoToggleTheme()" aria-label="Toggle color theme"></button>';

// Mirrors Python's `html.escape` (quote=True), which the original site generator used.
export function escapeHtml(text: string): string {
  return text
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#x27;");
}

// Hues are spread evenly over the alphabetized tag universe so every tag chip gets a distinct color
export function tagHue(tag: string, database: Database): number {
  const index = database.tags.indexOf(tag);
  return index < 0 ? 0 : Math.floor((index * 360) / database.tags.length);
}

export interface PageOptions {
  title: string;
  bodyClass: string;
  // Path from the page's directory back to the site root, e.g. "../" for recipe pages
  rootPath?: string;
  // Extra <script> tags for the head, beyond the theme script every page loads
  scripts?: string[];
  // Leading top-bar content; defaults to the brand link back to the index
  topBarLead?: string;
  // Top-bar actions placed before the theme toggle and GitHub link
  topBarActions?: string[];
  body: string;
}

export function pageHtml(options: PageOptions): string {
  const rootPath = options.rootPath ?? "";
  const brandHtml = `<a class="brand" href="${rootPath}index.html">
            <img class="brand-logo" src="${rootPath}assets/como_logo.jpg" alt="CoMo logo">
            <span>CoMo Recipes</span>
        </a>`;
  const headScripts = [`<script src="${rootPath}assets/theme.js"></script>`, ...(options.scripts ?? [])];
  const topBarActions = [...(options.topBarActions ?? []), THEME_TOGGLE_HTML, GITHUB_LINK_HTML];

  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${escapeHtml(options.title)}</title>
    <link rel="icon" href="${rootPath}assets/como_icon.ico">
    <link rel="stylesheet" href="${rootPath}assets/style.css">
    ${headScripts.join("\n    ")}
</head>
<body class="${options.bodyClass}">
    <nav class="top-bar">
        ${options.topBarLead ?? brandHtml}
        <div class="top-actions">
            ${topBarActions.join("\n            ")}
        </div>
    </nav>
${options.body}
</body>
</html>
`;
}
