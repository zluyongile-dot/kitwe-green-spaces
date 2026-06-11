/**
 * Universal Dark Mode System
 * Works across all pages with localStorage persistence
 */

(function() {
    'use strict';
    
    // Check for saved dark mode preference or default to light mode
    const darkMode = localStorage.getItem('darkMode');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    // Apply dark mode immediately to prevent flash
    if (darkMode === 'enabled' || (darkMode === null && prefersDark)) {
        document.documentElement.classList.add('dark');
    }
    
    // Initialize dark mode toggle when DOM is ready
    function initDarkMode() {
        const darkModeToggle = document.getElementById('darkModeToggle');
        
        if (!darkModeToggle) {
            console.warn('Dark mode toggle not found. Add id="darkModeToggle" to your toggle element.');
            return;
        }
        
        // Set initial state
        updateToggleButton();
        
        // Check if it's a checkbox or button and add appropriate event listener
        if (darkModeToggle.type === 'checkbox') {
            darkModeToggle.addEventListener('change', function() {
                if (this.checked) {
                    enableDarkMode();
                } else {
                    disableDarkMode();
                }
            });
        } else {
            // For button-style toggles
            darkModeToggle.addEventListener('click', toggleDarkMode);
        }
        
        // Listen for system theme changes
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
            if (localStorage.getItem('darkMode') === null) {
                if (e.matches) {
                    enableDarkMode();
                } else {
                    disableDarkMode();
                }
            }
        });
    }
    
    function toggleDarkMode() {
        const isDark = document.documentElement.classList.contains('dark');
        
        if (isDark) {
            disableDarkMode();
        } else {
            enableDarkMode();
        }
    }
    
    function enableDarkMode() {
        document.documentElement.classList.add('dark');
        localStorage.setItem('darkMode', 'enabled');
        updateToggleButton();
        
        // Dispatch custom event for other scripts to listen to
        window.dispatchEvent(new CustomEvent('darkModeChanged', { detail: { enabled: true } }));
    }
    
    function disableDarkMode() {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('darkMode', 'disabled');
        updateToggleButton();
        
        // Dispatch custom event for other scripts to listen to
        window.dispatchEvent(new CustomEvent('darkModeChanged', { detail: { enabled: false } }));
    }
    
    function updateToggleButton() {
        const darkModeToggle = document.getElementById('darkModeToggle');
        if (!darkModeToggle) return;
        
        const isDark = document.documentElement.classList.contains('dark');
        
        // If it's a checkbox, update its checked state
        if (darkModeToggle.type === 'checkbox') {
            darkModeToggle.checked = isDark;
        } else {
            // For button-style toggles, update icons
            const moonIcon = darkModeToggle.querySelector('.fa-moon');
            const sunIcon = darkModeToggle.querySelector('.fa-sun');
            
            if (moonIcon && sunIcon) {
                if (isDark) {
                    moonIcon.classList.add('hidden');
                    sunIcon.classList.remove('hidden');
                } else {
                    moonIcon.classList.remove('hidden');
                    sunIcon.classList.add('hidden');
                }
            }
            
            // Update aria-label for accessibility
            darkModeToggle.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
        }
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initDarkMode);
    } else {
        initDarkMode();
    }
    
    // Export functions for manual control if needed
    window.darkModeSystem = {
        enable: enableDarkMode,
        disable: disableDarkMode,
        toggle: toggleDarkMode,
        isEnabled: () => document.documentElement.classList.contains('dark')
    };
})();
