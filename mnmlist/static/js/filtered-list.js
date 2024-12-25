class FilteredArticles extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        
        const style = `
            <style>
                .filters {
                    margin-bottom: 1rem;
                    display: flex;
                    flex-wrap: wrap;
                    align-items: center;
                    gap: 10px;
                }
                .filters-label {
                    color: #666;
                    line-height: 30px;
                }
                .filter-btn {
                    background: none;
                    border: none;
                    border-bottom: 3px solid;
                    padding: 5px 10px;
                    margin: 0.2rem;
                    cursor: pointer;
                    line-height: 30px;
                    opacity: 0.6;
                }
                .filter-btn:hover {
                    opacity: 1;
                }
                .filter-btn.active {
                    opacity: 1;
                }
                .search-container {
                    display: flex;
                    align-items: center;
                    margin-left: auto;
                }
                .search-input {
                    padding: 5px 10px;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                    margin-left: 10px;
                    line-height: 20px;
                }
                ::slotted(.items) {
                    padding-left: 0px !important;
                }
                ::slotted(.item) {
                    display: none !important;
                    flex-direction: row !important;
                    padding-bottom: 0.5em !important;
                    padding-left: 1em !important;
                    border-left: 3px solid !important;
                    border-left-color: var(--item-color) !important;
                    line-height: 30px !important;
                }
                ::slotted(.item.visible) {
                    display: flex !important;
                }
                ::slotted(.item time) {
                    flex: 1 !important;
                    text-align: right !important;
                    color: #797878 !important;
                    padding-left: 1em !important;
                }
                @media screen and (max-width: 600px) {
                    .search-container {
                        width: 100%;
                        margin-left: 0;
                    }
                    .search-input {
                        width: 100%;
                    }
                    ::slotted(.item time) {
                        display: none !important;
                    }
                }
            </style>
        `;

        this.shadowRoot.innerHTML = `
            ${style}
            <div class="filters">
                <span class="filters-label">Filter by:</span>
                <div class="categories-container"></div>
                <div class="search-container">
                    <span class="filters-label">Search:</span>
                    <input type="text" class="search-input" placeholder="Type to search...">
                </div>
            </div>
            <slot></slot>
        `;

        this.currentCategory = 'all';
        this.searchText = '';
    }

    connectedCallback() {
        const slot = this.shadowRoot.querySelector('slot');
        const searchInput = this.shadowRoot.querySelector('.search-input');
        
        slot.addEventListener('slotchange', () => {
            this.init(slot.assignedElements());
        });

        searchInput.addEventListener('input', (e) => {
            this.searchText = e.target.value.toLowerCase();
            const items = slot.assignedElements();
            this.filterItems(items, this.currentCategory);
        });
    }

    init(items) {
        const categories = new Map();
        items.forEach(item => {
            const categoryClass = [...item.classList].find(cls => cls.startsWith('link-'));
            if (categoryClass) {
                const category = categoryClass.replace('link-', '');
                const color = getComputedStyle(item).getPropertyValue('--item-color').trim();
                categories.set(category, color);
            }
        });

        const categoriesContainer = this.shadowRoot.querySelector('.categories-container');
        categoriesContainer.innerHTML = ''; // Clear existing buttons
        
        // "All" button with a neutral color
        const allBtn = document.createElement('button');
        allBtn.className = 'filter-btn active';
        allBtn.textContent = 'All';
        allBtn.dataset.category = 'all';
        allBtn.style.borderBottomColor = '#666';
        categoriesContainer.appendChild(allBtn);
        
        // Category buttons with matching colors
        categories.forEach((color, category) => {
            const btn = document.createElement('button');
            btn.className = 'filter-btn';
            btn.textContent = category.charAt(0).toUpperCase() + category.slice(1);
            btn.dataset.category = category;
            btn.style.borderBottomColor = color;
            categoriesContainer.appendChild(btn);
        });

        this.shadowRoot.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                this.currentCategory = btn.dataset.category;
                this.filterItems(items, this.currentCategory);
            });
        });

        this.filterItems(items, 'all');
    }

    filterItems(items, category) {
        this.shadowRoot.querySelectorAll('.filter-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.category === category);
        });

        items.forEach(item => {
            const matchesCategory = category === 'all' || item.classList.contains(`link-${category}`);
            const matchesSearch = this.searchText === '' || 
                item.textContent.toLowerCase().includes(this.searchText);
            item.classList.toggle('visible', matchesCategory && matchesSearch);
        });
    }
}

customElements.define('filtered-articles', FilteredArticles);
