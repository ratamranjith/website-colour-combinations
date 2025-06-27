from pathlib import Path

# Step 1: Define color combinations
bg_colors = [
    "bg-white", "bg-gray-900", "bg-blue-900", "bg-black", "bg-yellow-50", "bg-cyan-500", "bg-pink-50", "bg-zinc-900",
    "bg-gray-800", "bg-rose-100", "bg-sky-900", "bg-amber-900", "bg-lime-50", "bg-teal-900", "bg-yellow-400", "bg-neutral-900",
    "bg-fuchsia-100", "bg-indigo-950", "bg-emerald-800", "bg-slate-900", "bg-orange-100", "bg-cyan-50", "bg-purple-900",
    "bg-red-900", "bg-blue-50", "bg-gray-700", "bg-yellow-900", "bg-green-100", "bg-purple-500", "bg-slate-50", "bg-gray-100",
    "bg-teal-400", "bg-indigo-600", "bg-blue-800", "bg-emerald-900", "bg-rose-50", "bg-cyan-900", "bg-pink-700", "bg-violet-900",
    "bg-stone-800", "bg-green-800", "bg-orange-900", "bg-red-800", "bg-purple-800", "bg-yellow-800", "bg-fuchsia-900", "bg-blue-700",
    "bg-lime-900", "bg-amber-800"
]

text_colors = [
    "text-red", "text-white", "text-cyan-300", "text-emerald-400", "text-yellow-900", "text-white", "text-pink-800", "text-fuchsia-400",
    "text-white", "text-rose-900", "text-sky-300", "text-amber-200", "text-lime-900", "text-teal-200", "text-white", "text-lime-400",
    "text-fuchsia-800", "text-indigo-200", "text-white", "text-orange-300", "text-orange-800", "text-cyan-900", "text-pink-300",
    "text-red-200", "text-blue-900", "text-white", "text-yellow-100", "text-green-900", "text-white", "text-slate-900", "text-gray-800",
    "text-white", "text-yellow-300", "text-cyan-200", "text-emerald-300", "text-rose-700", "text-cyan-50", "text-white", "text-pink-100",
    "text-stone-200", "text-lime-300", "text-orange-100", "text-red-100", "text-pink-100", "text-yellow-300", "text-white", "text-white",
    "text-lime-200", "text-amber-100"
]

# Step 2: Generate combos
combinations = list(zip(bg_colors, text_colors))

# Add gradient combinations
gradients = [
    ("bg-gradient-to-r from-indigo-900 to-purple-800", "text-white"),
    ("bg-gradient-to-r from-cyan-500 to-blue-500", "text-white"),
    ("bg-gradient-to-br from-gray-800 via-purple-900 to-violet-600", "text-white"),
    ("bg-gradient-to-r from-yellow-400 via-red-500 to-pink-500", "text-white"),
    ("bg-gradient-to-tl from-gray-700 via-gray-900 to-black", "text-white"),
    ("bg-gradient-to-r from-purple-500 to-pink-500", "text-white"),
    ("bg-gradient-to-br from-teal-400 to-blue-500", "text-white"),
    ("bg-gradient-to-tr from-pink-500 via-red-500 to-yellow-500", "text-white"),
    ("bg-gradient-to-b from-blue-600 to-indigo-900", "text-white"),
    ("bg-gradient-to-r from-green-400 via-blue-500 to-purple-600", "text-white"),
    ("bg-gradient-to-l from-pink-300 via-purple-300 to-indigo-400", "text-white"),
    ("bg-gradient-to-br from-slate-900 via-gray-800 to-black", "text-white"),
    ("bg-gradient-to-tr from-lime-400 via-green-500 to-emerald-600", "text-black"),
    ("bg-gradient-to-r from-yellow-200 via-yellow-400 to-yellow-700", "text-black"),
    ("bg-gradient-to-r from-red-200 via-red-400 to-red-600", "text-white"),
    ("bg-gradient-to-bl from-cyan-400 via-cyan-600 to-blue-700", "text-white"),
    ("bg-gradient-to-r from-teal-200 via-teal-400 to-teal-600", "text-black"),
    ("bg-gradient-to-br from-orange-300 via-red-300 to-pink-400", "text-white"),
    ("bg-gradient-to-tr from-fuchsia-400 via-pink-500 to-rose-500", "text-white"),
    ("bg-gradient-to-br from-sky-300 via-sky-500 to-indigo-500", "text-white"),
    ("bg-gradient-to-t from-zinc-700 via-gray-900 to-black", "text-white"),
    ("bg-gradient-to-br from-blue-100 via-blue-300 to-blue-500", "text-blue-900"),
    ("bg-gradient-to-r from-gray-100 via-gray-300 to-gray-500", "text-gray-900"),
    ("bg-gradient-to-r from-green-100 via-emerald-300 to-green-500", "text-green-900"),
    ("bg-gradient-to-tr from-rose-100 via-pink-200 to-fuchsia-300", "text-pink-900"),
    ("bg-gradient-to-br from-indigo-100 via-blue-300 to-indigo-400", "text-indigo-900"),
    ("bg-gradient-to-r from-purple-100 via-violet-200 to-purple-400", "text-purple-900"),
    ("bg-gradient-to-t from-red-100 via-rose-300 to-red-500", "text-rose-900"),
    ("bg-gradient-to-br from-yellow-100 via-yellow-300 to-yellow-500", "text-yellow-900"),
    ("bg-gradient-to-r from-orange-100 via-orange-300 to-orange-500", "text-orange-900"),
    ("bg-gradient-to-l from-slate-100 via-slate-300 to-slate-500", "text-slate-900"),
    ("bg-gradient-to-br from-emerald-100 via-emerald-300 to-emerald-500", "text-emerald-900"),
    ("bg-gradient-to-tr from-teal-100 via-teal-300 to-teal-500", "text-teal-900"),
    ("bg-gradient-to-r from-cyan-100 via-cyan-300 to-cyan-500", "text-cyan-900"),
    ("bg-gradient-to-br from-indigo-100 via-indigo-300 to-indigo-500", "text-indigo-900"),
    ("bg-gradient-to-r from-pink-100 via-pink-300 to-pink-500", "text-pink-900"),
    ("bg-gradient-to-l from-fuchsia-100 via-fuchsia-300 to-fuchsia-500", "text-fuchsia-900"),
    ("bg-gradient-to-r from-lime-100 via-lime-300 to-lime-500", "text-lime-900"),
    ("bg-gradient-to-br from-blue-100 via-blue-300 to-blue-500", "text-blue-900"),
    ("bg-gradient-to-tr from-amber-100 via-amber-300 to-amber-500", "text-amber-900"),
    ("bg-gradient-to-br from-stone-100 via-stone-300 to-stone-500", "text-stone-900"),
    ("bg-gradient-to-r from-zinc-100 via-zinc-300 to-zinc-500", "text-zinc-900"),
    ("bg-gradient-to-r from-gray-200 via-gray-400 to-gray-600", "text-gray-900"),
    ("bg-gradient-to-tr from-blue-100 via-blue-200 to-blue-400", "text-blue-900"),
    ("bg-gradient-to-t from-sky-100 via-sky-300 to-sky-500", "text-sky-900"),
    ("bg-gradient-to-br from-rose-200 via-rose-400 to-rose-600", "text-rose-900"),
    ("bg-gradient-to-br from-red-100 via-red-300 to-red-500", "text-red-900")
]

