// Powers the recipe index's "List Mode": tick as many recipes as you like, then
// hand the selection off to shopping_list.html, which totals up their ingredients.
(() => {
    const modeToggle = document.getElementById("list-mode-toggle");
    const selectionBar = document.querySelector(".selection-bar");
    if (modeToggle == null || selectionBar == null) {
        return;
    }

    const selectionCount = selectionBar.querySelector(".selection-count");
    const buildLink = selectionBar.querySelector(".build-list");
    const clearButton = selectionBar.querySelector(".clear-selection");
    const items = Array.from(document.querySelectorAll(".letter-section li"));

    const RECIPES_PARAMETER = "recipes";
    // Shared with shopping_list.js, which keeps both up to date as recipes are dropped there
    const SELECTION_STORAGE_KEY = "como-list-selection";
    const LIST_MODE_STORAGE_KEY = "como-list-mode";
    const RECIPE_PATH_PREFIX = "formatted_recipes/";
    const RECIPE_PATH_SUFFIX = ".html";

    // The index links to formatted_recipes/<file stem>.html, so the stem is the recipe's id.
    function fileStemOf(item) {
        const href = item.querySelector("a").getAttribute("href");
        return href.slice(RECIPE_PATH_PREFIX.length, -RECIPE_PATH_SUFFIX.length);
    }

    const checkboxByFileStem = new Map();
    for (const item of items) {
        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.className = "select-recipe";
        checkbox.setAttribute("aria-label", `Add ${item.textContent.trim()} to the shopping list`);
        item.prepend(checkbox);
        checkboxByFileStem.set(fileStemOf(item), checkbox);

        checkbox.addEventListener("change", () => {
            item.classList.toggle("selected", checkbox.checked);
            onSelectionChanged();
        });

        // In list mode the whole row is a selection target rather than a link to the recipe
        item.addEventListener("click", (event) => {
            if (!document.body.classList.contains("list-mode") || event.target === checkbox) {
                return;
            }
            event.preventDefault();
            checkbox.checked = !checkbox.checked;
            item.classList.toggle("selected", checkbox.checked);
            onSelectionChanged();
        });
    }

    function selectedFileStems() {
        return [...checkboxByFileStem]
            .filter(([, checkbox]) => checkbox.checked)
            .map(([fileStem]) => fileStem);
    }

    function setSelectedFileStems(fileStems) {
        const wanted = new Set(fileStems);
        for (const [fileStem, checkbox] of checkboxByFileStem) {
            checkbox.checked = wanted.has(fileStem);
            checkbox.closest("li").classList.toggle("selected", checkbox.checked);
        }
        onSelectionChanged();
    }

    function onSelectionChanged() {
        const fileStems = selectedFileStems();
        const query = new URLSearchParams({ [RECIPES_PARAMETER]: fileStems.join(",") });

        selectionCount.textContent =
            fileStems.length === 1 ? "1 recipe selected" : `${fileStems.length} recipes selected`;
        buildLink.href = `shopping_list.html?${query}`;
        buildLink.setAttribute("aria-disabled", String(fileStems.length === 0));

        try {
            sessionStorage.setItem(SELECTION_STORAGE_KEY, fileStems.join(","));
        } catch {
            // Private browsing modes can refuse session storage; the selection just will not persist
        }
    }

    // List mode stays on for the rest of the session, so leaving the index for a shopping
    // list (or a recipe) and coming back lands you right back in the picker.
    function setListMode(isActive) {
        document.body.classList.toggle("list-mode", isActive);
        modeToggle.setAttribute("aria-pressed", String(isActive));
        modeToggle.textContent = isActive ? "Exit List Mode" : "List Mode";
        selectionBar.hidden = !isActive;
        // Recipe links must not steal the keyboard while rows act as checkboxes
        for (const link of document.querySelectorAll(".letter-section li a")) {
            link.tabIndex = isActive ? -1 : 0;
        }

        try {
            sessionStorage.setItem(LIST_MODE_STORAGE_KEY, isActive ? "on" : "off");
        } catch {
            // Private browsing modes can refuse session storage; list mode just will not persist
        }
    }

    modeToggle.addEventListener("click", () => {
        setListMode(!document.body.classList.contains("list-mode"));
    });

    clearButton.addEventListener("click", () => setSelectedFileStems([]));

    buildLink.addEventListener("click", (event) => {
        if (buildLink.getAttribute("aria-disabled") === "true") {
            event.preventDefault();
        }
    });

    function storedFileStems() {
        try {
            return (sessionStorage.getItem(SELECTION_STORAGE_KEY) ?? "").split(",").filter(Boolean);
        } catch {
            return [];
        }
    }

    function wasListModeActive() {
        try {
            return sessionStorage.getItem(LIST_MODE_STORAGE_KEY) === "on";
        } catch {
            return false;
        }
    }

    // A ?recipes= link (the shopping list's "Edit selection", or a shared URL) names the
    // selection outright; otherwise the session's own selection is restored.
    const requestedFileStems = new URLSearchParams(location.search).get(RECIPES_PARAMETER);
    const restoredFileStems =
        requestedFileStems == null ? storedFileStems() : requestedFileStems.split(",").filter(Boolean);

    setSelectedFileStems(restoredFileStems);
    setListMode(requestedFileStems != null || wasListModeActive());
})();
