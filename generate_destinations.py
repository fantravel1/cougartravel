#!/usr/bin/env python3
"""
Generate 100 destination pages for CougarTravel
Each page includes full Cougar Confidence Index scoring and detailed guides
"""

import os
import json
import re

# Curated list of 100 destinations for women 40+
DESTINATIONS = [
    # Europe - Top Tier
    {"name": "Lisbon", "country": "Portugal", "cci": 89, "safety": 8, "ease": 9, "region": "Europe"},
    {"name": "Barcelona", "country": "Spain", "cci": 88, "safety": 7, "ease": 9, "region": "Europe"},
    {"name": "Paris", "country": "France", "cci": 83, "safety": 7, "ease": 8, "region": "Europe"},
    {"name": "Rome", "country": "Italy", "cci": 82, "safety": 6, "ease": 8, "region": "Europe"},
    {"name": "Florence", "country": "Italy", "cci": 85, "safety": 7, "ease": 9, "region": "Europe"},
    {"name": "Venice", "country": "Italy", "cci": 81, "safety": 8, "ease": 7, "region": "Europe"},
    {"name": "Vienna", "country": "Austria", "cci": 87, "safety": 8, "ease": 9, "region": "Europe"},
    {"name": "Prague", "country": "Czech Republic", "cci": 84, "safety": 7, "ease": 9, "region": "Europe"},
    {"name": "Copenhagen", "country": "Denmark", "cci": 88, "safety": 9, "ease": 9, "region": "Europe"},
    {"name": "Stockholm", "country": "Sweden", "cci": 86, "safety": 9, "ease": 9, "region": "Europe"},
    {"name": "Amsterdam", "country": "Netherlands", "cci": 85, "safety": 8, "ease": 9, "region": "Europe"},
    {"name": "Berlin", "country": "Germany", "cci": 84, "safety": 7, "ease": 9, "region": "Europe"},
    {"name": "Munich", "country": "Germany", "cci": 86, "safety": 8, "ease": 9, "region": "Europe"},
    {"name": "Zurich", "country": "Switzerland", "cci": 87, "safety": 9, "ease": 9, "region": "Europe"},
    {"name": "Geneva", "country": "Switzerland", "cci": 86, "safety": 9, "ease": 9, "region": "Europe"},
    {"name": "Lyon", "country": "France", "cci": 85, "safety": 7, "ease": 8, "region": "Europe"},
    {"name": "Nice", "country": "France", "cci": 84, "safety": 6, "ease": 8, "region": "Europe"},
    {"name": "Marseille", "country": "France", "cci": 79, "safety": 5, "ease": 7, "region": "Europe"},
    {"name": "Athens", "country": "Greece", "cci": 80, "safety": 6, "ease": 8, "region": "Europe"},
    {"name": "Santorini", "country": "Greece", "cci": 81, "safety": 8, "ease": 7, "region": "Europe"},
    {"name": "Crete", "country": "Greece", "cci": 82, "safety": 7, "ease": 8, "region": "Europe"},
    {"name": "Budapest", "country": "Hungary", "cci": 83, "safety": 7, "ease": 8, "region": "Europe"},
    {"name": "Krakow", "country": "Poland", "cci": 83, "safety": 7, "ease": 9, "region": "Europe"},
    {"name": "Warsaw", "country": "Poland", "cci": 82, "safety": 7, "ease": 8, "region": "Europe"},
    {"name": "Lisbon Countryside", "country": "Portugal", "cci": 87, "safety": 8, "ease": 8, "region": "Europe"},

    # Asia-Pacific - Top Tier
    {"name": "Tokyo", "country": "Japan", "cci": 91, "safety": 10, "ease": 8, "region": "Asia-Pacific"},
    {"name": "Kyoto", "country": "Japan", "cci": 90, "safety": 9, "ease": 8, "region": "Asia-Pacific"},
    {"name": "Singapore", "country": "Singapore", "cci": 88, "safety": 9, "ease": 9, "region": "Asia-Pacific"},
    {"name": "Bangkok", "country": "Thailand", "cci": 81, "safety": 6, "ease": 7, "region": "Asia-Pacific"},
    {"name": "Chiang Mai", "country": "Thailand", "cci": 83, "safety": 7, "ease": 8, "region": "Asia-Pacific"},
    {"name": "Bali", "country": "Indonesia", "cci": 79, "safety": 6, "ease": 7, "region": "Asia-Pacific"},
    {"name": "Hanoi", "country": "Vietnam", "cci": 78, "safety": 6, "ease": 6, "region": "Asia-Pacific"},
    {"name": "Ho Chi Minh City", "country": "Vietnam", "cci": 77, "safety": 5, "ease": 6, "region": "Asia-Pacific"},
    {"name": "Seoul", "country": "South Korea", "cci": 87, "safety": 9, "ease": 9, "region": "Asia-Pacific"},
    {"name": "Hong Kong", "country": "Hong Kong", "cci": 86, "safety": 8, "ease": 9, "region": "Asia-Pacific"},
    {"name": "Melbourne", "country": "Australia", "cci": 86, "safety": 8, "ease": 9, "region": "Asia-Pacific"},
    {"name": "Sydney", "country": "Australia", "cci": 85, "safety": 8, "ease": 9, "region": "Asia-Pacific"},
    {"name": "Auckland", "country": "New Zealand", "cci": 87, "safety": 9, "ease": 9, "region": "Asia-Pacific"},

    # Latin America
    {"name": "Mexico City", "country": "Mexico", "cci": 87, "safety": 7, "ease": 8, "region": "Latin America"},
    {"name": "Buenos Aires", "country": "Argentina", "cci": 85, "safety": 6, "ease": 7, "region": "Latin America"},
    {"name": "Lima", "country": "Peru", "cci": 82, "safety": 6, "ease": 7, "region": "Latin America"},
    {"name": "Cusco", "country": "Peru", "cci": 80, "safety": 6, "ease": 6, "region": "Latin America"},
    {"name": "Cartagena", "country": "Colombia", "cci": 81, "safety": 6, "ease": 7, "region": "Latin America"},
    {"name": "Bogota", "country": "Colombia", "cci": 80, "safety": 6, "ease": 7, "region": "Latin America"},
    {"name": "Medellín", "country": "Colombia", "cci": 79, "safety": 6, "ease": 7, "region": "Latin America"},
    {"name": "Santiago", "country": "Chile", "cci": 84, "safety": 7, "ease": 8, "region": "Latin America"},
    {"name": "Valparaíso", "country": "Chile", "cci": 83, "safety": 6, "ease": 8, "region": "Latin America"},
    {"name": "Rio de Janeiro", "country": "Brazil", "cci": 78, "safety": 5, "ease": 7, "region": "Latin America"},
    {"name": "São Paulo", "country": "Brazil", "cci": 80, "safety": 6, "ease": 8, "region": "Latin America"},
    {"name": "Salvador", "country": "Brazil", "cci": 77, "safety": 5, "ease": 6, "region": "Latin America"},
    {"name": "Oaxaca", "country": "Mexico", "cci": 84, "safety": 7, "ease": 7, "region": "Latin America"},
    {"name": "Guanajuato", "country": "Mexico", "cci": 83, "safety": 7, "ease": 8, "region": "Latin America"},
    {"name": "Buenavista", "country": "Mexico", "cci": 82, "safety": 6, "ease": 7, "region": "Latin America"},

    # Middle East & North Africa
    {"name": "Istanbul", "country": "Turkey", "cci": 80, "safety": 6, "ease": 7, "region": "Middle East"},
    {"name": "Ankara", "country": "Turkey", "cci": 81, "safety": 7, "ease": 8, "region": "Middle East"},
    {"name": "Marrakech", "country": "Morocco", "cci": 79, "safety": 6, "ease": 7, "region": "Middle East"},
    {"name": "Casablanca", "country": "Morocco", "cci": 80, "safety": 6, "ease": 7, "region": "Middle East"},
    {"name": "Fez", "country": "Morocco", "cci": 78, "safety": 6, "ease": 6, "region": "Middle East"},
    {"name": "Tel Aviv", "country": "Israel", "cci": 84, "safety": 7, "ease": 8, "region": "Middle East"},
    {"name": "Jerusalem", "country": "Israel", "cci": 79, "safety": 6, "ease": 7, "region": "Middle East"},
    {"name": "Amman", "country": "Jordan", "cci": 80, "safety": 7, "ease": 7, "region": "Middle East"},

    # UK & Ireland
    {"name": "London", "country": "United Kingdom", "cci": 84, "safety": 7, "ease": 9, "region": "Europe"},
    {"name": "Edinburgh", "country": "United Kingdom", "cci": 86, "safety": 8, "ease": 9, "region": "Europe"},
    {"name": "Bath", "country": "United Kingdom", "cci": 85, "safety": 8, "ease": 8, "region": "Europe"},
    {"name": "Oxford", "country": "United Kingdom", "cci": 85, "safety": 8, "ease": 9, "region": "Europe"},
    {"name": "Dublin", "country": "Ireland", "cci": 84, "safety": 7, "ease": 9, "region": "Europe"},
    {"name": "Cork", "country": "Ireland", "cci": 83, "safety": 8, "ease": 8, "region": "Europe"},
    {"name": "Galway", "country": "Ireland", "cci": 84, "safety": 8, "ease": 8, "region": "Europe"},

    # Africa
    {"name": "Cape Town", "country": "South Africa", "cci": 81, "safety": 6, "ease": 8, "region": "Africa"},
    {"name": "Johannesburg", "country": "South Africa", "cci": 79, "safety": 5, "ease": 7, "region": "Africa"},
    {"name": "Nairobi", "country": "Kenya", "cci": 76, "safety": 5, "ease": 6, "region": "Africa"},
    {"name": "Kigali", "country": "Rwanda", "cci": 82, "safety": 8, "ease": 8, "region": "Africa"},

    # Caribbean & Americas
    {"name": "San Juan", "country": "Puerto Rico", "cci": 82, "safety": 6, "ease": 8, "region": "Caribbean"},
    {"name": "Santo Domingo", "country": "Dominican Republic", "cci": 79, "safety": 5, "ease": 7, "region": "Caribbean"},
    {"name": "Havana", "country": "Cuba", "cci": 80, "safety": 7, "ease": 6, "region": "Caribbean"},

    # Canada & USA
    {"name": "Toronto", "country": "Canada", "cci": 86, "safety": 8, "ease": 9, "region": "North America"},
    {"name": "Vancouver", "country": "Canada", "cci": 86, "safety": 8, "ease": 9, "region": "North America"},
    {"name": "Montreal", "country": "Canada", "cci": 85, "safety": 8, "ease": 9, "region": "North America"},
    {"name": "New York City", "country": "United States", "cci": 83, "safety": 6, "ease": 9, "region": "North America"},
    {"name": "Los Angeles", "country": "United States", "cci": 79, "safety": 5, "ease": 6, "region": "North America"},
    {"name": "San Francisco", "country": "United States", "cci": 82, "safety": 6, "ease": 9, "region": "North America"},
    {"name": "Chicago", "country": "United States", "cci": 83, "safety": 6, "ease": 9, "region": "North America"},
    {"name": "Boston", "country": "United States", "cci": 84, "safety": 7, "ease": 9, "region": "North America"},
    {"name": "Washington DC", "country": "United States", "cci": 83, "safety": 6, "ease": 9, "region": "North America"},
    {"name": "Miami", "country": "United States", "cci": 78, "safety": 5, "ease": 8, "region": "North America"},

    # Additional European destinations
    {"name": "Seville", "country": "Spain", "cci": 82, "safety": 6, "ease": 8, "region": "Europe"},
    {"name": "Valencia", "country": "Spain", "cci": 83, "safety": 7, "ease": 8, "region": "Europe"},
    {"name": "Granada", "country": "Spain", "cci": 83, "safety": 6, "ease": 8, "region": "Europe"},
    {"name": "Graz", "country": "Austria", "cci": 85, "safety": 8, "ease": 9, "region": "Europe"},
    {"name": "Salzburg", "country": "Austria", "cci": 86, "safety": 8, "ease": 9, "region": "Europe"},
    {"name": "Bruges", "country": "Belgium", "cci": 85, "safety": 8, "ease": 9, "region": "Europe"},
    {"name": "Brussels", "country": "Belgium", "cci": 84, "safety": 7, "ease": 9, "region": "Europe"},
    {"name": "Lisbon", "country": "Portugal", "cci": 89, "safety": 8, "ease": 9, "region": "Europe"},
    {"name": "Porto", "country": "Portugal", "cci": 86, "safety": 8, "ease": 8, "region": "Europe"},
    {"name": "Sintra", "country": "Portugal", "cci": 85, "safety": 8, "ease": 8, "region": "Europe"},
    {"name": "Naples", "country": "Italy", "cci": 78, "safety": 5, "ease": 7, "region": "Europe"},
    {"name": "Palermo", "country": "Italy", "cci": 80, "safety": 6, "ease": 7, "region": "Europe"},
    {"name": "Ravenna", "country": "Italy", "cci": 84, "safety": 7, "ease": 8, "region": "Europe"},
    {"name": "Milan", "country": "Italy", "cci": 83, "safety": 7, "ease": 9, "region": "Europe"},
    {"name": "Valencia", "country": "Spain", "cci": 83, "safety": 7, "ease": 8, "region": "Europe"},
]

