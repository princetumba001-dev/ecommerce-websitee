import os

file_path = r"C:\Users\Prince kumar\.gemini\antigravity\scratch\ecommerce-app\index.html"

html_content = """<!-- SINGLE FILE E-COMMERCE APPLICATION -->
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ShopNexus | Premium Modern E-Commerce</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- FontAwesome 6 CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        /* ==========================================
           1. CSS VARIABLES & THEME CONFIGURATION
           ========================================== */
        :root {
            --primary: #4f46e5;
            --primary-hover: #4338ca;
            --primary-light: #eef2ff;
            --secondary: #06b6d4;
            --accent: #f59e0b;
            --danger: #ef4444;
            --success: #10b981;
            --warning: #f59e0b;
            --info: #3b82f6;

            --bg-main: #f8fafc;
            --bg-card: #ffffff;
            --bg-header: rgba(255, 255, 255, 0.95);
            --bg-input: #f1f5f9;
            --bg-subtle: #f1f5f9;

            --text-main: #0f172a;
            --text-muted: #64748b;
            --text-light: #94a3b8;
            --border-color: #e2e8f0;
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            
            --radius-sm: 6px;
            --radius-md: 10px;
            --radius-lg: 16px;
            --radius-full: 9999px;
            
            --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
            --container-max: 1320px;
        }

        [data-theme="dark"] {
            --primary: #6366f1;
            --primary-hover: #4f46e5;
            --primary-light: #1e1b4b;
            --bg-main: #0f172a;
            --bg-card: #1e293b;
            --bg-header: rgba(30, 41, 59, 0.95);
            --bg-input: #334155;
            --bg-subtle: #1e293b;

            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --text-light: #64748b;
            --border-color: #334155;
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.4);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.4);
            --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
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
            padding: 0.6rem 1rem;
            transition: var(--transition);
        }

        input:focus, select:focus, textarea:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15);
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
           3. UI COMPONENTS & UTILITIES
           ========================================== */
        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            font-weight: 600;
            font-size: 0.9rem;
            padding: 0.65rem 1.3rem;
            border-radius: var(--radius-md);
            transition: var(--transition);
            white-space: nowrap;
        }

        .btn-primary {
            background: var(--primary);
            color: #ffffff;
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25);
        }

        .btn-primary:hover {
            background: var(--primary-hover);
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(79, 70, 229, 0.35);
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

        .btn-danger:hover {
            opacity: 0.9;
        }

        .btn-sm {
            padding: 0.4rem 0.8rem;
            font-size: 0.8rem;
            border-radius: var(--radius-sm);
        }

        .btn-lg {
            padding: 0.85rem 1.8rem;
            font-size: 1rem;
            border-radius: var(--radius-lg);
        }

        .btn-icon {
            width: 40px;
            height: 40px;
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
        }

        .badge {
            display: inline-flex;
            align-items: center;
            padding: 0.2rem 0.6rem;
            font-size: 0.75rem;
            font-weight: 700;
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
            width: 18px;
            height: 18px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Top Announcement Bar */
        .announcement-bar {
            background: linear-gradient(90deg, #4f46e5, #06b6d4);
            color: #ffffff;
            font-size: 0.825rem;
            font-weight: 600;
            padding: 0.4rem 0;
            text-align: center;
        }

        .announcement-content {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1.5rem;
        }

        /* Header Navigation */
        header {
            position: sticky;
            top: 0;
            z-index: 100;
            background: var(--bg-header);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-color);
            transition: var(--transition);
        }

        .nav-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 72px;
            gap: 1.5rem;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--text-main);
            letter-spacing: -0.5px;
        }

        .logo i {
            color: var(--primary);
            font-size: 1.75rem;
        }

        .search-box {
            flex: 1;
            max-width: 550px;
            position: relative;
        }

        .search-input-wrapper {
            position: relative;
            display: flex;
            align-items: center;
        }

        .search-input-wrapper input {
            width: 100%;
            padding-left: 2.75rem;
            padding-right: 3rem;
            height: 44px;
            border-radius: var(--radius-full);
            background: var(--bg-input);
            border: 1px solid transparent;
        }

        .search-input-wrapper input:focus {
            background: var(--bg-card);
            border-color: var(--primary);
        }

        .search-icon {
            position: absolute;
            left: 1rem;
            color: var(--text-muted);
        }

        .search-suggestions {
            position: absolute;
            top: 110%;
            left: 0;
            right: 0;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-xl);
            z-index: 200;
            max-height: 350px;
            overflow-y: auto;
            display: none;
        }

        .search-suggestions.active {
            display: block;
        }

        .suggestion-item {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.75rem 1rem;
            cursor: pointer;
            border-bottom: 1px solid var(--border-color);
            transition: var(--transition);
        }

        .suggestion-item:hover {
            background: var(--bg-subtle);
        }

        .suggestion-item img {
            width: 40px;
            height: 40px;
            object-fit: cover;
            border-radius: var(--radius-sm);
        }

        .nav-actions {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        /* Category Sub-Bar */
        .category-bar {
            background: var(--bg-card);
            border-bottom: 1px solid var(--border-color);
            overflow-x: auto;
            white-space: nowrap;
            scrollbar-width: none;
        }

        .category-bar::-webkit-scrollbar {
            display: none;
        }

        .category-nav-list {
            display: flex;
            align-items: center;
            gap: 1.5rem;
            padding: 0.6rem 0;
            list-style: none;
        }

        .category-nav-item {
            font-size: 0.875rem;
            font-weight: 600;
            color: var(--text-muted);
            cursor: pointer;
            padding: 0.25rem 0.75rem;
            border-radius: var(--radius-full);
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }

        .category-nav-item:hover, .category-nav-item.active {
            color: var(--primary);
            background: var(--primary-light);
        }

        /* Hero Banner */
        .hero-section {
            padding: 2rem 0;
        }

        .hero-banner {
            background: linear-gradient(135deg, #312e81 0%, #4f46e5 50%, #06b6d4 100%);
            border-radius: var(--radius-lg);
            padding: 3.5rem 3rem;
            color: #ffffff;
            position: relative;
            overflow: hidden;
            box-shadow: var(--shadow-xl);
            display: grid;
            grid-template-columns: 1fr 1fr;
            align-items: center;
            gap: 2rem;
        }

        .hero-text h1 {
            font-size: 2.75rem;
            font-weight: 800;
            line-height: 1.15;
            margin-bottom: 1rem;
        }

        .hero-text p {
            font-size: 1.1rem;
            opacity: 0.9;
            margin-bottom: 1.75rem;
            max-width: 500px;
        }

        .hero-image img {
            width: 100%;
            max-height: 320px;
            object-fit: contain;
            filter: drop-shadow(0 20px 30px rgba(0,0,0,0.3));
            animation: float 4s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        /* Section Styling */
        .section {
            padding: 2.5rem 0;
        }

        .section-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.5rem;
        }

        .section-title {
            font-size: 1.5rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .section-title i {
            color: var(--primary);
        }

        /* Product Grid */
        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
            gap: 1.5rem;
        }

        /* Product Card */
        .product-card {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            overflow: hidden;
            transition: var(--transition);
            position: relative;
            display: flex;
            flex-direction: column;
        }

        .product-card:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-lg);
            border-color: rgba(79, 70, 229, 0.3);
        }

        .product-img-wrapper {
            position: relative;
            padding-top: 80%;
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
            transition: transform 0.5s ease;
        }

        .product-card:hover .product-img-wrapper img {
            transform: scale(1.06);
        }

        .discount-badge {
            position: absolute;
            top: 10px;
            left: 10px;
            background: var(--danger);
            color: #ffffff;
            font-size: 0.7rem;
            font-weight: 800;
            padding: 0.25rem 0.5rem;
            border-radius: var(--radius-sm);
            z-index: 2;
        }

        .card-actions-overlay {
            position: absolute;
            top: 10px;
            right: 10px;
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
            opacity: 0;
            transform: translateX(10px);
            transition: var(--transition);
            z-index: 2;
        }

        .product-card:hover .card-actions-overlay {
            opacity: 1;
            transform: translateX(0);
        }

        .product-info {
            padding: 1rem;
            display: flex;
            flex-direction: column;
            flex: 1;
        }

        .product-category {
            font-size: 0.75rem;
            color: var(--text-muted);
            text-transform: uppercase;
            font-weight: 600;
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
        }

        .product-rating {
            display: flex;
            align-items: center;
            gap: 0.3rem;
            font-size: 0.8rem;
            color: var(--accent);
            margin-bottom: 0.6rem;
        }

        .review-count {
            color: var(--text-muted);
            font-size: 0.75rem;
        }

        .product-price-row {
            display: flex;
            align-items: baseline;
            gap: 0.5rem;
            margin-top: auto;
            margin-bottom: 0.75rem;
        }

        .current-price {
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--text-main);
        }

        .original-price {
            font-size: 0.85rem;
            color: var(--text-muted);
            text-decoration: line-through;
        }

        .card-add-btn {
            width: 100%;
        }

        /* Flash Sale Countdown Timer */
        .flash-sale-bar {
            background: linear-gradient(90deg, #ef4444, #f59e0b);
            border-radius: var(--radius-md);
            padding: 1.25rem 1.75rem;
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.5rem;
        }

        .countdown-timer {
            display: flex;
            gap: 0.5rem;
            align-items: center;
            font-weight: 700;
        }

        .timer-box {
            background: rgba(0,0,0,0.25);
            padding: 0.4rem 0.6rem;
            border-radius: var(--radius-sm);
            font-size: 1.1rem;
            min-width: 36px;
            text-align: center;
        }

        /* Shop Layout (Filters Sidebar + Main Grid) */
        .shop-container {
            display: grid;
            grid-template-columns: 260px 1fr;
            gap: 1.75rem;
            padding: 2rem 0;
        }

        .filter-sidebar {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.25rem;
            height: fit-content;
            position: sticky;
            top: 90px;
        }

        .filter-group {
            margin-bottom: 1.25rem;
            padding-bottom: 1.25rem;
            border-bottom: 1px solid var(--border-color);
        }

        .filter-group:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }

        .filter-title {
            font-size: 0.95rem;
            font-weight: 700;
            margin-bottom: 0.75rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .filter-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            max-height: 180px;
            overflow-y: auto;
        }

        .filter-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.85rem;
            cursor: pointer;
            color: var(--text-muted);
        }

        .filter-item:hover {
            color: var(--primary);
        }

        .filter-item input[type="checkbox"], .filter-item input[type="radio"] {
            cursor: pointer;
            accent-color: var(--primary);
        }

        .range-slider {
            width: 100%;
            accent-color: var(--primary);
        }

        .shop-toolbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 0.75rem 1.25rem;
            margin-bottom: 1.5rem;
        }

        /* Product Detail View Modal */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(4px);
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            visibility: hidden;
            transition: var(--transition);
            padding: 1rem;
        }

        .modal-overlay.active {
            opacity: 1;
            visibility: visible;
        }

        .modal-content {
            background: var(--bg-card);
            border-radius: var(--radius-lg);
            width: 100%;
            max-width: 900px;
            max-height: 90vh;
            overflow-y: auto;
            position: relative;
            box-shadow: var(--shadow-xl);
            padding: 2rem;
            transform: scale(0.95);
            transition: var(--transition);
        }

        .modal-overlay.active .modal-content {
            transform: scale(1);
        }

        .modal-close {
            position: absolute;
            top: 1.25rem;
            right: 1.25rem;
            font-size: 1.25rem;
            color: var(--text-muted);
            cursor: pointer;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--bg-subtle);
        }

        .modal-close:hover {
            color: var(--danger);
        }

        .product-detail-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
        }

        .detail-gallery img {
            width: 100%;
            border-radius: var(--radius-md);
            background: var(--bg-subtle);
            object-fit: cover;
            max-height: 400px;
        }

        .specs-table {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
            font-size: 0.85rem;
        }

        .specs-table td {
            padding: 0.5rem 0.75rem;
            border-bottom: 1px solid var(--border-color);
        }

        .specs-table td:first-child {
            font-weight: 700;
            color: var(--text-muted);
            width: 35%;
        }

        /* Cart View & Drawer */
        .cart-table {
            width: 100%;
            border-collapse: collapse;
        }

        .cart-table th {
            text-align: left;
            padding: 1rem;
            background: var(--bg-subtle);
            font-size: 0.85rem;
            color: var(--text-muted);
        }

        .cart-table td {
            padding: 1rem;
            border-bottom: 1px solid var(--border-color);
        }

        .cart-item-info {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .cart-item-info img {
            width: 60px;
            height: 60px;
            object-fit: cover;
            border-radius: var(--radius-sm);
        }

        .qty-picker {
            display: inline-flex;
            align-items: center;
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            overflow: hidden;
        }

        .qty-picker button {
            width: 30px;
            height: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--bg-subtle);
        }

        .qty-picker input {
            width: 40px;
            height: 30px;
            text-align: center;
            border: none;
            border-radius: 0;
            padding: 0;
            font-weight: 700;
        }

        .order-summary-card {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.5rem;
        }

        .summary-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.75rem;
            font-size: 0.9rem;
            color: var(--text-muted);
        }

        .summary-row.total {
            font-size: 1.2rem;
            font-weight: 800;
            color: var(--text-main);
            border-top: 1px dashed var(--border-color);
            padding-top: 1rem;
            margin-top: 1rem;
        }

        /* Checkout Form */
        .checkout-grid {
            display: grid;
            grid-template-columns: 1fr 380px;
            gap: 2rem;
            padding: 2rem 0;
        }

        .checkout-form-section {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }

        .form-grid-2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }

        .form-group {
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
            margin-bottom: 1rem;
        }

        .form-group label {
            font-size: 0.85rem;
            font-weight: 700;
        }

        .payment-tabs {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 0.5rem;
            margin-bottom: 1rem;
        }

        .payment-tab-btn {
            padding: 0.75rem;
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            font-size: 0.85rem;
            font-weight: 600;
            text-align: center;
            cursor: pointer;
        }

        .payment-tab-btn.active {
            border-color: var(--primary);
            background: var(--primary-light);
            color: var(--primary);
        }

        /* Dashboards & Admin */
        .dashboard-grid {
            display: grid;
            grid-template-columns: 240px 1fr;
            gap: 1.75rem;
            padding: 2rem 0;
        }

        .dashboard-menu {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 0.75rem;
            list-style: none;
            height: fit-content;
        }

        .dashboard-menu-item {
            padding: 0.75rem 1rem;
            border-radius: var(--radius-md);
            font-weight: 600;
            font-size: 0.9rem;
            color: var(--text-muted);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 0.25rem;
        }

        .dashboard-menu-item:hover, .dashboard-menu-item.active {
            background: var(--primary-light);
            color: var(--primary);
        }

        .admin-stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.25rem;
            margin-bottom: 1.5rem;
        }

        .stat-card {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.25rem;
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .stat-icon {
            width: 48px;
            height: 48px;
            border-radius: var(--radius-md);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.4rem;
        }

        .data-table-wrapper {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            overflow-x: auto;
        }

        .data-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.875rem;
        }

        .data-table th {
            background: var(--bg-subtle);
            padding: 0.85rem 1rem;
            text-align: left;
            font-weight: 700;
            color: var(--text-muted);
        }

        .data-table td {
            padding: 0.85rem 1rem;
            border-bottom: 1px solid var(--border-color);
            vertical-align: middle;
        }

        /* Order Tracking Timeline */
        .timeline {
            display: flex;
            justify-content: space-between;
            position: relative;
            margin: 2.5rem 0;
        }

        .timeline::before {
            content: '';
            position: absolute;
            top: 20px;
            left: 5%;
            right: 5%;
            height: 4px;
            background: var(--border-color);
            z-index: 1;
        }

        .timeline-step {
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.5rem;
        }

        .step-icon {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: var(--bg-card);
            border: 3px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            color: var(--text-muted);
        }

        .timeline-step.completed .step-icon {
            background: var(--success);
            border-color: var(--success);
            color: #fff;
        }

        .timeline-step.active .step-icon {
            background: var(--primary);
            border-color: var(--primary);
            color: #fff;
        }

        /* Floating Support Chat Widget */
        .chat-widget-btn {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: var(--primary);
            color: #fff;
            font-size: 1.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: var(--shadow-xl);
            z-index: 900;
        }

        .chat-drawer {
            position: fixed;
            bottom: 6rem;
            right: 2rem;
            width: 350px;
            height: 450px;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-xl);
            z-index: 900;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            display: none;
        }

        .chat-drawer.active {
            display: flex;
        }

        .chat-header {
            background: var(--primary);
            color: #fff;
            padding: 1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-weight: 700;
        }

        .chat-body {
            flex: 1;
            padding: 1rem;
            overflow-y: auto;
            display: flex;
            flex-direction: flex-start;
            flex-direction: column;
            gap: 0.75rem;
        }

        .chat-msg {
            max-width: 80%;
            padding: 0.6rem 0.9rem;
            border-radius: var(--radius-md);
            font-size: 0.85rem;
        }

        .chat-msg.bot {
            background: var(--bg-subtle);
            color: var(--text-main);
            align-self: flex-start;
        }

        .chat-msg.user {
            background: var(--primary);
            color: #fff;
            align-self: flex-end;
        }

        /* Toast Notifications */
        .toast-container {
            position: fixed;
            top: 85px;
            right: 20px;
            z-index: 9999;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }

        .toast {
            background: var(--bg-card);
            border-left: 4px solid var(--primary);
            padding: 0.9rem 1.25rem;
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

        /* Back to top button */
        .back-to-top {
            position: fixed;
            bottom: 2rem;
            left: 2rem;
            z-index: 900;
            display: none;
        }

        .back-to-top.active {
            display: flex;
        }

        /* Footer */
        footer {
            background: var(--bg-card);
            border-top: 1px solid var(--border-color);
            padding: 4rem 0 2rem 0;
            margin-top: auto;
        }

        .footer-grid {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1fr;
            gap: 3rem;
            margin-bottom: 3rem;
        }

        .footer-col h4 {
            font-size: 1rem;
            font-weight: 700;
            margin-bottom: 1.25rem;
        }

        .footer-links {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            font-size: 0.9rem;
            color: var(--text-muted);
        }

        .footer-links a:hover {
            color: var(--primary);
        }

        /* Responsive Breakpoints */
        @media (max-width: 1024px) {
            .hero-banner { grid-template-columns: 1fr; text-align: center; }
            .hero-image { display: none; }
            .shop-container { grid-template-columns: 1fr; }
            .filter-sidebar { display: none; }
            .filter-sidebar.active-mobile { display: block; position: fixed; top: 0; left: 0; right: 0; bottom: 0; z-index: 1000; overflow-y: auto; }
            .checkout-grid { grid-template-columns: 1fr; }
            .dashboard-grid { grid-template-columns: 1fr; }
            .admin-stats-grid { grid-template-columns: repeat(2, 1fr); }
            .footer-grid { grid-template-columns: 1fr 1fr; }
        }

        @media (max-width: 640px) {
            .product-detail-grid { grid-template-columns: 1fr; }
            .admin-stats-grid { grid-template-columns: 1fr; }
            .footer-grid { grid-template-columns: 1fr; }
            .payment-tabs { grid-template-columns: 1fr 1fr; }
        }
    </style>
</head>
<body>

    <!-- Announcement Top Bar -->
    <div class="announcement-bar">
        <div class="container announcement-content">
            <span>🎉 FLASH SALE: Get 20% OFF with coupon <strong>WELCOME</strong></span>
            <span>⚡ Free Express Delivery on orders over $50</span>
        </div>
    </div>

    <!-- Header Navbar -->
    <header>
        <div class="container nav-container">
            <a href="javascript:void(0)" onclick="navigateTo('home')" class="logo">
                <i class="fa-solid fa-cube"></i> ShopNexus
            </a>

            <!-- Search Bar -->
            <div class="search-box">
                <div class="search-input-wrapper">
                    <i class="fa-solid fa-magnifying-glass search-icon"></i>
                    <input type="text" id="global-search" placeholder="Search 30+ products, brands, categories..." oninput="handleSearchInput(this.value)">
                </div>
                <div id="search-suggestions" class="search-suggestions"></div>
            </div>

            <!-- Nav Action Buttons -->
            <div class="nav-actions">
                <button class="btn-icon" title="Toggle Light/Dark Theme" onclick="toggleTheme()">
                    <i id="theme-icon" class="fa-solid fa-moon"></i>
                </button>
                <button class="btn-icon" title="Compare Products" onclick="openCompareModal()">
                    <i class="fa-solid fa-sliders"></i>
                    <span id="compare-badge" class="counter-badge">0</span>
                </button>
                <button class="btn-icon" title="Wishlist" onclick="navigateTo('user-dashboard', {tab: 'wishlist'})">
                    <i class="fa-regular fa-heart"></i>
                    <span id="wishlist-badge" class="counter-badge">0</span>
                </button>
                <button class="btn-icon" title="Shopping Cart" onclick="navigateTo('cart')">
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

        <!-- Category Sub-Nav -->
        <div class="category-bar">
            <div class="container">
                <ul class="category-nav-list" id="category-nav-list">
                    <!-- Populated dynamically by JS -->
                </ul>
            </div>
        </div>
    </header>

    <!-- Toast Notification Container -->
    <div id="toast-container" class="toast-container"></div>

    <!-- MAIN APP CONTENT AREA -->
    <main id="app-content">

        <!-- ==========================================
           VIEW: HOME
           ========================================== -->
        <section id="view-home" class="page-view">
            <div class="container">
                <!-- Hero Banner -->
                <div class="hero-section">
                    <div class="hero-banner">
                        <div class="hero-text">
                            <span class="badge badge-warning" style="margin-bottom: 1rem;">NEXT-GEN SHOPPING</span>
                            <h1>Upgrade Your Lifestyle with Tech & Fashion</h1>
                            <p>Discover flagship smartphones, gaming laptops, premium watches, and trendy outfits at unbeatable prices.</p>
                            <div style="display: flex; gap: 1rem;">
                                <button class="btn btn-primary btn-lg" onclick="navigateTo('shop')">
                                    <i class="fa-solid fa-bag-shopping"></i> Shop Now
                                </button>
                                <button class="btn btn-secondary btn-lg" onclick="filterByCategory('Electronics')">
                                    Explore Electronics
                                </button>
                            </div>
                        </div>
                        <div class="hero-image">
                            <img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&auto=format&fit=crop&q=80" alt="Headphones Hero">
                        </div>
                    </div>
                </div>

                <!-- Flash Sale Ticker Section -->
                <div class="flash-sale-bar">
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <i class="fa-solid fa-bolt" style="font-size: 1.75rem;"></i>
                        <div>
                            <h3 style="font-size: 1.1rem; font-weight: 800;">Flash Sale Countdown</h3>
                            <p style="font-size: 0.85rem; opacity: 0.9;">Limited time deals on top brands ending soon!</p>
                        </div>
                    </div>
                    <div class="countdown-timer">
                        <div class="timer-box" id="timer-hours">05</div>:
                        <div class="timer-box" id="timer-minutes">42</div>:
                        <div class="timer-box" id="timer-seconds">19</div>
                    </div>
                </div>

                <!-- Featured Products -->
                <div class="section">
                    <div class="section-header">
                        <h2 class="section-title"><i class="fa-solid fa-fire"></i> Featured Deals</h2>
                        <button class="btn btn-secondary btn-sm" onclick="navigateTo('shop')">View All <i class="fa-solid fa-arrow-right"></i></button>
                    </div>
                    <div class="product-grid" id="featured-products-grid"></div>
                </div>

                <!-- Categories Grid -->
                <div class="section">
                    <div class="section-header">
                        <h2 class="section-title"><i class="fa-solid fa-layer-group"></i> Shop by Category</h2>
                    </div>
                    <div class="product-grid" id="categories-grid" style="grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));"></div>
                </div>

                <!-- Trending Products -->
                <div class="section">
                    <div class="section-header">
                        <h2 class="section-title"><i class="fa-solid fa-chart-line"></i> Trending This Week</h2>
                    </div>
                    <div class="product-grid" id="trending-products-grid"></div>
                </div>
            </div>
        </section>

        <!-- ==========================================
           VIEW: SHOP (Filterable Product Catalog)
           ========================================== -->
        <section id="view-shop" class="page-view" style="display: none;">
            <div class="container shop-container">
                <!-- Filter Sidebar -->
                <aside class="filter-sidebar" id="filter-sidebar">
                    <div class="filter-group">
                        <div class="filter-title">
                            <span>Categories</span>
                            <button class="btn-sm" style="color: var(--primary);" onclick="resetCategoryFilter()">Clear</button>
                        </div>
                        <ul class="filter-list" id="shop-filter-categories"></ul>
                    </div>

                    <div class="filter-group">
                        <div class="filter-title">
                            <span>Price Range</span>
                            <span id="price-range-val" style="color: var(--primary); font-size: 0.85rem;">$0 - $2500</span>
                        </div>
                        <input type="range" class="range-slider" id="price-slider" min="0" max="2500" step="50" value="2500" oninput="handlePriceFilter(this.value)">
                    </div>

                    <div class="filter-group">
                        <div class="filter-title"><span>Minimum Rating</span></div>
                        <div class="filter-list">
                            <label class="filter-item"><input type="radio" name="rating-filter" value="0" checked onchange="applyShopFilters()"> All Ratings</label>
                            <label class="filter-item"><input type="radio" name="rating-filter" value="4.5" onchange="applyShopFilters()"> 4.5★ & Above</label>
                            <label class="filter-item"><input type="radio" name="rating-filter" value="4.0" onchange="applyShopFilters()"> 4.0★ & Above</label>
                        </div>
                    </div>

                    <div class="filter-group">
                        <div class="filter-title"><span>Discount</span></div>
                        <div class="filter-list">
                            <label class="filter-item"><input type="checkbox" id="discount-only-cb" onchange="applyShopFilters()"> Discounted Items Only</label>
                        </div>
                    </div>

                    <button class="btn btn-secondary btn-sm" style="width: 100%;" onclick="resetAllFilters()">
                        <i class="fa-solid fa-rotate-left"></i> Reset All Filters
                    </button>
                </aside>

                <!-- Main Shop Product Gallery -->
                <div>
                    <div class="shop-toolbar">
                        <span id="shop-results-count" style="font-size: 0.9rem; font-weight: 600; color: var(--text-muted);">Showing 30 products</span>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <label style="font-size: 0.85rem; font-weight: 600;">Sort By:</label>
                            <select id="shop-sort-select" onchange="applyShopFilters()" style="padding: 0.4rem 0.8rem; font-size: 0.85rem;">
                                <option value="featured">Featured</option>
                                <option value="price-low">Price: Low to High</option>
                                <option value="price-high">Price: High to Low</option>
                                <option value="rating">Highest Rated</option>
                                <option value="newest">Newest Arrivals</option>
                            </select>
                        </div>
                    </div>
                    <div class="product-grid" id="shop-products-grid"></div>
                </div>
            </div>
        </section>

        <!-- ==========================================
           VIEW: CART
           ========================================== -->
        <section id="view-cart" class="page-view" style="display: none;">
            <div class="container" style="padding: 2.5rem 0;">
                <h1 style="font-size: 1.75rem; font-weight: 800; margin-bottom: 1.5rem;"><i class="fa-solid fa-cart-shopping"></i> Shopping Cart</h1>
                <div class="checkout-grid">
                    <div class="data-table-wrapper" style="height: fit-content;">
                        <table class="cart-table">
                            <thead>
                                <tr>
                                    <th>Product</th>
                                    <th>Price</th>
                                    <th>Quantity</th>
                                    <th>Subtotal</th>
                                    <th>Action</th>
                                </tr>
                            </thead>
                            <tbody id="cart-table-body"></tbody>
                        </table>
                    </div>

                    <!-- Cart Summary Sidebar -->
                    <div class="order-summary-card">
                        <h3 style="font-size: 1.1rem; font-weight: 800; margin-bottom: 1rem;">Order Summary</h3>
                        <div class="summary-row"><span>Subtotal</span><span id="summary-subtotal">$0.00</span></div>
                        <div class="summary-row"><span>Estimated Tax (18% GST)</span><span id="summary-tax">$0.00</span></div>
                        <div class="summary-row"><span>Shipping Fee</span><span id="summary-shipping">$0.00</span></div>
                        <div class="summary-row" style="color: var(--success);" id="coupon-discount-row"><span>Discount Coupon</span><span id="summary-discount">-$0.00</span></div>
                        
                        <!-- Coupon Form -->
                        <div style="display: flex; gap: 0.5rem; margin: 1.25rem 0;">
                            <input type="text" id="coupon-input" placeholder="Coupon (e.g. WELCOME)" style="text-transform: uppercase;">
                            <button class="btn btn-secondary btn-sm" onclick="applyCoupon()">Apply</button>
                        </div>

                        <div class="summary-row total"><span>Grand Total</span><span id="summary-grand-total">$0.00</span></div>

                        <button class="btn btn-primary btn-lg" style="width: 100%; margin-top: 1.5rem;" onclick="navigateTo('checkout')">
                            Proceed to Checkout <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==========================================
           VIEW: CHECKOUT
           ========================================== -->
        <section id="view-checkout" class="page-view" style="display: none;">
            <div class="container">
                <div class="checkout-grid">
                    <div>
                        <!-- Address Info Form -->
                        <div class="checkout-form-section">
                            <h3 style="font-size: 1.1rem; font-weight: 800; margin-bottom: 1rem;"><i class="fa-solid fa-truck-fast"></i> 1. Shipping Address</h3>
                            <div class="form-grid-2">
                                <div class="form-group"><label>Full Name *</label><input type="text" id="chk-name" placeholder="John Doe"></div>
                                <div class="form-group"><label>Mobile Number *</label><input type="tel" id="chk-phone" placeholder="+1 234 567 8900"></div>
                            </div>
                            <div class="form-group"><label>Street Address *</label><input type="text" id="chk-address" placeholder="123 Shopping Blvd, Suite 400"></div>
                            <div class="form-grid-2">
                                <div class="form-group"><label>City *</label><input type="text" id="chk-city" placeholder="New York"></div>
                                <div class="form-group"><label>State *</label><input type="text" id="chk-state" placeholder="NY"></div>
                                <div class="form-group"><label>PIN / ZIP Code *</label><input type="text" id="chk-zip" placeholder="10001"></div>
                            </div>
                        </div>

                        <!-- Payment Method Simulation -->
                        <div class="checkout-form-section">
                            <h3 style="font-size: 1.1rem; font-weight: 800; margin-bottom: 1rem;"><i class="fa-solid fa-credit-card"></i> 2. Payment Options (Demo Simulation)</h3>
                            <div class="payment-tabs">
                                <div class="payment-tab-btn active" onclick="selectPaymentMethod(this, 'cod')"><i class="fa-solid fa-hand-holding-dollar"></i> COD</div>
                                <div class="payment-tab-btn" onclick="selectPaymentMethod(this, 'upi')"><i class="fa-solid fa-qrcode"></i> UPI</div>
                                <div class="payment-tab-btn" onclick="selectPaymentMethod(this, 'card')"><i class="fa-solid fa-credit-card"></i> Card</div>
                                <div class="payment-tab-btn" onclick="selectPaymentMethod(this, 'net')"><i class="fa-solid fa-building-columns"></i> Net Banking</div>
                            </div>
                            
                            <div id="payment-details-container" style="background: var(--bg-subtle); padding: 1rem; border-radius: var(--radius-md);">
                                <p style="font-size: 0.85rem; color: var(--text-muted);"><i class="fa-solid fa-shield-halved"></i> Payment is simulated safely. No actual money or card data is transmitted.</p>
                            </div>
                        </div>
                    </div>

                    <!-- Checkout Side Order Summary -->
                    <div class="order-summary-card" style="height: fit-content;">
                        <h3 style="font-size: 1.1rem; font-weight: 800; margin-bottom: 1rem;">Order Review</h3>
                        <div id="checkout-items-list" style="max-height: 200px; overflow-y: auto; margin-bottom: 1rem;"></div>
                        <div class="summary-row"><span>Total Payable</span><strong id="chk-pay-total" style="font-size: 1.2rem; color: var(--primary);">$0.00</strong></div>
                        <button class="btn btn-primary btn-lg" style="width: 100%; margin-top: 1.5rem;" onclick="processOrderPlacement()">
                            <i class="fa-solid fa-lock"></i> Place Order Now
                        </button>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==========================================
           VIEW: USER DASHBOARD
           ========================================== -->
        <section id="view-user-dashboard" class="page-view" style="display: none;">
            <div class="container dashboard-grid">
                <!-- Dashboard Left Menu -->
                <ul class="dashboard-menu">
                    <li class="dashboard-menu-item active" onclick="switchDashboardTab('orders', this)"><i class="fa-solid fa-box"></i> My Orders</li>
                    <li class="dashboard-menu-item" onclick="switchDashboardTab('wishlist', this)"><i class="fa-solid fa-heart"></i> Wishlist</li>
                    <li class="dashboard-menu-item" onclick="switchDashboardTab('profile', this)"><i class="fa-solid fa-user-gear"></i> Profile & Address</li>
                    <li class="dashboard-menu-item" style="color: var(--danger);" onclick="logoutUser()"><i class="fa-solid fa-right-from-bracket"></i> Logout</li>
                </ul>

                <!-- Dashboard Right Content -->
                <div>
                    <!-- Tab: Orders -->
                    <div id="dash-tab-orders" class="dash-tab-content">
                        <h2 style="font-size: 1.3rem; font-weight: 800; margin-bottom: 1.25rem;">My Order History</h2>
                        <div id="user-orders-list"></div>
                    </div>

                    <!-- Tab: Wishlist -->
                    <div id="dash-tab-wishlist" class="dash-tab-content" style="display: none;">
                        <h2 style="font-size: 1.3rem; font-weight: 800; margin-bottom: 1.25rem;">My Wishlist</h2>
                        <div class="product-grid" id="user-wishlist-grid"></div>
                    </div>

                    <!-- Tab: Profile -->
                    <div id="dash-tab-profile" class="dash-tab-content" style="display: none;">
                        <h2 style="font-size: 1.3rem; font-weight: 800; margin-bottom: 1.25rem;">Account Profile</h2>
                        <div class="checkout-form-section">
                            <div class="form-group"><label>Email Address</label><input type="email" id="profile-email" readonly></div>
                            <div class="form-group"><label>Full Name</label><input type="text" id="profile-name" placeholder="User Name"></div>
                            <button class="btn btn-primary btn-sm" onclick="saveProfileChanges()">Save Profile</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==========================================
           VIEW: ADMIN DASHBOARD
           ========================================== -->
        <section id="view-admin-dashboard" class="page-view" style="display: none;">
            <div class="container" style="padding: 2rem 0;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                    <div>
                        <h1 style="font-size: 1.75rem; font-weight: 800;"><i class="fa-solid fa-chart-pie"></i> Admin Control Panel</h1>
                        <p style="font-size: 0.9rem; color: var(--text-muted);">Manage store inventory, orders, and view sales metrics.</p>
                    </div>
                    <button class="btn btn-primary" onclick="openAddProductModal()"><i class="fa-solid fa-plus"></i> Add New Product</button>
                </div>

                <!-- Admin Analytics Cards -->
                <div class="admin-stats-grid">
                    <div class="stat-card">
                        <div class="stat-icon" style="background: rgba(79, 70, 229, 0.15); color: var(--primary);"><i class="fa-solid fa-dollar-sign"></i></div>
                        <div>
                            <span style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600;">TOTAL SALES</span>
                            <h3 id="admin-stat-sales" style="font-size: 1.4rem; font-weight: 800;">$0.00</h3>
                        </div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-icon" style="background: rgba(6, 182, 212, 0.15); color: var(--secondary);"><i class="fa-solid fa-cart-shopping"></i></div>
                        <div>
                            <span style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600;">TOTAL ORDERS</span>
                            <h3 id="admin-stat-orders" style="font-size: 1.4rem; font-weight: 800;">0</h3>
                        </div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-icon" style="background: rgba(16, 185, 129, 0.15); color: var(--success);"><i class="fa-solid fa-boxes-stacked"></i></div>
                        <div>
                            <span style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600;">TOTAL PRODUCTS</span>
                            <h3 id="admin-stat-products" style="font-size: 1.4rem; font-weight: 800;">30</h3>
                        </div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-icon" style="background: rgba(239, 68, 68, 0.15); color: var(--danger);"><i class="fa-solid fa-triangle-exclamation"></i></div>
                        <div>
                            <span style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600;">LOW STOCK ITEMS</span>
                            <h3 id="admin-stat-lowstock" style="font-size: 1.4rem; font-weight: 800;">0</h3>
                        </div>
                    </div>
                </div>

                <!-- Admin Chart Canvas -->
                <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.5rem; margin-bottom: 2rem;">
                    <h3 style="font-size: 1.1rem; font-weight: 800; margin-bottom: 1rem;">Sales & Revenue Analytics</h3>
                    <div style="height: 250px; position: relative;">
                        <canvas id="adminSalesChart"></canvas>
                    </div>
                </div>

                <!-- Admin Management Tables -->
                <div class="data-table-wrapper" style="margin-bottom: 2rem;">
                    <div style="padding: 1rem; background: var(--bg-subtle); display: flex; justify-content: space-between; align-items: center;">
                        <h3 style="font-size: 1rem; font-weight: 700;">Product Inventory</h3>
                        <input type="text" placeholder="Filter inventory..." oninput="filterAdminProductsTable(this.value)" style="padding: 0.4rem 0.8rem; font-size: 0.85rem;">
                    </div>
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Product Name</th>
                                <th>Category</th>
                                <th>Price</th>
                                <th>Stock</th>
                                <th>Rating</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody id="admin-products-table-body"></tbody>
                    </table>
                </div>

                <!-- Order Management Table -->
                <div class="data-table-wrapper">
                    <div style="padding: 1rem; background: var(--bg-subtle);">
                        <h3 style="font-size: 1rem; font-weight: 700;">Customer Orders Management</h3>
                    </div>
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>Order ID</th>
                                <th>Customer</th>
                                <th>Date</th>
                                <th>Amount</th>
                                <th>Payment</th>
                                <th>Status</th>
                                <th>Update Status</th>
                            </tr>
                        </thead>
                        <tbody id="admin-orders-table-body"></tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- ==========================================
           VIEW: ORDER TRACKING & TIMELINE
           ========================================== -->
        <section id="view-order-tracking" class="page-view" style="display: none;">
            <div class="container" style="padding: 3rem 0; max-width: 800px;">
                <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 2rem; box-shadow: var(--shadow-lg);">
                    <h2 style="font-size: 1.5rem; font-weight: 800; text-align: center; margin-bottom: 0.5rem;">Track Your Order</h2>
                    <p style="text-align: center; color: var(--text-muted); font-size: 0.9rem; margin-bottom: 2rem;" id="track-order-subtitle">Enter your Order ID to track shipment timeline</p>
                    
                    <div class="timeline" id="tracking-timeline">
                        <div class="timeline-step completed"><div class="step-icon"><i class="fa-solid fa-check"></i></div><span>Placed</span></div>
                        <div class="timeline-step completed"><div class="step-icon"><i class="fa-solid fa-box"></i></div><span>Confirmed</span></div>
                        <div class="timeline-step active"><div class="step-icon"><i class="fa-solid fa-truck"></i></div><span>Shipped</span></div>
                        <div class="timeline-step"><div class="step-icon"><i class="fa-solid fa-house"></i></div><span>Delivered</span></div>
                    </div>

                    <div id="tracking-details-box" style="background: var(--bg-subtle); padding: 1.25rem; border-radius: var(--radius-md); margin-top: 2rem;"></div>
                </div>
            </div>
        </section>

    </main>

    <!-- ==========================================
       MODALS & OVERLAYS
       ========================================== -->

    <!-- Product Details Modal -->
    <div id="modal-product-details" class="modal-overlay">
        <div class="modal-content">
            <div class="modal-close" onclick="closeModal('modal-product-details')">&times;</div>
            <div class="product-detail-grid">
                <div class="detail-gallery">
                    <img id="modal-product-img" src="" alt="Product Detail">
                </div>
                <div>
                    <span id="modal-product-cat" class="product-category"></span>
                    <h2 id="modal-product-title" style="font-size: 1.5rem; font-weight: 800; margin-bottom: 0.5rem;"></h2>
                    <div class="product-rating" id="modal-product-rating"></div>
                    <div class="product-price-row" style="margin-top: 1rem;">
                        <span class="current-price" id="modal-product-price" style="font-size: 1.5rem;"></span>
                        <span class="original-price" id="modal-product-orig-price"></span>
                        <span id="modal-product-badge" class="badge badge-success"></span>
                    </div>
                    <p id="modal-product-desc" style="font-size: 0.9rem; color: var(--text-muted); margin: 1rem 0;"></p>
                    
                    <table class="specs-table" id="modal-product-specs"></table>

                    <div style="display: flex; gap: 1rem; align-items: center; margin-top: 1.5rem;">
                        <div class="qty-picker">
                            <button onclick="adjustModalQty(-1)">-</button>
                            <input type="text" id="modal-qty-input" value="1" readonly>
                            <button onclick="adjustModalQty(1)">+</button>
                        </div>
                        <button class="btn btn-primary" id="modal-add-cart-btn"><i class="fa-solid fa-bag-shopping"></i> Add to Cart</button>
                        <button class="btn btn-secondary" id="modal-wishlist-btn"><i class="fa-regular fa-heart"></i></button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Auth Modal (Login / Register) -->
    <div id="modal-auth" class="modal-overlay">
        <div class="modal-content" style="max-width: 420px;">
            <div class="modal-close" onclick="closeModal('modal-auth')">&times;</div>
            <div style="display: flex; gap: 1rem; border-bottom: 1px solid var(--border-color); margin-bottom: 1.5rem; padding-bottom: 0.5rem;">
                <h3 id="tab-auth-login" style="cursor: pointer; font-weight: 800;" onclick="toggleAuthTab('login')">Login</h3>
                <h3 id="tab-auth-register" style="cursor: pointer; color: var(--text-muted);" onclick="toggleAuthTab('register')">Register</h3>
            </div>

            <!-- Login Form -->
            <form id="form-auth-login" onsubmit="handleLoginSubmit(event)">
                <div class="form-group"><label>Email Address</label><input type="email" id="login-email" required placeholder="user@example.com"></div>
                <div class="form-group"><label>Password</label><input type="password" id="login-password" required placeholder="123456"></div>
                <div style="margin-bottom: 1rem; background: var(--bg-subtle); padding: 0.75rem; border-radius: var(--radius-sm); font-size: 0.8rem;">
                    <strong>Demo Accounts:</strong><br>
                    • Customer: user@example.com / 123456<br>
                    • Admin: admin@example.com / admin123
                </div>
                <button type="submit" class="btn btn-primary" style="width: 100%;">Sign In</button>
            </form>

            <!-- Register Form -->
            <form id="form-auth-register" onsubmit="handleRegisterSubmit(event)" style="display: none;">
                <div class="form-group"><label>Full Name</label><input type="text" id="reg-name" required placeholder="Jane Doe"></div>
                <div class="form-group"><label>Email Address</label><input type="email" id="reg-email" required placeholder="jane@example.com"></div>
                <div class="form-group"><label>Password</label><input type="password" id="reg-password" required placeholder="******"></div>
                <button type="submit" class="btn btn-primary" style="width: 100%;">Create Account</button>
            </form>
        </div>
    </div>

    <!-- Add/Edit Product Admin Modal -->
    <div id="modal-admin-product" class="modal-overlay">
        <div class="modal-content" style="max-width: 550px;">
            <div class="modal-close" onclick="closeModal('modal-admin-product')">&times;</div>
            <h3 id="admin-product-modal-title" style="font-size: 1.25rem; font-weight: 800; margin-bottom: 1.25rem;">Add New Product</h3>
            <form onsubmit="handleSaveProductAdmin(event)">
                <input type="hidden" id="admin-prod-id">
                <div class="form-group"><label>Product Name</label><input type="text" id="admin-prod-name" required></div>
                <div class="form-grid-2">
                    <div class="form-group"><label>Category</label><input type="text" id="admin-prod-cat" required></div>
                    <div class="form-group"><label>Brand</label><input type="text" id="admin-prod-brand" required></div>
                </div>
                <div class="form-grid-2">
                    <div class="form-group"><label>Price ($)</label><input type="number" step="0.01" id="admin-prod-price" required></div>
                    <div class="form-group"><label>Stock Qty</label><input type="number" id="admin-prod-stock" required></div>
                </div>
                <div class="form-group"><label>Image URL</label><input type="url" id="admin-prod-img" required></div>
                <div class="form-group"><label>Description</label><textarea id="admin-prod-desc" rows="3"></textarea></div>
                <button type="submit" class="btn btn-primary" style="width: 100%;">Save Product</button>
            </form>
        </div>
    </div>

    <!-- Product Comparison Modal -->
    <div id="modal-compare" class="modal-overlay">
        <div class="modal-content" style="max-width: 950px;">
            <div class="modal-close" onclick="closeModal('modal-compare')">&times;</div>
            <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 1.25rem;">Product Comparison</h3>
            <div id="compare-table-container" style="overflow-x: auto;"></div>
        </div>
    </div>

    <!-- Support Chat Drawer -->
    <div class="chat-widget-btn" onclick="toggleChatDrawer()"><i class="fa-solid fa-headset"></i></div>
    <div class="chat-drawer" id="chat-drawer">
        <div class="chat-header">
            <span><i class="fa-solid fa-comments"></i> Nexus Support Chat</span>
            <span style="cursor: pointer;" onclick="toggleChatDrawer()">&times;</span>
        </div>
        <div class="chat-body" id="chat-messages">
            <div class="chat-msg bot">Hi there! 👋 How can I help you today?</div>
        </div>
        <div style="padding: 0.75rem; background: var(--bg-card); border-top: 1px solid var(--border-color); display: flex; gap: 0.5rem;">
            <input type="text" id="chat-input" placeholder="Type a message..." style="font-size: 0.85rem;" onkeypress="if(event.key==='Enter') sendChatMessage()">
            <button class="btn btn-primary btn-sm" onclick="sendChatMessage()"><i class="fa-solid fa-paper-plane"></i></button>
        </div>
    </div>

    <!-- Back to Top Button -->
    <button class="btn-icon back-to-top" id="back-to-top" onclick="window.scrollTo({top:0, behavior:'smooth'})"><i class="fa-solid fa-arrow-up"></i></button>

    <!-- Footer -->
    <footer>
        <div class="container footer-grid">
            <div>
                <a href="javascript:void(0)" class="logo" style="margin-bottom: 1rem; display: inline-flex;">
                    <i class="fa-solid fa-cube"></i> ShopNexus
                </a>
                <p style="font-size: 0.875rem; color: var(--text-muted); margin-bottom: 1rem; max-width: 320px;">
                    Your ultimate modern destination for flagship electronics, high-end laptops, footwear, fashion, and home appliances.
                </p>
                <div style="display: flex; gap: 0.75rem;">
                    <button class="btn-icon"><i class="fa-brands fa-facebook-f"></i></button>
                    <button class="btn-icon"><i class="fa-brands fa-twitter"></i></button>
                    <button class="btn-icon"><i class="fa-brands fa-instagram"></i></button>
                </div>
            </div>
            <div>
                <h4>Shop Categories</h4>
                <ul class="footer-links">
                    <li><a href="javascript:void(0)" onclick="filterByCategory('Electronics')">Electronics</a></li>
                    <li><a href="javascript:void(0)" onclick="filterByCategory('Mobiles')">Mobiles & Tablets</a></li>
                    <li><a href="javascript:void(0)" onclick="filterByCategory('Laptops')">Laptops & PC</a></li>
                    <li><a href="javascript:void(0)" onclick="filterByCategory('Fashion')">Fashion & Clothing</a></li>
                </ul>
            </div>
            <div>
                <h4>Customer Support</h4>
                <ul class="footer-links">
                    <li><a href="javascript:void(0)" onclick="navigateTo('order-tracking')">Track Your Order</a></li>
                    <li><a href="javascript:void(0)" onclick="openAuthModal('login')">My Account</a></li>
                    <li><a href="javascript:void(0)" onclick="toggleChatDrawer()">24/7 Live Chat</a></li>
                    <li><a href="javascript:void(0)">Return & Refund Policy</a></li>
                </ul>
            </div>
            <div>
                <h4>Newsletter</h4>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0.75rem;">Subscribe for exclusive discounts & updates.</p>
                <div style="display: flex; gap: 0.5rem;">
                    <input type="email" placeholder="Your email..." style="font-size: 0.85rem;">
                    <button class="btn btn-primary btn-sm" onclick="showToast('Thank you for subscribing!', 'success')">Join</button>
                </div>
            </div>
        </div>
        <div class="container" style="border-top: 1px solid var(--border-color); padding-top: 1.5rem; text-align: center; font-size: 0.8rem; color: var(--text-muted);">
            © 2026 ShopNexus Inc. All rights reserved. Single-File SPA Demo Application.
        </div>
    </footer>

    <!-- ==========================================
       VANILLA JAVASCRIPT APPLICATION LOGIC
       ========================================== -->
    <script>
        /* ==========================================
           1. INITIAL SEED DATA (30 REALISTIC PRODUCTS)
           ========================================== */
        const SEED_PRODUCTS = [
            // Electronics (3)
            { id: "P101", name: "Sony WH-1000XM5 Wireless Headphones", category: "Electronics", brand: "Sony", price: 399.00, originalPrice: 449.00, discount: 11, rating: 4.8, reviewsCount: 1240, stock: 25, image: "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600&auto=format&fit=crop&q=80", description: "Industry-leading noise canceling headphones with two processors and 8 microphones.", specs: { "Noise Canceling": "Active (ANC)", "Battery Life": "30 Hours", "Bluetooth": "5.2" } },
            { id: "P102", name: "Apple iPad Air 10.9\" M1 Chip", category: "Electronics", brand: "Apple", price: 599.00, originalPrice: 649.00, discount: 8, rating: 4.9, reviewsCount: 890, stock: 18, image: "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=600&auto=format&fit=crop&q=80", description: "Powerful Apple M1 chip with 10.9-inch Liquid Retina display and Touch ID.", specs: { "Display": "10.9-inch Liquid Retina", "Processor": "Apple M1", "Storage": "128GB" } },
            { id: "P103", name: "Samsung 55\" QLED 4K Smart TV", category: "Electronics", brand: "Samsung", price: 799.00, originalPrice: 999.00, discount: 20, rating: 4.7, reviewsCount: 650, stock: 12, image: "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=600&auto=format&fit=crop&q=80", description: "Quantum Dot tech delivers 100% color volume for vibrant 4K UHD picture quality.", specs: { "Screen Size": "55 Inch", "Resolution": "4K UHD", "Refresh Rate": "120Hz" } },

            // Mobiles (3)
            { id: "P104", name: "iPhone 15 Pro Max 256GB Titanium", category: "Mobiles", brand: "Apple", price: 1199.00, originalPrice: 1299.00, discount: 8, rating: 4.9, reviewsCount: 2100, stock: 15, image: "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=600&auto=format&fit=crop&q=80", description: "Aerospace-grade titanium design with A17 Pro chip and customizable Action button.", specs: { "Chip": "A17 Pro", "Camera": "48MP Main", "RAM": "8GB" } },
            { id: "P105", name: "Samsung Galaxy S24 Ultra 512GB", category: "Mobiles", brand: "Samsung", price: 1299.00, originalPrice: 1419.00, discount: 8, rating: 4.8, reviewsCount: 1750, stock: 20, image: "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=600&auto=format&fit=crop&q=80", description: "Galaxy AI powered with built-in S-Pen and 200MP ultra-clear camera system.", specs: { "RAM": "12GB", "Storage": "512GB", "Stylus": "S-Pen Included" } },
            { id: "P106", name: "Google Pixel 8 Pro 128GB", category: "Mobiles", brand: "Google", price: 899.00, originalPrice: 999.00, discount: 10, rating: 4.6, reviewsCount: 920, stock: 30, image: "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=600&auto=format&fit=crop&q=80", description: "Powered by Tensor G3 with Google AI camera features and 7 years of OS updates.", specs: { "Processor": "Tensor G3", "RAM": "12GB", "Battery": "5050mAh" } },

            // Laptops (3)
            { id: "P107", name: "MacBook Air M3 15-inch Midnight", category: "Laptops", brand: "Apple", price: 1299.00, originalPrice: 1399.00, discount: 7, rating: 4.9, reviewsCount: 1420, stock: 14, image: "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=600&auto=format&fit=crop&q=80", description: "Ultra-thin aluminum chassis with powerful M3 8-core CPU and up to 18 hours battery.", specs: { "RAM": "16GB", "SSD": "512GB", "Weight": "3.3 lbs" } },
            { id: "P108", name: "Dell XPS 15 OLED Touchscreen", category: "Laptops", brand: "Dell", price: 1799.00, originalPrice: 1999.00, discount: 10, rating: 4.7, reviewsCount: 540, stock: 8, image: "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=600&auto=format&fit=crop&q=80", description: "13th Gen Intel Core i9 processor with breathtaking 3.5K OLED InfinityEdge touch screen.", specs: { "RAM": "32GB", "Storage": "1TB NVMe", "GPU": "RTX 4060" } },
            { id: "P109", name: "ASUS ROG Zephyrus G16 Gaming Laptop", category: "Laptops", brand: "ASUS", price: 1999.00, originalPrice: 2299.00, discount: 13, rating: 4.8, reviewsCount: 410, stock: 5, image: "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=600&auto=format&fit=crop&q=80", description: "Ultra-fast 240Hz ROG Nebula OLED display driven by NVIDIA GeForce RTX 4070.", specs: { "Display": "240Hz OLED", "GPU": "RTX 4070 8GB", "RAM": "32GB LPDDR5X" } },

            // Fashion (3)
            { id: "P110", name: "Levi's Men's Slim Fit Denim Jacket", category: "Fashion", brand: "Levi's", price: 79.00, originalPrice: 110.00, discount: 28, rating: 4.5, reviewsCount: 320, stock: 50, image: "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=600&auto=format&fit=crop&q=80", description: "Timeless trucker denim jacket crafted from 100% premium rigid cotton fabric.", specs: { "Material": "100% Cotton", "Fit": "Slim Fit", "Care": "Machine Wash" } },
            { id: "P111", name: "Zara Women's Floral Summer Maxi Dress", category: "Fashion", brand: "Zara", price: 59.00, originalPrice: 89.00, discount: 33, rating: 4.6, reviewsCount: 280, stock: 40, image: "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=600&auto=format&fit=crop&q=80", description: "Lightweight breathable viscose maxi dress featuring vibrant floral watercolor prints.", specs: { "Pattern": "Floral", "Length": "Maxi", "Sleeve": "Sleeveless" } },
            { id: "P112", name: "AllSaints Genuine Leather Biker Jacket", category: "Fashion", brand: "AllSaints", price: 349.00, originalPrice: 499.00, discount: 30, rating: 4.8, reviewsCount: 190, stock: 12, image: "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=600&auto=format&fit=crop&q=80", description: "Handcrafted soft sheepskin leather jacket with silver asymmetric zips.", specs: { "Material": "100% Sheep Leather", "Lining": "Polyester", "Color": "Black" } },

            // Shoes (3)
            { id: "P113", name: "Nike Air Max 270 Sneakers", category: "Shoes", brand: "Nike", price: 150.00, originalPrice: 180.00, discount: 16, rating: 4.7, reviewsCount: 3100, stock: 45, image: "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&auto=format&fit=crop&q=80", description: "Features Nike's biggest heel Air unit yet for a super-soft ride that feels impossible.", specs: { "Upper": "Breathable Mesh", "Cushioning": "Max Air 270", "Gender": "Unisex" } },
            { id: "P114", name: "Adidas Ultraboost Light Running Shoes", category: "Shoes", brand: "Adidas", price: 140.00, originalPrice: 190.00, discount: 26, rating: 4.8, reviewsCount: 1890, stock: 35, image: "https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=600&auto=format&fit=crop&q=80", description: "Lightest Ultraboost ever made with 30% lighter Light BOOST material.", specs: { "Outsole": "Continental Rubber", "Weight": "299 grams", "Type": "Road Running" } },
            { id: "P115", name: "Puma RS-X Reinvent Retro Sneakers", category: "Shoes", brand: "Puma", price: 95.00, originalPrice: 120.00, discount: 20, rating: 4.5, reviewsCount: 760, stock: 28, image: "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=600&auto=format&fit=crop&q=80", description: "Chunky silhouette with bold color blocking and retro Running System technology.", specs: { "Style": "Retro Casual", "Closure": "Lace Up", "Sole": "Rubber" } },

            // Watches (3)
            { id: "P116", name: "Apple Watch Ultra 2 Titanium 49mm", category: "Watches", brand: "Apple", price: 799.00, originalPrice: 849.00, discount: 6, rating: 4.9, reviewsCount: 1150, stock: 22, image: "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&auto=format&fit=crop&q=80", description: "Most capable Apple Watch with rugged titanium case, precision dual-frequency GPS.", specs: { "Case": "49mm Titanium", "Water Resistance": "100m", "Display": "3000 nits" } },
            { id: "P117", name: "Fossil Gen 6 Touchscreen Smartwatch", category: "Watches", brand: "Fossil", price: 199.00, originalPrice: 299.00, discount: 33, rating: 4.3, reviewsCount: 480, stock: 18, image: "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=600&auto=format&fit=crop&q=80", description: "Snapdragon Wear 4100+ platform with heart rate, SpO2, and fast charging.", specs: { "OS": "Wear OS by Google", "Battery": "24+ Hours", "Compatibility": "Android & iOS" } },
            { id: "P118", name: "Seiko Automatic Diver's 200m Watch", category: "Watches", brand: "Seiko", price: 320.00, originalPrice: 420.00, discount: 23, rating: 4.8, reviewsCount: 620, stock: 10, image: "https://images.unsplash.com/photo-1524805444758-089113d48a6d?w=600&auto=format&fit=crop&q=80", description: "Iconic automatic movement watch with lumibrite hands and ISO certified 200m water resistance.", specs: { "Movement": "Automatic 4R36", "Glass": "Hardlex Crystal", "Water Resistance": "200m" } },

            // Accessories (3)
            { id: "P119", name: "Ray-Ban Classic Wayfarer Sunglasses", category: "Accessories", brand: "Ray-Ban", price: 135.00, originalPrice: 165.00, discount: 18, rating: 4.7, reviewsCount: 1400, stock: 60, image: "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=600&auto=format&fit=crop&q=80", description: "The iconic Wayfarer shape crafted from lightweight durable acetate with G-15 glass lenses.", specs: { "Frame": "Black Acetate", "Lens": "G-15 Green Glass", "UV Protection": "100% UV400" } },
            { id: "P120", name: "Samsonite Pro Travel Business Backpack", category: "Accessories", brand: "Samsonite", price: 110.00, originalPrice: 150.00, discount: 26, rating: 4.6, reviewsCount: 530, stock: 30, image: "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=600&auto=format&fit=crop&q=80", description: "Water-resistant ballistic nylon backpack with TSA lock and 15.6-inch laptop pocket.", specs: { "Capacity": "28 Liters", "Material": "Ballistic Nylon", "USB Port": "External Pass-through" } },
            { id: "P121", name: "Anker 737 Power Bank 24,000mAh 140W", category: "Accessories", brand: "Anker", price: 99.00, originalPrice: 149.00, discount: 33, rating: 4.9, reviewsCount: 2300, stock: 80, image: "https://images.unsplash.com/photo-1609592424109-dd9892f1b177?w=600&auto=format&fit=crop&q=80", description: "Ultra-powerful 140W bi-directional fast charging battery pack with digital smart display.", specs: { "Output": "140W Power Delivery", "Capacity": "24,000mAh", "Ports": "2x USB-C, 1x USB-A" } },

            // Home & Kitchen (3)
            { id: "P122", name: "Nespresso Vertuo Next Coffee Machine", category: "Home & Kitchen", brand: "Nespresso", price: 159.00, originalPrice: 209.00, discount: 24, rating: 4.6, reviewsCount: 1780, stock: 25, image: "https://images.unsplash.com/photo-1517668808822-9fea0282b941?w=600&auto=format&fit=crop&q=80", description: "Centrifusion technology reads barcode on pod to automatically adjust brew parameters.", specs: { "Heat-up Time": "25 Seconds", "Water Tank": "1.1 Liters", "Auto-off": "9 Minutes" } },
            { id: "P123", name: "Dyson V15 Detect Cordless Vacuum", category: "Home & Kitchen", brand: "Dyson", price: 649.00, originalPrice: 749.00, discount: 13, rating: 4.8, reviewsCount: 940, stock: 14, image: "https://images.unsplash.com/photo-1558317374-067fb5f30001?w=600&auto=format&fit=crop&q=80", description: "Illuminated cleaner head reveals invisible dust on hard floors with piezometer particle sensor.", specs: { "Suction Power": "230 AW", "Runtime": "Up to 60 Mins", "Filter": "HEPA Whole Machine" } },
            { id: "P124", name: "Instant Pot Duo 7-in-1 Electric Cooker", category: "Home & Kitchen", brand: "Instant Pot", price: 89.00, originalPrice: 120.00, discount: 25, rating: 4.7, reviewsCount: 4200, stock: 40, image: "https://images.unsplash.com/photo-1585515320310-259814833e62?w=600&auto=format&fit=crop&q=80", description: "Replaces 7 kitchen appliances: pressure cooker, slow cooker, rice cooker, steamer, and sauté pan.", specs: { "Capacity": "6 Quart", "Programs": "13 One-Touch Smart", "Material": "Stainless Steel" } },

            // Beauty (3)
            { id: "P125", name: "Estée Lauder Advanced Night Repair 50ml", category: "Beauty", brand: "Estée Lauder", price: 115.00, originalPrice: 135.00, discount: 14, rating: 4.8, reviewsCount: 1250, stock: 50, image: "https://images.unsplash.com/photo-1608248597262-838d6970f592?w=600&auto=format&fit=crop&q=80", description: "Deep night recovery serum reduces visible signs of aging with hyaluronic acid hydration.", specs: { "Volume": "50 ml", "Skin Type": "All Skin Types", "Key Ingredient": "Tripeptide-32" } },
            { id: "P126", name: "Dyson Airwrap Multi-Styler Complete", category: "Beauty", brand: "Dyson", price: 549.00, originalPrice: 599.00, discount: 8, rating: 4.9, reviewsCount: 2100, stock: 9, image: "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=600&auto=format&fit=crop&q=80", description: "Curl, shape, and hide flyaways using Coanda airflow without extreme heat damage.", specs: { "Technology": "Coanda Airflow", "Attachments": "6 Included", "Heat Control": "Intelligent Sensors" } },
            { id: "P127", name: "Chanel Bleu de Chanel Parfum 100ml", category: "Beauty", brand: "Chanel", price: 165.00, originalPrice: 180.00, discount: 8, rating: 4.9, reviewsCount: 980, stock: 20, image: "https://images.unsplash.com/photo-1541643600914-78b084683601?w=600&auto=format&fit=crop&q=80", description: "A profound woody aromatic fragrance with fresh citrus opening and rich New Caledonian sandalwood.", specs: { "Concentration": "Parfum", "Volume": "100 ml", "Scent Family": "Woody Aromatic" } },

            // Gaming (3)
            { id: "P128", name: "Sony PlayStation 5 Slim Digital Console", category: "Gaming", brand: "Sony", price: 499.00, originalPrice: 549.00, discount: 9, rating: 4.9, reviewsCount: 5400, stock: 16, image: "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=600&auto=format&fit=crop&q=80", description: "Slimmer PS5 design with 1TB SSD storage, haptic feedback DualSense wireless controller.", specs: { "Storage": "1TB Custom SSD", "Resolution": "4K 120Hz", "HDR": "Yes" } },
            { id: "P129", name: "Xbox Series X 1TB Gaming Console", category: "Gaming", brand: "Microsoft", price: 479.00, originalPrice: 529.00, discount: 9, rating: 4.8, reviewsCount: 3800, stock: 18, image: "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=600&auto=format&fit=crop&q=80", description: "Fastest, most powerful Xbox ever with 12 teraflops of raw graphic processing power.", specs: { "Power": "12 Teraflops", "Storage": "1TB NVMe SSD", "Architecture": "Velocity" } },
            { id: "P130", name: "Nintendo Switch OLED Model White", category: "Gaming", brand: "Nintendo", price: 349.00, originalPrice: 379.00, discount: 8, rating: 4.8, reviewsCount: 4900, stock: 35, image: "https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?w=600&auto=format&fit=crop&q=80", description: "Vibrant 7-inch OLED screen with wide adjustable stand, wired LAN dock, and 64GB storage.", specs: { "Screen": "7-inch OLED", "Storage": "64GB Internal", "Modes": "TV, Tabletop, Handheld" } }
        ];

        const DEFAULT_USERS = [
            { id: "U1", name: "Demo User", email: "user@example.com", password: "123456", role: "customer" },
            { id: "U2", name: "Store Admin", email: "admin@example.com", password: "admin123", role: "admin" }
        ];

        /* ==========================================
           2. STATE & LOCALSTORAGE STORAGE HELPERS
           ========================================== */
        let state = {
            products: [],
            cart: [],
            wishlist: [],
            compareList: [],
            orders: [],
            currentUser: null,
            activeView: 'home',
            activeCategory: 'All',
            priceMax: 2500,
            ratingMin: 0,
            discountOnly: false,
            sort: 'featured',
            searchQuery: '',
            appliedCoupon: null
        };

        function initStorage() {
            if (!localStorage.getItem('products')) localStorage.setItem('products', JSON.stringify(SEED_PRODUCTS));
            if (!localStorage.getItem('users')) localStorage.setItem('users', JSON.stringify(DEFAULT_USERS));
            if (!localStorage.getItem('cart')) localStorage.setItem('cart', JSON.stringify([]));
            if (!localStorage.getItem('wishlist')) localStorage.setItem('wishlist', JSON.stringify([]));
            if (!localStorage.getItem('orders')) localStorage.setItem('orders', JSON.stringify([]));
            if (!localStorage.getItem('theme')) localStorage.setItem('theme', 'light');

            state.products = JSON.parse(localStorage.getItem('products'));
            state.cart = JSON.parse(localStorage.getItem('cart'));
            state.wishlist = JSON.parse(localStorage.getItem('wishlist'));
            state.orders = JSON.parse(localStorage.getItem('orders'));
            state.currentUser = JSON.parse(localStorage.getItem('currentUser')) || null;
            
            // Set saved theme
            document.documentElement.setAttribute('data-theme', localStorage.getItem('theme'));
            updateThemeIcon();
        }

        function saveProducts() { localStorage.setItem('products', JSON.stringify(state.products)); }
        function saveCart() { localStorage.setItem('cart', JSON.stringify(state.cart)); updateBadges(); }
        function saveWishlist() { localStorage.setItem('wishlist', JSON.stringify(state.wishlist)); updateBadges(); }
        function saveOrders() { localStorage.setItem('orders', JSON.stringify(state.orders)); }

        /* ==========================================
           3. ROUTING & VIEW NAVIGATION
           ========================================== */
        function navigateTo(viewId, params = {}) {
            document.querySelectorAll('.page-view').forEach(el => el.style.display = 'none');
            
            const targetView = document.getElementById(`view-${viewId}`);
            if (targetView) {
                targetView.style.display = 'block';
                state.activeView = viewId;
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }

            if (viewId === 'home') renderHome();
            else if (viewId === 'shop') renderShop();
            else if (viewId === 'cart') renderCart();
            else if (viewId === 'checkout') renderCheckout();
            else if (viewId === 'user-dashboard') renderUserDashboard(params);
            else if (viewId === 'admin-dashboard') renderAdminDashboard();
            else if (viewId === 'order-tracking') renderOrderTracking(params.orderId);
        }

        /* ==========================================
           4. RENDERERS & HOME PAGE
           ========================================== */
        function renderHome() {
            // Category Nav List
            const categories = ["All", "Electronics", "Mobiles", "Laptops", "Fashion", "Shoes", "Watches", "Accessories", "Home & Kitchen", "Beauty", "Gaming"];
            const catNavHtml = categories.map(cat => `
                <li class="category-nav-item ${state.activeCategory === cat ? 'active' : ''}" onclick="filterByCategory('${cat}')">
                    ${cat}
                </li>
            `).join('');
            document.getElementById('category-nav-list').innerHTML = catNavHtml;

            // Categories visual grid
            const catGridHtml = categories.filter(c => c !== 'All').map(cat => {
                const sampleProd = state.products.find(p => p.category === cat) || state.products[0];
                return `
                    <div class="product-card" style="cursor:pointer;" onclick="filterByCategory('${cat}')">
                        <div class="product-img-wrapper" style="padding-top:70%;">
                            <img src="${sampleProd.image}" alt="${cat}">
                        </div>
                        <div style="padding:0.75rem; text-align:center; font-weight:700; font-size:0.9rem;">${cat}</div>
                    </div>
                `;
            }).join('');
            document.getElementById('categories-grid').innerHTML = catGridHtml;

            // Featured & Trending Grids
            const featured = state.products.slice(0, 8);
            const trending = state.products.slice(8, 16);

            document.getElementById('featured-products-grid').innerHTML = featured.map(renderProductCardHtml).join('');
            document.getElementById('trending-products-grid').innerHTML = trending.map(renderProductCardHtml).join('');
        }

        function filterByCategory(cat) {
            state.activeCategory = cat;
            navigateTo('shop');
            renderShop();
        }

        function renderProductCardHtml(p) {
            const isWish = state.wishlist.includes(p.id);
            return `
                <div class="product-card">
                    <div class="product-img-wrapper" onclick="openProductDetails('${p.id}')" style="cursor:pointer;">
                        <img src="${p.image}" alt="${p.name}">
                        ${p.discount ? `<span class="discount-badge">-${p.discount}%</span>` : ''}
                        <div class="card-actions-overlay" onclick="event.stopPropagation()">
                            <button class="btn-icon" title="Wishlist" onclick="toggleWishlist('${p.id}')">
                                <i class="fa-${isWish ? 'solid' : 'regular'} fa-heart" style="${isWish ? 'color:var(--danger)' : ''}"></i>
                            </button>
                            <button class="btn-icon" title="Compare" onclick="toggleCompare('${p.id}')">
                                <i class="fa-solid fa-sliders"></i>
                            </button>
                        </div>
                    </div>
                    <div class="product-info">
                        <span class="product-category">${p.category} • ${p.brand}</span>
                        <h4 class="product-title" onclick="openProductDetails('${p.id}')" style="cursor:pointer;">${p.name}</h4>
                        <div class="product-rating">
                            <i class="fa-solid fa-star"></i> <strong>${p.rating}</strong>
                            <span class="review-count">(${p.reviewsCount})</span>
                        </div>
                        <div class="product-price-row">
                            <span class="current-price">$${p.price.toFixed(2)}</span>
                            ${p.originalPrice ? `<span class="original-price">$${p.originalPrice.toFixed(2)}</span>` : ''}
                        </div>
                        <button class="btn btn-primary btn-sm card-add-btn" onclick="addToCart('${p.id}')">
                            <i class="fa-solid fa-bag-shopping"></i> Add to Cart
                        </button>
                    </div>
                </div>
            `;
        }

        /* ==========================================
           5. SHOP PAGE & FILTERS
           ========================================== */
        function renderShop() {
            // Category sidebar items
            const categories = ["All", "Electronics", "Mobiles", "Laptops", "Fashion", "Shoes", "Watches", "Accessories", "Home & Kitchen", "Beauty", "Gaming"];
            document.getElementById('shop-filter-categories').innerHTML = categories.map(cat => `
                <label class="filter-item">
                    <input type="radio" name="shop-category" value="${cat}" ${state.activeCategory === cat ? 'checked' : ''} onchange="filterByCategory('${cat}')"> ${cat}
                </label>
            `).join('');

            applyShopFilters();
        }

        function applyShopFilters() {
            let filtered = [...state.products];

            // Search Filter
            if (state.searchQuery) {
                const q = state.searchQuery.toLowerCase();
                filtered = filtered.filter(p => p.name.toLowerCase().includes(q) || p.category.toLowerCase().includes(q) || p.brand.toLowerCase().includes(q));
            }

            // Category Filter
            if (state.activeCategory !== 'All') {
                filtered = filtered.filter(p => p.category === state.activeCategory);
            }

            // Price Filter
            filtered = filtered.filter(p => p.price <= state.priceMax);

            // Rating Filter
            const selRating = parseFloat(document.querySelector('input[name="rating-filter"]:checked')?.value || 0);
            if (selRating > 0) filtered = filtered.filter(p => p.rating >= selRating);

            // Discount Only
            if (document.getElementById('discount-only-cb')?.checked) {
                filtered = filtered.filter(p => p.discount > 0);
            }

            // Sort Order
            const sortVal = document.getElementById('shop-sort-select')?.value || 'featured';
            if (sortVal === 'price-low') filtered.sort((a,b) => a.price - b.price);
            else if (sortVal === 'price-high') filtered.sort((a,b) => b.price - a.price);
            else if (sortVal === 'rating') filtered.sort((a,b) => b.rating - a.rating);

            document.getElementById('shop-results-count').innerText = `Showing ${filtered.length} products`;
            document.getElementById('shop-products-grid').innerHTML = filtered.length > 0
                ? filtered.map(renderProductCardHtml).join('')
                : `<p style="grid-column: 1/-1; text-align:center; padding: 3rem 0; color:var(--text-muted);">No products match your search/filter criteria.</p>`;
        }

        function handlePriceFilter(val) {
            state.priceMax = parseFloat(val);
            document.getElementById('price-range-val').innerText = `$0 - $${val}`;
            applyShopFilters();
        }

        function resetAllFilters() {
            state.activeCategory = 'All';
            state.priceMax = 2500;
            state.searchQuery = '';
            document.getElementById('global-search').value = '';
            document.getElementById('price-slider').value = 2500;
            document.getElementById('price-range-val').innerText = '$0 - $2500';
            if (document.getElementById('discount-only-cb')) document.getElementById('discount-only-cb').checked = false;
            renderShop();
        }

        function resetCategoryFilter() {
            state.activeCategory = 'All';
            renderShop();
        }

        /* ==========================================
           6. SEARCH & LIVE AUTOCOMPLETE
           ========================================== */
        function handleSearchInput(query) {
            state.searchQuery = query.trim();
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
                        <img src="${p.image}" alt="${p.name}">
                        <div>
                            <div style="font-weight:700; font-size:0.85rem;">${p.name}</div>
                            <div style="font-size:0.75rem; color:var(--primary);">$${p.price.toFixed(2)}</div>
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
           7. PRODUCT DETAIL MODAL
           ========================================== */
        let currentModalProductId = null;

        function openProductDetails(id) {
            const p = state.products.find(item => item.id === id);
            if (!p) return;

            currentModalProductId = id;
            document.getElementById('modal-product-img').src = p.image;
            document.getElementById('modal-product-cat').innerText = `${p.category} • ${p.brand}`;
            document.getElementById('modal-product-title').innerText = p.name;
            document.getElementById('modal-product-rating').innerHTML = `<i class="fa-solid fa-star"></i> <strong>${p.rating}</strong> (${p.reviewsCount} customer reviews)`;
            document.getElementById('modal-product-price').innerText = `$${p.price.toFixed(2)}`;
            document.getElementById('modal-product-orig-price').innerText = p.originalPrice ? `$${p.originalPrice.toFixed(2)}` : '';
            document.getElementById('modal-product-badge').innerText = p.stock > 0 ? `In Stock (${p.stock})` : `Out of Stock`;
            document.getElementById('modal-product-desc').innerText = p.description;

            // Specs table
            const specsHtml = Object.entries(p.specs || {}).map(([k, v]) => `
                <tr><td>${k}</td><td>${v}</td></tr>
            `).join('');
            document.getElementById('modal-product-specs').innerHTML = specsHtml;

            document.getElementById('modal-qty-input').value = 1;
            document.getElementById('modal-add-cart-btn').onclick = () => {
                const qty = parseInt(document.getElementById('modal-qty-input').value) || 1;
                addToCart(p.id, qty);
                closeModal('modal-product-details');
            };

            document.getElementById('modal-product-details').classList.add('active');
        }

        function adjustModalQty(delta) {
            const input = document.getElementById('modal-qty-input');
            let val = parseInt(input.value) + delta;
            if (val < 1) val = 1;
            input.value = val;
        }

        function closeModal(modalId) {
            document.getElementById(modalId)?.classList.remove('active');
        }

        /* ==========================================
           8. CART LOGIC & CHECKOUT
           ========================================== */
        function addToCart(productId, quantity = 1) {
            const product = state.products.find(p => p.id === productId);
            if (!product) return;

            const existing = state.cart.find(item => item.productId === productId);
            if (existing) {
                existing.quantity += quantity;
            } else {
                state.cart.push({ productId, quantity });
            }

            saveCart();
            showToast(`Added "${product.name}" to cart!`, 'success');
        }

        function updateCartQty(productId, delta) {
            const item = state.cart.find(i => i.productId === productId);
            if (!item) return;

            item.quantity += delta;
            if (item.quantity <= 0) {
                state.cart = state.cart.filter(i => i.productId !== productId);
            }
            saveCart();
            renderCart();
        }

        function removeFromCart(productId) {
            state.cart = state.cart.filter(i => i.productId !== productId);
            saveCart();
            renderCart();
            showToast('Item removed from cart', 'info');
        }

        function renderCart() {
            const body = document.getElementById('cart-table-body');
            if (state.cart.length === 0) {
                body.innerHTML = `<tr><td colspan="5" style="text-align:center; padding: 3rem; color:var(--text-muted);">Your cart is empty. <a href="javascript:void(0)" onclick="navigateTo('shop')" style="color:var(--primary); font-weight:700;">Explore Shop</a></td></tr>`;
                calculateTotals(0);
                return;
            }

            let subtotal = 0;
            body.innerHTML = state.cart.map(item => {
                const p = state.products.find(x => x.id === item.productId);
                if (!p) return '';
                const itemSubtotal = p.price * item.quantity;
                subtotal += itemSubtotal;

                return `
                    <tr>
                        <td>
                            <div class="cart-item-info">
                                <img src="${p.image}" alt="${p.name}">
                                <div>
                                    <h4 style="font-size:0.9rem; font-weight:700;">${p.name}</h4>
                                    <span style="font-size:0.75rem; color:var(--text-muted);">${p.brand}</span>
                                </div>
                            </div>
                        </td>
                        <td style="font-weight:700;">$${p.price.toFixed(2)}</td>
                        <td>
                            <div class="qty-picker">
                                <button onclick="updateCartQty('${p.id}', -1)">-</button>
                                <input type="text" value="${item.quantity}" readonly>
                                <button onclick="updateCartQty('${p.id}', 1)">+</button>
                            </div>
                        </td>
                        <td style="font-weight:800; color:var(--primary);">$${itemSubtotal.toFixed(2)}</td>
                        <td>
                            <button class="btn-icon" style="color:var(--danger);" onclick="removeFromCart('${p.id}')">
                                <i class="fa-solid fa-trash-can"></i>
                            </button>
                        </td>
                    </tr>
                `;
            }).join('');

            calculateTotals(subtotal);
        }

        function calculateTotals(subtotal) {
            const tax = subtotal * 0.18; // 18% GST
            const shipping = (subtotal > 50 || subtotal === 0) ? 0.00 : 10.00;
            
            let discountAmount = 0;
            if (state.appliedCoupon === 'SAVE10') discountAmount = subtotal * 0.10;
            else if (state.appliedCoupon === 'SAVE20') discountAmount = subtotal * 0.20;
            else if (state.appliedCoupon === 'WELCOME') discountAmount = 15.00;

            const grandTotal = Math.max(0, subtotal + tax + shipping - discountAmount);

            document.getElementById('summary-subtotal').innerText = `$${subtotal.toFixed(2)}`;
            document.getElementById('summary-tax').innerText = `$${tax.toFixed(2)}`;
            document.getElementById('summary-shipping').innerText = shipping === 0 ? 'FREE' : `$${shipping.toFixed(2)}`;
            document.getElementById('summary-discount').innerText = `-$${discountAmount.toFixed(2)}`;
            document.getElementById('summary-grand-total').innerText = `$${grandTotal.toFixed(2)}`;
            
            if (document.getElementById('chk-pay-total')) {
                document.getElementById('chk-pay-total').innerText = `$${grandTotal.toFixed(2)}`;
            }
        }

        function applyCoupon() {
            const code = document.getElementById('coupon-input')?.value.trim().toUpperCase();
            if (['SAVE10', 'SAVE20', 'WELCOME'].includes(code)) {
                state.appliedCoupon = code;
                showToast(`Coupon "${code}" applied successfully!`, 'success');
                renderCart();
            } else {
                showToast('Invalid coupon code. Try WELCOME or SAVE10', 'error');
            }
        }

        /* ==========================================
           9. CHECKOUT & ORDER PLACEMENT
           ========================================== */
        let selectedPaymentMode = 'cod';

        function renderCheckout() {
            if (state.currentUser) {
                document.getElementById('chk-name').value = state.currentUser.name || '';
                document.getElementById('chk-phone').value = '+1 555 019 2834';
                document.getElementById('chk-address').value = '742 Evergreen Terrace';
                document.getElementById('chk-city').value = 'Springfield';
                document.getElementById('chk-state').value = 'OR';
                document.getElementById('chk-zip').value = '97477';
            }

            // Checkout Items Review
            const listHtml = state.cart.map(i => {
                const p = state.products.find(x => x.id === i.productId);
                return p ? `
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem; font-size:0.85rem;">
                        <span>${p.name} (x${i.quantity})</span>
                        <strong>$${(p.price * i.quantity).toFixed(2)}</strong>
                    </div>
                ` : '';
            }).join('');
            document.getElementById('checkout-items-list').innerHTML = listHtml;
            renderCart(); // Trigger total calculations
        }

        function selectPaymentMethod(btn, mode) {
            document.querySelectorAll('.payment-tab-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            selectedPaymentMode = mode;
        }

        function processOrderPlacement() {
            if (state.cart.length === 0) {
                showToast('Cart is empty!', 'error');
                return;
            }

            const name = document.getElementById('chk-name').value.trim();
            const address = document.getElementById('chk-address').value.trim();
            if (!name || !address) {
                showToast('Please fill out address fields', 'error');
                return;
            }

            const orderId = 'ORD-' + Math.floor(100000 + Math.random() * 900000);
            const total = parseFloat(document.getElementById('summary-grand-total').innerText.replace('$', ''));

            const newOrder = {
                orderId,
                customer: name,
                email: state.currentUser ? state.currentUser.email : 'guest@example.com',
                items: [...state.cart],
                totalAmount: total,
                paymentMethod: selectedPaymentMode.toUpperCase(),
                date: new Date().toLocaleDateString(),
                status: 'Placed'
            };

            state.orders.unshift(newOrder);
            saveOrders();

            // Clear cart
            state.cart = [];
            saveCart();

            showToast(`Order ${orderId} placed successfully!`, 'success');
            navigateTo('order-tracking', { orderId });
        }

        /* ==========================================
           10. ORDER TRACKING TIMELINE
           ========================================== */
        function renderOrderTracking(orderId) {
            const order = state.orders.find(o => o.orderId === orderId) || state.orders[0];
            const detailsBox = document.getElementById('tracking-details-box');
            
            if (!order) {
                detailsBox.innerHTML = `<p style="text-align:center; color:var(--text-muted);">No orders found. Place an order to track shipment status!</p>`;
                return;
            }

            document.getElementById('track-order-subtitle').innerText = `Order ID: #${order.orderId} • Placed on ${order.date}`;
            
            detailsBox.innerHTML = `
                <div style="display:flex; justify-content:space-between; margin-bottom:0.75rem;">
                    <span>Customer: <strong>${order.customer}</strong></span>
                    <span>Status: <strong class="badge badge-primary">${order.status}</strong></span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span>Total Amount: <strong>$${order.totalAmount.toFixed(2)}</strong></span>
                    <span>Payment: <strong>${order.paymentMethod}</strong></span>
                </div>
            `;
        }

        /* ==========================================
           11. USER AUTHENTICATION & DASHBOARD
           ========================================== */
        function openAuthModal(tab = 'login') {
            toggleAuthTab(tab);
            document.getElementById('modal-auth').classList.add('active');
        }

        function toggleAuthTab(tab) {
            const loginForm = document.getElementById('form-auth-login');
            const regForm = document.getElementById('form-auth-register');
            const tabLogin = document.getElementById('tab-auth-login');
            const tabReg = document.getElementById('tab-auth-register');

            if (tab === 'login') {
                loginForm.style.display = 'block';
                regForm.style.display = 'none';
                tabLogin.style.color = 'var(--text-main)';
                tabReg.style.color = 'var(--text-muted)';
            } else {
                loginForm.style.display = 'none';
                regForm.style.display = 'block';
                tabReg.style.color = 'var(--text-main)';
                tabLogin.style.color = 'var(--text-muted)';
            }
        }

        function handleLoginSubmit(e) {
            e.preventDefault();
            const email = document.getElementById('login-email').value.trim();
            const pass = document.getElementById('login-password').value.trim();

            const users = JSON.parse(localStorage.getItem('users'));
            const user = users.find(u => u.email === email && u.password === pass);

            if (user) {
                state.currentUser = user;
                localStorage.setItem('currentUser', JSON.stringify(user));
                closeModal('modal-auth');
                updateUserNav();
                showToast(`Welcome back, ${user.name}!`, 'success');
                if (user.role === 'admin') navigateTo('admin-dashboard');
            } else {
                showToast('Invalid email or password!', 'error');
            }
        }

        function handleRegisterSubmit(e) {
            e.preventDefault();
            const name = document.getElementById('reg-name').value.trim();
            const email = document.getElementById('reg-email').value.trim();
            const pass = document.getElementById('reg-password').value.trim();

            const users = JSON.parse(localStorage.getItem('users'));
            if (users.find(u => u.email === email)) {
                showToast('User already exists with this email!', 'error');
                return;
            }

            const newUser = { id: 'U' + Date.now(), name, email, password: pass, role: 'customer' };
            users.push(newUser);
            localStorage.setItem('users', JSON.stringify(users));

            state.currentUser = newUser;
            localStorage.setItem('currentUser', JSON.stringify(newUser));
            closeModal('modal-auth');
            updateUserNav();
            showToast('Account created successfully!', 'success');
        }

        function logoutUser() {
            state.currentUser = null;
            localStorage.removeItem('currentUser');
            updateUserNav();
            showToast('Logged out successfully', 'info');
            navigateTo('home');
        }

        function updateUserNav() {
            const container = document.getElementById('user-nav-container');
            if (state.currentUser) {
                container.innerHTML = `
                    <div style="display:flex; align-items:center; gap:0.5rem;">
                        <button class="btn btn-secondary btn-sm" onclick="navigateTo('${state.currentUser.role === 'admin' ? 'admin-dashboard' : 'user-dashboard'}')">
                            <i class="fa-solid fa-user-circle"></i> ${state.currentUser.name}
                        </button>
                    </div>
                `;
            } else {
                container.innerHTML = `
                    <button class="btn btn-primary btn-sm" onclick="openAuthModal('login')">
                        <i class="fa-solid fa-user"></i> Login
                    </button>
                `;
            }
        }

        function renderUserDashboard(params = {}) {
            if (!state.currentUser) {
                openAuthModal('login');
                return;
            }

            document.getElementById('profile-email').value = state.currentUser.email;
            document.getElementById('profile-name').value = state.currentUser.name;

            // My Orders List
            const myOrders = state.orders.filter(o => o.email === state.currentUser.email || o.email === 'guest@example.com');
            document.getElementById('user-orders-list').innerHTML = myOrders.length > 0 ? myOrders.map(o => `
                <div style="background:var(--bg-card); border:1px solid var(--border-color); padding:1rem; border-radius:var(--radius-md); margin-bottom:1rem;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:0.5rem;">
                        <strong>Order #${o.orderId}</strong>
                        <span class="badge badge-success">${o.status}</span>
                    </div>
                    <div style="font-size:0.85rem; color:var(--text-muted); margin-bottom:0.5rem;">Date: ${o.date} • Total: $${o.totalAmount.toFixed(2)}</div>
                    <button class="btn btn-secondary btn-sm" onclick="navigateTo('order-tracking', {orderId: '${o.orderId}'})">Track Package</button>
                </div>
            `).join('') : `<p style="color:var(--text-muted);">No order history found.</p>`;

            // Wishlist Tab
            const wishProds = state.products.filter(p => state.wishlist.includes(p.id));
            document.getElementById('user-wishlist-grid').innerHTML = wishProds.length > 0
                ? wishProds.map(renderProductCardHtml).join('')
                : `<p style="color:var(--text-muted);">Your wishlist is empty.</p>`;

            if (params.tab) switchDashboardTab(params.tab);
        }

        function switchDashboardTab(tab, el) {
            document.querySelectorAll('.dash-tab-content').forEach(d => d.style.display = 'none');
            document.querySelectorAll('.dashboard-menu-item').forEach(m => m.classList.remove('active'));
            document.getElementById(`dash-tab-${tab}`).style.display = 'block';
            if (el) el.classList.add('active');
        }

        function toggleWishlist(id) {
            if (state.wishlist.includes(id)) {
                state.wishlist = state.wishlist.filter(x => x !== id);
                showToast('Removed from Wishlist', 'info');
            } else {
                state.wishlist.push(id);
                showToast('Saved to Wishlist!', 'success');
            }
            saveWishlist();
            if (state.activeView === 'home') renderHome();
            if (state.activeView === 'shop') applyShopFilters();
        }

        /* ==========================================
           12. ADMIN DASHBOARD & CRUD MANAGEMENT
           ========================================== */
        function renderAdminDashboard() {
            if (!state.currentUser || state.currentUser.role !== 'admin') {
                showToast('Admin authorization required!', 'error');
                openAuthModal('login');
                return;
            }

            const totalSales = state.orders.reduce((acc, o) => acc + o.totalAmount, 0);
            const lowStockCount = state.products.filter(p => p.stock < 15).length;

            document.getElementById('admin-stat-sales').innerText = `$${totalSales.toFixed(2)}`;
            document.getElementById('admin-stat-orders').innerText = state.orders.length;
            document.getElementById('admin-stat-products').innerText = state.products.length;
            document.getElementById('admin-stat-lowstock').innerText = lowStockCount;

            // Admin Products Table
            renderAdminProductsTable();

            // Admin Orders Table
            document.getElementById('admin-orders-table-body').innerHTML = state.orders.map(o => `
                <tr>
                    <td>#${o.orderId}</td>
                    <td>${o.customer}</td>
                    <td>${o.date}</td>
                    <td>$${o.totalAmount.toFixed(2)}</td>
                    <td>${o.paymentMethod}</td>
                    <td><span class="badge badge-primary">${o.status}</span></td>
                    <td>
                        <select onchange="updateOrderStatus('${o.orderId}', this.value)" style="padding:0.2rem 0.5rem; font-size:0.8rem;">
                            <option value="Placed" ${o.status==='Placed'?'selected':''}>Placed</option>
                            <option value="Confirmed" ${o.status==='Confirmed'?'selected':''}>Confirmed</option>
                            <option value="Shipped" ${o.status==='Shipped'?'selected':''}>Shipped</option>
                            <option value="Delivered" ${o.status==='Delivered'?'selected':''}>Delivered</option>
                            <option value="Cancelled" ${o.status==='Cancelled'?'selected':''}>Cancelled</option>
                        </select>
                    </td>
                </tr>
            `).join('');

            // Chart.js initialization
            renderAdminCharts();
        }

        function renderAdminProductsTable(query = '') {
            let list = [...state.products];
            if (query) list = list.filter(p => p.name.toLowerCase().includes(query.toLowerCase()));

            document.getElementById('admin-products-table-body').innerHTML = list.map(p => `
                <tr>
                    <td>${p.id}</td>
                    <td><strong>${p.name}</strong></td>
                    <td>${p.category}</td>
                    <td>$${p.price.toFixed(2)}</td>
                    <td><span class="badge ${p.stock < 15 ? 'badge-danger' : 'badge-success'}">${p.stock}</span></td>
                    <td>${p.rating} ★</td>
                    <td>
                        <button class="btn-sm btn-secondary" onclick="editProductAdmin('${p.id}')"><i class="fa-solid fa-pen"></i></button>
                        <button class="btn-sm btn-danger" onclick="deleteProductAdmin('${p.id}')"><i class="fa-solid fa-trash"></i></button>
                    </td>
                </tr>
            `).join('');
        }

        function filterAdminProductsTable(q) {
            renderAdminProductsTable(q);
        }

        function openAddProductModal() {
            document.getElementById('admin-product-modal-title').innerText = 'Add New Product';
            document.getElementById('admin-prod-id').value = '';
            document.getElementById('admin-prod-name').value = '';
            document.getElementById('admin-prod-cat').value = 'Electronics';
            document.getElementById('admin-prod-brand').value = '';
            document.getElementById('admin-prod-price').value = '';
            document.getElementById('admin-prod-stock').value = '25';
            document.getElementById('admin-prod-img').value = '';
            document.getElementById('admin-prod-desc').value = '';
            document.getElementById('modal-admin-product').classList.add('active');
        }

        function editProductAdmin(id) {
            const p = state.products.find(x => x.id === id);
            if (!p) return;

            document.getElementById('admin-product-modal-title').innerText = 'Edit Product';
            document.getElementById('admin-prod-id').value = p.id;
            document.getElementById('admin-prod-name').value = p.name;
            document.getElementById('admin-prod-cat').value = p.category;
            document.getElementById('admin-prod-brand').value = p.brand;
            document.getElementById('admin-prod-price').value = p.price;
            document.getElementById('admin-prod-stock').value = p.stock;
            document.getElementById('admin-prod-img').value = p.image;
            document.getElementById('admin-prod-desc').value = p.description;
            document.getElementById('modal-admin-product').classList.add('active');
        }

        function handleSaveProductAdmin(e) {
            e.preventDefault();
            const id = document.getElementById('admin-prod-id').value;
            const name = document.getElementById('admin-prod-name').value;
            const category = document.getElementById('admin-prod-cat').value;
            const brand = document.getElementById('admin-prod-brand').value;
            const price = parseFloat(document.getElementById('admin-prod-price').value);
            const stock = parseInt(document.getElementById('admin-prod-stock').value);
            const image = document.getElementById('admin-prod-img').value;
            const description = document.getElementById('admin-prod-desc').value;

            if (id) {
                // Update
                const p = state.products.find(x => x.id === id);
                if (p) {
                    p.name = name; p.category = category; p.brand = brand;
                    p.price = price; p.stock = stock; p.image = image; p.description = description;
                }
                showToast('Product updated successfully!', 'success');
            } else {
                // Add
                const newP = {
                    id: 'P' + Math.floor(100 + Math.random() * 900),
                    name, category, brand, price, originalPrice: price * 1.1,
                    discount: 10, rating: 4.5, reviewsCount: 1, stock, image, description, specs: {}
                };
                state.products.unshift(newP);
                showToast('New product added!', 'success');
            }

            saveProducts();
            closeModal('modal-admin-product');
            renderAdminDashboard();
        }

        function deleteProductAdmin(id) {
            if (confirm('Are you sure you want to delete this product?')) {
                state.products = state.products.filter(p => p.id !== id);
                saveProducts();
                renderAdminDashboard();
                showToast('Product deleted', 'info');
            }
        }

        function updateOrderStatus(orderId, newStatus) {
            const o = state.orders.find(x => x.orderId === orderId);
            if (o) {
                o.status = newStatus;
                saveOrders();
                showToast(`Order #${orderId} status updated to ${newStatus}`, 'success');
            }
        }

        function renderAdminCharts() {
            if (window.Chart) {
                const ctx = document.getElementById('adminSalesChart')?.getContext('2d');
                if (!ctx) return;
                
                if (window.mySalesChart) window.mySalesChart.destroy();

                window.mySalesChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
                        datasets: [{
                            label: 'Monthly Revenue ($)',
                            data: [12000, 19000, 15000, 25000, 22000, 30000, 28000, 35000],
                            borderColor: '#4f46e5',
                            backgroundColor: 'rgba(79, 70, 229, 0.1)',
                            fill: true,
                            tension: 0.4
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false
                    }
                });
            }
        }

        /* ==========================================
           13. PRODUCT COMPARISON MODAL
           ========================================== */
        function toggleCompare(id) {
            if (state.compareList.includes(id)) {
                state.compareList = state.compareList.filter(x => x !== id);
                showToast('Removed from compare list', 'info');
            } else {
                if (state.compareList.length >= 4) {
                    showToast('Max 4 items can be compared at once', 'warning');
                    return;
                }
                state.compareList.push(id);
                showToast('Added to compare list!', 'success');
            }
            updateBadges();
        }

        function openCompareModal() {
            const prods = state.products.filter(p => state.compareList.includes(p.id));
            const container = document.getElementById('compare-table-container');

            if (prods.length === 0) {
                container.innerHTML = `<p style="text-align:center; color:var(--text-muted); padding:2rem;">No products added to comparison list. Click the slider icon on product cards to add!</p>`;
            } else {
                container.innerHTML = `
                    <table class="specs-table" style="min-width:600px;">
                        <thead>
                            <tr>
                                <th>Feature</th>
                                ${prods.map(p => `
                                    <th style="text-align:center;">
                                        <img src="${p.image}" style="width:60px; height:60px; object-fit:cover; margin:0 auto 0.5rem auto; border-radius:4px;">
                                        <div>${p.name}</div>
                                        <div style="color:var(--primary);">$${p.price.toFixed(2)}</div>
                                    </th>
                                `).join('')}
                            </tr>
                        </thead>
                        <tbody>
                            <tr><td>Category</td>${prods.map(p => `<td style="text-align:center;">${p.category}</td>`).join('')}</tr>
                            <tr><td>Brand</td>${prods.map(p => `<td style="text-align:center;">${p.brand}</td>`).join('')}</tr>
                            <tr><td>Rating</td>${prods.map(p => `<td style="text-align:center;">${p.rating} ★</td>`).join('')}</tr>
                            <tr><td>Stock Status</td>${prods.map(p => `<td style="text-align:center;">${p.stock} units</td>`).join('')}</tr>
                        </tbody>
                    </table>
                `;
            }
            document.getElementById('modal-compare').classList.add('active');
        }

        /* ==========================================
           14. CHAT WIDGET & TOAST SYSTEM
           ========================================== */
        function toggleChatDrawer() {
            document.getElementById('chat-drawer').classList.toggle('active');
        }

        function sendChatMessage() {
            const input = document.getElementById('chat-input');
            const msg = input.value.trim();
            if (!msg) return;

            const body = document.getElementById('chat-messages');
            body.innerHTML += `<div class="chat-msg user">${msg}</div>`;
            input.value = '';

            setTimeout(() => {
                let reply = "Thanks for contacting Nexus Support! Our team is available 24/7. How can we assist with your order?";
                if (msg.toLowerCase().includes('order') || msg.toLowerCase().includes('track')) reply = "You can track your order status anytime using the Order Tracking page at the top!";
                if (msg.toLowerCase().includes('coupon') || msg.toLowerCase().includes('discount')) reply = "Try code WELCOME for $15 OFF or SAVE20 for 20% OFF at checkout!";
                body.innerHTML += `<div class="chat-msg bot">${reply}</div>`;
                body.scrollTop = body.scrollHeight;
            }, 600);
        }

        function showToast(msg, type = 'info', duration = 3000) {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            toast.className = `toast`;
            
            const icon = type === 'success' ? 'fa-circle-check' : (type === 'error' ? 'fa-circle-xmark' : 'fa-circle-info');
            const color = type === 'success' ? 'var(--success)' : (type === 'error' ? 'var(--danger)' : 'var(--primary)');
            toast.style.borderLeftColor = color;

            toast.innerHTML = `<i class="fa-solid ${icon}" style="color:${color}; font-size:1.1rem;"></i> <span>${msg}</span>`;
            container.appendChild(toast);

            setTimeout(() => toast.remove(), duration);
        }

        function updateBadges() {
            document.getElementById('cart-badge').innerText = state.cart.reduce((a, b) => a + b.quantity, 0);
            document.getElementById('wishlist-badge').innerText = state.wishlist.length;
            document.getElementById('compare-badge').innerText = state.compareList.length;
        }

        function toggleTheme() {
            const current = document.documentElement.getAttribute('data-theme');
            const next = current === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('theme', next);
            updateThemeIcon();
        }

        function updateThemeIcon() {
            const current = document.documentElement.getAttribute('data-theme');
            const icon = document.getElementById('theme-icon');
            if (icon) icon.className = current === 'dark' ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
        }

        // Flash Sale Countdown Ticker
        setInterval(() => {
            const sBox = document.getElementById('timer-seconds');
            const mBox = document.getElementById('timer-minutes');
            if (!sBox || !mBox) return;

            let sec = parseInt(sBox.innerText) - 1;
            if (sec < 0) {
                sec = 59;
                let min = parseInt(mBox.innerText) - 1;
                if (min < 0) min = 59;
                mBox.innerText = String(min).padStart(2, '0');
            }
            sBox.innerText = String(sec).padStart(2, '0');
        }, 1000);

        // App Initialization
        window.addEventListener('DOMContentLoaded', () => {
            initStorage();
            updateUserNav();
            updateBadges();
            renderHome();
        });
    </script>
</body>
</html>
<!-- For production: connect authentication, API, database, payment gateway and server-side security here. -->
"""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully written index.html to:", file_path)
