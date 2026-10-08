import os

file_path = r"C:\Users\Prince kumar\.gemini\antigravity\scratch\ecommerce-app\index.html"

full_html = """<!-- SINGLE FILE E-COMMERCE APPLICATION -->
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
            --bg-header: rgba(255, 255, 255, 0.94);
            --bg-input: #f1f5f9;
            --bg-subtle: #f1f5f9;
            --glass-bg: rgba(255, 255, 255, 0.75);

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
            --bg-header: rgba(19, 28, 46, 0.94);
            --bg-input: #1e293b;
            --bg-subtle: #182238;
            --glass-bg: rgba(19, 28, 46, 0.75);

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

        html { scroll-behavior: smooth; }

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

        a { color: inherit; text-decoration: none; }

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

        img { max-width: 100%; height: auto; display: block; }

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

        .btn-success {
            background: var(--success);
            color: #ffffff;
        }

        .btn-success:hover {
            opacity: 0.9;
            transform: translateY(-2px);
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
            gap: 1.25rem;
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
            max-width: 520px;
            position: relative;
        }

        .search-input-wrapper {
            position: relative;
            display: flex;
            align-items: center;
        }

        .search-input-wrapper input {
            width: 100%;
            padding-left: 2.85rem;
            padding-right: 2.5rem;
            height: 44px;
            border-radius: var(--radius-full);
            background: var(--bg-input);
            border: 1px solid transparent;
            font-size: 0.875rem;
        }

        .search-input-wrapper input:focus {
            background: var(--bg-card);
            border-color: var(--primary);
        }

        .search-icon {
            position: absolute;
            left: 1.1rem;
            color: var(--text-muted);
            font-size: 1rem;
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

        .search-suggestions.active { display: block; }

        .suggestion-item {
            display: flex;
            align-items: center;
            gap: 0.85rem;
            padding: 0.65rem 0.75rem;
            cursor: pointer;
            border-radius: var(--radius-md);
            transition: var(--transition);
        }

        .suggestion-item:hover { background: var(--bg-subtle); }

        .suggestion-item img {
            width: 44px;
            height: 44px;
            object-fit: cover;
            border-radius: var(--radius-sm);
        }

        .nav-actions {
            display: flex;
            align-items: center;
            gap: 0.65rem;
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
            gap: 1.25rem;
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
        .hero-section { padding: 2rem 0 1.25rem 0; }

        .hero-banner {
            background: linear-gradient(135deg, #1e1b4b 0%, #312e81 40%, #4f46e5 70%, #06b6d4 100%);
            border-radius: var(--radius-lg);
            padding: 3.5rem 3rem;
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
            font-size: 3rem;
            font-weight: 700;
            line-height: 1.15;
            margin-bottom: 1.25rem;
            letter-spacing: -1px;
        }

        .hero-text p {
            font-size: 1.1rem;
            opacity: 0.9;
            margin-bottom: 1.75rem;
            max-width: 520px;
        }

        .hero-image-wrapper img {
            width: 100%;
            max-height: 340px;
            object-fit: contain;
            filter: drop-shadow(0 25px 35px rgba(0,0,0,0.4));
            animation: float 4s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-12px); }
        }

        .promo-features-strip {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.25rem;
            margin: 1.75rem 0;
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
            width: 44px;
            height: 44px;
            border-radius: var(--radius-md);
            background: var(--primary-light);
            color: var(--primary);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
        }

        /* ==========================================
           5. PRODUCT CARD & GALLERY
           ========================================== */
        .section { padding: 2.25rem 0; }

        .section-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.5rem;
        }

        .section-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.6rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }

        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1.5rem;
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
            transform: translateY(-5px);
            box-shadow: var(--shadow-xl);
            border-color: var(--primary-glow);
        }

        .product-img-wrapper {
            position: relative;
            padding-top: 80%;
            background: var(--bg-subtle);
            overflow: hidden;
            cursor: pointer;
        }

        .product-img-wrapper img {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            object-fit: cover;
            transition: transform 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
        }

        .product-card:hover .product-img-wrapper img { transform: scale(1.08); }

        .product-badges {
            position: absolute;
            top: 10px; left: 10px;
            display: flex; flex-direction: column; gap: 0.35rem;
            z-index: 2;
        }

        .card-overlay-actions {
            position: absolute;
            top: 10px; right: 10px;
            display: flex; flex-direction: column; gap: 0.35rem;
            opacity: 0; transform: translateX(10px);
            transition: var(--transition);
            z-index: 2;
        }

        .product-card:hover .card-overlay-actions { opacity: 1; transform: translateX(0); }

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
            margin-bottom: 0.25rem;
        }

        .product-title {
            font-size: 0.95rem;
            font-weight: 700;
            margin-bottom: 0.4rem;
            line-clamp: 2;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
            color: var(--text-main);
            height: 2.8rem;
            cursor: pointer;
        }

        .product-title:hover { color: var(--primary); }

        .product-rating {
            display: flex;
            align-items: center;
            gap: 0.35rem;
            font-size: 0.825rem;
            color: var(--accent);
            margin-bottom: 0.65rem;
        }

        .product-price-row {
            display: flex;
            align-items: baseline;
            gap: 0.5rem;
            margin-top: auto;
            margin-bottom: 0.85rem;
        }

        .current-price { font-size: 1.25rem; font-weight: 800; color: var(--text-main); }
        .original-price { font-size: 0.875rem; color: var(--text-muted); text-decoration: line-through; }

        .card-btn-group {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.5rem;
        }

        /* Flash Sale Header */
        .flash-sale-banner {
            background: linear-gradient(135deg, #ef4444 0%, #f59e0b 100%);
            border-radius: var(--radius-lg);
            padding: 1.25rem 2rem;
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.75rem;
        }

        .countdown-timer {
            display: flex;
            gap: 0.5rem;
            align-items: center;
            font-weight: 800;
        }

        .timer-box {
            background: rgba(0, 0, 0, 0.3);
            padding: 0.4rem 0.7rem;
            border-radius: var(--radius-sm);
            font-size: 1.1rem;
            min-width: 38px;
            text-align: center;
        }

        /* ==========================================
           6. SLIDE-OUT CART DRAWER
           ========================================== */
        .cart-drawer-overlay {
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(6px);
            z-index: 1000;
            opacity: 0;
            visibility: hidden;
            transition: var(--transition);
        }

        .cart-drawer-overlay.active { opacity: 1; visibility: visible; }

        .cart-drawer {
            position: fixed;
            top: 0; right: 0; bottom: 0;
            width: 100%;
            max-width: 440px;
            background: var(--bg-card);
            box-shadow: var(--shadow-xl);
            z-index: 1001;
            transform: translateX(100%);
            transition: transform 0.35s cubic-bezier(0.165, 0.84, 0.44, 1);
            display: flex;
            flex-direction: column;
        }

        .cart-drawer-overlay.active .cart-drawer { transform: translateX(0); }

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
            padding: 1.25rem;
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .cart-drawer-item {
            display: flex;
            gap: 1rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid var(--border-color);
            align-items: center;
        }

        .cart-drawer-item img {
            width: 65px;
            height: 65px;
            object-fit: cover;
            border-radius: var(--radius-md);
            background: var(--bg-subtle);
        }

        .cart-drawer-footer {
            padding: 1.25rem 1.5rem;
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
            width: 30px;
            height: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--bg-subtle);
            font-weight: 700;
        }

        .qty-picker input {
            width: 38px;
            height: 30px;
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
            max-width: 800px;
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
            width: 34px; height: 34px;
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            background: var(--bg-subtle);
            cursor: pointer;
            color: var(--text-muted);
            font-size: 1.1rem;
        }

        .modal-close:hover { color: var(--danger); }

        /* Checkout Progress */
        .checkout-progress {
            display: flex;
            justify-content: space-between;
            margin-bottom: 2rem;
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
            width: 36px; height: 36px;
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
        }

        /* Dashboards */
        .dashboard-grid {
            display: grid;
            grid-template-columns: 240px 1fr;
            gap: 2rem;
            padding: 2rem 0;
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
            padding: 0.75rem 1rem;
            border-radius: var(--radius-md);
            font-weight: 700;
            font-size: 0.9rem;
            color: var(--text-muted);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.75rem;
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
            cursor: pointer;
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
            padding: 0.85rem 1.25rem;
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-xl);
            display: flex;
            align-items: center;
            gap: 0.75rem;
            min-width: 280px;
            animation: slideInRight 0.3s ease;
        }

        @keyframes slideInRight {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }

        /* Canvas Confetti */
        #confetti-canvas {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            pointer-events: none;
            z-index: 99999;
        }

        /* Responsive Breakpoints */
        @media (max-width: 1024px) {
            .hero-banner { grid-template-columns: 1fr; text-align: center; }
            .hero-image-wrapper { display: none; }
            .promo-features-strip { grid-template-columns: repeat(2, 1fr); }
            .dashboard-grid { grid-template-columns: 1fr; }
        }

        @media (max-width: 768px) {
            .mobile-bottom-nav { display: flex; }
            .promo-features-strip { grid-template-columns: 1fr; }
            body { padding-bottom: 64px; }
            .card-btn-group { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>

    <!-- Canvas Confetti Layer -->
    <canvas id="confetti-canvas"></canvas>

    <!-- Top Announcement Ribbon -->
    <div class="announcement-bar">
        ⚡ 40+ NEW PRODUCTS JUST ADDED! Use code <strong>WELCOME10</strong> for 10% OFF + Free Express Shipping!
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
                    <input type="text" id="global-search" placeholder="Search 40+ products, categories, brands..." oninput="handleSearchInput(this.value)">
                </div>
                <div id="search-suggestions" class="search-suggestions"></div>
            </div>

            <!-- Navbar Actions -->
            <div class="nav-actions">
                <!-- Add Product / Item Button -->
                <button class="btn btn-primary btn-sm" onclick="openAddItemModal()" title="Add New Item to Store">
                    <i class="fa-solid fa-plus-circle"></i> Add Item
                </button>

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
                    <button class="btn btn-secondary btn-sm" onclick="openAuthModal('login')">
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
                            <p>Discover flagship smartphones, high-performance laptops, footwear, luxury watches, appliances, and cosmetics with free express delivery.</p>
                            <div style="display:flex; gap:1rem; flex-wrap:wrap;">
                                <button class="btn btn-primary btn-lg" onclick="navigateTo('shop')">
                                    <i class="fa-solid fa-bag-shopping"></i> Shop Catalog (40+ Items)
                                </button>
                                <button class="btn btn-secondary btn-lg" onclick="openAddItemModal()">
                                    <i class="fa-solid fa-plus"></i> Add New Product
                                </button>
                            </div>
                        </div>
                        <div class="hero-image-wrapper">
                            <img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&auto=format&fit=crop&q=80" alt="Headphones Hero">
                        </div>
                    </div>
                </div>

                <!-- Feature Strip -->
                <div class="promo-features-strip">
                    <div class="feature-box">
                        <div class="feature-icon"><i class="fa-solid fa-truck-fast"></i></div>
                        <div><strong style="font-size:0.9rem;">Free Shipping</strong><p style="font-size:0.75rem; color:var(--text-muted);">On orders above $50</p></div>
                    </div>
                    <div class="feature-box">
                        <div class="feature-icon"><i class="fa-solid fa-rotate-left"></i></div>
                        <div><strong style="font-size:0.9rem;">30-Day Returns</strong><p style="font-size:0.75rem; color:var(--text-muted);">Instant replacements</p></div>
                    </div>
                    <div class="feature-box">
                        <div class="feature-icon"><i class="fa-solid fa-lock"></i></div>
                        <div><strong style="font-size:0.9rem;">Secure Checkout</strong><p style="font-size:0.75rem; color:var(--text-muted);">256-Bit SSL Protection</p></div>
                    </div>
                    <div class="feature-box">
                        <div class="feature-icon"><i class="fa-solid fa-headset"></i></div>
                        <div><strong style="font-size:0.9rem;">24/7 Live Support</strong><p style="font-size:0.75rem; color:var(--text-muted);">Instant chat assistance</p></div>
                    </div>
                </div>

                <!-- Flash Sale Ticker Section -->
                <div class="flash-sale-banner">
                    <div style="display:flex; align-items:center; gap:1.25rem;">
                        <i class="fa-solid fa-bolt" style="font-size:2rem;"></i>
                        <div>
                            <h3 style="font-size:1.2rem; font-weight:800;">Flash Sale Countdown</h3>
                            <p style="font-size:0.85rem; opacity:0.95;">Grab mega deals across top categories!</p>
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
                        <button class="btn btn-secondary btn-sm" onclick="navigateTo('shop')">View All Items <i class="fa-solid fa-arrow-right"></i></button>
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
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.25rem;">
                            <h3 style="font-size:1.1rem; font-weight:800;">Filters</h3>
                            <button class="btn btn-sm btn-primary" onclick="openAddItemModal()">+ Add Item</button>
                        </div>
                        
                        <div style="margin-bottom:1.5rem;">
                            <label style="font-size:0.85rem; font-weight:800; display:block; margin-bottom:0.5rem;">Categories</label>
                            <select id="shop-category-select" onchange="filterByCategory(this.value)" style="width:100%;">
                                <option value="All">All Categories (40+ Items)</option>
                                <option value="Electronics">Electronics</option>
                                <option value="Mobiles">Mobiles</option>
                                <option value="Laptops">Laptops</option>
                                <option value="Fashion">Fashion</option>
                                <option value="Shoes">Shoes</option>
                                <option value="Watches">Watches</option>
                                <option value="Accessories">Accessories</option>
                                <option value="Home & Kitchen">Home & Kitchen</option>
                                <option value="Beauty">Beauty</option>
                                <option value="Gaming">Gaming</option>
                            </select>
                        </div>

                        <div style="margin-bottom:1.5rem;">
                            <label style="font-size:0.85rem; font-weight:800; display:block; margin-bottom:0.5rem;">Price Range</label>
                            <span id="price-val-label" style="font-size:0.85rem; color:var(--primary); font-weight:700;">$0 - $2500</span>
                            <input type="range" id="price-slider" min="0" max="2500" step="50" value="2500" style="width:100%; margin-top:0.5rem;" oninput="updatePriceFilter(this.value)">
                        </div>

                        <button class="btn btn-secondary btn-sm" style="width:100%;" onclick="resetShopFilters()">
                            <i class="fa-solid fa-rotate-left"></i> Reset Filters
                        </button>
                    </aside>

                    <!-- Main Grid -->
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center; background:var(--bg-card); border:1px solid var(--border-color); padding:0.85rem 1.25rem; border-radius:var(--radius-md); margin-bottom:1.5rem;">
                            <span id="shop-results-count" style="font-weight:700; font-size:0.9rem; color:var(--text-muted);">Showing 40 products</span>
                            <div style="display:flex; gap:0.5rem; align-items:center;">
                                <select id="shop-sort-select" onchange="applyShopFilters()" style="padding:0.4rem 0.8rem; font-size:0.85rem;">
                                    <option value="featured">Featured</option>
                                    <option value="price-low">Price: Low to High</option>
                                    <option value="price-high">Price: High to Low</option>
                                    <option value="rating">Highest Rated</option>
                                </select>
                            </div>
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
                            <input type="text" id="chk-name" placeholder="Full Name *" value="Demo User" required>
                            <input type="tel" id="chk-phone" placeholder="Mobile Number *" value="+1 234 567 8900" required>
                        </div>
                        <input type="text" id="chk-address" placeholder="Street Address *" value="123 Shopping Avenue, Suite 400" style="width:100%; margin-bottom:1rem;" required>
                        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:1rem; margin-bottom:1.5rem;">
                            <input type="text" id="chk-city" placeholder="City *" value="New York" required>
                            <input type="text" id="chk-state" placeholder="State *" value="NY" required>
                            <input type="text" id="chk-zip" placeholder="ZIP Code *" value="10001" required>
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
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem;">
                    <h1 style="font-size: 1.8rem; font-weight: 800;"><i class="fa-solid fa-chart-pie"></i> Store Admin Panel</h1>
                    <button class="btn btn-primary" onclick="openAddItemModal()"><i class="fa-solid fa-plus"></i> Add New Product</button>
                </div>
                
                <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:1.5rem; margin-bottom:2rem;">
                    <h3 style="font-size:1.1rem; font-weight:800; margin-bottom:1rem;">Monthly Sales Trend</h3>
                    <div style="height:260px;"><canvas id="adminSalesChart"></canvas></div>
                </div>

                <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); overflow-x:auto;">
                    <div style="padding:1rem; background:var(--bg-subtle); display:flex; justify-content:space-between; align-items:center;">
                        <strong>Product Inventory (<span id="admin-inventory-count">40</span> items)</strong>
                        <button class="btn btn-sm btn-primary" onclick="openAddItemModal()">+ Add Product</button>
                    </div>
                    <table style="width:100%; border-collapse:collapse; font-size:0.875rem;">
                        <thead>
                            <tr style="border-bottom:1px solid var(--border-color); text-align:left; background:var(--bg-subtle);">
                                <th style="padding:0.75rem 1rem;">ID</th>
                                <th style="padding:0.75rem 1rem;">Name</th>
                                <th style="padding:0.75rem 1rem;">Category</th>
                                <th style="padding:0.75rem 1rem;">Price</th>
                                <th style="padding:0.75rem 1rem;">Stock</th>
                                <th style="padding:0.75rem 1rem;">Action</th>
                            </tr>
                        </thead>
                        <tbody id="admin-inventory-body"></tbody>
                    </table>
                </div>
            </div>
        </section>

    </main>

    <!-- ==========================================
       MODAL: ADD NEW ITEM / PRODUCT
       ========================================== -->
    <div id="modal-add-item" class="modal-overlay">
        <div class="modal-content" style="max-width: 580px;">
            <div class="modal-close" onclick="closeModal('modal-add-item')">&times;</div>
            <h3 style="font-size: 1.35rem; font-weight: 800; margin-bottom: 1.25rem;"><i class="fa-solid fa-cart-plus" style="color:var(--primary);"></i> Add New Item to Store</h3>
            <form onsubmit="handleAddNewItem(event)">
                <div style="margin-bottom: 1rem;">
                    <label style="font-size: 0.85rem; font-weight: 700; display:block; margin-bottom: 0.35rem;">Item / Product Name *</label>
                    <input type="text" id="add-item-name" placeholder="e.g. Sony Wireless Earbuds" style="width:100%;" required>
                </div>
                
                <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
                    <div>
                        <label style="font-size: 0.85rem; font-weight: 700; display:block; margin-bottom: 0.35rem;">Category *</label>
                        <select id="add-item-category" style="width:100%;" required>
                            <option value="Electronics">Electronics</option>
                            <option value="Mobiles">Mobiles</option>
                            <option value="Laptops">Laptops</option>
                            <option value="Fashion">Fashion</option>
                            <option value="Shoes">Shoes</option>
                            <option value="Watches">Watches</option>
                            <option value="Accessories">Accessories</option>
                            <option value="Home & Kitchen">Home & Kitchen</option>
                            <option value="Beauty">Beauty</option>
                            <option value="Gaming">Gaming</option>
                        </select>
                    </div>
                    <div>
                        <label style="font-size: 0.85rem; font-weight: 700; display:block; margin-bottom: 0.35rem;">Brand *</label>
                        <input type="text" id="add-item-brand" placeholder="e.g. Sony, Apple, Nike" style="width:100%;" required>
                    </div>
                </div>

                <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
                    <div>
                        <label style="font-size: 0.85rem; font-weight: 700; display:block; margin-bottom: 0.35rem;">Price ($) *</label>
                        <input type="number" step="0.01" id="add-item-price" placeholder="199.99" style="width:100%;" required>
                    </div>
                    <div>
                        <label style="font-size: 0.85rem; font-weight: 700; display:block; margin-bottom: 0.35rem;">Original MRP ($)</label>
                        <input type="number" step="0.01" id="add-item-orig-price" placeholder="249.99" style="width:100%;">
                    </div>
                    <div>
                        <label style="font-size: 0.85rem; font-weight: 700; display:block; margin-bottom: 0.35rem;">Stock Qty *</label>
                        <input type="number" id="add-item-stock" placeholder="25" value="20" style="width:100%;" required>
                    </div>
                </div>

                <div style="margin-bottom: 1rem;">
                    <label style="font-size: 0.85rem; font-weight: 700; display:block; margin-bottom: 0.35rem;">Image URL *</label>
                    <input type="url" id="add-item-image" placeholder="https://images.unsplash.com/photo-..." value="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600&auto=format&fit=crop&q=80" style="width:100%;" required>
                </div>

                <div style="margin-bottom: 1.5rem;">
                    <label style="font-size: 0.85rem; font-weight: 700; display:block; margin-bottom: 0.35rem;">Product Description</label>
                    <textarea id="add-item-desc" rows="3" placeholder="Enter product highlights, features, or details..." style="width:100%;">Premium high-quality product with manufacturer warranty.</textarea>
                </div>

                <button type="submit" class="btn btn-primary" style="width: 100%;">
                    <i class="fa-solid fa-plus-circle"></i> Add Item to Store Now
                </button>
            </form>
        </div>
    </div>

    <!-- ==========================================
       MODAL: PRODUCT QUICK VIEW & DETAILS
       ========================================== -->
    <div id="modal-product-details" class="modal-overlay">
        <div class="modal-content" style="max-width: 820px;">
            <div class="modal-close" onclick="closeModal('modal-product-details')">&times;</div>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 2rem;" id="modal-product-detail-body">
                <!-- Dynamically rendered by JS -->
            </div>
        </div>
    </div>

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
                <div style="display:flex; justify-content:space-between; margin-bottom:1rem; font-weight:800; font-size:1.1rem;">
                    <span>Total Subtotal:</span>
                    <span id="cart-drawer-subtotal" style="color:var(--primary);">$0.00</span>
                </div>
                <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
                    <button class="btn btn-secondary btn-sm" onclick="toggleCartDrawer(); navigateTo('shop');">
                        Add More Items
                    </button>
                    <button class="btn btn-primary" onclick="toggleCartDrawer(); navigateTo('checkout');">
                        Checkout <i class="fa-solid fa-arrow-right"></i>
                    </button>
                </div>
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
                <input type="email" id="login-email" placeholder="Email (user@example.com)" value="user@example.com" style="width:100%; margin-bottom:0.75rem;" required>
                <input type="password" id="login-password" placeholder="Password (123456)" value="123456" style="width:100%; margin-bottom:1rem;" required>
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
        <div class="mobile-nav-btn" onclick="openAddItemModal()"><i class="fa-solid fa-plus-circle"></i>Add</div>
        <div class="mobile-nav-btn" onclick="toggleCartDrawer()"><i class="fa-solid fa-bag-shopping"></i>Cart</div>
        <div class="mobile-nav-btn" onclick="openAuthModal('login')"><i class="fa-solid fa-user"></i>Account</div>
    </div>

    <!-- FOOTER -->
    <footer>
        <div class="container footer-grid" style="display:grid; grid-template-columns: 2fr 1fr 1fr; gap:2.5rem; margin-bottom:2rem;">
            <div>
                <a href="javascript:void(0)" class="logo" style="margin-bottom:1rem; display:inline-flex;">
                    <div class="logo-icon"><i class="fa-solid fa-cube"></i></div>
                    <span>ShopNexus.</span>
                </a>
                <p style="font-size:0.875rem; color:var(--text-muted); max-width:320px;">
                    Next-generation commercial e-commerce platform with 40+ products, fast delivery, and instant support.
                </p>
            </div>
            <div>
                <h4 style="font-size:1rem; font-weight:800; margin-bottom:1rem;">Quick Categories</h4>
                <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.8;">
                    Electronics • Mobiles • Laptops • Fashion • Shoes • Watches • Gaming • Beauty
                </p>
            </div>
            <div>
                <h4 style="font-size:1rem; font-weight:800; margin-bottom:1rem;">Customer Care</h4>
                <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.8;">
                    Returns • Track Order • FAQs • Support 24/7
                </p>
            </div>
        </div>
        <div class="container" style="border-top: 1px solid var(--border-color); padding-top: 1.25rem; text-align:center; font-size: 0.8rem; color: var(--text-muted);">
            © 2026 ShopNexus Prime Inc. Single-File Commercial E-Commerce Platform.
        </div>
    </footer>

    <!-- ==========================================
       VANILLA JS APPLICATION ENGINE
       ========================================== -->
    <script>
        /* ==========================================
           SEED DATA: 40 REALISTIC DEMO PRODUCTS
           ACROSS 10 DIVERSE CATEGORIES
           ========================================== */
        const SEED_PRODUCTS = [
            // 1. Electronics (4)
            { id: "P101", name: "Sony WH-1000XM5 Wireless Headphones", category: "Electronics", brand: "Sony", price: 399.00, originalPrice: 449.00, discount: 11, rating: 4.8, reviewsCount: 1240, stock: 25, badge: "BEST SELLER", image: "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600&auto=format&fit=crop&q=80", description: "Industry-leading noise canceling headphones with 30-hour battery life and crystal clear calling." },
            { id: "P102", name: "Apple iPad Air 10.9\" M1 Chip", category: "Electronics", brand: "Apple", price: 599.00, originalPrice: 649.00, discount: 8, rating: 4.9, reviewsCount: 890, stock: 18, badge: "TRENDING", image: "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=600&auto=format&fit=crop&q=80", description: "Apple M1 chip with 10.9-inch Liquid Retina display, Touch ID, and all-day battery life." },
            { id: "P103", name: "Samsung 55\" QLED 4K Smart TV", category: "Electronics", brand: "Samsung", price: 799.00, originalPrice: 999.00, discount: 20, rating: 4.7, reviewsCount: 650, stock: 12, badge: "SALE", image: "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=600&auto=format&fit=crop&q=80", description: "Quantum Dot technology with 100% color volume and 120Hz native refresh rate." },
            { id: "P104", name: "Bose QuietComfort 45 Bluetooth Headphones", category: "Electronics", brand: "Bose", price: 279.00, originalPrice: 329.00, discount: 15, rating: 4.7, reviewsCount: 520, stock: 16, badge: "POPULAR", image: "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=600&auto=format&fit=crop&q=80", description: "Iconic quiet comfort with acoustic noise cancellation and high-fidelity audio." },

            // 2. Mobiles (4)
            { id: "P105", name: "iPhone 15 Pro Max 256GB Titanium", category: "Mobiles", brand: "Apple", price: 1199.00, originalPrice: 1299.00, discount: 8, rating: 4.9, reviewsCount: 2100, stock: 15, badge: "HOT", image: "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=600&auto=format&fit=crop&q=80", description: "Titanium chassis with A17 Pro processor, 48MP main camera, and USB-C speed." },
            { id: "P106", name: "Samsung Galaxy S24 Ultra 512GB", category: "Mobiles", brand: "Samsung", price: 1299.00, originalPrice: 1419.00, discount: 8, rating: 4.8, reviewsCount: 1750, stock: 20, badge: "NEW", image: "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=600&auto=format&fit=crop&q=80", description: "Galaxy AI powerhouse with titanium frame, integrated S-Pen stylus, and 200MP camera." },
            { id: "P107", name: "Google Pixel 8 Pro 128GB", category: "Mobiles", brand: "Google", price: 899.00, originalPrice: 999.00, discount: 10, rating: 4.6, reviewsCount: 920, stock: 30, badge: "LIMITED", image: "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=600&auto=format&fit=crop&q=80", description: "Google Tensor G3 chip with industry-defining photo AI features and 7 years of OS upgrades." },
            { id: "P108", name: "OnePlus 12 5G 256GB Emerald Green", category: "Mobiles", brand: "OnePlus", price: 799.00, originalPrice: 899.00, discount: 11, rating: 4.7, reviewsCount: 680, stock: 22, badge: "SALE", image: "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600&auto=format&fit=crop&q=80", description: "Snapdragon 8 Gen 3 with 100W SUPERVOOC charging and 4th Gen Hasselblad camera." },

            // 3. Laptops (4)
            { id: "P109", name: "MacBook Air M3 15-inch Midnight", category: "Laptops", brand: "Apple", price: 1299.00, originalPrice: 1399.00, discount: 7, rating: 4.9, reviewsCount: 1420, stock: 14, badge: "BEST SELLER", image: "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=600&auto=format&fit=crop&q=80", description: "Strikingly thin design with M3 speed, 18-hour battery life, and Liquid Retina display." },
            { id: "P110", name: "Dell XPS 15 OLED Touchscreen", category: "Laptops", brand: "Dell", price: 1799.00, originalPrice: 1999.00, discount: 10, rating: 4.7, reviewsCount: 540, stock: 8, badge: "PREMIUM", image: "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=600&auto=format&fit=crop&q=80", description: "13th Gen Intel Core i9 processor with breathtaking 3.5K OLED InfinityEdge touch screen." },
            { id: "P111", name: "ASUS ROG Zephyrus G16 Gaming Laptop", category: "Laptops", brand: "ASUS", price: 1999.00, originalPrice: 2299.00, discount: 13, rating: 4.8, reviewsCount: 410, stock: 5, badge: "GAMING", image: "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=600&auto=format&fit=crop&q=80", description: "240Hz ROG Nebula OLED display powered by NVIDIA GeForce RTX 4070." },
            { id: "P112", name: "Lenovo ThinkPad X1 Carbon Gen 11", category: "Laptops", brand: "Lenovo", price: 1499.00, originalPrice: 1699.00, discount: 12, rating: 4.8, reviewsCount: 310, stock: 11, badge: "BUSINESS", image: "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=600&auto=format&fit=crop&q=80", description: "Ultralight carbon-fiber business laptop tested against military-grade durability standards." },

            // 4. Fashion (4)
            { id: "P113", name: "Levi's Men's Slim Fit Trucker Denim Jacket", category: "Fashion", brand: "Levi's", price: 79.00, originalPrice: 110.00, discount: 28, rating: 4.5, reviewsCount: 320, stock: 50, badge: "CLASSIC", image: "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=600&auto=format&fit=crop&q=80", description: "Timeless trucker denim jacket crafted from 100% premium rigid cotton fabric." },
            { id: "P114", name: "Zara Floral Summer Maxi Dress", category: "Fashion", brand: "Zara", price: 59.00, originalPrice: 89.00, discount: 33, rating: 4.6, reviewsCount: 280, stock: 40, badge: "TRENDING", image: "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=600&auto=format&fit=crop&q=80", description: "Lightweight breathable viscose maxi dress featuring vibrant floral watercolor prints." },
            { id: "P115", name: "AllSaints Genuine Leather Biker Jacket", category: "Fashion", brand: "AllSaints", price: 349.00, originalPrice: 499.00, discount: 30, rating: 4.8, reviewsCount: 190, stock: 12, badge: "LUXURY", image: "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=600&auto=format&fit=crop&q=80", description: "Handcrafted soft sheepskin leather jacket with silver asymmetric zips." },
            { id: "P116", name: "Tommy Hilfiger Classic Oxford Cotton Shirt", category: "Fashion", brand: "Tommy Hilfiger", price: 65.00, originalPrice: 85.00, discount: 24, rating: 4.6, reviewsCount: 410, stock: 35, badge: "NEW", image: "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=600&auto=format&fit=crop&q=80", description: "Tailored fit pure cotton button-down shirt with iconic flag chest embroidery." },

            // 5. Shoes (4)
            { id: "P117", name: "Nike Air Max 270 Sneakers", category: "Shoes", brand: "Nike", price: 150.00, originalPrice: 180.00, discount: 16, rating: 4.7, reviewsCount: 3100, stock: 45, badge: "BEST SELLER", image: "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&auto=format&fit=crop&q=80", description: "Features Nike's largest heel Air unit for all-day comfort and a sleek lifestyle look." },
            { id: "P118", name: "Adidas Ultraboost Light Running Shoes", category: "Shoes", brand: "Adidas", price: 140.00, originalPrice: 190.00, discount: 26, rating: 4.8, reviewsCount: 1890, stock: 35, badge: "SALE", image: "https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=600&auto=format&fit=crop&q=80", description: "Lightest Ultraboost ever made with 30% lighter Light BOOST material." },
            { id: "P119", name: "Puma RS-X Reinvent Retro Sneakers", category: "Shoes", brand: "Puma", price: 95.00, originalPrice: 120.00, discount: 20, rating: 4.5, reviewsCount: 760, stock: 28, badge: "TRENDING", image: "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=600&auto=format&fit=crop&q=80", description: "Chunky silhouette with bold color blocking and retro Running System technology." },
            { id: "P120", name: "Jordan 1 Retro High OG Chicago", category: "Shoes", brand: "Nike Jordan", price: 180.00, originalPrice: 220.00, discount: 18, rating: 4.9, reviewsCount: 2400, stock: 8, badge: "RARE", image: "https://images.unsplash.com/photo-1552346154-21d32810aba3?w=600&auto=format&fit=crop&q=80", description: "Legendary silhouette in red, white, and black leather with encapsulated Air sole unit." },

            // 6. Watches (4)
            { id: "P121", name: "Apple Watch Ultra 2 Titanium 49mm", category: "Watches", brand: "Apple", price: 799.00, originalPrice: 849.00, discount: 6, rating: 4.9, reviewsCount: 1150, stock: 22, badge: "FLAGSHIP", image: "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&auto=format&fit=crop&q=80", description: "Aerospace-grade titanium case, precision dual-frequency GPS, and up to 36 hours of battery." },
            { id: "P122", name: "Fossil Gen 6 Touchscreen Smartwatch", category: "Watches", brand: "Fossil", price: 199.00, originalPrice: 299.00, discount: 33, rating: 4.3, reviewsCount: 480, stock: 18, badge: "SALE", image: "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=600&auto=format&fit=crop&q=80", description: "Snapdragon Wear 4100+ platform with heart rate, SpO2, and fast magnetic charging." },
            { id: "P123", name: "Seiko Automatic Diver's 200m Watch", category: "Watches", brand: "Seiko", price: 320.00, originalPrice: 420.00, discount: 23, rating: 4.8, reviewsCount: 620, stock: 10, badge: "CLASSIC", image: "https://images.unsplash.com/photo-1524805444758-089113d48a6d?w=600&auto=format&fit=crop&q=80", description: "Iconic Japanese mechanical automatic timepiece with ISO-certified 200m water resistance." },
            { id: "P124", name: "Casio G-Shock GA-2100 Octagon Carbon", category: "Watches", brand: "Casio", price: 99.00, originalPrice: 120.00, discount: 17, rating: 4.8, reviewsCount: 1300, stock: 40, badge: "TOUGH", image: "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=600&auto=format&fit=crop&q=80", description: "Shock resistant carbon core guard structure in ultra-slim octagonal bezel." },

            // 7. Accessories (4)
            { id: "P125", name: "Ray-Ban Classic Wayfarer Sunglasses", category: "Accessories", brand: "Ray-Ban", price: 135.00, originalPrice: 165.00, discount: 18, rating: 4.7, reviewsCount: 1400, stock: 60, badge: "ICONIC", image: "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=600&auto=format&fit=crop&q=80", description: "The iconic Wayfarer shape with lightweight black acetate and 100% UV400 glass lenses." },
            { id: "P126", name: "Samsonite Pro Travel Business Backpack", category: "Accessories", brand: "Samsonite", price: 110.00, originalPrice: 150.00, discount: 26, rating: 4.6, reviewsCount: 530, stock: 30, badge: "TRAVEL", image: "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=600&auto=format&fit=crop&q=80", description: "Ballistic water-resistant nylon with TSA-approved laptop fold and pass-through USB." },
            { id: "P127", name: "Anker 737 Power Bank 24,000mAh 140W", category: "Accessories", brand: "Anker", price: 99.00, originalPrice: 149.00, discount: 33, rating: 4.9, reviewsCount: 2300, stock: 80, badge: "TOP RATED", image: "https://images.unsplash.com/photo-1609592424109-dd9892f1b177?w=600&auto=format&fit=crop&q=80", description: "Ultra-powerful 140W bi-directional fast charging with interactive smart digital screen." },
            { id: "P128", name: "Bellroy Slim Leather Sleeve Wallet", category: "Accessories", brand: "Bellroy", price: 79.00, originalPrice: 95.00, discount: 17, rating: 4.7, reviewsCount: 880, stock: 45, badge: "SLIM", image: "https://images.unsplash.com/photo-1627123424574-724758594e93?w=600&auto=format&fit=crop&q=80", description: "Environmentally certified premium leather card wallet holding up to 12 cards with pull tab." },

            // 8. Home & Kitchen (4)
            { id: "P129", name: "Nespresso Vertuo Next Coffee Machine", category: "Home & Kitchen", brand: "Nespresso", price: 159.00, originalPrice: 209.00, discount: 24, rating: 4.6, reviewsCount: 1780, stock: 25, badge: "BEST SELLER", image: "https://images.unsplash.com/photo-1517668808822-9fea0282b941?w=600&auto=format&fit=crop&q=80", description: "Centrifusion technology reads capsule barcodes to brew exceptional coffee and rich crema." },
            { id: "P130", name: "Dyson V15 Detect Cordless Vacuum", category: "Home & Kitchen", brand: "Dyson", price: 649.00, originalPrice: 749.00, discount: 13, rating: 4.8, reviewsCount: 940, stock: 14, badge: "FLAGSHIP", image: "https://images.unsplash.com/photo-1558317374-067fb5f30001?w=600&auto=format&fit=crop&q=80", description: "Laser illumination reveals invisible microscopic dust with whole-machine HEPA filtration." },
            { id: "P131", name: "Instant Pot Duo 7-in-1 Electric Cooker", category: "Home & Kitchen", brand: "Instant Pot", price: 89.00, originalPrice: 120.00, discount: 25, rating: 4.7, reviewsCount: 4200, stock: 40, badge: "POPULAR", image: "https://images.unsplash.com/photo-1585515320310-259814833e62?w=600&auto=format&fit=crop&q=80", description: "Combines 7 appliances in one: pressure cooker, slow cooker, rice cooker, steamer, and yogurt maker." },
            { id: "P132", name: "Philips XXL Smart Sensing Airfryer", category: "Home & Kitchen", brand: "Philips", price: 199.00, originalPrice: 249.00, discount: 20, rating: 4.8, reviewsCount: 1100, stock: 20, badge: "HOT", image: "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?w=600&auto=format&fit=crop&q=80", description: "Fat Removal technology cooks meals with up to 90% less fat and automatic heat sensing." },

            // 9. Beauty (4)
            { id: "P133", name: "Estée Lauder Advanced Night Repair 50ml", category: "Beauty", brand: "Estée Lauder", price: 115.00, originalPrice: 135.00, discount: 14, rating: 4.8, reviewsCount: 1250, stock: 50, badge: "LUXURY", image: "https://images.unsplash.com/photo-1608248597262-838d6970f592?w=600&auto=format&fit=crop&q=80", description: "Deep night recovery serum reduces visible signs of aging with hyaluronic acid hydration." },
            { id: "P134", name: "Dyson Airwrap Multi-Styler Complete", category: "Beauty", brand: "Dyson", price: 549.00, originalPrice: 599.00, discount: 8, rating: 4.9, reviewsCount: 2100, stock: 9, badge: "TRENDING", image: "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=600&auto=format&fit=crop&q=80", description: "Curl, shape, and hide flyaways using Coanda aerodynamic airflow without heat damage." },
            { id: "P135", name: "Chanel Bleu de Chanel Parfum 100ml", category: "Beauty", brand: "Chanel", price: 165.00, originalPrice: 180.00, discount: 8, rating: 4.9, reviewsCount: 980, stock: 20, badge: "PREMIUM", image: "https://images.unsplash.com/photo-1541643600914-78b084683601?w=600&auto=format&fit=crop&q=80", description: "A profound woody aromatic fragrance with fresh citrus opening and rich sandalwood." },
            { id: "P136", name: "Olaplex No. 3 Hair Perfector Repair", category: "Beauty", brand: "Olaplex", price: 30.00, originalPrice: 38.00, discount: 21, rating: 4.7, reviewsCount: 3500, stock: 60, badge: "BEST SELLER", image: "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=600&auto=format&fit=crop&q=80", description: "At-home bond-building treatment that repairs damaged and compromised hair structure." },

            // 10. Gaming (4)
            { id: "P137", name: "Sony PlayStation 5 Slim Digital Console", category: "Gaming", brand: "Sony", price: 499.00, originalPrice: 549.00, discount: 9, rating: 4.9, reviewsCount: 5400, stock: 16, badge: "HOT", image: "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=600&auto=format&fit=crop&q=80", description: "Slimmer PS5 console with 1TB SSD storage and immersive DualSense haptic feedback." },
            { id: "P138", name: "Xbox Series X 1TB Gaming Console", category: "Gaming", brand: "Microsoft", price: 479.00, originalPrice: 529.00, discount: 9, rating: 4.8, reviewsCount: 3800, stock: 18, badge: "POWER", image: "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=600&auto=format&fit=crop&q=80", description: "Fastest Xbox ever with 12 teraflops processing power and 4K gaming up to 120 FPS." },
            { id: "P139", name: "Nintendo Switch OLED Model White", category: "Gaming", brand: "Nintendo", price: 349.00, originalPrice: 379.00, discount: 8, rating: 4.8, reviewsCount: 4900, stock: 35, badge: "POPULAR", image: "https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?w=600&auto=format&fit=crop&q=80", description: "Vibrant 7-inch OLED screen with wide adjustable stand and enhanced onboard audio." },
            { id: "P140", name: "Logitech G Pro X Wireless Gaming Headset", category: "Gaming", brand: "Logitech", price: 169.00, originalPrice: 229.00, discount: 26, rating: 4.7, reviewsCount: 1650, stock: 24, badge: "ESPORTS", image: "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=600&auto=format&fit=crop&q=80", description: "Pro-G 50mm precision drivers with Blue VO!CE microphone technology and LIGHTSPEED wireless." }
        ];

        /* ==========================================
           APPLICATION STATE & LOCAL STORAGE
           ========================================== */
        let state = {
            products: [],
            cart: [],
            wishlist: [],
            orders: [],
            currentUser: null,
            activeView: 'home',
            activeCategory: 'All',
            priceMax: 2500,
            searchQuery: ''
        };

        function initStorage() {
            // Check if existing stored products is empty or fewer than seed products
            const stored = localStorage.getItem('products');
            if (!stored || JSON.parse(stored).length < SEED_PRODUCTS.length) {
                localStorage.setItem('products', JSON.stringify(SEED_PRODUCTS));
            }

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
            updateThemeIcon();
        }

        function saveProducts() { localStorage.setItem('products', JSON.stringify(state.products)); }
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
            // Category navigation pills (10 categories)
            const categories = ["All", "Electronics", "Mobiles", "Laptops", "Fashion", "Shoes", "Watches", "Accessories", "Home & Kitchen", "Beauty", "Gaming"];
            document.getElementById('category-nav-list').innerHTML = categories.map(c => `
                <li class="category-nav-item ${state.activeCategory === c ? 'active' : ''}" onclick="filterByCategory('${c}')">
                    ${c}
                </li>
            `).join('');

            const featured = state.products.slice(0, 8);
            const trending = state.products.slice(8, 16);
            document.getElementById('featured-products-grid').innerHTML = featured.map(renderCardHtml).join('');
            document.getElementById('trending-products-grid').innerHTML = trending.map(renderCardHtml).join('');
        }

        function filterByCategory(c) {
            state.activeCategory = c;
            navigateTo('shop');
            const sel = document.getElementById('shop-category-select');
            if (sel) sel.value = c;
            applyShopFilters();
        }

        /* ==========================================
           PRODUCT CARD COMPONENT
           ========================================== */
        function renderCardHtml(p) {
            const isWish = state.wishlist.includes(p.id);
            return `
                <div class="product-card">
                    <div class="product-img-wrapper" onclick="openProductDetails('${p.id}')">
                        <img src="${p.image}" alt="${p.name}">
                        <div class="product-badges">
                            ${p.badge ? `<span class="badge badge-primary">${p.badge}</span>` : ''}
                            ${p.discount ? `<span class="badge badge-danger">-${p.discount}% OFF</span>` : ''}
                        </div>
                        <div class="card-overlay-actions" onclick="event.stopPropagation()">
                            <button class="btn-icon" onclick="toggleWishlist('${p.id}')" title="Wishlist">
                                <i class="fa-${isWish?'solid':'regular'} fa-heart" style="${isWish?'color:var(--danger)':''}"></i>
                            </button>
                            <button class="btn-icon" onclick="openProductDetails('${p.id}')" title="Quick View">
                                <i class="fa-solid fa-eye"></i>
                            </button>
                        </div>
                    </div>
                    <div class="product-info">
                        <span class="product-brand">${p.category} • ${p.brand}</span>
                        <h4 class="product-title" onclick="openProductDetails('${p.id}')">${p.name}</h4>
                        <div class="product-rating">
                            <i class="fa-solid fa-star"></i> <strong>${p.rating}</strong>
                            <span style="color:var(--text-muted); font-size:0.75rem;">(${p.reviewsCount})</span>
                            <span style="margin-left:auto; color:var(--success); font-size:0.75rem; font-weight:700;">In Stock (${p.stock})</span>
                        </div>
                        <div class="product-price-row">
                            <span class="current-price">$${p.price.toFixed(2)}</span>
                            ${p.originalPrice ? `<span class="original-price">$${p.originalPrice.toFixed(2)}</span>` : ''}
                        </div>
                        <div class="card-btn-group">
                            <button class="btn btn-secondary btn-sm" onclick="addToCart('${p.id}')">
                                <i class="fa-solid fa-bag-shopping"></i> Add to Cart
                            </button>
                            <button class="btn btn-primary btn-sm" onclick="buyNowItem('${p.id}')">
                                <i class="fa-solid fa-bolt"></i> Buy Now
                            </button>
                        </div>
                    </div>
                </div>
            `;
        }

        /* ==========================================
           PRODUCT QUICK VIEW MODAL
           ========================================== */
        function openProductDetails(id) {
            const p = state.products.find(x => x.id === id);
            if (!p) return;

            const isWish = state.wishlist.includes(p.id);
            const container = document.getElementById('modal-product-detail-body');
            container.innerHTML = `
                <div>
                    <img src="${p.image}" alt="${p.name}" style="width:100%; border-radius:var(--radius-lg); object-fit:cover; max-height:360px;">
                </div>
                <div>
                    <span class="badge badge-primary" style="margin-bottom:0.5rem;">${p.category} • ${p.brand}</span>
                    <h2 style="font-size:1.4rem; font-weight:800; margin-bottom:0.5rem;">${p.name}</h2>
                    <div style="display:flex; align-items:center; gap:0.5rem; color:var(--accent); margin-bottom:1rem; font-size:0.9rem;">
                        <i class="fa-solid fa-star"></i> <strong>${p.rating}</strong> (${p.reviewsCount} customer reviews)
                    </div>
                    <div style="display:flex; align-items:baseline; gap:0.75rem; margin-bottom:1rem;">
                        <span style="font-size:1.75rem; font-weight:800; color:var(--primary);">$${p.price.toFixed(2)}</span>
                        ${p.originalPrice ? `<span style="font-size:1rem; color:var(--text-muted); text-decoration:line-through;">$${p.originalPrice.toFixed(2)}</span>` : ''}
                        <span class="badge badge-success">In Stock (${p.stock} units)</span>
                    </div>
                    <p style="font-size:0.9rem; color:var(--text-muted); margin-bottom:1.5rem; line-height:1.6;">
                        ${p.description || "High quality product with official warranty and free express shipping."}
                    </p>
                    <div style="display:flex; gap:0.75rem; align-items:center; margin-bottom:1rem;">
                        <button class="btn btn-primary btn-lg" style="flex:1;" onclick="addToCart('${p.id}'); closeModal('modal-product-details');">
                            <i class="fa-solid fa-bag-shopping"></i> Add to Cart
                        </button>
                        <button class="btn btn-secondary btn-lg" onclick="buyNowItem('${p.id}'); closeModal('modal-product-details');">
                            Buy Now
                        </button>
                    </div>
                </div>
            `;
            document.getElementById('modal-product-details').classList.add('active');
        }

        /* ==========================================
           ADD NEW ITEM / PRODUCT LOGIC
           ========================================== */
        function openAddItemModal() {
            document.getElementById('modal-add-item').classList.add('active');
        }

        function handleAddNewItem(e) {
            e.preventDefault();
            const name = document.getElementById('add-item-name').value.trim();
            const category = document.getElementById('add-item-category').value;
            const brand = document.getElementById('add-item-brand').value.trim();
            const price = parseFloat(document.getElementById('add-item-price').value);
            const origPrice = parseFloat(document.getElementById('add-item-orig-price').value) || (price * 1.15);
            const stock = parseInt(document.getElementById('add-item-stock').value) || 20;
            const image = document.getElementById('add-item-image').value.trim();
            const desc = document.getElementById('add-item-desc').value.trim();

            const newItem = {
                id: 'P' + Math.floor(100 + Math.random() * 900),
                name,
                category,
                brand,
                price,
                originalPrice: origPrice,
                discount: Math.round(((origPrice - price) / origPrice) * 100),
                rating: 5.0,
                reviewsCount: 1,
                stock,
                badge: 'NEW',
                image,
                description: desc
            };

            // Prepend new item so it appears first!
            state.products.unshift(newItem);
            saveProducts();

            closeModal('modal-add-item');
            showToast(`Item "${name}" added to store successfully! 🎉`, 'success');

            // Refresh UI views
            renderHome();
            if (state.activeView === 'shop') applyShopFilters();
            if (state.activeView === 'admin-dashboard') renderAdminDashboard();
        }

        /* ==========================================
           SHOP / CATALOG FILTERS
           ========================================== */
        function renderShop() {
            applyShopFilters();
        }

        function applyShopFilters() {
            let list = [...state.products];

            if (state.activeCategory && state.activeCategory !== 'All') {
                list = list.filter(p => p.category === state.activeCategory);
            }

            if (state.searchQuery) {
                const q = state.searchQuery.toLowerCase();
                list = list.filter(p => p.name.toLowerCase().includes(q) || p.category.toLowerCase().includes(q) || p.brand.toLowerCase().includes(q));
            }

            list = list.filter(p => p.price <= state.priceMax);

            const sortVal = document.getElementById('shop-sort-select')?.value || 'featured';
            if (sortVal === 'price-low') list.sort((a,b) => a.price - b.price);
            else if (sortVal === 'price-high') list.sort((a,b) => b.price - a.price);
            else if (sortVal === 'rating') list.sort((a,b) => b.rating - a.rating);

            document.getElementById('shop-results-count').innerText = `Showing ${list.length} products`;
            document.getElementById('shop-products-grid').innerHTML = list.length > 0
                ? list.map(renderCardHtml).join('')
                : `<p style="grid-column:1/-1; text-align:center; padding:3rem; color:var(--text-muted);">No items match criteria.</p>`;
        }

        function updatePriceFilter(val) {
            state.priceMax = parseFloat(val);
            document.getElementById('price-val-label').innerText = `$0 - $${val}`;
            applyShopFilters();
        }

        function resetShopFilters() {
            state.activeCategory = 'All';
            state.priceMax = 2500;
            state.searchQuery = '';
            document.getElementById('price-slider').value = 2500;
            document.getElementById('price-val-label').innerText = '$0 - $2500';
            document.getElementById('shop-category-select').value = 'All';
            applyShopFilters();
        }

        /* ==========================================
           CART DRAWER ENGINE
           ========================================== */
        function toggleCartDrawer() {
            document.getElementById('cart-drawer-overlay').classList.toggle('active');
            renderCartDrawer();
        }

        function addToCart(id, qty = 1) {
            const product = state.products.find(p => p.id === id);
            if (!product) return;

            const existing = state.cart.find(i => i.id === id);
            if (existing) existing.qty += qty;
            else state.cart.push({ id, qty });
            saveCart();
            showToast(`Added "${product.name}" to cart! 🛒`, 'success');
        }

        function buyNowItem(id) {
            addToCart(id);
            navigateTo('checkout');
        }

        function updateCartQty(id, delta) {
            const item = state.cart.find(i => i.id === id);
            if (!item) return;
            item.qty += delta;
            if (item.qty <= 0) {
                state.cart = state.cart.filter(i => i.id !== id);
            }
            saveCart();
            renderCartDrawer();
        }

        function removeFromCart(id) {
            state.cart = state.cart.filter(i => i.id !== id);
            saveCart();
            renderCartDrawer();
            showToast('Item removed from cart', 'info');
        }

        function renderCartDrawer() {
            const body = document.getElementById('cart-drawer-body');
            if (state.cart.length === 0) {
                body.innerHTML = `
                    <div style="text-align:center; padding:3rem 1rem; color:var(--text-muted);">
                        <i class="fa-solid fa-cart-shopping" style="font-size:3rem; opacity:0.3; margin-bottom:1rem;"></i>
                        <p style="font-weight:700;">Your cart is empty.</p>
                        <p style="font-size:0.85rem; margin-top:0.25rem;">Browse our 40+ products and add your favorites!</p>
                    </div>
                `;
                document.getElementById('cart-drawer-subtotal').innerText = '$0.00';
                return;
            }

            let subtotal = 0;
            body.innerHTML = state.cart.map(item => {
                const p = state.products.find(x => x.id === item.id);
                if (!p) return '';
                const itemTotal = p.price * item.qty;
                subtotal += itemTotal;
                return `
                    <div class="cart-drawer-item">
                        <img src="${p.image}">
                        <div style="flex:1;">
                            <h4 style="font-size:0.875rem; font-weight:700; line-clamp:1; display:-webkit-box; -webkit-line-clamp:1; -webkit-box-orient:vertical; overflow:hidden;">${p.name}</h4>
                            <div style="font-size:0.825rem; color:var(--primary); font-weight:800; margin:0.2rem 0;">$${p.price.toFixed(2)}</div>
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <div class="qty-picker">
                                    <button onclick="updateCartQty('${p.id}', -1)">-</button>
                                    <input type="text" value="${item.qty}" readonly>
                                    <button onclick="updateCartQty('${p.id}', 1)">+</button>
                                </div>
                                <button style="color:var(--danger); font-size:0.9rem;" onclick="removeFromCart('${p.id}')">
                                    <i class="fa-solid fa-trash-can"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                `;
            }).join('');

            document.getElementById('cart-drawer-subtotal').innerText = `$${subtotal.toFixed(2)}`;
        }

        /* ==========================================
           CHECKOUT ENGINE & ORDER CONFIRMATION
           ========================================== */
        function goToCheckoutStep(step) {
            document.getElementById('chk-step-form-1').style.display = step === 1 ? 'block' : 'none';
            document.getElementById('chk-step-form-2').style.display = step === 2 ? 'block' : 'none';
            document.getElementById('chk-step-form-3').style.display = step === 3 ? 'block' : 'none';

            document.getElementById('chk-step-1').className = step >= 1 ? 'step-item active' : 'step-item';
            document.getElementById('chk-step-2').className = step >= 2 ? 'step-item active' : 'step-item';
            document.getElementById('chk-step-3').className = step >= 3 ? 'step-item active' : 'step-item';
        }

        function placeOrderFinal(mode) {
            if (state.cart.length === 0) {
                showToast('Please add items to cart first!', 'error');
                return;
            }

            const orderId = 'ORD-' + Math.floor(100000 + Math.random() * 900000);
            const total = state.cart.reduce((sum, item) => {
                const p = state.products.find(x => x.id === item.id);
                return sum + (p ? p.price * item.qty : 0);
            }, 0);

            const newOrder = {
                orderId,
                date: new Date().toLocaleDateString(),
                status: 'Placed',
                total,
                paymentMode: mode,
                items: [...state.cart]
            };

            state.orders.unshift(newOrder);
            localStorage.setItem('orders', JSON.stringify(state.orders));

            state.cart = [];
            saveCart();

            document.getElementById('success-order-id-label').innerText = `Order #${orderId} • Total: $${total.toFixed(2)} (${mode})`;
            goToCheckoutStep(3);
            triggerConfetti();
            showToast('Order confirmed! 🎉', 'success');
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
           SEARCH & LIVE SUGGESTIONS
           ========================================== */
        function handleSearchInput(val) {
            state.searchQuery = val.trim();
            const sugBox = document.getElementById('search-suggestions');

            if (!state.searchQuery) {
                sugBox.classList.remove('active');
                if (state.activeView === 'shop') applyShopFilters();
                return;
            }

            const matches = state.products.filter(p => 
                p.name.toLowerCase().includes(state.searchQuery.toLowerCase()) ||
                p.category.toLowerCase().includes(state.searchQuery.toLowerCase()) ||
                p.brand.toLowerCase().includes(state.searchQuery.toLowerCase())
            ).slice(0, 5);

            if (matches.length > 0) {
                sugBox.innerHTML = matches.map(p => `
                    <div class="suggestion-item" onclick="openProductDetails('${p.id}'); document.getElementById('search-suggestions').classList.remove('active');">
                        <img src="${p.image}">
                        <div>
                            <div style="font-weight:700; font-size:0.85rem;">${p.name}</div>
                            <div style="font-size:0.75rem; color:var(--primary); font-weight:800;">$${p.price.toFixed(2)} • ${p.category}</div>
                        </div>
                    </div>
                `).join('');
                sugBox.classList.add('active');
            } else {
                sugBox.classList.remove('active');
            }

            if (state.activeView === 'shop') applyShopFilters();
        }

        /* ==========================================
           ADMIN PANEL INVENTORY & CRUD
           ========================================== */
        function renderAdminDashboard() {
            document.getElementById('admin-inventory-count').innerText = state.products.length;
            const tbody = document.getElementById('admin-inventory-body');
            tbody.innerHTML = state.products.map(p => `
                <tr style="border-bottom:1px solid var(--border-color);">
                    <td style="padding:0.75rem 1rem;">#${p.id}</td>
                    <td style="padding:0.75rem 1rem;"><strong>${p.name}</strong></td>
                    <td style="padding:0.75rem 1rem;">${p.category}</td>
                    <td style="padding:0.75rem 1rem; color:var(--primary); font-weight:700;">$${p.price.toFixed(2)}</td>
                    <td style="padding:0.75rem 1rem;"><span class="badge ${p.stock < 15 ? 'badge-danger':'badge-success'}">${p.stock}</span></td>
                    <td style="padding:0.75rem 1rem;">
                        <button class="btn btn-sm btn-secondary" onclick="deleteItemAdmin('${p.id}')" style="color:var(--danger);">
                            <i class="fa-solid fa-trash"></i> Delete
                        </button>
                    </td>
                </tr>
            `).join('');

            // Chart
            if (window.Chart) {
                const ctx = document.getElementById('adminSalesChart')?.getContext('2d');
                if (ctx) {
                    if (window.adminSalesChartInstance) window.adminSalesChartInstance.destroy();
                    window.adminSalesChartInstance = new Chart(ctx, {
                        type: 'line',
                        data: {
                            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
                            datasets: [{
                                label: 'Revenue ($)',
                                data: [12000, 18500, 16000, 24000, 29000, 34000, 31000, 42000],
                                borderColor: '#4f46e5',
                                backgroundColor: 'rgba(79, 70, 229, 0.1)',
                                fill: true,
                                tension: 0.4
                            }]
                        },
                        options: { responsive: true, maintainAspectRatio: false }
                    });
                }
            }
        }

        function deleteItemAdmin(id) {
            if (confirm('Delete this item from store?')) {
                state.products = state.products.filter(p => p.id !== id);
                saveProducts();
                renderAdminDashboard();
                renderHome();
                showToast('Item deleted successfully', 'info');
            }
        }

        /* ==========================================
           USER DASHBOARD & WISHLIST
           ========================================== */
        function renderUserDashboard(params = {}) {
            // Orders
            const list = document.getElementById('user-orders-list');
            list.innerHTML = state.orders.length > 0 ? state.orders.map(o => `
                <div style="background:var(--bg-card); border:1px solid var(--border-color); padding:1rem; border-radius:var(--radius-md); margin-bottom:1rem;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:0.4rem;">
                        <strong>Order #${o.orderId}</strong>
                        <span class="badge badge-success">${o.status}</span>
                    </div>
                    <div style="font-size:0.85rem; color:var(--text-muted);">Placed on ${o.date} • Total: $${o.total.toFixed(2)}</div>
                </div>
            `).join('') : `<p style="color:var(--text-muted);">No orders found.</p>`;

            // Wishlist
            const wishProds = state.products.filter(p => state.wishlist.includes(p.id));
            document.getElementById('user-wishlist-grid').innerHTML = wishProds.length > 0
                ? wishProds.map(renderCardHtml).join('')
                : `<p style="color:var(--text-muted); grid-column:1/-1;">Wishlist is empty.</p>`;

            if (params.tab === 'wishlist') switchDashTab('wishlist');
        }

        function switchDashTab(tab, el) {
            document.getElementById('dashtab-orders').style.display = tab === 'orders' ? 'block' : 'none';
            document.getElementById('dashtab-wishlist').style.display = tab === 'wishlist' ? 'block' : 'none';
            document.querySelectorAll('.dashboard-menu-item').forEach(m => m.classList.remove('active'));
            if (el) el.classList.add('active');
        }

        function toggleWishlist(id) {
            if (state.wishlist.includes(id)) {
                state.wishlist = state.wishlist.filter(x => x !== id);
                showToast('Removed from Wishlist', 'info');
            } else {
                state.wishlist.push(id);
                showToast('Saved to Wishlist! ❤️', 'success');
            }
            saveWishlist();
            renderHome();
            if (state.activeView === 'shop') applyShopFilters();
        }

        /* ==========================================
           UTILITIES & HELPERS
           ========================================== */
        function updateBadges() {
            document.getElementById('cart-badge').innerText = state.cart.reduce((a,b) => a + b.qty, 0);
            document.getElementById('wishlist-badge').innerText = state.wishlist.length;
        }

        function showToast(msg, type = 'info') {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            toast.className = 'toast';
            const icon = type === 'success' ? 'fa-circle-check' : 'fa-circle-info';
            const color = type === 'success' ? 'var(--success)' : 'var(--primary)';
            toast.style.borderLeftColor = color;
            toast.innerHTML = `<i class="fa-solid ${icon}" style="color:${color};"></i> <span>${msg}</span>`;
            container.appendChild(toast);
            setTimeout(() => toast.remove(), 3000);
        }

        function toggleTheme() {
            const cur = document.documentElement.getAttribute('data-theme');
            const next = cur === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('theme', next);
            updateThemeIcon();
        }

        function updateThemeIcon() {
            const cur = document.documentElement.getAttribute('data-theme');
            const icon = document.getElementById('theme-icon');
            if (icon) icon.className = cur === 'dark' ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
        }

        function openAuthModal() { document.getElementById('modal-auth').classList.add('active'); }
        function closeModal(id) { document.getElementById(id)?.classList.remove('active'); }

        function handleLoginSubmit(e) {
            e.preventDefault();
            const email = document.getElementById('login-email').value;
            const role = email.includes('admin') ? 'admin' : 'customer';
            state.currentUser = { name: email.split('@')[0], email, role };
            closeModal('modal-auth');
            showToast(`Signed in as ${state.currentUser.name}!`, 'success');
            if (role === 'admin') navigateTo('admin-dashboard');
        }

        function logoutUser() {
            state.currentUser = null;
            showToast('Logged out', 'info');
            navigateTo('home');
        }

        // Countdown Ticker
        setInterval(() => {
            const sBox = document.getElementById('timer-seconds');
            if (!sBox) return;
            let sec = parseInt(sBox.innerText) - 1;
            if (sec < 0) sec = 59;
            sBox.innerText = String(sec).padStart(2, '0');
        }, 1000);

        // Initialization
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
    f.write(full_html)

print("Updated index.html with 40+ products and Add Item system successfully!")