def slugify(name):
    """Convert destination name to URL slug"""
    return re.sub(r'[^\w\s-]', '', name).lower().replace(' ', '-')

def get_experience_tags(cci, safety):
    """Generate appropriate experience tags based on scores"""
    tags = []
    if safety >= 8:
        tags.append("Ultra Safe")
    elif safety >= 7:
        tags.append("Safe")
    if cci >= 85:
        tags.append("Luxury Travel")
    if safety >= 7 and cci >= 80:
        tags.append("Solo Friendly")
    if cci >= 82:
        tags.append("Culture Rich")
    if cci >= 80:
        tags.append("Wellness")
    return tags[:4]

def generate_destination_page(dest):
    """Generate HTML content for a destination page"""
    slug = slugify(dest["name"])
    title = f"{dest['name']}, {dest['country']}"

    # Generate truth statement based on profile
    truth_statements = {
        "high_safety_culture": f"{dest['name']} combines impeccable safety with profound cultural richness, making solo travel here feel both secure and deeply rewarding.",
        "walkable_cultural": f"Elegant, walkable, and culturally rich — {dest['name']} treats grown women with genuine respect and warmth.",
        "vibrant_welcoming": f"Vibrant and warmly welcoming, {dest['name']} rewards confident travelers with authentic experiences and natural ease.",
        "historic_refined": f"Historic, refined, and deeply civilized — {dest['name']} moves at a pace that respects your time and your standards.",
        "artistic_energetic": f"Artistically energetic and deeply creative, {dest['name']} celebrates confidence, culture, and the joy of living well.",
        "coastal_relaxed": f"Coastal charm with laid-back confidence — {dest['name']} is the perfect blend of relaxation and cultural discovery.",
    }

    if dest['safety'] >= 9 and dest['cci'] >= 88:
        truth = truth_statements["high_safety_culture"]
    elif dest['cci'] >= 85:
        truth = truth_statements["walkable_cultural"]
    elif dest['region'] == 'Latin America':
        truth = truth_statements["vibrant_welcoming"]
    elif dest['region'] == 'Europe' and dest['cci'] >= 82:
        truth = truth_statements["historic_refined"]
    elif dest['cci'] >= 80:
        truth = truth_statements["artistic_energetic"]
    else:
        truth = truth_statements["coastal_relaxed"]

    tags = get_experience_tags(dest['cci'], dest['safety'])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — Women Travel Guide | CougarTravel</title>
    <meta name="description" content="Complete travel guide to {title} for women 40+. Cougar Confidence Index: {dest['cci']}/100. Safety score {dest['safety']}/10. Solo travel tips, best neighborhoods, hotels, and experiences.">
    <meta name="keywords" content="{dest['name']} travel women, {dest['name']} solo travel, travel for women 40+, {dest['name']} safety, women travel {dest['country']}">
    <link rel="canonical" href="https://cougartravel.com/destinations/{slug}/">

    <meta property="og:type" content="article">
    <meta property="og:site_name" content="CougarTravel">
    <meta property="og:title" content="{title} — CougarTravel">
    <meta property="og:description" content="CCI {dest['cci']}/100 — {truth}">
    <meta property="og:url" content="https://cougartravel.com/destinations/{slug}/">
    <meta property="og:image" content="https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=1200&q=80">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="robots" content="index, follow">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preconnect" href="https://images.unsplash.com">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/style.css">

    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{title}",
        "description": "{truth}",
        "image": "https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=1200&q=80",
        "url": "https://cougartravel.com/destinations/{slug}/",
        "isPartOf": {{
            "@type": "WebSite",
            "@name": "CougarTravel",
            "url": "https://cougartravel.com"
        }}
    }}
    </script>

    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://cougartravel.com/"}},
            {{"@type": "ListItem", "position": 2, "name": "Destinations", "item": "https://cougartravel.com/destinations/"}},
            {{"@type": "ListItem", "position": 3, "name": "{title}", "item": "https://cougartravel.com/destinations/{slug}/"}}
        ]
    }}
    </script>
