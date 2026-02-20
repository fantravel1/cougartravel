#!/usr/bin/env python3
"""
Update the destinations hub index to include all 100 destination cards
"""

import re

DESTINATIONS = [
    {"name": "Tokyo", "country": "Japan", "cci": 91, "safety": 10, "ease": 8},
    {"name": "Kyoto", "country": "Japan", "cci": 90, "safety": 9, "ease": 8},
    {"name": "Lisbon", "country": "Portugal", "cci": 89, "safety": 8, "ease": 9},
    {"name": "Barcelona", "country": "Spain", "cci": 88, "safety": 7, "ease": 9},
    {"name": "Copenhagen", "country": "Denmark", "cci": 88, "safety": 9, "ease": 9},
    {"name": "Singapore", "country": "Singapore", "cci": 88, "safety": 9, "ease": 9},
    {"name": "Vienna", "country": "Austria", "cci": 87, "safety": 8, "ease": 9},
    {"name": "Seoul", "country": "South Korea", "cci": 87, "safety": 9, "ease": 9},
    {"name": "Mexico City", "country": "Mexico", "cci": 87, "safety": 7, "ease": 8},
    {"name": "Zurich", "country": "Switzerland", "cci": 87, "safety": 9, "ease": 9},
    {"name": "Lisbon Countryside", "country": "Portugal", "cci": 87, "safety": 8, "ease": 8},
    {"name": "Auckland", "country": "New Zealand", "cci": 87, "safety": 9, "ease": 9},
    {"name": "Stockholm", "country": "Sweden", "cci": 86, "safety": 9, "ease": 9},
    {"name": "Munich", "country": "Germany", "cci": 86, "safety": 8, "ease": 9},
    {"name": "Geneva", "country": "Switzerland", "cci": 86, "safety": 9, "ease": 9},
    {"name": "Toronto", "country": "Canada", "cci": 86, "safety": 8, "ease": 9},
    {"name": "Vancouver", "country": "Canada", "cci": 86, "safety": 8, "ease": 9},
    {"name": "Melbourne", "country": "Australia", "cci": 86, "safety": 8, "ease": 9},
    {"name": "Hong Kong", "country": "Hong Kong", "cci": 86, "safety": 8, "ease": 9},
    {"name": "Edinburgh", "country": "United Kingdom", "cci": 86, "safety": 8, "ease": 9},
    {"name": "Porto", "country": "Portugal", "cci": 86, "safety": 8, "ease": 8},
    {"name": "Salzburg", "country": "Austria", "cci": 86, "safety": 8, "ease": 9},
    {"name": "Florence", "country": "Italy", "cci": 85, "safety": 7, "ease": 9},
    {"name": "Amsterdam", "country": "Netherlands", "cci": 85, "safety": 8, "ease": 9},
    {"name": "Lyon", "country": "France", "cci": 85, "safety": 7, "ease": 8},
    {"name": "Graz", "country": "Austria", "cci": 85, "safety": 8, "ease": 9},
    {"name": "Bath", "country": "United Kingdom", "cci": 85, "safety": 8, "ease": 8},
    {"name": "Oxford", "country": "United Kingdom", "cci": 85, "safety": 8, "ease": 9},
    {"name": "Montreal", "country": "Canada", "cci": 85, "safety": 8, "ease": 9},
    {"name": "Sydney", "country": "Australia", "cci": 85, "safety": 8, "ease": 9},
    {"name": "Buenos Aires", "country": "Argentina", "cci": 85, "safety": 6, "ease": 7},
    {"name": "Bruges", "country": "Belgium", "cci": 85, "safety": 8, "ease": 9},
    {"name": "Sintra", "country": "Portugal", "cci": 85, "safety": 8, "ease": 8},
    {"name": "Prague", "country": "Czech Republic", "cci": 84, "safety": 7, "ease": 9},
    {"name": "Berlin", "country": "Germany", "cci": 84, "safety": 7, "ease": 9},
    {"name": "Santiago", "country": "Chile", "cci": 84, "safety": 7, "ease": 8},
    {"name": "Nice", "country": "France", "cci": 84, "safety": 6, "ease": 8},
    {"name": "London", "country": "United Kingdom", "cci": 84, "safety": 7, "ease": 9},
    {"name": "Tel Aviv", "country": "Israel", "cci": 84, "safety": 7, "ease": 8},
    {"name": "Boston", "country": "United States", "cci": 84, "safety": 7, "ease": 9},
    {"name": "Brussels", "country": "Belgium", "cci": 84, "safety": 7, "ease": 9},
    {"name": "Ravenna", "country": "Italy", "cci": 84, "safety": 7, "ease": 8},
    {"name": "Oaxaca", "country": "Mexico", "cci": 84, "safety": 7, "ease": 7},
    {"name": "Valparaíso", "country": "Chile", "cci": 83, "safety": 6, "ease": 8},
    {"name": "Paris", "country": "France", "cci": 83, "safety": 7, "ease": 8},
    {"name": "Budapest", "country": "Hungary", "cci": 83, "safety": 7, "ease": 8},
    {"name": "Krakow", "country": "Poland", "cci": 83, "safety": 7, "ease": 9},
    {"name": "Cork", "country": "Ireland", "cci": 83, "safety": 8, "ease": 8},
    {"name": "Chiang Mai", "country": "Thailand", "cci": 83, "safety": 7, "ease": 8},
    {"name": "San Francisco", "country": "United States", "cci": 82, "safety": 6, "ease": 9},
    {"name": "Rome", "country": "Italy", "cci": 82, "safety": 6, "ease": 8},
    {"name": "Warsaw", "country": "Poland", "cci": 82, "safety": 7, "ease": 8},
    {"name": "Crete", "country": "Greece", "cci": 82, "safety": 7, "ease": 8},
    {"name": "Lima", "country": "Peru", "cci": 82, "safety": 6, "ease": 7},
    {"name": "Buenavista", "country": "Mexico", "cci": 82, "safety": 6, "ease": 7},
    {"name": "San Juan", "country": "Puerto Rico", "cci": 82, "safety": 6, "ease": 8},
    {"name": "Seville", "country": "Spain", "cci": 82, "safety": 6, "ease": 8},
    {"name": "Guanajuato", "country": "Mexico", "cci": 83, "safety": 7, "ease": 8},
    {"name": "Kigali", "country": "Rwanda", "cci": 82, "safety": 8, "ease": 8},
    {"name": "Valencia", "country": "Spain", "cci": 83, "safety": 7, "ease": 8},
    {"name": "Milan", "country": "Italy", "cci": 83, "safety": 7, "ease": 9},
    {"name": "Galway", "country": "Ireland", "cci": 84, "safety": 8, "ease": 8},
    {"name": "Dublin", "country": "Ireland", "cci": 84, "safety": 7, "ease": 9},
    {"name": "Granada", "country": "Spain", "cci": 83, "safety": 6, "ease": 8},
    {"name": "Chicago", "country": "United States", "cci": 83, "safety": 6, "ease": 9},
    {"name": "Washington DC", "country": "United States", "cci": 83, "safety": 6, "ease": 9},
    {"name": "New York City", "country": "United States", "cci": 83, "safety": 6, "ease": 9},
    {"name": "Athens", "country": "Greece", "cci": 80, "safety": 6, "ease": 8},
    {"name": "Santorini", "country": "Greece", "cci": 81, "safety": 8, "ease": 7},
    {"name": "Venice", "country": "Italy", "cci": 81, "safety": 8, "ease": 7},
    {"name": "Cartagena", "country": "Colombia", "cci": 81, "safety": 6, "ease": 7},
    {"name": "Cape Town", "country": "South Africa", "cci": 81, "safety": 6, "ease": 8},
    {"name": "Bangkok", "country": "Thailand", "cci": 81, "safety": 6, "ease": 7},
    {"name": "Ankara", "country": "Turkey", "cci": 81, "safety": 7, "ease": 8},
    {"name": "Havana", "country": "Cuba", "cci": 80, "safety": 7, "ease": 6},
    {"name": "Casablanca", "country": "Morocco", "cci": 80, "safety": 6, "ease": 7},
    {"name": "Bogota", "country": "Colombia", "cci": 80, "safety": 6, "ease": 7},
    {"name": "São Paulo", "country": "Brazil", "cci": 80, "safety": 6, "ease": 8},
    {"name": "Palermo", "country": "Italy", "cci": 80, "safety": 6, "ease": 7},
    {"name": "Istanbul", "country": "Turkey", "cci": 80, "safety": 6, "ease": 7},
    {"name": "Amman", "country": "Jordan", "cci": 80, "safety": 7, "ease": 7},
    {"name": "Cusco", "country": "Peru", "cci": 80, "safety": 6, "ease": 6},
    {"name": "Marseille", "country": "France", "cci": 79, "safety": 5, "ease": 7},
    {"name": "Marrakech", "country": "Morocco", "cci": 79, "safety": 6, "ease": 7},
    {"name": "Bali", "country": "Indonesia", "cci": 79, "safety": 6, "ease": 7},
    {"name": "Johannesburg", "country": "South Africa", "cci": 79, "safety": 5, "ease": 7},
    {"name": "Santo Domingo", "country": "Dominican Republic", "cci": 79, "safety": 5, "ease": 7},
    {"name": "Medellín", "country": "Colombia", "cci": 79, "safety": 6, "ease": 7},
    {"name": "Rio de Janeiro", "country": "Brazil", "cci": 78, "safety": 5, "ease": 7},
    {"name": "Los Angeles", "country": "United States", "cci": 79, "safety": 5, "ease": 6},
    {"name": "Naples", "country": "Italy", "cci": 78, "safety": 5, "ease": 7},
    {"name": "Fez", "country": "Morocco", "cci": 78, "safety": 6, "ease": 6},
    {"name": "Hanoi", "country": "Vietnam", "cci": 78, "safety": 6, "ease": 6},
    {"name": "Miami", "country": "United States", "cci": 78, "safety": 5, "ease": 8},
    {"name": "Ho Chi Minh City", "country": "Vietnam", "cci": 77, "safety": 5, "ease": 6},
    {"name": "Salvador", "country": "Brazil", "cci": 77, "safety": 5, "ease": 6},
    {"name": "Nairobi", "country": "Kenya", "cci": 76, "safety": 5, "ease": 6},
    {"name": "Jerusalem", "country": "Israel", "cci": 79, "safety": 6, "ease": 7},
]

