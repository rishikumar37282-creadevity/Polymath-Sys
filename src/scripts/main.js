// Unified Minimalist Interaction Script for AI Roadmaps

document.addEventListener('DOMContentLoaded', () => {

    // 1. STAGGERED ENTRANCE (Used in Index Page)
    const cards = document.querySelectorAll('.card');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    cards.forEach(card => {
        const rect = card.getBoundingClientRect();
        if (rect.top > window.innerHeight) {
            card.style.opacity = '0';
            observer.observe(card);
        }
    });

    // 2. MAKE ALL BUTTONS FUNCTIONAL VIRTUALLY
    // Any button lacking an onclick, or an A tag linking to '#' 
    window.sendPrompt = function(message) {
        // Minimalist toast notification
        showToast("AI Assistant Request", message);
    };

    function showToast(title, message) {
        const existing = document.getElementById('ai-toast');
        if(existing) existing.remove();

        const toast = document.createElement('div');
        toast.id = 'ai-toast';
        toast.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #111;
            border: 1px solid #333;
            padding: 16px 20px;
            border-radius: 6px;
            font-family: inherit;
            color: #fff;
            box-shadow: 0 10px 40px rgba(0,0,0,0.8);
            transform: translateY(100px);
            opacity: 0;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 1000;
            max-width: 320px;
        `;
        
        toast.innerHTML = `
            <div style="font-size:11px; font-weight:600; text-transform:uppercase; color:#888; margin-bottom:6px;">${title}</div>
            <div style="font-size:13px; line-height:1.5; color:#ddd;">"${message}"</div>
            <div style="font-size:11px; margin-top:10px; color:#555;">[Simulated backend request]</div>
        `;

        document.body.appendChild(toast);
        
        // Annimate in
        requestAnimationFrame(() => {
            toast.style.transform = 'translateY(0)';
            toast.style.opacity = '1';
        });

        // Remove after 4 seconds
        setTimeout(() => {
            toast.style.transform = 'translateY(20px)';
            toast.style.opacity = '0';
            setTimeout(() => toast.remove(), 400);
        }, 4000);
    }
});

// 3. TAB CONTROLS
window.show = function(index) {
    // Hide all panels
    const allPanels = document.querySelectorAll('.panel, .phase-panel');
    allPanels.forEach((p, j) => {
        p.classList.toggle('active', j === index);
    });

    // Deactivate all tabs
    const allTabs = document.querySelectorAll('.tab, .ntab, .tn');
    allTabs.forEach((t, j) => {
        t.classList.toggle('active', j === index);
    });

    // Update progress bar if it exists (for polymath roadmap)
    const pbar = document.getElementById('pbar');
    if (pbar) {
        const totalTabs = allTabs.length;
        const percentage = Math.round(((index + 1) / totalTabs) * 100);
        pbar.style.width = percentage + '%';
    }
};

// 4. ACCORDION CONTROLS
window.tog = function(id) {
    const bodyId = 'b-' + id;
    const arrowId = 'a-' + id;
    const body = document.getElementById(bodyId);
    const arrow = document.getElementById(arrowId);
    
    if (body) {
        const isOpen = body.classList.toggle('open');
        if (arrow) {
            arrow.classList.toggle('open', isOpen);
        }
    }
};