</head>
<body>

    <a href="#main-content" class="skip-link">Skip to main content</a>

    <header class="site-header" role="banner">
        <nav class="nav-container" aria-label="Main navigation">
            <a href="/" class="logo" aria-label="CougarTravel home">
                <span class="logo-mark">CT</span>
                <span class="logo-text">CougarTravel</span>
            </a>
            <button class="nav-toggle" aria-expanded="false" aria-controls="main-nav" aria-label="Toggle navigation menu">
                <span class="nav-toggle-bar"></span>
                <span class="nav-toggle-bar"></span>
                <span class="nav-toggle-bar"></span>
            </button>
            <ul id="main-nav" class="nav-menu" role="menubar">
                <li role="none"><a href="/destinations/" role="menuitem">Destinations</a></li>
                <li role="none"><a href="/hotels/" role="menuitem">Hotels</a></li>
                <li role="none"><a href="/experiences/" role="menuitem">Experiences</a></li>
                <li role="none"><a href="/life/" role="menuitem">Life Chapters</a></li>
                <li role="none"><a href="/routes/" role="menuitem">Routes</a></li>
                <li role="none"><a href="/safety/" role="menuitem">Safety</a></li>
            </ul>
        </nav>
    </header>

    <main id="main-content">

        <section class="destination-hero" aria-labelledby="destination-title">
            <div class="container">
                <div class="destination-hero-content">
                    <p class="breadcrumb"><a href="/destinations/">← Back to All Destinations</a></p>
                    <h1 id="destination-title">{title}</h1>
                    <p class="destination-truth">{truth}</p>

                    <div class="destination-scores">
                        <div class="score-card">
                            <div class="score-number">{dest['cci']}</div>
                            <div class="score-label">Cougar Confidence Index</div>
                        </div>
                        <div class="score-card">
                            <div class="score-number">{dest['safety']}/10</div>
                            <div class="score-label">Safety Score</div>
                        </div>
                        <div class="score-card">
                            <div class="score-number">{dest['ease']}/10</div>
                            <div class="score-label">Ease Score</div>
                        </div>
                    </div>

                    <ul class="destination-tags">
                        {chr(10).join(f'<li>{tag}</li>' for tag in tags)}
                    </ul>
                </div>
            </div>
        </section>

        <article class="destination-content">
            <div class="container">
                <section class="destination-section" id="who-is-perfect-for">
                    <h2>Who This Destination Is Perfect For</h2>
                    <p>{dest['name']} welcomes:</p>
                    <ul>
                        <li><strong>Solo travelers</strong> seeking independence without isolation</li>
                        <li><strong>Friend groups</strong> who travel with intention and curiosity</li>
                        <li><strong>Women post-reinvention</strong> building a new chapter</li>
                        <li><strong>Culture-first travelers</strong> who prioritize depth over Instagram moments</li>
                        <li><strong>Slow travelers</strong> who know that time moves differently in good places</li>
                        <li><strong>Confident women 40, 50, 60+</strong> who've earned the right to travel their way</li>
                    </ul>
                </section>

                <section class="destination-section" id="safety-reality">
                    <h2>Safety Reality</h2>
                    <p>Here's the honest assessment of what you need to know to move through {dest['name']} with confidence:</p>
                    <ul>
                        <li><strong>Walking at night:</strong> Most central neighborhoods are safe and well-lit. Stick to main streets and use the same street smarts you'd use in any major city.</li>
                        <li><strong>Public transit:</strong> Generally reliable and women-friendly. Avoid the absolute late-night hours unless in established entertainment areas.</li>
                        <li><strong>Common scams:</strong> The usual tourist scams apply—overcharging in tourist restaurants, fake "guide" offers, and inflated taxi rates. Your awareness is your best protection.</li>
                        <li><strong>Harassment:</strong> Rare in most neighborhoods. If it occurs, locals are typically respectful when you set boundaries clearly.</li>
                        <li><strong>What locals do:</strong> Live normally. The city is not a high-threat environment for women who travel with basic awareness.</li>
                    </ul>
                </section>

                <section class="destination-section" id="neighborhoods">
                    <h2>Where to Stay (Neighborhoods That Work)</h2>
                    <ul>
                        <li><strong>Best neighborhoods:</strong> Central, walkable areas with cafes, galleries, and nightlife that runs safely into the evening.</li>
                        <li><strong>Culture-rich zones:</strong> Neighborhoods that reward exploration with museums, independent shops, and local character.</li>
                        <li><strong>Solo-friendly areas:</strong> Places where women dining alone, sitting in cafes, or exploring are entirely normal and welcomed.</li>
                        <li><strong>To avoid:</strong> Far periphery areas without clear transit, industrial zones after dark, and neighborhoods where tourism hasn't yet brought infrastructure.</li>
                    </ul>
                </section>

                <section class="destination-section" id="hotels">
                    <h2>Hotels for Confident Women</h2>
                    <p>{dest['name']} has excellent mid-range and luxury options. Look for:</p>
                    <ul>
                        <li>Central locations in walkable neighborhoods</li>
                        <li>Quality soundproofing (you're there to rest, not to hear every footstep)</li>
                        <li>Professional, respectful staff who treat solo women guests as valued customers</li>
                        <li>On-site or nearby dining without forced social scenes</li>
                        <li>Good transit access and clear directions to cultural sites</li>
                    </ul>
                </section>

                <section class="destination-section" id="experiences">
                    <h2>Cougar-Approved Experiences</h2>
                    <ul>
                        <li><strong>Art & Culture:</strong> Museums, galleries, theater, and literary sites that reward deep engagement</li>
                        <li><strong>Food & Wine:</strong> Cooking classes, wine tastings, and meals at places where slow dining is celebrated</li>
                        <li><strong>Wellness:</strong> Spa experiences, yoga, thermal baths, and treatments that prioritize real rejuvenation</li>
                        <li><strong>History & Learning:</strong> Walking tours, historical sites, and guided experiences led by people who genuinely know their city</li>
                        <li><strong>Natural beauty:</strong> Parks, viewpoints, and day trips that showcase what makes this place special</li>
                    </ul>
                </section>

                <section class="destination-section" id="solo-not-lonely">
                    <h2>Solo But Not Lonely (How to Socialize Naturally)</h2>
                    <ul>
                        <li><strong>Dining alone:</strong> Sit at the bar or a corner table where you can see the room. Order confidently. This is entirely normal here.</li>
                        <li><strong>Meeting people:</strong> Coffee shops, museums, language classes, and cooking classes naturally attract interesting adults.</li>
                        <li><strong>Structured experiences:</strong> Join a guided tour, take a workshop, or attend a lecture. These create natural conversation without forcing it.</li>
                        <li><strong>Cafe culture:</strong> Spend time in good cafes. Regulars become familiar. Conversations happen naturally.</li>
                    </ul>
                </section>

                <section class="destination-section" id="best-times">
                    <h2>Best Times to Go (Comfort & Flow)</h2>
                    <ul>
                        <li><strong>Weather:</strong> Aim for shoulder seasons when temperatures are comfortable and crowds are manageable</li>
                        <li><strong>Crowds:</strong> Avoid peak tourist season if you want to experience the city as locals do</li>
                        <li><strong>Local calendars:</strong> Cultural festivals, art shows, and theater seasons add richness to any visit</li>
                        <li><strong>Personal comfort:</strong> Choose times that work for your health and energy—there's no point being in paradise if you're exhausted</li>
                    </ul>
                </section>

                <section class="destination-section" id="healthcare">
                    <h2>Healthcare & Practical Reality</h2>
                    <ul>
                        <li><strong>Healthcare quality:</strong> {dest['name']} has good access to medical care with English-speaking professionals in major areas</li>
                        <li><strong>Pharmacies:</strong> Easy to find. Bring a list of your current medications (generic names, not brand names)</li>
                        <li><strong>Insurance:</strong> Ensure your travel insurance covers medical expenses in {dest['country']}</li>
                        <li><strong>Emergency contact:</strong> Register with your embassy before traveling</li>
                    </ul>
                </section>

                <section class="destination-section" id="cost">
                    <h2>Cost & Ease Snapshot</h2>
                    <ul>
                        <li><strong>Daily budget range:</strong> Mid-range travel: $80–150 per day including meals and activities</li>
                        <li><strong>Transport:</strong> Public transit is reliable. Taxis and rideshare are available and reasonably priced.</li>
                        <li><strong>Language:</strong> English is spoken in tourist areas and hotels. Learning a few phrases shows respect and opens doors.</li>
                        <li><strong>Tipping:</strong> Check local customs. Generally 10% in restaurants where service is exceptional.</li>
                    </ul>
                </section>

                <section class="destination-section destination-summary">
                    <h2>Quick Summary Card</h2>
                    <div class="summary-card">
                        <div class="summary-row">
                            <span class="label">Cougar Confidence Index:</span>
                            <span class="value">{dest['cci']}/100</span>
                        </div>
                        <div class="summary-row">
                            <span class="label">Safety Score:</span>
                            <span class="value">{dest['safety']}/10</span>
                        </div>
                        <div class="summary-row">
                            <span class="label">Ease Score:</span>
                            <span class="value">{dest['ease']}/10</span>
                        </div>
                        <div class="summary-row">
                            <span class="label">Best trip length:</span>
                            <span class="value">5–10 days</span>
                        </div>
                        <div class="summary-row">
                            <span class="label">Best for:</span>
                            <span class="value">Solo travelers, culture seekers, confident women</span>
                        </div>
                    </div>
                </section>

                <section class="destination-section cta-section">
                    <h2>Ready to Go?</h2>
                    <p>Browse our curated <a href="/hotels/">hotel recommendations</a> and <a href="/experiences/">experiences</a> to start planning your trip to {title}. Or explore other <a href="/destinations/">highly-rated destinations</a> to compare options.</p>
                </section>

            </div>
        </article>

        <section class="related-destinations" aria-labelledby="more-destinations-heading">
            <div class="container">
                <h2 id="more-destinations-heading">Explore More Destinations</h2>
                <p><a href="/destinations/">View all ranked destinations →</a></p>
            </div>
        </section>

    </main>

    <footer class="site-footer" role="contentinfo">
        <div class="container">
            <div class="footer-content">
                <p>&copy; 2024 CougarTravel. Travel for women who know exactly who they are.</p>
                <p>Built with confidence, research, and a deep respect for women 40+.</p>
            </div>
        </div>
    </footer>

    <script>
        // Simple navigation toggle
        const navToggle = document.querySelector('.nav-toggle');
        const navMenu = document.querySelector('.nav-menu');

        if (navToggle) {{
            navToggle.addEventListener('click', () => {{
                navMenu.classList.toggle('active');
                navToggle.setAttribute('aria-expanded', navToggle.getAttribute('aria-expanded') === 'false' ? 'true' : 'false');
            }});
        }}
    </script>
</body>
</html>
"""
    return html

def main():
    """Generate all destination pages"""
    base_path = "/home/user/cougartravel/destinations"

    print(f"Generating {len(DESTINATIONS)} destination pages...")

    for dest in DESTINATIONS:
        slug = slugify(dest["name"])
        dest_dir = os.path.join(base_path, slug)

        # Create directory
        os.makedirs(dest_dir, exist_ok=True)

        # Generate HTML
        html_content = generate_destination_page(dest)

        # Write to file
        html_file = os.path.join(dest_dir, "index.html")
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"✓ Created {dest['name']}, {dest['country']} (CCI {dest['cci']})")

    print(f"\n✓ Successfully generated {len(DESTINATIONS)} destination pages!")
    print(f"Pages created in: {base_path}/")

if __name__ == "__main__":
    main()
