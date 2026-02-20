#!/usr/bin/env python3
"""
Update the routes hub to include all 16 curated routes
"""

import re

ROUTES = [
    {
        "name": "The European Reinvention Route",
        "slug": "european-reinvention",
        "stops": "Lisbon → Barcelona → Amalfi Coast → Paris",
        "description": "Four cities that celebrate confidence, beauty, and the art of starting over. Begin with Lisbon's gentle warmth and golden light — a city that rewards women in transition with kindness and space. Build momentum through Barcelona's creative energy and Mediterranean ease. Slow down along the Amalfi Coast, where the cliffs and the wine teach you what unhurried really means. And arrive in Paris as the woman you've been becoming — sharper, lighter, and certain about what you want for dinner. 3–4 weeks, fully adjustable."
    },
    {
        "name": "The Latin Dance Route",
        "slug": "latin-dance",
        "stops": "Buenos Aires → Havana → Medellín → Mexico City",
        "description": "Tango, salsa, cumbia, and son — four cities where music lives in the streets and the dance floors welcome women who show up with confidence, not perfection. Buenos Aires teaches you tango at midnight milongas where the best dancers are over fifty. Havana fills your evenings with salsa rhythms that forgive every misstep. Medellín pulses with cumbia and warmth. Mexico City wraps it all up with neighborhoods that feel like home. 3–5 weeks, paced for practice and real immersion."
    },
    {
        "name": "The Slow Mediterranean Route",
        "slug": "slow-mediterranean",
        "stops": "Lisbon → Évora → Ravenna → Cinque Terre → Provence",
        "description": "Five destinations for deep breathing, good wine, and the pace of life that actually heals. Gentle introduction to slow living, medieval hilltop towns, Byzantine mosaics, five fishing villages on cliffs, and lavender fields. This is where time works at human speed, and every meal is a meditation. 4–5 weeks of earned rest."
    },
    {
        "name": "The Art & Wine Route",
        "slug": "art-wine",
        "stops": "Florence → Lyon → Bordeaux → Paris",
        "description": "Museums, galleries, and vineyards across Europe's most culturally rich cities. Renaissance masterpieces and Tuscan wine. France's gastronomic capital with world-class museums. The wine capital with châteaux and renowned cellars. And Paris for Louvre, Musée d'Orsay, and infinite galleries. 3–4 weeks for art lovers and wine enthusiasts."
    },
    {
        "name": "The Sacred Cities Route",
        "slug": "sacred-cities",
        "stops": "Jerusalem → Rome → Athens → Istanbul",
        "description": "Four cities where history, spirituality, and women's stories intersect across centuries. Three thousand years of faith in Jerusalem. Sacred layers of pagan temples and Christian churches in Rome. Philosophy's birthplace in Athens. Where East meets West in Istanbul. A spiritual journey through time. 2–3 weeks for seekers."
    },
    {
        "name": "The Healing Coast Route",
        "slug": "healing-coast",
        "stops": "Cascais → Costa Brava → Cinque Terre → Nice",
        "description": "Coastal towns for rest, wellness, and the sound of waves doing their job. Close to Lisbon but worlds away. Hidden coves in Spain. Cliffside villages with swimming. French Riviera sophistication. For recovery, renewal, and post-divorce healing. 2–3 weeks of genuine retreat."
    },
    {
        "name": "The Southeast Asia Escape Route",
        "slug": "southeast-asia",
        "stops": "Bangkok → Chiang Mai → Bali → Hanoi",
        "description": "Three countries where luxury is affordable, spas are sacred, and time moves at your pace. Chaotic and sensory Bangkok. Slow-paced Chiang Mai temples and mountains. Bali's wellness capital and rice terraces. Vietnam's heart in Hanoi. Best for wellness travelers and budget-conscious luxury seekers. 3–4 weeks."
    },
    {
        "name": "The Nordic Light Route",
        "slug": "nordic-light",
        "stops": "Copenhagen → Stockholm → Oslo → Helsinki",
        "description": "Scandinavian cities of design, wellness culture, and long summer days or winter magic. Hygge in Copenhagen. Archipelago islands in Stockholm. Mountains meeting city in Oslo. Design capital Helsinki with sauna culture. For designers, minimalism lovers, and light-seeking travelers. 2–3 weeks."
    },
    {
        "name": "The Reinvention Through Food Route",
        "slug": "food-reinvention",
        "stops": "Mexico City → Lima → Lyon → Bangkok",
        "description": "Four capitals of cuisine where cooking classes, markets, and dining become meditation. Mexico's culinary soul and mole traditions. Peru's gastronomic capital and Andean ingredients. France's food philosophy. Southeast Asia's flavor capital. For food lovers transforming their relationship with pleasure. 3–4 weeks."
    },
    {
        "name": "The Literary Wandering Route",
        "slug": "literary-wandering",
        "stops": "Dublin → Paris → Prague → Barcelona",
        "description": "Cities where writers lived, wrote, and loved — bookshops, cafes, and literary ghosts everywhere. Joyce, Beckett, Heaney in Dublin. Hemingway and Shakespeare and Company in Paris. Kafka's Prague. Mirό and Gaudí in Barcelona. For writers, readers, and seekers of inspiration. 2–3 weeks."
    },
    {
        "name": "The Coastal Reinvention Route",
        "slug": "coastal-reinvention",
        "stops": "Cascais → Costa Brava → Côte d'Azur → Amalfi Coast",
        "description": "Beach towns and cliff villages where change happens slowly, then all at once. Atlantic cliffs and local culture. Hidden coves and small villages. French Riviera elegance. Dramatic cliffs and Mediterranean soul. For women in transition and reset seekers. 2–3 weeks."
    },
    {
        "name": "The Empires & Architecture Route",
        "slug": "empires-architecture",
        "stops": "Vienna → Prague → Budapest → Krakow",
        "description": "Built history: palaces, fortresses, and the stones that tell who held power. Hapsburg palaces in Vienna. Medieval beauty in Prague. Austro-Hungarian grandeur in Budapest. Renaissance courtyards in Krakow. For history buffs and architecture lovers. 3–4 weeks."
    },
    {
        "name": "The Tropical Wellness Route",
        "slug": "tropical-wellness",
        "stops": "Ubud → Koh Samui → Phuket",
        "description": "Island and jungle destinations for complete reset: spa, yoga, nature immersion. Yoga and rice terraces in Ubud. Island wellness and spa resorts in Thailand. For wellness travelers and digital detox needs. 2–3 weeks of healing."
    },
    {
        "name": "The African Safari & Culture Route",
        "slug": "african-safari",
        "stops": "Cape Town → Kigali → Volcanoes NP → Serengeti",
        "description": "Wildlife, landscape, and cultures where women travelers are welcomed and cherished. Table Mountain in Cape Town. Gorilla trekking in Rwanda. Wildlife spectacle in Tanzania's Serengeti. For adventure travelers and wildlife enthusiasts. 2–3 weeks of transformation."
    },
    {
        "name": "The Reinvention Across Time Zones Route",
        "slug": "time-zone-adventure",
        "stops": "Tokyo → Bangkok → Istanbul → Rome",
        "description": "East-meets-West journey: precision Tokyo to sensory Bangkok to East-meets-West Istanbul to ancient Rome. Chasing light and complete worldview shifts. For extended travelers and adventurous explorers. 4–5 weeks."
    },
    {
        "name": "The Off-Season Explorer Route",
        "slug": "off-season",
        "stops": "Barcelona → Venice → Florence → Vienna → Prague",
        "description": "European cities in autumn when tourists fade, light turns golden, and the real city shows up. September-October is when these cities become themselves again. Golden light, fewer crowds, authentic experiences. 3–4 weeks for crowds-averse travelers."
    }
]

