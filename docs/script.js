async function fetchMarkdownFiles() {
    const repoOwner = 'CodyCBakerPhD';
    const repoName = 'como_recipes_database';
    const directoryPath = '_markdown';
    const apiUrl = `https://api.github.com/repos/${repoOwner}/${repoName}/contents/${directoryPath}`;

    const response = await fetch(apiUrl);
    const files = await response.json();
    const contentDiv = document.getElementById('content');

    for (const file of files) {
        if (file.name.endsWith('.md')) {
            const fileResponse = await fetch(file.download_url);
            const markdown = await fileResponse.text();
            const html = marked(markdown);
            const div = document.createElement('div');
            div.className = 'markdown-content';
            div.innerHTML = html;
            contentDiv.appendChild(div);
        }
    }
}

fetchMarkdownFiles().then(r => console.log('done'));