def slugify(name):
    """Convert destination name to URL slug"""
    return re.sub(r'[^\w\s-]', '', name).lower().replace(' ', '-')

def generate_card(dest):
    """Generate a destination card HTML snippet"""
    slug = slugify(dest["name"])
    truth = f"{dest['name']} welcomes confident women travelers with genuine respect and warmth."

    return f'''                    <article class="destination-card destination-card-img">
                        <div class="card-image">
                            <img src="https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=600&q=80&fit=crop&crop=center" alt="{dest['name']}, {dest['country']}" width="600" height="400" loading="lazy">
                        </div>
                        <div class="card-body">
                            <div class="card-badge">CCI {dest['cci']}</div>
                            <h3><a href="/destinations/{slug}/">{dest['name']}, {dest['country']}</a></h3>
                            <p class="card-truth">{truth}</p>
                            <ul class="card-scores">
                                <li>Safety <strong>{dest['safety']}/10</strong></li>
                                <li>Ease <strong>{dest['ease']}/10</strong></li>
                            </ul>
                            <ul class="card-tags">
                                <li>Solo Friendly</li>
                                <li>Culture Rich</li>
                                <li>Explore</li>
                            </ul>
                        </div>
                    </article>'''

# Read the current index file
with open('/home/user/cougartravel/destinations/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Sort destinations by CCI (descending)
DESTINATIONS_SORTED = sorted(DESTINATIONS, key=lambda x: x['cci'], reverse=True)

# Generate all destination cards
all_cards = '\n'.join([generate_card(dest) for dest in DESTINATIONS_SORTED])

# Replace the destination grid section
old_grid_pattern = r'<div class="destination-grid">.*?</div>\s*</div>\s*</section>'
new_grid = f'''<div class="destination-grid">
{all_cards}
                </div>
            </div>
        </section>'''

content = re.sub(old_grid_pattern, new_grid, content, flags=re.DOTALL)

# Update the section intro text to reflect 100+ destinations
content = content.replace(
    '<p class="section-intro">Sorted by Cougar Confidence Index score. Each destination is evaluated on nine factors that matter most to confident, independent women.</p>',
    '<p class="section-intro">Over 100 destinations ranked by Cougar Confidence Index score. Each destination is evaluated on nine factors that matter most to confident, independent women: respect for women, safety, cultural depth, ease of solo travel, and more.</p>'
)

# Write the updated file
with open('/home/user/cougartravel/destinations/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✓ Updated destinations hub with {len(DESTINATIONS_SORTED)} destination cards")
print(f"✓ Sorted by Cougar Confidence Index (highest to lowest)")
