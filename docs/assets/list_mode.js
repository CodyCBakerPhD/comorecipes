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
    const selectAllButton = selectionBar.querySelector(".select-all");
    const clearButton = selectionBar.querySelector(".clear-selection");
    const items = Array.from(document.querySelectorAll(".letter-section li"));

    const RECIPES_PARAMETER = "recipes";
    const SELECTION_STORAGE_KEY = "como-list-selection";
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

    function setListMode(isActive) {
        document.body.classList.toggle("list-mode", isActive);
        modeToggle.setAttribute("aria-pressed", String(isActive));
        modeToggle.textContent = isActive ? "Exit List Mode" : "List Mode";
        selectionBar.hidden = !isActive;
        // Recipe links must not steal the keyboard while rows act as checkboxes
        for (const link of document.querySelectorAll(".letter-section li a")) {
            link.tabIndex = isActive ? -1 : 0;
        }
    }

    modeToggle.addEventListener("click", () => {
        setListMode(!document.body.classList.contains("list-mode"));
    });

    selectAllButton.addEventListener("click", () => {
        // "Shown" respects the active search query and tag filters
        const shown = items.filter((item) => !item.hidden && !item.closest(".letter-section").hidden);
        setSelectedFileStems(shown.map(fileStemOf));
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

    // Arriving from the shopping list's "Edit selection" link reopens list mode with that selection
    const requestedFileStems = new URLSearchParams(location.search).get(RECIPES_PARAMETER);
    const restoredFileStems =
        requestedFileStems == null ? storedFileStems() : requestedFileStems.split(",").filter(Boolean);

    setListMode(requestedFileStems != null && restoredFileStems.length > 0);
    setSelectedFileStems(restoredFileStems);
})();