def generate_route_card(route):
    """Generate a route card HTML"""
    return f"""                    <article class="route-card route-card-img">
                        <div class="route-image">
                            <img src="https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=600&q=80&fit=crop&crop=center" alt="{route['name']}" width="600" height="280" loading="lazy">
                        </div>
                        <div class="route-body">
                            <h3><a href="/routes/{route['slug']}/">{route['name']}</a></h3>
                            <p class="route-stops">{route['stops']}</p>
                            <p>{route['description']}</p>
                        </div>
                    </article>"""

# Read the current routes index
with open('/home/user/cougartravel/routes/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Generate all route cards
all_cards = '\n'.join([generate_route_card(route) for route in ROUTES])

# Replace the route-grid section
old_grid_pattern = r'<div class="route-grid">.*?</div>\s*</div>\s*</section>'
new_grid = f"""<div class="route-grid">
{all_cards}
                </div>
            </div>
        </section>"""

content = re.sub(old_grid_pattern, new_grid, content, flags=re.DOTALL)

# Update the section intro
content = content.replace(
    '<p class="section-intro">Each route connects destinations that flow naturally together &mdash; by geography, culture, and the kind of energy they reward. Built for women who want more than a single city, and who know that the journey between places is part of the point.</p>',
    '<p class="section-intro">Over 16 curated journeys connecting destinations that flow naturally together — by geography, culture, and the kind of energy they reward. Built for women who want more than a single city, and who know that the journey between places is part of the point. Choose by your mood: reinvention, dance, food, art, wellness, adventure, culture, or healing.</p>'
)

# Write the updated file
with open('/home/user/cougartravel/routes/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✓ Updated routes hub with {len(ROUTES)} route cards")
print("✓ Routes include: European Reinvention, Latin Dance, Mediterranean, Art & Wine, Sacred Cities, and more")
