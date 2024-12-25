class TranslatedText extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });

        // Détection de la langue du navigateur
        const userLang = navigator.language || navigator.userLanguage;
        const isFrench = userLang.startsWith('fr');

        const style = document.createElement('style');
        style.textContent = `
            .controls {
                text-align: right;
                margin-bottom: 10px;
            }
            .lang-toggle { display: none; }
            .lang-label {
                padding: 5px 10px;
                cursor: pointer;
            }
            .content-section { display: none; }
            #fr:checked ~ .content .fr-content,
            #en:checked ~ .content .en-content { display: block; }

            #fr:checked ~ .controls label[for="fr"],
            #en:checked ~ .controls label[for="en"] { 
                display: none; 
            }
        `;

        const html = `
            <input type="radio" id="fr" name="lang" class="lang-toggle" ${isFrench ? 'checked' : ''}>
            <input type="radio" id="en" name="lang" class="lang-toggle" ${!isFrench ? 'checked' : ''}>
            <div class="controls">
                <label for="fr" class="lang-label">(voir le contenu en Français)</label>
                <label for="en" class="lang-label">(see English content)</label>
            </div>
            <div class="content">
                <div class="content-section fr-content">
                    <slot name="fr"></slot>
                </div>
                <div class="content-section en-content">
                    <slot name="en"></slot>
                </div>
            </div>
        `;

        this.shadowRoot.innerHTML = `${style.outerHTML}${html}`;
    }
}

customElements.define('translated-text', TranslatedText);
