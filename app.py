<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>M/S Hossain Machineries & Sanitary - এম/এস হোসেন মেসিনারী অ্যান্ড সেনিটারী</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts: Hind Siliguri -->
    <link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <style>
        body {
            font-family: 'Hind Siliguri', sans-serif;
            background-color: #f3f4f6;
        }
        .bg-teal-dark { background-color: #014a34; }
        .bg-emerald-main { background-color: #00885a; }
        .bg-hotline-card { background-color: #00754e; }
        .hover-bg-hotline:hover { background-color: #006040; }
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    </style>
</head>
<body class="text-gray-800 antialiased min-h-screen flex flex-col relative">

    <!-- Top Location & Notice Bar -->
    <div class="bg-teal-dark text-white text-xs md:text-sm py-2 px-3 sm:px-6 flex flex-col sm:flex-row justify-between items-center gap-1 border-b border-emerald-800">
        <div class="flex items-center gap-1.5 text-emerald-100 text-center sm:text-left">
            <i class="fa-solid fa-location-dot text-emerald-400"></i>
            <span id="top-location">সোনালী ব্যাংক গ্রাউন্ড ফ্লোর, মোল্লাহাট, বাগেরহাট</span>
        </div>
        <div class="flex items-center gap-2 font-mono text-[11px] sm:text-xs">
            <span class="bg-emerald-900/60 px-2 py-0.5 rounded border border-emerald-700/50" id="top-h1"><i class="fa-solid fa-phone text-emerald-400 mr-1"></i>01711-223344</span>
            <span class="bg-emerald-900/60 px-2 py-0.5 rounded border border-emerald-700/50 hidden sm:inline" id="top-h2"><i class="fa-solid fa-phone text-emerald-400 mr-1"></i>01855-667788</span>
            <span class="bg-emerald-900/60 px-2 py-0.5 rounded border border-emerald-700/50 hidden md:inline" id="top-h3"><i class="fa-solid fa-phone text-emerald-400 mr-1"></i>01999-001122</span>
        </div>
    </div>

    <!-- Main Branding Header -->
    <header class="bg-white shadow-sm sticky top-0 z-30">
        <div class="max-w-6xl mx-auto px-4 py-3 flex justify-between items-center">
            <div class="flex items-center gap-3">
                <!-- Secret 10-Tap Trigger Logo -->
                <button id="secret-logo-btn" type="button" class="w-12 h-12 bg-emerald-main text-white font-bold rounded-full flex items-center justify-center text-xl shadow-md active:scale-95 transition-transform border-2 border-emerald-300 cursor-pointer select-none" title="Admin Trigger">
                    MH
                </button>
                <div>
                    <h1 class="text-lg md:text-xl font-bold text-gray-900 leading-tight">M/S Hossain Machineries & Sanitary</h1>
                    <p class="text-xs text-emerald-700 font-semibold">এম/এস হোসেন মেসিনারী অ্যান্ড সেনিটারী</p>
                </div>
            </div>

            <div class="flex items-center gap-2">
                <button onclick="openQRModal()" type="button" class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-700 border border-emerald-200 flex items-center justify-center hover:bg-emerald-100 transition cursor-pointer" title="QR Scanner">
                    <i class="fa-solid fa-qrcode text-lg"></i>
                </button>
                <button id="lang-btn" onclick="toggleLanguage()" type="button" class="px-2.5 py-1.5 rounded-lg bg-gray-100 text-gray-700 text-xs font-bold border border-gray-300 hover:bg-gray-200 cursor-pointer">
                    ENG
                </button>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="bg-emerald-main text-white py-6 px-4 shadow-inner">
        <div class="max-w-4xl mx-auto text-center">
            <div class="inline-flex items-center gap-1.5 bg-emerald-900/40 border border-emerald-300/30 text-emerald-100 px-3 py-1 rounded-full text-xs md:text-sm font-medium mb-3">
                <i class="fa-solid fa-circle-check text-emerald-300"></i>
                <span id="txt-trust">১০০% অরিজিনাল সেনিটারী, কালার পেইন্টস ও মেসিনারী পণ্য</span>
            </div>

            <h2 id="txt-hero-title" class="text-2xl md:text-3xl font-extrabold mb-2 leading-snug">
                সেনিটারী, পেইন্টস ও মেসিনারী সামগ্রীর এক বিশ্বস্ত প্রতিষ্ঠান
            </h2>
            <p id="txt-hero-sub" class="text-xs md:text-sm text-emerald-100 max-w-2xl mx-auto mb-6">
                সোনালী ব্যাংক গ্রাউন্ড ফ্লোর, মোল্লাহাট, বাগেরহাট। কমোড, বেসিন, গিজার, সিঙ্ক, বার্জার ও নিপ্পন পেইন্টস এবং মেসিনারী মালামালের জন্য আজই যোগাযোগ করুন।
            </p>

            <!-- Dynamic Hotline Cards -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 max-w-3xl mx-auto">
                <!-- Sales -->
                <a id="link-h1" href="tel:01711223344" class="bg-hotline-card hover-bg-hotline p-3.5 rounded-2xl border border-emerald-400/30 shadow-md flex items-center justify-between transition group">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-emerald-400/20 flex items-center justify-center text-emerald-200 group-hover:scale-110 transition-transform">
                            <i class="fa-solid fa-phone"></i>
                        </div>
                        <div class="text-left">
                            <span class="text-[11px] text-emerald-200 block uppercase font-medium" id="lbl-h1">হটলাইন ১ (বিক্রয়)</span>
                            <span class="text-base font-bold font-mono tracking-wide text-white" id="val-h1">01711-223344</span>
                        </div>
                    </div>
                    <i class="fa-solid fa-chevron-right text-xs text-emerald-300"></i>
                </a>

                <!-- Manager -->
                <a id="link-h2" href="tel:01855667788" class="bg-hotline-card hover-bg-hotline p-3.5 rounded-2xl border border-emerald-400/30 shadow-md flex items-center justify-between transition group">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-emerald-400/20 flex items-center justify-center text-emerald-200 group-hover:scale-110 transition-transform">
                            <i class="fa-solid fa-user-tie"></i>
                        </div>
                        <div class="text-left">
                            <span class="text-[11px] text-emerald-200 block uppercase font-medium" id="lbl-h2">হটলাইন ২ (ম্যানেজার)</span>
                            <span class="text-base font-bold font-mono tracking-wide text-white" id="val-h2">01855-667788</span>
                        </div>
                    </div>
                    <i class="fa-solid fa-chevron-right text-xs text-emerald-300"></i>
                </a>

                <!-- Support -->
                <a id="link-h3" href="tel:01999001122" class="bg-hotline-card hover-bg-hotline p-3.5 rounded-2xl border border-emerald-400/30 shadow-md flex items-center justify-between transition group">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-emerald-400/20 flex items-center justify-center text-emerald-200 group-hover:scale-110 transition-transform">
                            <i class="fa-solid fa-headset"></i>
                        </div>
                        <div class="text-left">
                            <span class="text-[11px] text-emerald-200 block uppercase font-medium" id="lbl-h3">হটলাইন ৩ (সাপোর্ট)</span>
                            <span class="text-base font-bold font-mono tracking-wide text-white" id="val-h3">01999-001122</span>
                        </div>
                    </div>
                    <i class="fa-solid fa-chevron-right text-xs text-emerald-300"></i>
                </a>
            </div>
        </div>
    </section>
    
    <!-- Search & Filters Container -->
    <main class="max-w-6xl mx-auto px-4 py-6 flex-grow">
        <!-- Search Input -->
        <div class="relative max-w-xl mx-auto mb-4">
            <i class="fa-solid fa-magnifying-glass absolute left-4 top-1/2 -translate-y-1/2 text-gray-400"></i>
            <input type="text" id="search-input" onkeyup="filterProducts()" placeholder="পণ্যের নাম বা মডেল খুঁজুন..." 
                class="w-full pl-11 pr-4 py-3 rounded-xl border border-gray-200 shadow-sm focus:outline-none focus:ring-2 focus:ring-emerald-600 bg-white text-sm">
        </div>

        <!-- Scrollable Category Badges -->
        <div class="flex items-center gap-2 overflow-x-auto no-scrollbar pb-3 mb-6">
            <button onclick="setCategory('all', event)" type="button" class="cat-btn bg-emerald-main text-white text-xs font-semibold px-4 py-2 rounded-full shadow-sm whitespace-nowrap transition cursor-pointer">সব পণ্য</button>
            <button onclick="setCategory('sanitary', event)" type="button" class="cat-btn bg-white text-gray-700 text-xs font-semibold px-4 py-2 rounded-full border border-gray-200 shadow-sm whitespace-nowrap hover:bg-gray-50 transition cursor-pointer">🚽 সেনিটারী সামগ্রী</button>
            <button onclick="setCategory('paint', event)" type="button" class="cat-btn bg-white text-gray-700 text-xs font-semibold px-4 py-2 rounded-full border border-gray-200 shadow-sm whitespace-nowrap hover:bg-gray-50 transition cursor-pointer">🎨 রং ও পেইন্ট</button>
            <button onclick="setCategory('berger', event)" type="button" class="cat-btn bg-white text-gray-700 text-xs font-semibold px-4 py-2 rounded-full border border-gray-200 shadow-sm whitespace-nowrap hover:bg-gray-50 transition cursor-pointer">Berger Paints</button>
            <button onclick="setCategory('nippon', event)" type="button" class="cat-btn bg-white text-gray-700 text-xs font-semibold px-4 py-2 rounded-full border border-gray-200 shadow-sm whitespace-nowrap hover:bg-gray-50 transition cursor-pointer">Nippon Paint</button>
            <button onclick="setCategory('pump', event)" type="button" class="cat-btn bg-white text-gray-700 text-xs font-semibold px-4 py-2 rounded-full border border-gray-200 shadow-sm whitespace-nowrap hover:bg-gray-50 transition cursor-pointer">🚰 ওয়াটার পাম্প</button>
            <button onclick="setCategory('motor', event)" type="button" class="cat-btn bg-white text-gray-700 text-xs font-semibold px-4 py-2 rounded-full border border-gray-200 shadow-sm whitespace-nowrap hover:bg-gray-50 transition cursor-pointer">⚡ ইলেকট্রিক মোটর</button>
            <button onclick="setCategory('fittings', event)" type="button" class="cat-btn bg-white text-gray-700 text-xs font-semibold px-4 py-2 rounded-full border border-gray-200 shadow-sm whitespace-nowrap hover:bg-gray-50 transition cursor-pointer">🔧 পাইপ ও ফিটিংস</button>
        </div>

        <!-- Product Display Grid -->
        <div id="product-grid" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3 md:gap-4">
            <!-- Dynamic JavaScript Rendered Content -->
        </div>
    </main>

    <!-- Floating Admin Add Product Button (Visible only when logged in) -->
    <button id="floating-add-btn" onclick="openAddProductModal()" type="button" class="fixed bottom-6 right-6 w-14 h-14 bg-emerald-600 hover:bg-emerald-700 text-white rounded-full shadow-2xl flex items-center justify-center text-2xl z-40 transition-transform active:scale-90 hidden cursor-pointer border-2 border-white" title="নতুন পণ্য যোগ করুন">
        <i class="fa-solid fa-plus"></i>
    </button>

    <!-- Footer -->
    <footer class="bg-teal-dark text-emerald-100 text-xs py-6 mt-8 border-t border-emerald-900">
        <div class="max-w-6xl mx-auto px-4 text-center space-y-2">
            <p class="font-bold text-white text-sm">এম/এস হোসেন মেসিনারী অ্যান্ড সেনিটারী</p>
            <p>সোনালী ব্যাংক গ্রাউন্ড ফ্লোর, মোল্লাহাট, বাগেরহাট</p>
            <p class="text-emerald-400 font-mono">জরুরি প্রয়োজনে: <span id="foot-h1">01711-223344</span></p>
            <p class="text-[10px] text-emerald-300/70 pt-2 border-t border-emerald-900/60">© 2026 M/S Hossain Machineries & Sanitary. All rights reserved.</p>
        </div>
    </footer>

    <!-- Secret Admin Login Modal -->
    <div id="admin-modal" class="fixed inset-0 bg-black/60 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
        <div class="bg-white w-full max-w-md rounded-2xl p-5 shadow-2xl relative border border-gray-100">
            <button onclick="closeAdminModal()" type="button" class="absolute right-4 top-4 text-gray-400 hover:text-gray-600 cursor-pointer">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>

            <!-- Login View -->
            <div id="admin-login-view" class="space-y-4">
                <div class="text-center">
                    <div class="w-12 h-12 bg-emerald-100 text-emerald-700 rounded-full flex items-center justify-center mx-auto mb-2 text-xl font-bold">
                        <i class="fa-solid fa-user-shield"></i>
                    </div>
                    <h3 class="text-lg font-bold text-gray-800">এডমিন লগইন প্যানেল</h3>
                    <p class="text-xs text-gray-500">গোপন একসেস সিস্টেমে স্বাগতম</p>
                </div>
                <div>
                    <input type="password" id="admin-pass" placeholder="এডমিন পাসওয়ার্ড দিন" class="w-full px-4 py-2.5 rounded-xl border border-gray-300 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-600">
                </div>
                <button onclick="verifyAdmin()" type="button" class="w-full py-2.5 bg-emerald-main text-white rounded-xl text-sm font-bold shadow-sm hover:bg-emerald-700 transition cursor-pointer">
                    লগইন করুন
                </button>
            </div>

            <!-- Panel View (Unlocked Settings) -->
            <div id="admin-panel-view" class="space-y-4 hidden">
                <div class="flex items-center justify-between border-b pb-2">
                    <h3 class="font-bold text-gray-800 text-sm"><i class="fa-solid fa-sliders text-emerald-600 mr-1.5"></i>এডমিন সেটিংস প্যানেল</h3>
                    <button onclick="adminLogout()" type="button" class="text-xs text-red-600 font-semibold hover:underline">লগআউট</button>
                </div>

                <!-- Update Hotlines -->
                <div class="space-y-2 text-xs">
                    <label class="font-bold text-gray-700 block">হটলাইন ১ (বিক্রয়):</label>
                    <input type="text" id="edit-h1" class="w-full px-3 py-1.5 border rounded-lg">

                    <label class="font-bold text-gray-700 block">হটলাইন ২ (ম্যানেজার):</label>
                    <input type="text" id="edit-h2" class="w-full px-3 py-1.5 border rounded-lg">

                    <label class="font-bold text-gray-700 block">হটলাইন ৩ (সাপোর্ট):</label>
                    <input type="text" id="edit-h3" class="w-full px-3 py-1.5 border rounded-lg">
                </div>

                <div class="pt-2 flex gap-2">
                    <button onclick="saveHotlines()" type="button" class="flex-1 py-2 bg-emerald-main text-white rounded-lg text-xs font-bold cursor-pointer">হটলাইন সেভ করুন</button>
                    <button onclick="closeAdminModal()" type="button" class="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg text-xs font-bold cursor-pointer">বন্ধ করুন</button>
                </div>
            </div>
        </div>
    </div>
     <!-- Add Product Modal (For Admin) -->
    <div id="add-product-modal" class="fixed inset-0 bg-black/70 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
        <div class="bg-white w-full max-w-lg rounded-2xl p-6 shadow-2xl relative max-h-[90vh] overflow-y-auto">
            <button onclick="closeAddProductModal()" type="button" class="absolute right-4 top-4 text-gray-400 hover:text-gray-600 cursor-pointer">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>

            <h3 class="text-base font-bold text-gray-800 mb-4 flex items-center gap-2 border-b pb-2">
                <i class="fa-solid fa-circle-plus text-emerald-600"></i> নতুন পণ্য যোগ করুন (এডমিন প্যানেল)
            </h3>

            <form id="new-product-form" onsubmit="handleAddNewProduct(event)" class="space-y-3.5 text-xs">
                <!-- SKU & Barcode Scanner Trigger -->
                <div>
                    <label class="font-bold text-gray-700 block mb-1">SKU / বারকোড কোড:</label>
                    <div class="flex gap-2">
                        <input type="text" id="new-sku" required placeholder="উদা: SAN-C02" class="w-full px-3 py-2 border rounded-xl font-mono uppercase">
                        <button type="button" onclick="openScannerModal()" class="px-3 bg-emerald-50 text-emerald-700 border border-emerald-200 rounded-xl hover:bg-emerald-100 flex items-center gap-1 font-bold" title="স্ক্যান বারকোড">
                            <i class="fa-solid fa-camera"></i> স্ক্যান
                        </button>
                    </div>
                </div>

                <!-- Product Name Bengali -->
                <div>
                    <label class="font-bold text-gray-700 block mb-1">পণ্যের নাম (বাংলা):</label>
                    <input type="text" id="new-title-bn" required placeholder="উদা: ইম্পোর্টেড ওয়ান পিস কমোড" class="w-full px-3 py-2 border rounded-xl">
                </div>

                <!-- Product Name English -->
                <div>
                    <label class="font-bold text-gray-700 block mb-1">পণ্যের নাম (ইংরেজি):</label>
                    <input type="text" id="new-title-en" required placeholder="উদা: Imported One Piece Commode" class="w-full px-3 py-2 border rounded-xl">
                </div>

                <!-- Category & Brand -->
                <div class="grid grid-cols-2 gap-2">
                    <div>
                        <label class="font-bold text-gray-700 block mb-1">ক্যাটাগরি:</label>
                        <select id="new-category" class="w-full px-3 py-2 border rounded-xl bg-white">
                            <option value="sanitary">🚽 সেনিটারী সামগ্রী</option>
                            <option value="paint">🎨 রং ও পেইন্ট</option>
                            <option value="pump">🚰 ওয়াটার পাম্প</option>
                            <option value="motor">⚡ ইলেকট্রিক মোটর</option>
                            <option value="fittings">🔧 পাইপ ও ফিটিংস</option>
                        </select>
                    </div>
                    <div>
                        <label class="font-bold text-gray-700 block mb-1">ব্র্যান্ড / সাব-টাইপ:</label>
                        <select id="new-brand" class="w-full px-3 py-2 border rounded-xl bg-white">
                            <option value="sanitary">জেনারেল সেনিটারী</option>
                            <option value="berger">Berger Paint</option>
                            <option value="nippon">Nippon Paint</option>
                            <option value="gazi">Gazi Pump</option>
                            <option value="fittings">Fittings & Pipes</option>
                            <option value="other">অন্যান্য</option>
                        </select>
                    </div>
                </div>

                <!-- Price & Unit -->
                <div class="grid grid-cols-2 gap-2">
                    <div>
                        <label class="font-bold text-gray-700 block mb-1">মূল্য (টাকা ৳):</label>
                        <input type="number" id="new-price" required placeholder="উদা: 7500" class="w-full px-3 py-2 border rounded-xl font-mono">
                    </div>
                    <div>
                        <label class="font-bold text-gray-700 block mb-1">ইউনিট / পিস:</label>
                        <input type="text" id="new-unit" required value="১ সেট" class="w-full px-3 py-2 border rounded-xl">
                    </div>
                </div>

                <!-- Badge & Image Upload -->
                <div class="grid grid-cols-2 gap-2">
                    <div>
                        <label class="font-bold text-gray-700 block mb-1">বিশেষ ব্যাজ (ঐচ্ছিক):</label>
                        <input type="text" id="new-badge" placeholder="উদা: New Model" class="w-full px-3 py-2 border rounded-xl">
                    </div>
                    <div>
                        <label class="font-bold text-gray-700 block mb-1">পণ্যের ছবি আপলোড:</label>
                        <input type="file" id="new-image-file" accept="image/*" onchange="previewUploadedImage(event)" class="w-full text-[11px] file:mr-2 file:py-1 file:px-2 file:rounded-lg file:border-0 file:bg-emerald-50 file:text-emerald-700">
                    </div>
                </div>

                <!-- Image Preview Box -->
                <div id="image-preview-container" class="hidden text-center">
                    <img id="uploaded-img-preview" src="" alt="Preview" class="w-20 h-20 object-cover mx-auto rounded-lg border">
                </div>

                <div class="pt-2 flex gap-2">
                    <button type="submit" class="flex-1 py-2.5 bg-emerald-main text-white rounded-xl font-bold shadow-md hover:bg-emerald-700 cursor-pointer">পণ্য সেভ ও যুক্ত করুন</button>
                    <button type="button" onclick="closeAddProductModal()" class="px-4 py-2.5 bg-gray-200 text-gray-700 rounded-xl font-bold cursor-pointer">বাতিল</button>
                </div>
            </form>
        </div>
    </div>

    <!-- Barcode / QR Scanner Simulation Modal -->
    <div id="scanner-modal" class="fixed inset-0 bg-black/80 z-60 flex items-center justify-center p-4 hidden">
        <div class="bg-white w-full max-w-sm rounded-2xl p-5 text-center relative shadow-2xl">
            <button onclick="closeScannerModal()" type="button" class="absolute right-4 top-4 text-gray-400 hover:text-gray-600 cursor-pointer">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>
            <h3 class="font-bold text-gray-800 mb-3"><i class="fa-solid fa-barcode text-emerald-600 mr-2"></i>বারকোড স্ক্যানার</h3>
            
            <div class="w-48 h-48 bg-gray-900 rounded-xl mx-auto mb-4 relative flex items-center justify-center overflow-hidden border-2 border-emerald-500">
                <div class="w-full h-0.5 bg-emerald-400 absolute animate-pulse shadow-[0_0_15px_#00ff9d]"></div>
                <i class="fa-solid fa-camera text-gray-500 text-3xl"></i>
            </div>

            <p class="text-xs text-gray-500 mb-4">প্যাকেটের বারকোড ক্যামেরার সামনে ধরুন</p>
            <button onclick="simulateScan()" type="button" class="w-full py-2.5 bg-emerald-main text-white text-xs font-bold rounded-xl hover:bg-emerald-700 cursor-pointer">
                কোড স্ক্যান সম্পন্ন করুন (Demo)
            </button>
        </div>
    </div>

    <!-- QR Modal Controls (Top Header) -->
    <div id="qr-modal" class="fixed inset-0 bg-black/70 z-50 flex items-center justify-center p-4 hidden">
        <div class="bg-white w-full max-w-sm rounded-2xl p-5 text-center relative shadow-2xl">
            <button onclick="closeQRModal()" type="button" class="absolute right-4 top-4 text-gray-400 hover:text-gray-600 cursor-pointer">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>
            <h3 class="font-bold text-gray-800 mb-3"><i class="fa-solid fa-qrcode text-emerald-600 mr-2"></i>প্রোডাক্ট কিউআর স্ক্যান</h3>
            
            <div class="w-48 h-48 bg-gray-900 rounded-xl mx-auto mb-4 relative flex items-center justify-center overflow-hidden border-2 border-emerald-500">
                <div class="w-full h-0.5 bg-emerald-400 absolute animate-pulse shadow-[0_0_15px_#00ff9d]"></div>
                <i class="fa-solid fa-camera text-gray-500 text-3xl"></i>
            </div>

            <p class="text-xs text-gray-500 mb-4">প্যাকেটের বা পণ্যের বারকোড ক্যামেরা এর সামনে রাখুন</p>
            <button onclick="closeQRModal()" type="button" class="w-full py-2 bg-gray-100 text-gray-700 text-xs font-bold rounded-lg hover:bg-gray-200 cursor-pointer">
                স্কিপ / ম্যানুয়ালি লিখুন
            </button>
        </div>
    </div>

    <!-- Application Script Logic -->
    <script>
        // Initial Product Catalog
        let products = [
            {
                id: 's1',
                sku: 'SAN-C01',
                title_bn: 'প্রিমিয়াম গ্লাসি সিরামিক হাই কমোড (সফট ক্লোজ)',
                title_en: 'Premium Ceramic High Commode',
                brand: 'sanitary',
                category: 'sanitary',
                price: 8500,
                unit: '১ সেট',
                badge: 'Soft Cover',
                image: 'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=400&q=80'
            },
            {
                id: 's2',
                sku: 'SAN-G01',
                title_bn: '৩০ লিটার অটোমেটিক ফাস্ট হিটিং গিজার',
                title_en: '30L Fast Heating Electric Geyser',
                brand: 'sanitary',
                category: 'sanitary',
                price: 9800,
                unit: '১ সেট',
                badge: 'Safety Valve',
                image: 'https://images.unsplash.com/photo-1542013936693-884638332954?w=400&q=80'
            },
            {
                id: 's3',
                sku: 'SAN-K01',
                title_bn: 'স্টেইনলেস স্টিল ডাবল সিঙ্ক (রানিং ট্রে সহ)',
                title_en: 'Stainless Steel Double Kitchen Sink',
                brand: 'sanitary',
                category: 'sanitary',
                price: 5200,
                unit: '১ পিস',
                badge: '304 Grade SS',
                image: 'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=400&q=80'
            },
            {
                id: 's4',
                sku: 'SAN-B01',
                title_bn: 'আধুনিক পেডিস্টাল কাউন্টার ওয়াশ বেসিন',
                title_en: 'Pedestal Counter Wash Basin',
                brand: 'sanitary',
                category: 'sanitary',
                price: 4200,
                unit: '১ সেট',
                badge: 'Stain Proof',
                image: 'https://images.unsplash.com/photo-1620626011761-996317b8d101?w=400&q=80'
            },
            {
                id: 's5',
                sku: 'SAN-T01',
                title_bn: 'ব্রাস বডি ব্রাঞ্চ হেভি এসএস বেসিন ট্যাপ',
                title_en: 'Brass Body SS Basin Tap',
                brand: 'sanitary',
                category: 'sanitary',
                price: 1350,
                unit: '১ পিস',
                badge: 'Chrome Plated',
                image: 'https://images.unsplash.com/photo-1585704032915-c3400ca199e7?w=400&q=80'
            },
            {
                id: 's6',
                sku: 'SAN-SH1',
                title_bn: 'মাল্টি-ফাংশন রেইন শাওয়ার সেট উইথ মিক্সার',
                title_en: 'Rain Shower Set with Mixer',
                brand: 'sanitary',
                category: 'sanitary',
                price: 4500,
                unit: '১ সেট',
                badge: 'Hot & Cold',
                image: 'https://images.unsplash.com/photo-1604014237800-1c9102c219da?w=400&q=80'
            },
            {
                id: 'p1',
                sku: 'PNT-B01',
                title_bn: 'বার্জার ওয়েদারকোট স্মুথ এক্সটেরিয়র পেইন্ট',
                title_en: 'Berger WeatherCoat Smooth Paint',
                brand: 'berger',
                category: 'paint',
                price: 4800,
                unit: '১০ লিটার',
                swatches: ['#d92b2b', '#1e5fcc', '#ffffff', '#ffd700'],
                badge: 'UV Weather Guard',
                image: 'https://images.unsplash.com/photo-1562259949-e8e7689d7828?w=400&q=80'
            },
            {
                id: 'p2',
                sku: 'PNT-N01',
                title_bn: 'নিপ্পন অডার-লেস অল-ইন-১ ইন্টেরিয়র',
                title_en: 'Nippon Odour-less All-in-1',
                brand: 'nippon',
                category: 'paint',
                price: 3600,
                unit: '৫ লিটার',
                swatches: ['#00885a', '#f3f4f6', '#d2b48c', '#800020'],
                badge: 'Eco Friendly',
                image: 'https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=400&q=80'
            },
            {
                id: 'm1',
                sku: 'MAC-W15',
                title_bn: '১.৫ এইচপি গাজি কপার ওয়াটার পাম্প',
                title_en: '1.5 HP Gazi Water Pump',
                brand: 'gazi',
                category: 'pump',
                price: 8500,
                unit: '১ পিস',
                badge: 'High Suction',
                image: 'https://images.unsplash.com/photo-1616401784845-180882ba9ba8?w=400&q=80'
            },
            {
                id: 'f1',
                sku: 'FIT-P01',
                title_bn: 'হেভি ইউপিভিসি ৩ ইঞ্চি পাইপ (১০ ফুট)',
                title_en: 'uPVC 3 inch Pipe (10 ft)',
                brand: 'fittings',
                category: 'fittings',
                price: 650,
                unit: '১ পিস',
                badge: 'Pressure Proof',
                image: 'https://images.unsplash.com/photo-1542013936693-884638332954?w=400&q=80'
            }
        ];

        let activeCategory = 'all';
        let currentLang = 'bn';
        let tapCount = 0;
        let tapTimer = null;
        let tempUploadedImage = '';

        let hotlines = {
            h1: '01711-223344',
            h2: '01855-667788',
            h3: '01999-001122'
        };

        // Check persistent login state on load
        window.addEventListener('DOMContentLoaded', () => {
            const isAdminLoggedIn = localStorage.getItem('hossain_admin_logged') === 'true';
            if (isAdminLoggedIn) {
                document.getElementById('floating-add-btn').classList.remove('hidden');
            }
            renderProducts(products);
        });

        // Render Products Grid
        function renderProducts(items) {
            const grid = document.getElementById('product-grid');
            grid.innerHTML = '';

            if (items.length === 0) {
                grid.innerHTML = `<div class="col-span-full text-center py-12 text-gray-500 text-sm">কোনো পণ্য পাওয়া যায়নি</div>`;
                return;
            }

            items.forEach(p => {
                const title = currentLang === 'bn' ? p.title_bn : p.title_en;
                
                let swatchesHtml = '';
                if (p.swatches && p.swatches.length > 0) {
                    swatchesHtml = `<div class="flex items-center gap-1 my-1.5">
                        <span class="text-[10px] text-gray-400 mr-1">শেড:</span>
                        ${p.swatches.map(c => `<span class="w-3.5 h-3.5 rounded-full border border-gray-300 shadow-2xs" style="background-color: ${c}"></span>`).join('')}
                    </div>`;
                }

                const card = document.createElement('div');
                card.className = 'bg-white rounded-2xl p-2.5 md:p-3 border border-gray-100 shadow-sm flex flex-col justify-between hover:shadow-md transition';
                card.innerHTML = `
                    <div>
                        <div class="relative rounded-xl overflow-hidden bg-gray-100 mb-2 aspect-square">
                            <img src="${p.image}" alt="${title}" class="w-full h-full object-cover" loading="lazy">
                            <span class="absolute top-1.5 left-1.5 bg-black/60 backdrop-blur-xs text-white text-[9px] px-2 py-0.5 rounded-full font-mono">${p.sku}</span>
                            ${p.badge ? `<span class="absolute bottom-1.5 right-1.5 bg-emerald-700 text-white text-[9px] px-2 py-0.5 rounded font-semibold">${p.badge}</span>` : ''}
                        </div>
                        <h4 class="font-bold text-gray-800 text-xs md:text-sm line-clamp-2 leading-tight">${title}</h4>
                        ${swatchesHtml}
                    </div>
                    <div class="mt-3 pt-2 border-t border-gray-100 flex items-center justify-between">
                        <div>
                            <span class="text-emerald-700 font-extrabold text-xs md:text-base font-mono">৳ ${p.price.toLocaleString()}</span>
                            <span class="text-[10px] text-gray-400 block">${p.unit}</span>
                        </div>
                        <a href="tel:${hotlines.h1.replace(/[^0-9]/g, '')}" class="bg-emerald-main hover:bg-emerald-700 text-white p-2 rounded-xl text-xs flex items-center gap-1 font-bold shadow-xs transition">
                            <i class="fa-solid fa-phone"></i>
                            <span class="hidden sm:inline">কল করুন</span>
                        </a>
                    </div>
                `;
                grid.appendChild(card);
            });
        } 
      // Category Filter Setup
        function setCategory(cat, e) {
            activeCategory = cat;
            document.querySelectorAll('.cat-btn').forEach(btn => {
                btn.classList.remove('bg-emerald-main', 'text-white');
                btn.classList.add('bg-white', 'text-gray-700');
            });
            if (e && e.currentTarget) {
                e.currentTarget.classList.remove('bg-white', 'text-gray-700');
                e.currentTarget.classList.add('bg-emerald-main', 'text-white');
            }
            filterProducts();
        }

        // Filter Function
        function filterProducts() {
            const query = document.getElementById('search-input').value.toLowerCase();
            const filtered = products.filter(p => {
                const matchesCat = (activeCategory === 'all') ||
                                  (activeCategory === 'sanitary' && p.category === 'sanitary') ||
                                  (activeCategory === 'paint' && p.category === 'paint') ||
                                  (activeCategory === 'berger' && p.brand === 'berger') ||
                                  (activeCategory === 'nippon' && p.brand === 'nippon') ||
                                  (p.category === activeCategory);
                const matchesSearch = p.title_bn.toLowerCase().includes(query) ||
                                      p.title_en.toLowerCase().includes(query) ||
                                      p.sku.toLowerCase().includes(query);
                return matchesCat && matchesSearch;
            });
            renderProducts(filtered);
        }

        // Hidden 10-Tap Secret Trigger Logic
        document.getElementById('secret-logo-btn').addEventListener('click', () => {
            tapCount++;
            clearTimeout(tapTimer);
            tapTimer = setTimeout(() => { tapCount = 0; }, 3000);

            if (tapCount >= 10) {
                tapCount = 0;
                const isAdminLoggedIn = localStorage.getItem('hossain_admin_logged') === 'true';
                document.getElementById('admin-modal').classList.remove('hidden');
                
                if (isAdminLoggedIn) {
                    document.getElementById('admin-login-view').classList.add('hidden');
                    document.getElementById('admin-panel-view').classList.remove('hidden');
                    document.getElementById('edit-h1').value = hotlines.h1;
                    document.getElementById('edit-h2').value = hotlines.h2;
                    document.getElementById('edit-h3').value = hotlines.h3;
                } else {
                    document.getElementById('admin-login-view').classList.remove('hidden');
                    document.getElementById('admin-panel-view').classList.add('hidden');
                }
            }
        });

        // Admin Auth & Persistent Login
        function verifyAdmin() {
            const pass = document.getElementById('admin-pass').value;
            if (pass === 'MS221109#@senetery') {
                localStorage.setItem('hossain_admin_logged', 'true');
                document.getElementById('floating-add-btn').classList.remove('hidden');
                document.getElementById('admin-login-view').classList.add('hidden');
                document.getElementById('admin-panel-view').classList.remove('hidden');
                document.getElementById('edit-h1').value = hotlines.h1;
                document.getElementById('edit-h2').value = hotlines.h2;
                document.getElementById('edit-h3').value = hotlines.h3;
            } else {
                alert('ভুল পাসওয়ার্ড!');
            }
        }

        function adminLogout() {
            localStorage.removeItem('hossain_admin_logged');
            document.getElementById('floating-add-btn').classList.add('hidden');
            closeAdminModal();
            alert('এডমিন লগআউট সফল হয়েছে!');
        }

        function saveHotlines() {
            hotlines.h1 = document.getElementById('edit-h1').value;
            hotlines.h2 = document.getElementById('edit-h2').value;
            hotlines.h3 = document.getElementById('edit-h3').value;

            document.getElementById('val-h1').innerText = hotlines.h1;
            document.getElementById('val-h2').innerText = hotlines.h2;
            document.getElementById('val-h3').innerText = hotlines.h3;
            
            document.getElementById('link-h1').href = `tel:${hotlines.h1.replace(/[^0-9]/g, '')}`;
            document.getElementById('link-h2').href = `tel:${hotlines.h2.replace(/[^0-9]/g, '')}`;
            document.getElementById('link-h3').href = `tel:${hotlines.h3.replace(/[^0-9]/g, '')}`;

            document.getElementById('top-h1').innerHTML = `<i class="fa-solid fa-phone text-emerald-400 mr-1"></i>${hotlines.h1}`;
            document.getElementById('top-h2').innerHTML = `<i class="fa-solid fa-phone text-emerald-400 mr-1"></i>${hotlines.h2}`;
            document.getElementById('top-h3').innerHTML = `<i class="fa-solid fa-phone text-emerald-400 mr-1"></i>${hotlines.h3}`;
            document.getElementById('foot-h1').innerText = hotlines.h1;

            alert('হটলাইন নম্বরসমূহ সফলভাবে আপডেট করা হয়েছে!');
            closeAdminModal();
            renderProducts(products);
        }

        function closeAdminModal() {
            document.getElementById('admin-modal').classList.add('hidden');
            document.getElementById('admin-pass').value = '';
        }

        // Add Product Modal Controls
        function openAddProductModal() {
            document.getElementById('add-product-modal').classList.remove('hidden');
        }

        function closeAddProductModal() {
            document.getElementById('add-product-modal').classList.add('hidden');
            document.getElementById('new-product-form').reset();
            document.getElementById('image-preview-container').classList.add('hidden');
            tempUploadedImage = '';
        }

        // Image File Preview Handling
        function previewUploadedImage(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    tempUploadedImage = e.target.result;
                    document.getElementById('uploaded-img-preview').src = tempUploadedImage;
                    document.getElementById('image-preview-container').classList.remove('hidden');
                }
                reader.readAsDataURL(file);
            }
        }

        // Barcode Scanner Modal Controls
        function openScannerModal() { document.getElementById('scanner-modal').classList.remove('hidden'); }
        function closeScannerModal() { document.getElementById('scanner-modal').classList.add('hidden'); }
        function simulateScan() {
            const randomCode = 'BAR-' + Math.floor(1000 + Math.random() * 9000);
            document.getElementById('new-sku').value = randomCode;
            closeScannerModal();
        }

        // Handle Form Submission for New Product
        function handleAddNewProduct(e) {
            e.preventDefault();
            const sku = document.getElementById('new-sku').value;
            const titleBn = document.getElementById('new-title-bn').value;
            const titleEn = document.getElementById('new-title-en').value;
            const category = document.getElementById('new-category').value;
            const brand = document.getElementById('new-brand').value;
            const price = parseFloat(document.getElementById('new-price').value);
            const unit = document.getElementById('new-unit').value;
            const badge = document.getElementById('new-badge').value;
            
            const image = tempUploadedImage || 'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=400&q=80';

            const newProduct = {
                id: 'prod_' + Date.now(),
                sku: sku,
                title_bn: titleBn,
                title_en: titleEn,
                category: category,
                brand: brand,
                price: price,
                unit: unit,
                badge: badge,
                image: image
            };

            products.unshift(newProduct);
            filterProducts();
            closeAddProductModal();
            alert('নতুন পণ্য সফলভাবে ক্যাটালগে যুক্ত করা হয়েছে!');
        }

        // QR Modal Controls
        function openQRModal() { document.getElementById('qr-modal').classList.remove('hidden'); }
        function closeQRModal() { document.getElementById('qr-modal').classList.add('hidden'); }

        // Language Switcher Toggle
        function toggleLanguage() {
            currentLang = currentLang === 'bn' ? 'en' : 'bn';
            document.getElementById('lang-btn').innerText = currentLang === 'bn' ? 'ENG' : 'বাংলা';
            renderProducts(products);
        }
    </script>
</body>
</html>