combinations.extend(gradients)

# Step 3: Build HTML with flexbox grid
cards = ""
for i, (bg, text) in enumerate(combinations, 1):
    cards += f"""
    <div class="max-w-sm rounded overflow-hidden shadow-lg">
      <div class="w-full h-32 {bg} {text} flex items-center justify-center">
        <span class="text-xl font-bold">Hello World</span>
      </div>
      
      <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2">{bg} with {text}</div>
        
        <button onclick="copyColors('{bg}', '{text}')"
                class="w-full bg-gray-100 hover:bg-gray-200 text-gray-800 py-2 px-4 rounded flex items-center justify-center gap-2">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
          </svg>
          Copy Classes
        </button>
      </div>
    </div>
    """
html = f"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tailwind Color Combinations</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .toast {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #4CAF50;
            color: white;
            padding: 12px 24px;
            border-radius: 4px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transform: translateY(100px);
            opacity: 0;
            transition: all 0.3s ease;
            z-index: 1000;
        }}
        .toast.show {{
            transform: translateY(0);
            opacity: 1;
        }}
        .color-card {{
            transition: all 0.2s ease;
        }}
        .color-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }}
    </style>
</head>

<body class="p-4 bg-gray-50">
    <!-- Toast Notification -->
    <div id="toast" class="toast">Copied to clipboard!</div>

    <div class="container mx-auto">
        <h1 class="text-3xl font-bold mb-6 text-gray-800">Tailwind Color Combinations</h1>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">
            {cards}
        </div>
    </div>

    <script>
        function showToast() {{
            const toast = document.getElementById('toast');
            toast.classList.add('show');
            setTimeout(() => {{
                toast.classList.remove('show');
            }}, 2000);
        }}

        function copyColors(bgClass, textClass) {{
            const textToCopy = `class="${'{bgClass}'} ${'{textClass}'}"`;
            navigator.clipboard.writeText(textToCopy).then(() => {{
                showToast();
            }}).catch(err => {{
                console.error('Failed to copy: ', err);
                const toast = document.getElementById('toast');
                toast.textContent = 'Failed to copy!';
                toast.style.backgroundColor = '#f44336';
                showToast();
                setTimeout(() => {{
                    toast.textContent = 'Copied to clipboard!';
                    toast.style.backgroundColor = '#4CAF50';
                }}, 2000);
            }});
        }}
    </script>
</body>

</html>
"""

# Save the file
path = Path("index.html").resolve()
with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ HTML file created:", path)