// Builds the combined shopping list from the recipes named in ?recipes=<file stems>.
// Every recipe's measurements are embedded in the page, so totalling happens client
// side and the list stays live as recipes are dropped or items are ticked off.
(() => {
    const recipesByFileStem = JSON.parse(document.getElementById("recipe-data").textContent);
    const recipeChips = document.getElementById("recipe-chips");
    const shoppingItems = document.getElementById("shopping-items");
    const listSummary = document.getElementById("list-summary");
    const listCard = document.querySelector(".shopping-card");
    const emptyState = document.querySelector(".empty-state");
    const editLink = document.querySelector(".edit-selection");

    const RECIPES_PARAMETER = "recipes";
    // Units the recipe pages leave unwritten, either because there is none or because
    // the amount already reads naturally without it (e.g. "1 thin spaghetti").
    const UNWRITTEN_UNITS = new Set(["", "portions"]);

    const requestedFileStems = (new URLSearchParams(location.search).get(RECIPES_PARAMETER) ?? "").split(",");
    let selectedFileStems = [...new Set(requestedFileStems)].filter((fileStem) => fileStem in recipesByFileStem);

    // Ticked-off ingredients are remembered by name so they survive a re-total
    const purchasedIngredientKeys = new Set();

    function ingredientKeyOf(ingredient) {
        return ingredient.trim().toLowerCase();
    }

    // One entry per ingredient, with a running total per unit so grams and portions of the
    // same thing stay distinguishable ("454 grams + 1 thin spaghetti").
    function totalIngredients() {
        const totalByIngredientKey = new Map();
        for (const fileStem of selectedFileStems) {
            const recipe = recipesByFileStem[fileStem];
            for (const item of recipe.items) {
                const ingredientKey = ingredientKeyOf(item.ingredient);
                let total = totalByIngredientKey.get(ingredientKey);
                if (total == null) {
                    total = {
                        ingredient: item.ingredient,
                        amountByUnit: new Map(),
                        needsUnmeasuredAmount: false,
                        qualifiers: new Set(),
                        recipeNames: new Set(),
                    };
                    totalByIngredientKey.set(ingredientKey, total);
                }

                if (item.amount == null) {
                    total.needsUnmeasuredAmount = true;
                } else {
                    total.amountByUnit.set(item.unit, (total.amountByUnit.get(item.unit) ?? 0) + item.amount);
                }
                if (item.qualifier != null) {
                    total.qualifiers.add(item.qualifier);
                }
                total.recipeNames.add(recipe.name);
            }
        }

        return [...totalByIngredientKey.entries()].sort(([left], [right]) => left.localeCompare(right));
    }

    // Sums of fractional gram amounts pick up floating point dust, so trim it off
    function formatAmount(amount) {
        return `${Math.round(amount * 100) / 100}`;
    }

    function formatTotalAmount(total) {
        const parts = [...total.amountByUnit].map(([unit, amount]) =>
            UNWRITTEN_UNITS.has(unit) ? formatAmount(amount) : `${formatAmount(amount)} ${unit}`,
        );
        if (total.needsUnmeasuredAmount) {
            parts.push("enough");
        }
        return parts.join(" + ");
    }

    function renderRecipeChips() {
        recipeChips.replaceChildren();
        for (const fileStem of selectedFileStems) {
            const chip = document.createElement("li");
            chip.className = "recipe-chip";

            const link = document.createElement("a");
            link.href = `formatted_recipes/${fileStem}.html`;
            link.textContent = recipesByFileStem[fileStem].name;
            chip.append(link);

            const removeButton = document.createElement("button");
            removeButton.type = "button";
            removeButton.className = "remove-recipe";
            removeButton.textContent = "×";
            removeButton.setAttribute("aria-label", `Remove ${recipesByFileStem[fileStem].name} from the list`);
            removeButton.addEventListener("click", () => {
                selectedFileStems = selectedFileStems.filter((candidate) => candidate !== fileStem);
                render();
            });
            chip.append(removeButton);

            recipeChips.append(chip);
        }
    }

    function renderIngredient(ingredientKey, total) {
        const item = document.createElement("li");
        item.className = "ingredient shopping-item";
        item.classList.toggle("purchased", purchasedIngredientKeys.has(ingredientKey));

        const label = document.createElement("label");
        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.checked = purchasedIngredientKeys.has(ingredientKey);
        checkbox.addEventListener("change", () => {
            if (checkbox.checked) {
                purchasedIngredientKeys.add(ingredientKey);
            } else {
                purchasedIngredientKeys.delete(ingredientKey);
            }
            item.classList.toggle("purchased", checkbox.checked);
            renderSummary();
        });

        const text = document.createElement("span");
        text.className = "ingredient-text";
        const amount = document.createElement("span");
        amount.className = "amount";
        amount.textContent = formatTotalAmount(total);
        text.append(amount, ` ${total.ingredient}`);

        label.append(checkbox, text);
        item.append(label);

        if (total.qualifiers.size > 0) {
            const qualifiers = document.createElement("span");
            qualifiers.className = "item-qualifiers";
            qualifiers.textContent = [...total.qualifiers].join(", ");
            item.append(qualifiers);
        }

        const sources = document.createElement("span");
        sources.className = "item-sources";
        sources.textContent = [...total.recipeNames].join(", ");
        item.append(sources);

        return item;
    }

    function renderSummary() {
        const totalCount = shoppingItems.children.length;
        const remainingCount = totalCount - purchasedIngredientKeys.size;
        const recipeCount = selectedFileStems.length;
        const recipeText = recipeCount === 1 ? "1 recipe" : `${recipeCount} recipes`;
        const itemText = totalCount === 1 ? "1 ingredient" : `${totalCount} ingredients`;
        listSummary.textContent = `${recipeText} · ${itemText} · ${remainingCount} left to buy`;
    }

    function render() {
        const totals = totalIngredients();

        // Ingredients only from recipes that have since been removed are no longer ticked off
        const ingredientKeys = new Set(totals.map(([ingredientKey]) => ingredientKey));
        for (const ingredientKey of purchasedIngredientKeys) {
            if (!ingredientKeys.has(ingredientKey)) {
                purchasedIngredientKeys.delete(ingredientKey);
            }
        }

        renderRecipeChips();
        shoppingItems.replaceChildren(...totals.map(([ingredientKey, total]) => renderIngredient(ingredientKey, total)));
        renderSummary();

        const isEmpty = selectedFileStems.length === 0;
        listCard.hidden = isEmpty;
        emptyState.hidden = !isEmpty;

        const query = new URLSearchParams({ [RECIPES_PARAMETER]: selectedFileStems.join(",") });
        editLink.href = `index.html?${query}`;
        history.replaceState(null, "", isEmpty ? location.pathname : `?${query}`);
    }

    render();
})();
