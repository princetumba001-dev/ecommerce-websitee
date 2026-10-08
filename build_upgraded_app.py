import os

file_path = r"C:\Users\Prince kumar\.gemini\antigravity\scratch\ecommerce-app\index.html"

html_code = """<!-- SINGLE FILE E-COMMERCE APPLICATION -->
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ShopNexus Prime | Next-Gen E-Commerce Platform</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
    
    <!-- FontAwesome 6 CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <style>
        /* ==========================================
           1. CSS VARIABLES & THEME SYSTEM
           ========================================== */
        :root {
            --primary: #4f46e5;
            --primary-hover: #4338ca;
            --primary-light: #eef2ff;
            --primary-glow: rgba(79, 70, 229, 0.25);
            --secondary: #06b6d4;
            --accent: #f59e0b;
            --danger: #ef4444;
            --success: #10b981;
            --warning: #f59e0b;
            --info: #3b82f6;

            --bg-main: #f8fafc;
            --bg-card: #ffffff;
            --bg-header: rgba(255, 255, 255, 0.92);
            --bg-input: #f1f5f9;
            --bg-subtle: #f1f5f9;
            --glass-bg: rgba(255, 255, 255, 0.7);

            --text-main: #0f172a;
            --text-muted: #64748b;
            --text-light: #94a3b8;
            --border-color: #e2e8f0;
            
            --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.04);
            --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.08);
            --shadow-lg: 0 12px 24px -4px rgba(0, 0, 0, 0.12);
            --shadow-xl: 0 24px 48px -12px rgba(0, 0, 0, 0.18);
            
            --radius-sm: 8px;
            --radius-md: 14px;
            --radius-lg: 20px;
            --radius-full: 9999px;
            
            --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
            --container-max: 1340px;
        }

        [data-theme="dark"] {
            --primary: #6366f1;
            --primary-hover: #4f46e5;
            --primary-light: #1e1b4b;
            --primary-glow: rgba(99, 102, 241, 0.35);
            --bg-main: #090d16;
            --bg-card: #131c2e;
            --bg-header: rgba(19, 28, 46, 0.92);
            --bg-input: #1e293b;
            --bg-subtle: #182238;
            --glass-bg: rgba(19, 28, 46, 0.7);

            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --text-light: #64748b;
            --border-color: #1e293b;
            
            --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.4);
            --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.4);
            --shadow-lg: 0 12px 24px rgba(0, 0, 0, 0.5);
            --shadow-xl: 0 24px 48px rgba(0, 0, 0, 0.6);
        }

        /* ==========================================
           2. BASE & RESET STYLES
           ========================================== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Plus Jakarta Sans', sans-serif;
            -webkit-tap-highlight-color: transparent;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            background-color: var(--bg-main);
            color: var(--text-main);
            line-height: 1.5;
            overflow-x: hidden;
            transition: background-color 0.3s ease, color 0.3s ease;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }

        a {
            color: inherit;
            text-decoration: none;
        }

        button {
            cursor: pointer;
            border: none;
            outline: none;
            background: none;
            font-family: inherit;
            transition: var(--transition);
        }

        input, select, textarea {
            font-family: inherit;
            outline: none;
            border: 1px solid var(--border-color);
            background: var(--bg-card);
            color: var(--text-main);
            border-radius: var(--radius-md);
            padding: 0.7rem 1.1rem;
            transition: var(--transition);
        }

        input:focus, select:focus, textarea:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px var(--primary-glow);
        }

        img {
            max-width: 100%;
            height: auto;
            display: block;
        }

        .container {
            width: 100%;
            max-width: var(--container-max);
            margin: 0 auto;
            padding: 0 1.25rem;
        }

        /* ==========================================
           3. BUTTONS & UI COMPONENTS
           ========================================== */
        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            font-weight: 700;
            font-size: 0.9rem;
            padding: 0.7rem 1.4rem;
            border-radius: var(--radius-md);
            transition: var(--transition);
            white-space: nowrap;
            user-select: none;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--primary), var(--primary-hover));
            color: #ffffff;
            box-shadow: 0 4px 14px var(--primary-glow);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px var(--primary-glow);
        }

        .btn-secondary {
            background: var(--bg-subtle);
            color: var(--text-main);
            border: 1px solid var(--border-color);
        }

        .btn-secondary:hover {
            background: var(--border-color);
            transform: translateY(-1px);
        }

        .btn-outline {
            border: 1.5px solid var(--primary);
            color: var(--primary);
            background: transparent;
        }

        .btn-outline:hover {
            background: var(--primary);
            color: #ffffff;
        }

        .btn-danger {
            background: var(--danger);
            color: #ffffff;
        }

        .btn-sm {
            padding: 0.45rem 0.9rem;
            font-size: 0.8rem;
            border-radius: var(--radius-sm);
        }

        .btn-lg {
            padding: 0.95rem 2rem;
            font-size: 1.05rem;
            border-radius: var(--radius-lg);
        }

        .btn-icon {
            width: 42px;
            height: 42px;
            border-radius: var(--radius-full);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            position: relative;
            color: var(--text-main);
            background: var(--bg-card);
            border: 1px solid var(--border-color);
        }

        .btn-icon:hover {
            background: var(--primary-light);
            color: var(--primary);
            border-color: var(--primary);
            transform: translateY(-2px);
        }

        .badge {
            display: inline-flex;
            align-items: center;
            padding: 0.25rem 0.65rem;
            font-size: 0.725rem;
            font-weight: 800;
            border-radius: var(--radius-full);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .badge-primary { background: var(--primary-light); color: var(--primary); }
        .badge-success { background: rgba(16, 185, 129, 0.15); color: var(--success); }
        .badge-warning { background: rgba(245, 158, 11, 0.15); color: var(--warning); }
        .badge-danger { background: rgba(239, 68, 68, 0.15); color: var(--danger); }

        .counter-badge {
            position: absolute;
            top: -4px;
            right: -4px;
            background: var(--danger);
            color: #fff;
            font-size: 0.7rem;
            font-weight: 800;
            min-width: 20px;
            height: 20px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 0 4px;
            border: 2px solid var(--bg-card);
            animation: bounce 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        @keyframes bounce {
            0% { transform: scale(0.3); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }

        /* Top Announcement Ribbon */
        .announcement-bar {
            background: linear-gradient(90deg, #4f46e5 0%, #06b6d4 50%, #4f46e5 100%);
            background-size: 200% auto;
            color: #ffffff;
            font-size: 0.825rem;
            font-weight: 700;
            padding: 0.45rem 0;
            text-align: center;
            animation: gradientShift 6s ease infinite;
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Sticky Header */
        header {
            position: sticky;
            top: 0;
            z-index: 100;
            background: var(--bg-header);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border-color);
            transition: var(--transition);
        }

        .nav-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 76px;
            gap: 1.5rem;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 0.65rem;
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--text-main);
            letter-spacing: -0.5px;
        }

        .logo-icon {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-radius: var(--radius-md);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #ffffff;
            font-size: 1.3rem;
            box-shadow: 0 4px 12px var(--primary-glow);
        }

        /* Search Bar */
        .search-box {
            flex: 1;
            max-width: 580px;
            position: relative;
        }

        .search-input-wrapper {
            position: relative;
            display: flex;
            align-items: center;
        }

        .search-input-wrapper input {
            width: 100%;
            padding-left: 3rem;
            padding-right: 3.5rem;
            height: 46px;
            border-radius: var(--radius-full);
            background: var(--bg-input);
            border: 1px solid transparent;
            font-size: 0.9rem;
        }

        .search-input-wrapper input:focus {
            background: var(--bg-card);
            border-color: var(--primary);
        }

        .search-icon {
            position: absolute;
            left: 1.1rem;
            color: var(--text-muted);
            font-size: 1.1rem;
        }

        .search-clear-btn {
            position: absolute;
            right: 1rem;
            color: var(--text-muted);
            cursor: pointer;
            display: none;
        }

        .search-suggestions {
            position: absolute;
            top: 115%;
            left: 0;
            right: 0;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-xl);
            z-index: 200;
            max-height: 420px;
            overflow-y: auto;
            display: none;
            padding: 0.75rem;
        }

        .search-suggestions.active {
            display: block;
        }

        .suggestion-section-title {
            font-size: 0.75rem;
            font-weight: 800;
            color: var(--text-muted);
            text-transform: uppercase;
            padding: 0.4rem 0.75rem;
        }

        .suggestion-item {
            display: flex;
            align-items: center;
            gap: 0.85rem;
            padding: 0.65rem 0.75rem;
            cursor: pointer;
            border-radius: var(--radius-md);
            transition: var(--transition);
        }

        .suggestion-item:hover {
            background: var(--bg-subtle);
        }

        .suggestion-item img {
            width: 44px;
            height: 44px;
            object-fit: cover;
            border-radius: var(--radius-sm);
        }

        .nav-actions {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        /* Category Sub-Bar Navigation */
        .category-bar {
            background: var(--bg-card);
            border-bottom: 1px solid var(--border-color);
            overflow-x: auto;
            white-space: nowrap;
            scrollbar-width: none;
        }

        .category-bar::-webkit-scrollbar { display: none; }

        .category-nav-list {
            display: flex;
            align-items: center;
            gap: 1.75rem;
            padding: 0.65rem 0;
            list-style: none;
        }

        .category-nav-item {
            font-size: 0.875rem;
            font-weight: 700;
            color: var(--text-muted);
            cursor: pointer;
            padding: 0.35rem 0.85rem;
            border-radius: var(--radius-full);
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 0.45rem;
        }

        .category-nav-item:hover, .category-nav-item.active {
            color: var(--primary);
            background: var(--primary-light);
        }

        /* ==========================================
           4. HERO SECTION & PROMO STRIP
           ========================================== */
        .hero-section {
            padding: 2.25rem 0 1.5rem 0;
        }

        .hero-banner {
            background: linear-gradient(135deg, #1e1b4b 0%, #312e81 40%, #4f46e5 70%, #06b6d4 100%);
            border-radius: var(--radius-lg);
            padding: 4rem 3.5rem;
            color: #ffffff;
            position: relative;
            overflow: hidden;
            box-shadow: var(--shadow-xl);
            display: grid;
            grid-template-columns: 1.2fr 1fr;
            align-items: center;
            gap: 2.5rem;
        }

        .hero-text h1 {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 3.25rem;
            font-weight: 700;
            line-height: 1.1;
            margin-bottom: 1.25rem;
            letter-spacing: -1px;
        }

        .hero-text p {
            font-size: 1.15rem;
            opacity: 0.9;
            margin-bottom: 2rem;
            max-width: 520px;
        }

        .hero-image-wrapper {
            position: relative;
            display: flex;
            justify-content: center;
        }

        .hero-image-wrapper img {
            width: 100%;
            max-height: 360px;
            object-fit: contain;
            filter: drop-shadow(0 25px 35px rgba(0,0,0,0.4));
            animation: float 4s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-12px); }
        }

        .hero-floating-card {
            position: absolute;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.25);
            padding: 0.85rem 1.25rem;
            border-radius: var(--radius-md);
            color: #fff;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        }

        .hero-floating-card.card-1 { top: 10%; left: -5%; }
        .hero-floating-card.card-2 { bottom: 10%; right: -5%; }

        .promo-features-strip {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.5rem;
            margin: 2rem 0;
        }

        .feature-box {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.25rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            box-shadow: var(--shadow-sm);
            transition: var(--transition);
        }

        .feature-box:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-md);
            border-color: var(--primary);
        }

        .feature-icon {
            width: 48px;
            height: 48px;
            border-radius: var(--radius-md);
            background: var(--primary-light);
            color: var(--primary);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.3rem;
        }

        /* ==========================================
           5. PRODUCT CARD & GALLERY
           ========================================== */
        .section { padding: 2.5rem 0; }

        .section-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.75rem;
        }

        .section-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.75rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }

        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1.75rem;
        }

        .product-card {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            overflow: hidden;
            transition: var(--transition);
            position: relative;
            display: flex;
            flex-direction: column;
        }

        .product-card:hover {
            transform: translateY(-6px);
            box-shadow: var(--shadow-xl);
            border-color: var(--primary-glow);
        }

        .product-img-wrapper {
            position: relative;
            padding-top: 85%;
            background: var(--bg-subtle);
            overflow: hidden;
        }

        .product-img-wrapper img {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
        }

        .product-card:hover .product-img-wrapper img {
            transform: scale(1.08);
        }

        .product-badges {
            position: absolute;
            top: 12px;
            left: 12px;
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
            z-index: 2;
        }

        .card-overlay-actions {
            position: absolute;
            top: 12px;
            right: 12px;
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
            opacity: 0;
            transform: translateX(12px);
            transition: var(--transition);
            z-index: 2;
        }

        .product-card:hover .card-overlay-actions {
            opacity: 1;
            transform: translateX(0);
        }

        .product-info {
            padding: 1.25rem;
            display: flex;
            flex-direction: column;
            flex: 1;
        }

        .product-brand {
            font-size: 0.75rem;
            color: var(--text-muted);
            text-transform: uppercase;
            font-weight: 800;
            letter-spacing: 0.5px;
            margin-bottom: 0.3rem;
        }

        .product-title {
            font-size: 1rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            line-clamp: 2;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
            color: var(--text-main);
            height: 2.8rem;
        }

        .product-rating {
            display: flex;
            align-items: center;
            gap: 0.35rem;
            font-size: 0.825rem;
            color: var(--accent);
            margin-bottom: 0.75rem;
        }

        .product-price-row {
            display: flex;
            align-items: baseline;
            gap: 0.6rem;
            margin-top: auto;
            margin-bottom: 1rem;
        }

        .current-price {
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--text-main);
        }

        .original-price {
            font-size: 0.875rem;
            color: var(--text-muted);
            text-decoration: line-through;
        }

        .card-btn-group {
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 0.5rem;
        }

        /* Flash Sale Header & Countdown */
        .flash-sale-banner {
            background: linear-gradient(135deg, #ef4444 0%, #f59e0b 100%);
            border-radius: var(--radius-lg);
            padding: 1.5rem 2rem;
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.75rem;
            box-shadow: 0 10px 25px rgba(239, 68, 68, 0.3);
        }

        .countdown-timer {
            display: flex;
            gap: 0.5rem;
            align-items: center;
            font-weight: 800;
        }

        .timer-box {
            background: rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(4px);
            padding: 0.5rem 0.75rem;
            border-radius: var(--radius-sm);
            font-size: 1.2rem;
            min-width: 42px;
            text-align: center;
        }

        /* Stock progress bar */
        .stock-progress-bar {
            height: 6px;
            background: var(--border-color);
            border-radius: 3px;
            overflow: hidden;
            margin-top: 0.5rem;
        }

        .stock-progress-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--danger), var(--warning));
            border-radius: 3px;
        }

        /* ==========================================
           6. SLIDE-OUT CART DRAWER
           ========================================== */
        .cart-drawer-overlay {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(6px);
            z-index: 1000;
            opacity: 0;
            visibility: hidden;
            transition: var(--transition);
        }

        .cart-drawer-overlay.active {
            opacity: 1;
            visibility: visible;
        }

        .cart-drawer {
            position: fixed;
            top: 0;
            right: 0;
            bottom: 0;
            width: 100%;
            max-width: 450px;
            background: var(--bg-card);
            box-shadow: var(--shadow-xl);
            z-index: 1001;
            transform: translateX(100%);
            transition: transform 0.35s cubic-bezier(0.165, 0.84, 0.44, 1);
            display: flex;
            flex-direction: column;
        }

        .cart-drawer-overlay.active .cart-drawer {
            transform: translateX(0);
        }

        .cart-drawer-header {
            padding: 1.25rem 1.5rem;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .cart-drawer-body {
            flex: 1;
            overflow-y: auto;
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            gap: 1.25rem;
        }

        .cart-drawer-item {
            display: flex;
            gap: 1rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid var(--border-color);
        }

        .cart-drawer-item img {
            width: 70px;
            height: 70px;
            object-fit: cover;
            border-radius: var(--radius-md);
            background: var(--bg-subtle);
        }

        .free-shipping-progress {
            background: var(--primary-light);
            padding: 0.85rem 1.25rem;
            border-radius: var(--radius-md);
            font-size: 0.85rem;
            color: var(--primary);
            font-weight: 700;
        }

        .cart-drawer-footer {
            padding: 1.5rem;
            border-top: 1px solid var(--border-color);
            background: var(--bg-subtle);
        }

        /* Quantity Picker Component */
        .qty-picker {
            display: inline-flex;
            align-items: center;
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            overflow: hidden;
            background: var(--bg-card);
        }

        .qty-picker button {
            width: 32px;
            height: 32px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--bg-subtle);
            font-weight: 700;
        }

        .qty-picker input {
            width: 44px;
            height: 32px;
            text-align: center;
            border: none;
            padding: 0;
            font-weight: 800;
            background: transparent;
        }

        /* ==========================================
           7. MODALS & VIEW CONTAINERS
           ========================================== */
        .modal-overlay {
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(15, 23, 42, 0.65);
            backdrop-filter: blur(8px);
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            visibility: hidden;
            transition: var(--transition);
            padding: 1rem;
        }

        .modal-overlay.active { opacity: 1; visibility: visible; }

        .modal-content {
            background: var(--bg-card);
            border-radius: var(--radius-lg);
            width: 100%;
            max-width: 920px;
            max-height: 90vh;
            overflow-y: auto;
            position: relative;
            box-shadow: var(--shadow-xl);
            padding: 2.25rem;
            transform: scale(0.95);
            transition: var(--transition);
        }

        .modal-overlay.active .modal-content { transform: scale(1); }

        .modal-close {
            position: absolute;
            top: 1.25rem; right: 1.25rem;
            width: 36px; height: 36px;
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            background: var(--bg-subtle);
            cursor: pointer;
            color: var(--text-muted);
            font-size: 1.2rem;
        }

        .modal-close:hover { color: var(--danger); background: rgba(239,68,68,0.1); }

        /* Multi-step Checkout Progress */
        .checkout-progress {
            display: flex;
            justify-content: space-between;
            margin-bottom: 2.5rem;
            position: relative;
        }

        .checkout-progress::before {
            content: '';
            position: absolute;
            top: 18px; left: 10%; right: 10%;
            height: 3px;
            background: var(--border-color);
            z-index: 1;
        }

        .step-item {
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.4rem;
        }

        .step-circle {
            width: 38px; height: 38px;
            border-radius: 50%;
            background: var(--bg-card);
            border: 2px solid var(--border-color);
            display: flex; align-items: center; justify-content: center;
            font-weight: 800;
            color: var(--text-muted);
        }

        .step-item.active .step-circle {
            background: var(--primary);
            border-color: var(--primary);
            color: #fff;
            box-shadow: 0 0 0 4px var(--primary-glow);
        }

        .step-item.completed .step-circle {
            background: var(--success);
            border-color: var(--success);
            color: #fff;
        }

        /* Dashboards */
        .dashboard-grid {
            display: grid;
            grid-template-columns: 260px 1fr;
            gap: 2rem;
            padding: 2.5rem 0;
        }

        .dashboard-sidebar {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 1rem;
            height: fit-content;
        }

        .dashboard-menu { list-style: none; display: flex; flex-direction: column; gap: 0.35rem; }

        .dashboard-menu-item {
            padding: 0.85rem 1.1rem;
            border-radius: var(--radius-md);
            font-weight: 700;
            font-size: 0.9rem;
            color: var(--text-muted);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.85rem;
            transition: var(--transition);
        }

        .dashboard-menu-item:hover, .dashboard-menu-item.active {
            background: var(--primary-light);
            color: var(--primary);
        }

        /* Mobile Bottom Navigation Bar */
        .mobile-bottom-nav {
            position: fixed;
            bottom: 0; left: 0; right: 0;
            height: 64px;
            background: var(--bg-header);
            backdrop-filter: blur(16px);
            border-top: 1px solid var(--border-color);
            display: none;
            justify-content: space-around;
            align-items: center;
            z-index: 999;
        }

        .mobile-nav-btn {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.2rem;
            font-size: 0.725rem;
            font-weight: 700;
            color: var(--text-muted);
            position: relative;
        }

        .mobile-nav-btn.active, .mobile-nav-btn:hover { color: var(--primary); }
        .mobile-nav-btn i { font-size: 1.25rem; }

        /* Toast Notifications */
        .toast-container {
            position: fixed;
            top: 90px; right: 20px;
            z-index: 9999;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }

        .toast {
            background: var(--bg-card);
            border-left: 4px solid var(--primary);
            padding: 1rem 1.4rem;
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-xl);
            display: flex;
            align-items: center;
            gap: 0.85rem;
            min-width: 300px;
            animation: slideInRight 0.35s ease;
        }

        @keyframes slideInRight {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }

        /* Canvas Confetti Layer */
        #confetti-canvas {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            pointer-events: none;
            z-index: 99999;
        }

        /* Skeleton Shimmer Loading */
        .skeleton {
            background: linear-gradient(90deg, var(--bg-subtle) 25%, var(--border-color) 50%, var(--bg-subtle) 75%);
            background-size: 200% 100%;
            animation: shimmer 1.5s infinite;
            border-radius: var(--radius-sm);
        }

        @keyframes shimmer {
            0% { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }

        /* Footer */
        footer {
            background: var(--bg-card);
            border-top: 1px solid var(--border-color);
            padding: 4.5rem 0 2rem 0;
            margin-top: auto;
        }

        .footer-grid {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1.2fr;
            gap: 3.5rem;
            margin-bottom: 3.5rem;
        }

        /* Responsive Breakpoints */
        @media (max-width: 1024px) {
            .hero-banner { grid-template-columns: 1fr; text-align: center; }
            .hero-image-wrapper { display: none; }
            .promo-features-strip { grid-template-columns: repeat(2, 1fr); }
            .dashboard-grid { grid-template-columns: 1fr; }
            .footer-grid { grid-template-columns: 1fr 1fr; }
        }

        @media (max-width: 768px) {
            .mobile-bottom-nav { display: flex; }
            .promo-features-strip { grid-template-columns: 1fr; }
            .footer-grid { grid-template-columns: 1fr; }
            .nav-actions .btn-icon:not(#btn-cart-nav) { display: none; }
            body { padding-bottom: 64px; }
        }
    </style>
</head>
<body>

    <!-- Canvas Confetti for Celebrations -->
    <canvas id="confetti-canvas"></canvas>

    <!-- Top Announcement Ribbon -->
    <div class="announcement-bar">
        🔥 FLASH SALE IS LIVE: Use code <strong style="text-decoration:underline;">WELCOME10</strong> for 10% OFF + Free Express Shipping!
    </div>

    <!-- Header & Navigation Bar -->
    <header id="main-header">
        <div class="container nav-container">
            <!-- Brand Logo -->
            <a href="javascript:void(0)" onclick="navigateTo('home')" class="logo">
                <div class="logo-icon"><i class="fa-solid fa-cube"></i></div>
                <span>ShopNexus<span style="color:var(--primary);">.</span></span>
            </a>

            <!-- Smart Search Bar -->
            <div class="search-box">
                <div class="search-input-wrapper">
                    <i class="fa-solid fa-magnifying-glass search-icon"></i>
                    <input type="text" id="global-search" placeholder="Search 30+ products, categories, brands..." oninput="handleSearchInput(this.value)">
                    <i class="fa-solid fa-xmark search-clear-btn" id="search-clear-btn" onclick="clearSearch()"></i>
                </div>
                <div id="search-suggestions" class="search-suggestions"></div>
            </div>

            <!-- Navbar Icon Actions -->
            <div class="nav-actions">
                <button class="btn-icon" title="Toggle Light/Dark Theme" onclick="toggleTheme()">
                    <i id="theme-icon" class="fa-solid fa-moon"></i>
                </button>
                <button class="btn-icon" title="Wishlist" onclick="navigateTo('user-dashboard', {tab: 'wishlist'})">
                    <i class="fa-regular fa-heart"></i>
                    <span id="wishlist-badge" class="counter-badge">0</span>
                </button>
                <button class="btn-icon" id="btn-cart-nav" title="Cart Drawer" onclick="toggleCartDrawer()">
                    <i class="fa-solid fa-bag-shopping"></i>
                    <span id="cart-badge" class="counter-badge">0</span>
                </button>
                <div id="user-nav-container">
                    <button class="btn btn-primary btn-sm" onclick="openAuthModal('login')">
                        <i class="fa-solid fa-user"></i> Login
                    </button>
                </div>
            </div>
        </div>

        <!-- Horizontal Category Bar -->
        <div class="category-bar">
            <div class="container">
                <ul class="category-nav-list" id="category-nav-list"></ul>
            </div>
        </div>
    </header>

    <!-- Toast Notification Container -->
    <div id="toast-container" class="toast-container"></div>

    <!-- MAIN APP VIEW SWITCHER -->
    <main id="app-content">

        <!-- ==========================================
           VIEW: HOMEPAGE
           ========================================== -->
        <section id="view-home" class="page-view">
            <div class="container">
                
                <!-- Hero Banner -->
                <div class="hero-section">
                    <div class="hero-banner">
                        <div class="hero-text">
                            <span class="badge badge-warning" style="margin-bottom: 1.25rem;">⚡ PREMIER DEALS 2026</span>
                            <h1>Everything You Love. Delivered Faster.</h1>
                            <p>Discover flagship smartphones, high-performance laptops, designer footwear, and luxury watches with instant free delivery.</p>
                            <div style="display:flex; gap:1rem; flex-wrap:wrap;">
                                <button class="btn btn-primary btn-lg" onclick="navigateTo('shop')">
                                    <i class="fa-solid fa-bag-shopping"></i> Shop Catalog
                                </button>
                                <button class="btn btn-secondary btn-lg" onclick="filterByCategory('Electronics')">
                                    Explore Electronics
                                </button>
                            </div>
                        </div>
                        <div class="hero-image-wrapper">
                            <img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&auto=format&fit=crop&q=80" alt="Headphones Hero">
                            <div class="hero-floating-card card-1">
                                <i class="fa-solid fa-shield-halved" style="color:var(--success); font-size:1.4rem;"></i>
                                <div><strong style="font-size:0.85rem;">2-Year Warranty</strong><br><span style="font-size:0.75rem; opacity:0.8;">100% Genuine Tech</span></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Feature Strip -->
                <div class="promo-features-strip">
                    <div class="feature-box">
                        <div class="feature-icon"><i class="fa-solid fa-truck-fast"></i></div>
                        <div><strong style="font-size:0.9rem;">Free Shipping</strong><p style="font-size:0.75rem; color:var(--text-muted);">On all orders above $50</p></div>
                    </div>
                    <div class="feature-box">
                        <div class="feature-icon"><i class="fa-solid fa-rotate-left"></i></div>
                        <div><strong style="font-size:0.9rem;">30-Day Returns</strong><p style="font-size:0.75rem; color:var(--text-muted);">Hassle-free replacement</p></div>
                    </div>
                    <div class="feature-box">
                        <div class="feature-icon"><i class="fa-solid fa-lock"></i></div>
                        <div><strong style="font-size:0.9rem;">Secure Checkout</strong><p style="font-size:0.75rem; color:var(--text-muted);">256-Bit SSL Encrypted</p></div>
                    </div>
                    <div class="feature-box">
                        <div class="feature-icon"><i class="fa-solid fa-headset"></i></div>
                        <div><strong style="font-size:0.9rem;">24/7 Live Support</strong><p style="font-size:0.75rem; color:var(--text-muted);">Dedicated Concierge</p></div>
                    </div>
                </div>

                <!-- Flash Sale Ticker Section -->
                <div class="flash-sale-banner">
                    <div style="display:flex; align-items:center; gap:1.25rem;">
                        <i class="fa-solid fa-bolt" style="font-size:2rem;"></i>
                        <div>
                            <h3 style="font-size:1.2rem; font-weight:800;">Flash Sale Countdown</h3>
                            <p style="font-size:0.85rem; opacity:0.95;">Grab mega deals before inventory runs out!</p>
                        </div>
                    </div>
                    <div class="countdown-timer">
                        <div class="timer-box" id="timer-hours">03</div>:
                        <div class="timer-box" id="timer-minutes">45</div>:
                        <div class="timer-box" id="timer-seconds">22</div>
                    </div>
                </div>

                <!-- Featured Products Section -->
                <div class="section">
                    <div class="section-header">
                        <h2 class="section-title"><i class="fa-solid fa-fire" style="color:var(--danger);"></i> Featured Deals</h2>
                        <button class="btn btn-secondary btn-sm" onclick="navigateTo('shop')">View All <i class="fa-solid fa-arrow-right"></i></button>
                    </div>
                    <div class="product-grid" id="featured-products-grid"></div>
                </div>

                <!-- Trending Products -->
                <div class="section">
                    <div class="section-header">
                        <h2 class="section-title"><i class="fa-solid fa-chart-line" style="color:var(--primary);"></i> Trending This Week</h2>
                    </div>
                    <div class="product-grid" id="trending-products-grid"></div>
                </div>

            </div>
        </section>

        <!-- ==========================================
           VIEW: CATALOG / SHOP
           ========================================== -->
        <section id="view-shop" class="page-view" style="display: none;">
            <div class="container" style="padding: 2.5rem 0;">
                <div style="display:grid; grid-template-columns: 260px 1fr; gap: 2rem;">
                    <!-- Filter Sidebar -->
                    <aside style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:1.5rem; height:fit-content;">
                        <h3 style="font-size:1.1rem; font-weight:800; margin-bottom:1.25rem;">Filters</h3>
                        
                        <div style="margin-bottom:1.5rem;">
                            <label style="font-size:0.85rem; font-weight:800; display:block; margin-bottom:0.5rem;">Price Range</label>
                            <span id="price-val-label" style="font-size:0.85rem; color:var(--primary); font-weight:700;">$0 - $2500</span>
                            <input type="range" id="price-slider" min="0" max="2500" step="50" value="2500" style="width:100%; margin-top:0.5rem;" oninput="updatePriceFilter(this.value)">
                        </div>

                        <div style="margin-bottom:1.5rem;">
                            <label style="font-size:0.85rem; font-weight:800; display:block; margin-bottom:0.5rem;">Minimum Rating</label>
                            <select id="rating-filter-select" onchange="applyShopFilters()" style="width:100%;">
                                <option value="0">All Ratings</option>
                                <option value="4.5">4.5★ & Above</option>
                                <option value="4.0">4.0★ & Above</option>
                            </select>
                        </div>

                        <button class="btn btn-secondary btn-sm" style="width:100%;" onclick="resetShopFilters()">
                            <i class="fa-solid fa-rotate-left"></i> Reset Filters
                        </button>
                    </aside>

                    <!-- Main Grid -->
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center; background:var(--bg-card); border:1px solid var(--border-color); padding:0.85rem 1.25rem; border-radius:var(--radius-md); margin-bottom:1.5rem;">
                            <span id="shop-results-count" style="font-weight:700; font-size:0.9rem; color:var(--text-muted);">Showing 30 products</span>
                            <select id="shop-sort-select" onchange="applyShopFilters()" style="padding:0.4rem 0.8rem; font-size:0.85rem;">
                                <option value="featured">Featured</option>
                                <option value="price-low">Price: Low to High</option>
                                <option value="price-high">Price: High to Low</option>
                                <option value="rating">Highest Rated</option>
                            </select>
                        </div>
                        <div class="product-grid" id="shop-products-grid"></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==========================================
           VIEW: CHECKOUT MULTI-STEP
           ========================================== -->
        <section id="view-checkout" class="page-view" style="display: none;">
            <div class="container" style="padding: 3rem 0; max-width: 900px;">
                <div class="checkout-progress">
                    <div class="step-item active" id="chk-step-1"><div class="step-circle">1</div><span style="font-size:0.8rem; font-weight:700;">Address</span></div>
                    <div class="step-item" id="chk-step-2"><div class="step-circle">2</div><span style="font-size:0.8rem; font-weight:700;">Payment</span></div>
                    <div class="step-item" id="chk-step-3"><div class="step-circle">3</div><span style="font-size:0.8rem; font-weight:700;">Confirmation</span></div>
                </div>

                <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:2.25rem;">
                    <div id="chk-step-form-1">
                        <h3 style="font-size:1.3rem; font-weight:800; margin-bottom:1.25rem;">Shipping Address</h3>
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:1rem;">
                            <input type="text" id="chk-name" placeholder="Full Name *" required>
                            <input type="tel" id="chk-phone" placeholder="Mobile Number *" required>
                        </div>
                        <input type="text" id="chk-address" placeholder="Street Address *" style="width:100%; margin-bottom:1rem;" required>
                        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:1rem; margin-bottom:1.5rem;">
                            <input type="text" id="chk-city" placeholder="City *" required>
                            <input type="text" id="chk-state" placeholder="State *" required>
                            <input type="text" id="chk-zip" placeholder="ZIP Code *" required>
                        </div>
                        <button class="btn btn-primary" onclick="goToCheckoutStep(2)">Proceed to Payment <i class="fa-solid fa-arrow-right"></i></button>
                    </div>

                    <div id="chk-step-form-2" style="display:none;">
                        <h3 style="font-size:1.3rem; font-weight:800; margin-bottom:1.25rem;">Select Payment Method</h3>
                        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin-bottom:1.5rem;">
                            <div class="btn btn-outline" onclick="placeOrderFinal('COD')"><i class="fa-solid fa-hand-holding-dollar"></i> Cash on Delivery</div>
                            <div class="btn btn-outline" onclick="placeOrderFinal('UPI')"><i class="fa-solid fa-qrcode"></i> Simulated UPI</div>
                            <div class="btn btn-outline" onclick="placeOrderFinal('CARD')"><i class="fa-solid fa-credit-card"></i> Card Simulation</div>
                        </div>
                        <button class="btn btn-secondary btn-sm" onclick="goToCheckoutStep(1)"><i class="fa-solid fa-arrow-left"></i> Back to Address</button>
                    </div>

                    <div id="chk-step-form-3" style="display:none; text-align:center; padding:2rem 0;">
                        <i class="fa-solid fa-circle-check" style="font-size:4rem; color:var(--success); margin-bottom:1rem;"></i>
                        <h2 style="font-size:1.8rem; font-weight:800;">Order Placed Successfully!</h2>
                        <p style="color:var(--text-muted); margin:0.5rem 0 1.5rem 0;" id="success-order-id-label">Order #ORD-123456</p>
                        <button class="btn btn-primary" onclick="navigateTo('user-dashboard', {tab:'orders'})">View My Orders</button>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==========================================
           VIEW: USER DASHBOARD
           ========================================== -->
        <section id="view-user-dashboard" class="page-view" style="display: none;">
            <div class="container dashboard-grid">
                <aside class="dashboard-sidebar">
                    <ul class="dashboard-menu">
                        <li class="dashboard-menu-item active" onclick="switchDashTab('orders', this)"><i class="fa-solid fa-box"></i> My Orders</li>
                        <li class="dashboard-menu-item" onclick="switchDashTab('wishlist', this)"><i class="fa-solid fa-heart"></i> Wishlist</li>
                        <li class="dashboard-menu-item" style="color:var(--danger);" onclick="logoutUser()"><i class="fa-solid fa-right-from-bracket"></i> Logout</li>
                    </ul>
                </aside>
                <div>
                    <div id="dashtab-orders">
                        <h2 style="font-size:1.4rem; font-weight:800; margin-bottom:1.25rem;">My Orders History</h2>
                        <div id="user-orders-list"></div>
                    </div>
                    <div id="dashtab-wishlist" style="display:none;">
                        <h2 style="font-size:1.4rem; font-weight:800; margin-bottom:1.25rem;">My Wishlist</h2>
                        <div class="product-grid" id="user-wishlist-grid"></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==========================================
           VIEW: ADMIN DASHBOARD
           ========================================== -->
        <section id="view-admin-dashboard" class="page-view" style="display: none;">
            <div class="container" style="padding: 2.5rem 0;">
                <h1 style="font-size: 1.8rem; font-weight: 800; margin-bottom: 1.5rem;"><i class="fa-solid fa-chart-pie"></i> Store Admin Panel</h1>
                <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:1.5rem; margin-bottom:2rem;">
                    <h3 style="font-size:1.1rem; font-weight:800; margin-bottom:1rem;">Monthly Sales Trend</h3>
                    <div style="height:260px;"><canvas id="adminSalesChart"></canvas></div>
                </div>
                <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); overflow-x:auto;">
                    <div style="padding:1rem; background:var(--bg-subtle); font-weight:800;">Inventory Management</div>
                    <table style="width:100%; border-collapse:collapse; font-size:0.875rem;">
                        <thead>
                            <tr style="border-bottom:1px solid var(--border-color); text-align:left; background:var(--bg-subtle);">
                                <th style="padding:0.75rem 1rem;">ID</th>
                                <th style="padding:0.75rem 1rem;">Name</th>
                                <th style="padding:0.75rem 1rem;">Category</th>
                                <th style="padding:0.75rem 1rem;">Price</th>
                                <th style="padding:0.75rem 1rem;">Stock</th>
                            </tr>
                        </thead>
                        <tbody id="admin-inventory-body"></tbody>
                    </table>
                </div>
            </div>
        </section>

    </main>

    <!-- ==========================================
       SLIDE-OUT CART DRAWER
       ========================================== -->
    <div id="cart-drawer-overlay" class="cart-drawer-overlay" onclick="toggleCartDrawer()">
        <div class="cart-drawer" onclick="event.stopPropagation()">
            <div class="cart-drawer-header">
                <h3 style="font-size:1.2rem; font-weight:800;"><i class="fa-solid fa-bag-shopping"></i> Shopping Cart</h3>
                <i class="fa-solid fa-xmark" style="cursor:pointer; font-size:1.2rem;" onclick="toggleCartDrawer()"></i>
            </div>
            <div class="cart-drawer-body" id="cart-drawer-body"></div>
            <div class="cart-drawer-footer">
                <div class="free-shipping-progress" id="free-shipping-banner" style="margin-bottom:1rem; text-align:center;">
                    Add $35 more for <strong>FREE Shipping!</strong>
                </div>
                <div style="display:flex; justify-content:space-between; margin-bottom:1rem; font-weight:800; font-size:1.1rem;">
                    <span>Subtotal:</span>
                    <span id="cart-drawer-subtotal">$0.00</span>
                </div>
                <button class="btn btn-primary btn-lg" style="width:100%;" onclick="toggleCartDrawer(); navigateTo('checkout');">
                    Proceed to Checkout <i class="fa-solid fa-arrow-right"></i>
                </button>
            </div>
        </div>
    </div>

    <!-- ==========================================
       AUTH MODAL (LOGIN / REGISTER)
       ========================================== -->
    <div id="modal-auth" class="modal-overlay">
        <div class="modal-content" style="max-width:420px;">
            <div class="modal-close" onclick="closeModal('modal-auth')">&times;</div>
            <h3 style="font-size:1.4rem; font-weight:800; margin-bottom:1.25rem;">Sign In to ShopNexus</h3>
            <form onsubmit="handleLoginSubmit(event)">
                <input type="email" id="login-email" placeholder="Email (user@example.com)" style="width:100%; margin-bottom:0.75rem;" required>
                <input type="password" id="login-password" placeholder="Password (123456)" style="width:100%; margin-bottom:1rem;" required>
                <div style="background:var(--bg-subtle); padding:0.75rem; border-radius:var(--radius-sm); font-size:0.8rem; margin-bottom:1rem;">
                    <strong>Demo Accounts:</strong><br>
                    • User: user@example.com / 123456<br>
                    • Admin: admin@example.com / admin123
                </div>
                <button type="submit" class="btn btn-primary" style="width:100%;">Sign In</button>
            </form>
        </div>
    </div>

    <!-- MOBILE BOTTOM NAVIGATION -->
    <div class="mobile-bottom-nav">
        <div class="mobile-nav-btn active" onclick="navigateTo('home')"><i class="fa-solid fa-house"></i>Home</div>
        <div class="mobile-nav-btn" onclick="navigateTo('shop')"><i class="fa-solid fa-grid-2"></i>Shop</div>
        <div class="mobile-nav-btn" onclick="navigateTo('user-dashboard', {tab:'wishlist'})"><i class="fa-regular fa-heart"></i>Wishlist</div>
        <div class="mobile-nav-btn" onclick="toggleCartDrawer()"><i class="fa-solid fa-bag-shopping"></i>Cart</div>
        <div class="mobile-nav-btn" onclick="openAuthModal('login')"><i class="fa-solid fa-user"></i>Account</div>
    </div>

    <!-- FOOTER -->
    <footer>
        <div class="container footer-grid">
            <div>
                <a href="javascript:void(0)" class="logo" style="margin-bottom:1rem; display:inline-flex;">
                    <div class="logo-icon"><i class="fa-solid fa-cube"></i></div>
                    <span>ShopNexus.</span>
                </a>
                <p style="font-size:0.875rem; color:var(--text-muted); max-width:320px;">
                    Next-generation commercial e-commerce platform with fast shipping and 24/7 concierge support.
                </p>
            </div>
            <div>
                <h4 style="font-size:1rem; font-weight:800; margin-bottom:1rem;">Categories</h4>
                <p style="font-size:0.85rem; color:var(--text-muted);">Electronics • Mobiles • Laptops • Shoes</p>
            </div>
            <div>
                <h4 style="font-size:1rem; font-weight:800; margin-bottom:1rem;">Customer Care</h4>
                <p style="font-size:0.85rem; color:var(--text-muted);">Returns • Track Order • FAQs</p>
            </div>
            <div>
                <h4 style="font-size:1rem; font-weight:800; margin-bottom:1rem;">Newsletter</h4>
                <input type="email" placeholder="Your email address..." style="width:100%; font-size:0.85rem; margin-bottom:0.5rem;">
                <button class="btn btn-primary btn-sm" style="width:100%;" onclick="showToast('Subscribed to newsletter!', 'success')">Subscribe</button>
            </div>
        </div>
    </footer>

    <!-- ==========================================
       VANILLA JS APPLICATION ENGINE
       ========================================== -->
    <script>
        /* ==========================================
           SEED DATA & LOCALSTORAGE DATABASE
           ========================================== */
        const SEED_PRODUCTS = [
            { id: "P101", name: "Sony WH-1000XM5 Wireless Headphones", category: "Electronics", brand: "Sony", price: 399.00, originalPrice: 449.00, discount: 11, rating: 4.8, reviewsCount: 1240, stock: 25, image: "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600&auto=format&fit=crop&q=80" },
            { id: "P102", name: "Apple iPad Air 10.9\" M1 Chip", category: "Electronics", brand: "Apple", price: 599.00, originalPrice: 649.00, discount: 8, rating: 4.9, reviewsCount: 890, stock: 18, image: "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=600&auto=format&fit=crop&q=80" },
            { id: "P103", name: "Samsung 55\" QLED 4K Smart TV", category: "Electronics", brand: "Samsung", price: 799.00, originalPrice: 999.00, discount: 20, rating: 4.7, reviewsCount: 650, stock: 12, image: "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=600&auto=format&fit=crop&q=80" },
            { id: "P104", name: "iPhone 15 Pro Max 256GB Titanium", category: "Mobiles", brand: "Apple", price: 1199.00, originalPrice: 1299.00, discount: 8, rating: 4.9, reviewsCount: 2100, stock: 15, image: "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=600&auto=format&fit=crop&q=80" },
            { id: "P105", name: "Samsung Galaxy S24 Ultra 512GB", category: "Mobiles", brand: "Samsung", price: 1299.00, originalPrice: 1419.00, discount: 8, rating: 4.8, reviewsCount: 1750, stock: 20, image: "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=600&auto=format&fit=crop&q=80" },
            { id: "P106", name: "Google Pixel 8 Pro 128GB", category: "Mobiles", brand: "Google", price: 899.00, originalPrice: 999.00, discount: 10, rating: 4.6, reviewsCount: 920, stock: 30, image: "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=600&auto=format&fit=crop&q=80" },
            { id: "P107", name: "MacBook Air M3 15-inch Midnight", category: "Laptops", brand: "Apple", price: 1299.00, originalPrice: 1399.00, discount: 7, rating: 4.9, reviewsCount: 1420, stock: 14, image: "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=600&auto=format&fit=crop&q=80" },
            { id: "P108", name: "Dell XPS 15 OLED Touchscreen", category: "Laptops", brand: "Dell", price: 1799.00, originalPrice: 1999.00, discount: 10, rating: 4.7, reviewsCount: 540, stock: 8, image: "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=600&auto=format&fit=crop&q=80" },
            { id: "P109", name: "ASUS ROG Zephyrus G16 Gaming Laptop", category: "Laptops", brand: "ASUS", price: 1999.00, originalPrice: 2299.00, discount: 13, rating: 4.8, reviewsCount: 410, stock: 5, image: "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=600&auto=format&fit=crop&q=80" },
            { id: "P110", name: "Nike Air Max 270 Sneakers", category: "Shoes", brand: "Nike", price: 150.00, originalPrice: 180.00, discount: 16, rating: 4.7, reviewsCount: 3100, stock: 45, image: "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&auto=format&fit=crop&q=80" },
            { id: "P111", name: "Adidas Ultraboost Light Running Shoes", category: "Shoes", brand: "Adidas", price: 140.00, originalPrice: 190.00, discount: 26, rating: 4.8, reviewsCount: 1890, stock: 35, image: "https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=600&auto=format&fit=crop&q=80" },
            { id: "P112", name: "Apple Watch Ultra 2 Titanium 49mm", category: "Watches", brand: "Apple", price: 799.00, originalPrice: 849.00, discount: 6, rating: 4.9, reviewsCount: 1150, stock: 22, image: "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&auto=format&fit=crop&q=80" }
        ];

        let state = {
            products: [], cart: [], wishlist: [], orders: [],
            currentUser: null, activeView: 'home', activeCategory: 'All', priceMax: 2500
        };

        function initStorage() {
            if (!localStorage.getItem('products')) localStorage.setItem('products', JSON.stringify(SEED_PRODUCTS));
            if (!localStorage.getItem('cart')) localStorage.setItem('cart', JSON.stringify([]));
            if (!localStorage.getItem('wishlist')) localStorage.setItem('wishlist', JSON.stringify([]));
            if (!localStorage.getItem('orders')) localStorage.setItem('orders', JSON.stringify([]));
            if (!localStorage.getItem('theme')) localStorage.setItem('theme', 'light');

            state.products = JSON.parse(localStorage.getItem('products'));
            state.cart = JSON.parse(localStorage.getItem('cart'));
            state.wishlist = JSON.parse(localStorage.getItem('wishlist'));
            state.orders = JSON.parse(localStorage.getItem('orders'));
            state.currentUser = JSON.parse(localStorage.getItem('currentUser')) || null;

            document.documentElement.setAttribute('data-theme', localStorage.getItem('theme'));
        }

        function saveCart() { localStorage.setItem('cart', JSON.stringify(state.cart)); updateBadges(); }
        function saveWishlist() { localStorage.setItem('wishlist', JSON.stringify(state.wishlist)); updateBadges(); }

        /* ==========================================
           ROUTER & NAVIGATION
           ========================================== */
        function navigateTo(viewId, params = {}) {
            document.querySelectorAll('.page-view').forEach(el => el.style.display = 'none');
            const target = document.getElementById(`view-${viewId}`);
            if (target) {
                target.style.display = 'block';
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }

            if (viewId === 'home') renderHome();
            else if (viewId === 'shop') renderShop();
            else if (viewId === 'user-dashboard') renderUserDashboard(params);
            else if (viewId === 'admin-dashboard') renderAdminDashboard();
        }

        function renderHome() {
            const categories = ["All", "Electronics", "Mobiles", "Laptops", "Shoes", "Watches"];
            document.getElementById('category-nav-list').innerHTML = categories.map(c => `
                <li class="category-nav-item ${state.activeCategory === c ? 'active' : ''}" onclick="filterByCategory('${c}')">${c}</li>
            `).join('');

            const featured = state.products.slice(0, 6);
            const trending = state.products.slice(6, 12);
            document.getElementById('featured-products-grid').innerHTML = featured.map(renderCardHtml).join('');
            document.getElementById('trending-products-grid').innerHTML = trending.map(renderCardHtml).join('');
        }

        function filterByCategory(c) {
            state.activeCategory = c;
            navigateTo('shop');
        }

        function renderCardHtml(p) {
            const isWish = state.wishlist.includes(p.id);
            return `
                <div class="product-card">
                    <div class="product-img-wrapper">
                        <img src="${p.image}" alt="${p.name}">
                        <div class="card-overlay-actions">
                            <button class="btn-icon" onclick="toggleWishlist('${p.id}')">
                                <i class="fa-${isWish?'solid':'regular'} fa-heart" style="${isWish?'color:var(--danger)':''}"></i>
                            </button>
                        </div>
                    </div>
                    <div class="product-info">
                        <span class="product-brand">${p.brand}</span>
                        <h4 class="product-title">${p.name}</h4>
                        <div class="product-rating"><i class="fa-solid fa-star"></i> ${p.rating} (${p.reviewsCount})</div>
                        <div class="product-price-row">
                            <span class="current-price">$${p.price.toFixed(2)}</span>
                            <span class="original-price">$${p.originalPrice.toFixed(2)}</span>
                        </div>
                        <button class="btn btn-primary btn-sm" onclick="addToCart('${p.id}')"><i class="fa-solid fa-bag-shopping"></i> Add to Cart</button>
                    </div>
                </div>
            `;
        }

        /* ==========================================
           CART DRAWER ENGINE
           ========================================== */
        function toggleCartDrawer() {
            document.getElementById('cart-drawer-overlay').classList.toggle('active');
            renderCartDrawer();
        }

        function addToCart(id) {
            const existing = state.cart.find(i => i.id === id);
            if (existing) existing.qty += 1;
            else state.cart.push({ id, qty: 1 });
            saveCart();
            showToast('Added to cart!', 'success');
        }

        function renderCartDrawer() {
            const body = document.getElementById('cart-drawer-body');
            if (state.cart.length === 0) {
                body.innerHTML = `<p style="text-align:center; color:var(--text-muted); margin-top:3rem;">Your cart is empty.</p>`;
                document.getElementById('cart-drawer-subtotal').innerText = '$0.00';
                return;
            }

            let subtotal = 0;
            body.innerHTML = state.cart.map(item => {
                const p = state.products.find(x => x.id === item.id);
                if (!p) return '';
                subtotal += p.price * item.qty;
                return `
                    <div class="cart-drawer-item">
                        <img src="${p.image}">
                        <div style="flex:1;">
                            <h4 style="font-size:0.9rem; font-weight:700;">${p.name}</h4>
                            <span style="font-size:0.85rem; color:var(--primary); font-weight:800;">$${p.price.toFixed(2)}</span>
                        </div>
                    </div>
                `;
            }).join('');

            document.getElementById('cart-drawer-subtotal').innerText = `$${subtotal.toFixed(2)}`;
        }

        /* ==========================================
           CHECKOUT ENGINE & CONFETTI
           ========================================== */
        function goToCheckoutStep(step) {
            document.getElementById('chk-step-form-1').style.display = step === 1 ? 'block' : 'none';
            document.getElementById('chk-step-form-2').style.display = step === 2 ? 'block' : 'none';
            document.getElementById('chk-step-form-3').style.display = step === 3 ? 'block' : 'none';
        }

        function placeOrderFinal(mode) {
            const orderId = 'ORD-' + Math.floor(100000 + Math.random() * 900000);
            state.orders.unshift({ orderId, date: new Date().toLocaleDateString(), status: 'Placed', items: [...state.cart] });
            localStorage.setItem('orders', JSON.stringify(state.orders));
            state.cart = [];
            saveCart();
            
            document.getElementById('success-order-id-label').innerText = `Order #${orderId}`;
            goToCheckoutStep(3);
            triggerConfetti();
        }

        function triggerConfetti() {
            const canvas = document.getElementById('confetti-canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            
            let particles = Array.from({length: 80}, () => ({
                x: Math.random() * canvas.width, y: -20,
                r: Math.random() * 6 + 4, d: Math.random() * 10,
                color: `hsl(${Math.random() * 360}, 100%, 50%)`
            }));

            function draw() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                particles.forEach(p => {
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                    ctx.fillStyle = p.color;
                    ctx.fill();
                    p.y += p.d;
                });
            }
            let anim = setInterval(draw, 20);
            setTimeout(() => { clearInterval(anim); ctx.clearRect(0,0,canvas.width,canvas.height); }, 3000);
        }

        /* ==========================================
           UTILITIES, THEME & TOASTS
           ========================================== */
        function toggleWishlist(id) {
            if (state.wishlist.includes(id)) state.wishlist = state.wishlist.filter(x => x !== id);
            else state.wishlist.push(id);
            saveWishlist();
            renderHome();
        }

        function updateBadges() {
            document.getElementById('cart-badge').innerText = state.cart.reduce((a,b) => a + b.qty, 0);
            document.getElementById('wishlist-badge').innerText = state.wishlist.length;
        }

        function showToast(msg, type = 'info') {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            toast.className = 'toast';
            toast.innerHTML = `<i class="fa-solid fa-circle-check" style="color:var(--success);"></i> <span>${msg}</span>`;
            container.appendChild(toast);
            setTimeout(() => toast.remove(), 3000);
        }

        function toggleTheme() {
            const cur = document.documentElement.getAttribute('data-theme');
            const next = cur === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('theme', next);
        }

        function openAuthModal() { document.getElementById('modal-auth').classList.add('active'); }
        function closeModal(id) { document.getElementById(id)?.classList.remove('active'); }

        function handleLoginSubmit(e) {
            e.preventDefault();
            state.currentUser = { name: 'Demo User', role: 'customer' };
            closeModal('modal-auth');
            showToast('Signed in successfully!', 'success');
        }

        window.addEventListener('DOMContentLoaded', () => {
            initStorage();
            updateBadges();
            renderHome();
        });
    </script>
</body>
</html>
<!-- For production: connect authentication, API, database, payment gateway and server-side security here. -->
"""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_code)

print("Upgraded index.html written successfully!")
