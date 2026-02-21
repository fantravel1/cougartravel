#!/usr/bin/env python3
"""
Generate 15+ curated route pages for CougarTravel
Each route includes full itineraries, hotels, experiences, and practical details
"""

import os
import re

ROUTES = [
    {
        "name": "The European Reinvention Route",
        "slug": "european-reinvention",
        "subtitle": "Four cities that celebrate confidence, beauty, and the art of starting over",
        "duration": "21–28 days",
        "cost": "$4,500–7,500 per person",
        "season": "April–June, September–October",
        "best_for": "Women in transition, post-divorce travel, solo explorers, cultural deep-divers",
        "stops": [
            {
                "city": "Lisbon, Portugal",
                "days": 5,
                "summary": "Begin with Lisbon's gentle warmth and golden light — a city that rewards women in transition with kindness and space.",
                "highlights": [
                    "Miradouros (viewpoints) at sunset with vinho verde",
                    "Belém pastéis de nata masterclass",
                    "Fado music in Alfama (authentic, not touristy)",
                    "São Jorge Castle for solitude and perspective",
                    "Sintra day trip: palaces and forest walks"
                ]
            },
            {
                "city": "Barcelona, Spain",
                "days": 4,
                "summary": "Build momentum through Barcelona's creative energy and Mediterranean ease.",
                "highlights": [
                    "Gaudí's Sagrada Familia (morning, fewer crowds)",
                    "Park Güell at sunset for golden-hour reflection",
                    "El Born neighborhood: galleries, tapas, wandering",
                    "Beach walk at Barceloneta",
                    "Gothic Quarter alleyways and hidden plazas"
                ]
            },
            {
                "city": "Amalfi Coast, Italy",
                "days": 5,
                "summary": "Slow down along the cliffs, where the wine and the views teach you what unhurried really means.",
                "highlights": [
                    "Positano: steep streets, pastel villages, limoncello",
                    "Ravello: gardens and terraces at altitude",
                    "Amalfi town: ceramics and lemons",
                    "Boat ride to Emerald Grotto",
                    "Coastal walks between villages"
                ]
            },
            {
                "city": "Paris, France",
                "days": 6,
                "summary": "Arrive as the woman you've been becoming — sharper, lighter, and certain about what you want.",
                "highlights": [
                    "Musée de l'Orangerie for water lilies and solitude",
                    "Canal Saint-Martin morning walk",
                    "Marais museums and galleries",
                    "Latin Quarter bookshops and cafes",
                    "Dinner reservations at neighborhood bistros"
                ]
            }
        ]
    },
    {
        "name": "The Latin Dance Route",
        "slug": "latin-dance",
        "subtitle": "Four cities where music lives in the streets and the dance floors welcome women with confidence",
        "duration": "21–35 days",
        "cost": "$3,500–5,500 per person",
        "season": "Year-round (winter warmest)",
        "best_for": "Dance enthusiasts, sensuality seekers, women embracing their bodies, solo travelers, music lovers",
        "stops": [
            {
                "city": "Buenos Aires, Argentina",
                "days": 7,
                "summary": "Tango at midnight milongas where the best dancers are over fifty. This is where tango happens.",
                "highlights": [
                    "Midnight tango milongas (4am finales)",
                    "Tango lesson with professional dancers",
                    "San Telmo antique markets and atmosphere",
                    "Recoleta cemetery and historic neighborhoods",
                    "Wine tastings and parrilla (grill) dinners"
                ]
            },
            {
                "city": "Havana, Cuba",
                "days": 5,
                "summary": "Salsa rhythms fill the evenings. The dance floors forgive every misstep.",
                "highlights": [
                    "Casa de la Música salsa club (locals, not tourists)",
                    "Tropicana for full-production cabaret",
                    "Old Havana restoration walk and mojitos",
                    "Malecon sunset and seafront stroll",
                    "Salsa lesson at a local studio"
                ]
            },
            {
                "city": "Medellín, Colombia",
                "days": 5,
                "summary": "Cumbia pulses through this reinvented city with genuine warmth and creative energy.",
                "highlights": [
                    "Comuna 13 graffiti tour (transformed neighborhood)",
                    "Cumbia dancing at Gusto",
                    "Plaza Botero art and culture",
                    "Cable car views over the city",
                    "Flower Festival (if traveling late August)"
                ]
            },
            {
                "city": "Mexico City, Mexico",
                "days": 5,
                "summary": "Son jarocho, cumbia, and salsa traditions wrap it all up in neighborhoods that feel like home.",
                "highlights": [
                    "Ballet Folklórico for cultural immersion",
                    "Dance lessons at cultural centers",
                    "Frida Kahlo and Diego Rivera museums",
                    "Condesa neighborhood wandering and cafes",
                    "Teotihuacán pyramids day trip"
                ]
            }
        ]
    },
    {
        "name": "The Slow Mediterranean Route",
        "slug": "slow-mediterranean",
        "subtitle": "Five destinations for deep breathing, good wine, and the pace of life that actually heals",
        "duration": "28–35 days",
        "cost": "$4,000–6,500 per person",
        "season": "May–June, September–October",
        "best_for": "Wellness seekers, slow travelers, writers and artists, post-loss journeys, burnout recovery",
        "stops": [
            {
                "city": "Lisbon, Portugal",
                "days": 4,
                "summary": "Gentle introduction to the slow life with golden light and terraced views.",
                "highlights": [
                    "Daily cafe sitting with notebook",
                    "Thermal baths in nearby Caldas da Rainha",
                    "Vintage bookshop browsing",
                    "Sunday markets and local food culture",
                    "Quiet monastery visits"
                ]
            },
            {
                "city": "Évora, Portugal",
                "days": 3,
                "summary": "Medieval hilltop town for genuine retreat and stillness.",
                "highlights": [
                    "Walled old town exploration",
                    "Roman temple and chapel of bones",
                    "Countryside wine tastings",
                    "Silence and stone architecture",
                    "Olive groves and countryside drives"
                ]
            },
            {
                "city": "Ravenna, Italy",
                "days": 3,
                "summary": "Byzantine mosaics and quiet piazzas — art and architecture for the contemplative mind.",
                "highlights": [
                    "Basilica mosaics and sacred art",
                    "Dante's tomb and literary history",
                    "Piadina (flatbread) makers and street food",
                    "Adriatic beaches nearby",
                    "Small-town Italian rhythm"
                ]
            },
            {
                "city": "Cinque Terre, Italy",
                "days": 4,
                "summary": "Five fishing villages on cliffs where modern life hasn't stolen the magic.",
                "highlights": [
                    "Hiking between villages at your own pace",
                    "Pesto-making classes",
                    "Swimming in Mediterranean coves",
                    "Train rides between towns",
                    "Fresh pasta and local wine"
                ]
            },
            {
                "city": "Provence, France",
                "days": 5,
                "summary": "Lavender, markets, and the color of contentment at every turn.",
                "highlights": [
                    "Lavender fields at peak bloom (July)",
                    "Provençal markets (Tuesday-Sunday)",
                    "Cooking classes with local chefs",
                    "Hilltop village wandering",
                    "Wine tastings in Châteauneuf-du-Pape"
                ]
            }
        ]
    },
    {
        "name": "The Art & Wine Route",
        "slug": "art-wine",
        "subtitle": "Museums, galleries, and vineyards across Europe's most culturally rich cities",
        "duration": "21–28 days",
        "cost": "$4,500–7,000 per person",
        "season": "September–November, March–May",
        "best_for": "Art collectors, wine enthusiasts, museum lovers, intellectuals, cultural deep-divers",
        "stops": [
            {
                "city": "Florence, Italy",
                "days": 5,
                "summary": "Renaissance masterpieces and Tuscan wine in the city that invented the modern world.",
                "highlights": [
                    "Uffizi Gallery early-morning visit",
                    "Accademia for Michelangelo's David",
                    "Chianti wine tasting in vineyards",
                    "Ponte Vecchio and leather markets",
                    "Duomo and climbing the dome"
                ]
            },
            {
                "city": "Lyon, France",
                "days": 4,
                "summary": "France's gastronomic capital with world-class museums and silk-weaving heritage.",
                "highlights": [
                    "Musée des Beaux-Arts (major collection)",
                    "Bouchon (traditional Lyonnaise restaurant) dining",
                    "Confluence Museum of modern culture",
                    "Silk district and textile history",
                    "Rhône wine tastings"
                ]
            },
            {
                "city": "Bordeaux, France",
                "days": 4,
                "summary": "The wine capital: châteaux, vineyards, and world-renowned cellars.",
                "highlights": [
                    "Left Bank wine region tours",
                    "Right Bank Pomerol tastings",
                    "Musée de l'Aquarium and cultural spaces",
                    "18th-century architecture walks",
                    "Cooking classes with wine pairings"
                ]
            },
            {
                "city": "Paris, France",
                "days": 6,
                "summary": "The art capital: Louvre, Musée d'Orsay, and neighborhood galleries without end.",
                "highlights": [
                    "Louvre early-morning masterpieces",
                    "Musée d'Orsay for Impressionists",
                    "Marais galleries and contemporary art",
                    "Latin Quarter bookshops and museums",
                    "Wine bar tastings in small neighborhoods"
                ]
            }
        ]
    },
    {
        "name": "The Sacred Cities Route",
        "slug": "sacred-cities",
        "subtitle": "Four cities where history, spirituality, and women's stories intersect across centuries",
        "duration": "18–24 days",
        "cost": "$3,500–5,500 per person",
        "season": "October–April (avoid summer crowds)",
        "best_for": "Spiritual seekers, history enthusiasts, women on pilgrimages, philosophical travelers, writers",
        "stops": [
            {
                "city": "Jerusalem, Israel",
                "days": 4,
                "summary": "Three thousand years of faith, conflict, and resilience in one ancient city.",
                "highlights": [
                    "Old City walking tours (early morning)",
                    "Western Wall and Temple Mount",
                    "Church of the Holy Sepulchre",
                    "Muslim Quarter markets and voices",
                    "Mount of Olives at sunrise"
                ]
            },
            {
                "city": "Rome, Italy",
                "days": 5,
                "summary": "Rome's sacred layers: pagan temples, Christian churches, and women's power through time.",
                "highlights": [
                    "Vatican and Sistine Chapel (early tickets)",
                    "Pantheon and pagan origins",
                    "Pilgrimage churches and women saints",
                    "Catacombs and early Christian history",
                    "Roman Forum and ancient women's roles"
                ]
            },
            {
                "city": "Athens, Greece",
                "days": 4,
                "summary": "Where philosophy was born: democracy, wisdom, and the goddesses who ruled it all.",
                "highlights": [
                    "Parthenon and Acropolis Museum",
                    "Delphi day trip (Oracle's sanctuary)",
                    "Ancient Agora and philosophical sites",
                    "Museum of Cycladic Art (female figurines)",
                    "Plaka wandering and philosopher cafes"
                ]
            },
            {
                "city": "Istanbul, Turkey",
                "days": 4,
                "summary": "Where East meets West, sacred converges with secular, and women navigate centuries of power.",
                "highlights": [
                    "Blue Mosque and Hagia Sophia",
                    "Topkapi Palace and sultans' stories",
                    "Sufi whirling ceremony experience",
                    "Grand Bazaar and spice markets",
                    "Bosphorus sunset crossing"
                ]
            }
        ]
    },
    {
        "name": "The Healing Coast Route",
        "slug": "healing-coast",
        "subtitle": "Coastal towns for rest, wellness, and the sound of waves doing their job",
        "duration": "14–21 days",
        "cost": "$2,500–4,500 per person",
        "season": "May–October (warm waters)",
        "best_for": "Recovery and renewal, post-divorce travel, burnout recovery, solo introspection, wellness seekers",
        "stops": [
            {
                "city": "Cascais, Portugal",
                "days": 3,
                "summary": "Close to Lisbon but worlds away: cliffs, golden beaches, and coastal walks that heal.",
                "highlights": [
                    "Cliff walks overlooking the Atlantic",
                    "Swimming and coastal exploration",
                    "Seafood restaurants on the water",
                    "Nearby Sintra mountains for contrast",
                    "Calm beach towns nearby"
                ]
            },
            {
                "city": "Costa Brava, Spain",
                "days": 4,
                "summary": "Cala coves, pine trees to the water's edge, and Mediterranean warmth.",
                "highlights": [
                    "Hiking between hidden coves",
                    "Swimming in turquoise water",
                    "Paella dinners overlooking the sea",
                    "Small village wandering",
                    "Underwater snorkeling"
                ]
            },
            {
                "city": "Cinque Terre, Italy",
                "days": 4,
                "summary": "Cliffside villages with train connections — hiking, swimming, and genuine retreat.",
                "highlights": [
                    "Village-to-village hiking trails",
                    "Mediterranean swimming",
                    "Pesto and fresh pasta",
                    "Wine from terraced vineyards",
                    "Sunset watching from the rocks"
                ]
            },
            {
                "city": "Nice, France",
                "days": 4,
                "summary": "French Riviera sophistication with beach culture and Promenade des Anglais ease.",
                "highlights": [
                    "Shingle beach and Mediterranean",
                    "Promenade walks and cafe culture",
                    "Old Town (Vieux Nice) wandering",
                    "Museum visits (Chagall, Matisse)",
                    "Port restaurants and evening strolls"
                ]
            }
        ]
    },
    {
        "name": "The Southeast Asia Escape Route",
        "slug": "southeast-asia",
        "subtitle": "Three countries where luxury is affordable, spas are sacred, and time moves at your pace",
        "duration": "21–28 days",
        "cost": "$2,500–4,000 per person",
        "season": "November–February (cool and dry)",
        "best_for": "Wellness travelers, budget-conscious luxury seekers, spa lovers, culture explorers, extended travelers",
        "stops": [
            {
                "city": "Bangkok, Thailand",
                "days": 3,
                "summary": "Chaotic, sensory, and deeply alive — markets, temples, and street food that changes you.",
                "highlights": [
                    "Grand Palace and Wat Phra Kaew",
                    "Floating markets early morning",
                    "Traditional Thai massage training",
                    "Street food tours in Bangkok neighborhoods",
                    "Muay Thai culture and boxing gyms"
                ]
            },
            {
                "city": "Chiang Mai, Thailand",
                "days": 5,
                "summary": "Northern Thailand's slow-paced heartland: temples, mountains, and daily life at human speed.",
                "highlights": [
                    "Temple visits and monk talks",
                    "Cooking class with local families",
                    "Elephant sanctuaries (ethical only)",
                    "Mountain hiking and viewpoints",
                    "Night markets and street food"
                ]
            },
            {
                "city": "Bali, Indonesia",
                "days": 6,
                "summary": "Wellness capital with rice terraces, spa culture, and spiritual energy.",
                "highlights": [
                    "Yoga and meditation centers",
                    "Spa treatments and traditional healing",
                    "Rice terrace walks in Ubud",
                    "Temple visits and rituals",
                    "Beach time in Seminyak or Canggu"
                ]
            },
            {
                "city": "Hanoi, Vietnam",
                "days": 5,
                "summary": "Vietnam's heart: narrow streets, complex history, and food that tells stories.",
                "highlights": [
                    "Old Quarter walking tours",
                    "Hoan Kiem Lake and temple area",
                    "War Museum and historical context",
                    "Street food tours by motorbike",
                    "Perfume River sunset cruise"
                ]
            }
        ]
    },
    {
        "name": "The Nordic Light Route",
        "slug": "nordic-light",
        "subtitle": "Scandinavian cities of design, wellness culture, and long summer days (or winter magic)",
        "duration": "14–21 days",
        "cost": "$3,500–5,500 per person",
        "season": "June–August (long days), December (winter lights)",
        "best_for": "Design enthusiasts, minimalism lovers, wellness seekers, architecture nerds, light-seeking travelers",
        "stops": [
            {
                "city": "Copenhagen, Denmark",
                "days": 4,
                "summary": "Hygge capital: design, cycling, and happiness engineered into the everyday.",
                "highlights": [
                    "Nyhavn canal walks and restaurant sits",
                    "Tivoli Gardens for pure joy",
                    "Design and craft museums",
                    "Cycling like locals",
                    "Smørrebrød (open sandwich) experience"
                ]
            },
            {
                "city": "Stockholm, Sweden",
                "days": 4,
                "summary": "On water, islands, and forests: Nordic beauty meets sophisticated design.",
                "highlights": [
                    "Archipelago boat tours",
                    "Vasa Museum and maritime history",
                    "Modern art museums",
                    "Gamla Stan (Old Town) wandering",
                    "Sauna culture and spa time"
                ]
            },
            {
                "city": "Oslo, Norway",
                "days": 4,
                "summary": "Mountains meet city: Viking history, modern art, and Nordic wellness.",
                "highlights": [
                    "Viking Ship Museum",
                    "Munch Museum (The Scream and more)",
                    "Vigeland Park sculpture garden",
                    "Fjord views and hiking access",
                    "Restaurant culture and local design"
                ]
            },
            {
                "city": "Helsinki, Finland",
                "days": 3,
                "summary": "Design capital of the north: architecture, saunas, and Nordic minimalism.",
                "highlights": [
                    "Sauna culture (public saunas)",
                    "Architecture walking tours",
                    "Design and craft museums",
                    "Suomenlinna island ferry trip",
                    "Modern restaurant and food scene"
                ]
            }
        ]
    },
    {
        "name": "The Reinvention Through Food Route",
        "slug": "food-reinvention",
        "subtitle": "Four capitals of cuisine where cooking classes, markets, and dining become meditation",
        "duration": "21–28 days",
        "cost": "$4,500–6,500 per person",
        "season": "September–November, March–May",
        "best_for": "Food lovers, cooking enthusiasts, people transforming their relationship with pleasure, culinary explorers",
        "stops": [
            {
                "city": "Mexico City, Mexico",
                "days": 5,
                "summary": "Mexico's culinary soul: markets, mole traditions, and food that is philosophy.",
                "highlights": [
                    "Cooking classes in home kitchens",
                    "Oaxaca day trip for mole deep-dive",
                    "Merced Market exploration",
                    "Street food and taco tours",
                    "Mezcal tastings and agave education"
                ]
            },
            {
                "city": "Lima, Peru",
                "days": 4,
                "summary": "The gastronomic capital of South America: Andean ingredients and Peruvian soul.",
                "highlights": [
                    "Cooking class with Peruvian chef",
                    "Central Market (Mercado Central) tour",
                    "Cevichería crawl and seafood mastery",
                    "Mistura food festival (September)",
                    "Sacred Valley farm visits"
                ]
            },
            {
                "city": "Lyon, France",
                "days": 4,
                "summary": "France's gastronomic capital where food is not just nourishment—it's identity.",
                "highlights": [
                    "Cooking class in Michelin-chef kitchens",
                    "Bouchon traditional restaurant dining",
                    "Quenelles and Lyonnaise specialties",
                    "Paul Bocuse Market exploration",
                    "Wine and cheese education"
                ]
            },
            {
                "city": "Bangkok, Thailand",
                "days": 5,
                "summary": "Southeast Asia's flavor capital: street food education and cooking mastery.",
                "highlights": [
                    "Thai cooking classes (all levels)",
                    "Floating market food tours",
                    "Street food crawls by neighborhood",
                    "Spice market education",
                    "Street vendor cooking lessons"
                ]
            }
        ]
    },
    {
        "name": "The Literary Wandering Route",
        "slug": "literary-wandering",
        "subtitle": "Cities where writers lived, wrote, and loved — bookshops, cafes, and literary ghosts everywhere",
        "duration": "18–24 days",
        "cost": "$3,500–5,000 per person",
        "season": "September–May",
        "best_for": "Writers, readers, literary enthusiasts, seekers of inspiration, introverts who love stories",
        "stops": [
            {
                "city": "Dublin, Ireland",
                "days": 4,
                "summary": "Joyce, Beckett, Heaney: Dublin's literary DNA is everywhere.",
                "highlights": [
                    "Joyce Centre and literary tours",
                    "Abbey Theatre and Irish drama",
                    "Guinness Storehouse and Temple Bar",
                    "Literary pub crawls",
                    "Trinity College library and Book of Kells"
                ]
            },
            {
                "city": "Paris, France",
                "days": 5,
                "summary": "Shakespeare and Company, Hemingway's cafes, and a century of writers in exile and love.",
                "highlights": [
                    "Shakespeare and Company bookshop (hours)",
                    "Hemingway's bar and café haunts",
                    "Latin Quarter literary history",
                    "Musée Delacroix and artist homes",
                    "Evening poetry readings (in English)"
                ]
            },
            {
                "city": "Prague, Czech Republic",
                "days": 4,
                "summary": "Kafka's city: literature, magic, and a whole different eastern European literary tradition.",
                "highlights": [
                    "Kafka Museum and biographical tours",
                    "Old Town Square literary walks",
                    "Charles Bridge and atmospheric strolls",
                    "Independent bookshops and cafes",
                    "Bohemian culture and artistic heritage"
                ]
            },
            {
                "city": "Barcelona, Spain",
                "days": 4,
                "summary": "Mirό, Gaudí, and García Márquez: literary and artistic convergence.",
                "highlights": [
                    "Bookshops and rare collections",
                    "El Born's literary bar scene",
                    "Modernisme architecture and design",
                    "Montjuïc museums",
                    "Local author readings and literary events"
                ]
            }
        ]
    },
    {
        "name": "The Coastal Reinvention Route",
        "slug": "coastal-reinvention",
        "subtitle": "Beach towns and cliff villages where change happens slowly, then all at once",
        "duration": "14–21 days",
        "cost": "$2,500–4,000 per person",
        "season": "May–September",
        "best_for": "Women in transition, post-divorce retreat, solo soul-searching, beach lovers, reset seekers",
        "stops": [
            {
                "city": "Cascais, Portugal",
                "days": 4,
                "summary": "Atlantic cliffs, local culture, and the pace that allows real thinking.",
                "highlights": [
                    "Cliff-edge walks at any time",
                    "Swimming and coastal exploration",
                    "Seafood dinners on the water",
                    "Nearby Lisbon escapes",
                    "Artist communities and creative vibes"
                ]
            },
            {
                "city": "Costa Brava, Spain",
                "days": 3,
                "summary": "Hidden coves and small villages where time works differently.",
                "highlights": [
                    "Cala cove swimming",
                    "Hiking between villages",
                    "Fish restaurants overlooking water",
                    "Snorkeling in turquoise water",
                    "Evening paseo and quiet reflection"
                ]
            },
            {
                "city": "Côte d'Azur, France",
                "days": 4,
                "summary": "French Riviera elegance with beach culture and genuine warmth.",
                "highlights": [
                    "Nice beachfront and promenade",
                    "Antibes old town and marina",
                    "Cannes less-touristy neighborhoods",
                    "Grasse perfume capital day trip",
                    "Evening waterfront dining"
                ]
            },
            {
                "city": "Amalfi Coast, Italy",
                "days": 4,
                "summary": "Dramatic cliffs, villages on hillsides, and food that tastes like the sun.",
                "highlights": [
                    "Positano pastel village wandering",
                    "Ravello high-altitude gardens",
                    "Lemon grove visits",
                    "Boat swims in hidden coves",
                    "Local pasta and seafood traditions"
                ]
            }
        ]
    },
    {
        "name": "The Empires & Architecture Route",
        "slug": "empires-architecture",
        "subtitle": "Built history: palaces, fortresses, and the stones that tell who held power",
        "duration": "21–28 days",
        "cost": "$3,500–5,500 per person",
        "season": "April–May, September–October",
        "best_for": "History buffs, architecture lovers, heritage explorers, museum enthusiasts, scholarly travelers",
        "stops": [
            {
                "city": "Vienna, Austria",
                "days": 5,
                "summary": "Hapsburg empire: palaces, concert halls, and the glory days of Central European power.",
                "highlights": [
                    "Schönbrunn Palace and gardens",
                    "St. Stephen's Cathedral exploration",
                    "Hofburg Palace and imperial apartments",
                    "Vienna State Opera and music",
                    "Kunsthistorisches Museum masterpieces"
                ]
            },
            {
                "city": "Prague, Czech Republic",
                "days": 4,
                "summary": "Medieval beauty: castles, bridges, and centuries of contested history.",
                "highlights": [
                    "Prague Castle complex and gardens",
                    "Charles Bridge and architectural detail",
                    "St. Vitus Cathedral and craftsmanship",
                    "Old Town Square and astronomical clock",
                    "Jewish Quarter history and museums"
                ]
            },
            {
                "city": "Budapest, Hungary",
                "days": 5,
                "summary": "Austro-Hungarian grandeur on the Danube: thermal baths and architectural splendor.",
                "highlights": [
                    "Thermal baths (Széchenyi, Gellért)",
                    "Buda Castle and hilltop palace",
                    "Parliament Building architecture",
                    "Danube cruise and city views",
                    "Jewish Quarter hidden synagogues"
                ]
            },
            {
                "city": "Krakow, Poland",
                "days": 4,
                "summary": "Medieval market squares, Renaissance courtyards, and the weight of 20th century history.",
                "highlights": [
                    "Wawel Castle and royal apartments",
                    "Main Market Square and cloth hall",
                    "Kazimierz Jewish quarter",
                    "Schindler's Factory museum tour",
                    "Church of the Holy Cross architecture"
                ]
            }
        ]
    },
    {
        "name": "The Tropical Wellness Route",
        "slug": "tropical-wellness",
        "subtitle": "Island and jungle destinations for complete reset: spa, yoga, nature immersion",
        "duration": "14–21 days",
        "cost": "$2,000–3,500 per person",
        "season": "December–April",
        "best_for": "Wellness travelers, yoga enthusiasts, spa seekers, digital detox needs, recovery from burnout",
        "stops": [
            {
                "city": "Ubud, Bali",
                "days": 6,
                "summary": "Yoga, rice terraces, and healing traditions that work.",
                "highlights": [
                    "Yoga and meditation centers",
                    "Spa and massage culture",
                    "Rice terrace walks and farming",
                    "Art galleries and craft studios",
                    "Temple visits and rituals"
                ]
            },
            {
                "city": "Koh Samui, Thailand",
                "days": 4,
                "summary": "Island wellness: beaches, spa resorts, and tropical healing.",
                "highlights": [
                    "Spa resort pampering days",
                    "Beach time and water activities",
                    "Wellness centers and holistic healing",
                    "Thai massage training",
                    "Sunset beach walks"
                ]
            },
            {
                "city": "Phuket, Thailand",
                "days": 4,
                "summary": "Larger island with wellness centers, beaches, and adventure access.",
                "highlights": [
                    "Luxury spa resorts",
                    "Beach clubs and water sports",
                    "Phi Phi Islands day trips",
                    "Thai cooking and wellness food",
                    "Snorkeling and marine beauty"
                ]
            }
        ]
    },
    {
        "name": "The African Safari & Culture Route",
        "slug": "african-safari",
        "subtitle": "Wildlife, landscape, and cultures where women travelers are welcomed and cherished",
        "duration": "14–18 days",
        "cost": "$3,500–5,500 per person",
        "season": "June–August (dry season)",
        "best_for": "Adventure travelers, wildlife enthusiasts, nature lovers, women seeking transformative experiences",
        "stops": [
            {
                "city": "Cape Town, South Africa",
                "days": 3,
                "summary": "Mountain meeting ocean: Table Mountain hikes and urban sophistication.",
                "highlights": [
                    "Table Mountain cable car and hikes",
                    "Cape Peninsula scenic drive",
                    "Robben Island historical tour",
                    "Bo-Kaap colorful neighborhoods",
                    "Waterfront dining and shopping"
                ]
            },
            {
                "city": "Kigali, Rwanda",
                "days": 2,
                "summary": "Rwanda's healing capital: genocide memorial, gorilla trekking access point.",
                "highlights": [
                    "Kigali Genocide Memorial",
                    "Local markets and food",
                    "Women's cooperatives and weaving",
                    "Gateway to mountain gorilla trekking",
                    "Vibrant music and nightlife"
                ]
            },
            {
                "city": "Volcanoes National Park, Rwanda",
                "days": 3,
                "summary": "Mountain gorilla trekking: one of Earth's most transformative experiences.",
                "highlights": [
                    "Mountain gorilla trekking (permit-based)",
                    "Bisoke volcano hike",
                    "Local village visits",
                    "Bird watching and nature immersion",
                    "High-altitude forest walks"
                ]
            },
            {
                "city": "Serengeti, Tanzania",
                "days": 4,
                "summary": "Wildlife spectacle: elephants, lions, zebras, and the circle of life in real time.",
                "highlights": [
                    "Safari game drives (multiple per day)",
                    "Wildebeest migration (if timing right)",
                    "Big Five viewing",
                    "Maasai Mara connections",
                    "Hot air balloon safari at sunrise"
                ]
            }
        ]
    },
    {
        "name": "The Reinvention Across Time Zones Route",
        "slug": "time-zone-adventure",
        "subtitle": "East-meets-West journey: Tokyo to Bangkok to Istanbul, chasing light and transformation",
        "duration": "28–35 days",
        "cost": "$5,000–7,500 per person",
        "season": "October–April",
        "best_for": "Extended travelers, jet-lag enthusiasts, women seeking complete worldview shifts, adventurous explorers",
        "stops": [
            {
                "city": "Tokyo, Japan",
                "days": 5,
                "summary": "Precision, beauty, and hyper-modern living—safe enough to let your guard completely down.",
                "highlights": [
                    "Senso-ji Temple and Asakusa",
                    "Shibuya Crossing and neighborhoods",
                    "Tsukiji Outer Market food tours",
                    "Tea ceremony and traditional arts",
                    "Imperial Palace and city views"
                ]
            },
            {
                "city": "Bangkok, Thailand",
                "days": 4,
                "summary": "Chaotic sensory explosion: temples, markets, and the opposite of Tokyo's order.",
                "highlights": [
                    "Grand Palace and sacred temples",
                    "Floating markets at dawn",
                    "Street food and night markets",
                    "Muay Thai and boxing culture",
                    "Chao Phraya River cruises"
                ]
            },
            {
                "city": "Istanbul, Turkey",
                "days": 5,
                "summary": "Straddling continents: where East truly meets West, sacred meets secular.",
                "highlights": [
                    "Blue Mosque and Hagia Sophia",
                    "Topkapi Palace exploration",
                    "Grand Bazaar and spice markets",
                    "Bosphorus cruise at sunset",
                    "Sufi whirling ceremony"
                ]
            },
            {
                "city": "Rome, Italy",
                "days": 4,
                "summary": "Return to the West with 3,000 years of history underfoot.",
                "highlights": [
                    "Colosseum and Roman Forum",
                    "Vatican and Sistine Chapel",
                    "Trevi Fountain and baroque grandeur",
                    "Renaissance art and churches",
                    "Dinner in charming neighborhoods"
                ]
            }
        ]
    },
    {
        "name": "The Off-Season Explorer Route",
        "slug": "off-season",
        "subtitle": "European cities in autumn when tourists fade, light turns golden, and the real city shows up",
        "duration": "18–24 days",
        "cost": "$3,500–5,000 per person",
        "season": "September–October (primarily)",
        "best_for": "Cultural explorers, crowds-averse travelers, photographers, introverts, authentic experience seekers",
        "stops": [
            {
                "city": "Barcelona, Spain",
                "days": 4,
                "summary": "September-October Barcelona: warm, fewer tourists, perfect for wandering.",
                "highlights": [
                    "Park Güell golden-hour walks",
                    "Sagrada Familia without throngs",
                    "La Boqueria market (local food)",
                    "Gothic Quarter quiet exploration",
                    "Beach time in moderate weather"
                ]
            },
            {
                "city": "Venice, Italy",
                "days": 3,
                "summary": "Autumn Venice: fewer cruise ships, restored canals, genuine Venetian life.",
                "highlights": [
                    "St. Mark's with shorter queues",
                    "Gondola rides and canal wandering",
                    "Local neighborhoods (Dorsoduro)",
                    "Rialto Bridge and markets",
                    "Sunset from quiet bridges"
                ]
            },
            {
                "city": "Florence, Italy",
                "days": 4,
                "summary": "October Florence: golden light, manageable crowds, perfect museum hours.",
                "highlights": [
                    "Uffizi Gallery (pre-book)",
                    "Duomo and climbing the dome",
                    "Tuscan countryside day trips",
                    "Leather markets and artisan studios",
                    "Arno River evening walks"
                ]
            },
            {
                "city": "Vienna, Austria",
                "days": 4,
                "summary": "Autumn Vienna: fall colors, coffee house culture, concert season beginning.",
                "highlights": [
                    "Schönbrunn Palace gardens in fall",
                    "St. Stephen's Cathedral quiet hours",
                    "Classical concerts and theater",
                    "Coffee house literary culture",
                    "Danube walk and parks"
                ]
            },
            {
                "city": "Prague, Czech Republic",
                "days": 4,
                "summary": "October Prague: golden light on baroque facades, fewer selfie sticks.",
                "highlights": [
                    "Prague Castle at golden hour",
                    "Charles Bridge morning walks",
                    "Astronomical clock without crowds",
                    "Literary pub crawls",
                    "Neighborhood exploring (Vinohrady, Žižkov)"
                ]
            }
        ]
    }
]

def slugify(name):
    """Convert to URL slug"""
    return re.sub(r'[^\w\s-]', '', name).lower().replace(' ', '-')

def generate_route_page(route):
    """Generate a complete route page"""
    stops_html = ""
    for i, stop in enumerate(route['stops'], 1):
        highlights_html = "\n".join([f"<li>{h}</li>" for h in stop['highlights']])
        stops_html += f"""
        <section class="destination-section" id="stop-{i}">
            <h3>Stop {i}: {stop['city']} ({stop['days']} days)</h3>
            <p><strong>{stop['summary']}</strong></p>
            <h4>Highlights & Experiences:</h4>
            <ul>
                {highlights_html}
            </ul>
        </section>
"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{route['name']} — CougarTravel Itinerary</title>
    <meta name="description" content="{route['subtitle']} Duration: {route['duration']}. Cost: {route['cost']}. Best for: {route['best_for']}">
    <meta name="keywords" content="travel itinerary, {route['slug']}, women travel, group trip, curated route">
    <link rel="canonical" href="https://cougartravel.com/routes/{route['slug']}/">

    <meta property="og:type" content="article">
    <meta property="og:site_name" content="CougarTravel">
    <meta property="og:title" content="{route['name']} — CougarTravel">
    <meta property="og:description" content="{route['subtitle']}">
    <meta property="og:url" content="https://cougartravel.com/routes/{route['slug']}/">
    <meta property="og:image" content="https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=1200&q=80">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="robots" content="index, follow">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/style.css">

    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{route['name']}",
        "description": "{route['subtitle']}",
        "url": "https://cougartravel.com/routes/{route['slug']}/",
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
            {{"@type": "ListItem", "position": 2, "name": "Routes", "item": "https://cougartravel.com/routes/"}},
            {{"@type": "ListItem", "position": 3, "name": "{route['name']}", "item": "https://cougartravel.com/routes/{route['slug']}/"}}
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
                <li role="none"><a href="/routes/" role="menuitem" aria-current="page">Routes</a></li>
                <li role="none"><a href="/safety/" role="menuitem">Safety</a></li>
            </ul>
        </nav>
    </header>

    <main id="main-content">

        <section class="route-hero" aria-labelledby="route-title">
            <div class="container">
                <div class="route-hero-content">
                    <p class="breadcrumb"><a href="/routes/">← Back to All Routes</a></p>
                    <h1 id="route-title">{route['name']}</h1>
                    <p class="route-subtitle">{route['subtitle']}</p>

                    <div class="route-specs">
                        <div class="spec-card">
                            <span class="spec-label">Duration</span>
                            <span class="spec-value">{route['duration']}</span>
                        </div>
                        <div class="spec-card">
                            <span class="spec-label">Cost (per person)</span>
                            <span class="spec-value">{route['cost']}</span>
                        </div>
                        <div class="spec-card">
                            <span class="spec-label">Best Season</span>
                            <span class="spec-value">{route['season']}</span>
                        </div>
                        <div class="spec-card">
                            <span class="spec-label">Best For</span>
                            <span class="spec-value">{route['best_for']}</span>
                        </div>
                    </div>

                    <p class="route-intro" style="margin-top: var(--space-lg); font-size: 1.1rem; line-height: 1.6;">{route['stops'][0]['summary']}</p>
                </div>
            </div>
        </section>

        <article class="route-content">
            <div class="container">
                <section class="route-section">
                    <h2>Route Overview</h2>
                    <p>This curated journey connects {len(route['stops'])} exceptional destinations in a rhythm that allows for deep engagement, genuine rest, and the kind of transformation that only happens when you give yourself permission to slow down. Each stop is chosen not for its Instagram value, but for how it serves the larger arc of the journey.</p>
                    <p>The route is flexible—extend a city if you fall in love, compress if energy shifts. The point is pacing yourself like the confident woman you are: with intention, without apology.</p>
                </section>

                <section class="route-section">
                    <h2>The Full Itinerary</h2>
                    {stops_html}
                </section>

                <section class="route-section">
                    <h2>How to Use This Route</h2>
                    <ul>
                        <li><strong>Adjust timing:</strong> The duration and costs are guides, not commandments. Add days where you want to linger; compress if needed.</li>
                        <li><strong>Book hotels strategically:</strong> We recommend mid-range hotels (€80–150/night) in walkable central neighborhoods.</li>
                        <li><strong>Plan transport between cities:</strong> Flights, trains, or buses—check availability and book 4–6 weeks in advance for better rates.</li>
                        <li><strong>Leave space for spontaneity:</strong> The best travel moments are unplanned. Budget 30% unstructured time in each city.</li>
                        <li><strong>Travel solo or with a friend:</strong> This route works equally well either way.</li>
                        <li><strong>Consider a travel companion service:</strong> Many women on this route find group components (one shared meal, one group tour) helpful without losing independence.</li>
                    </ul>
                </section>

                <section class="route-section">
                    <h2>Practical Details</h2>
                    <h3>Visas & Documentation</h3>
                    <p>Check visa requirements for your nationality well in advance. EU citizens travel freely within Europe. Non-EU visitors should verify entry requirements for each country.</p>

                    <h3>Budget Breakdown</h3>
                    <ul>
                        <li><strong>Hotels:</strong> €80–150/night (includes breakfast in some)</li>
                        <li><strong>Food:</strong> €30–60/day (mix of street food and restaurants)</li>
                        <li><strong>Activities & Experiences:</strong> €200–500 depending on choice</li>
                        <li><strong>Transport (internal):</strong> €500–1,000 for flights/trains between cities</li>
                        <li><strong>Contingency:</strong> Always budget 20% extra</li>
                    </ul>

                    <h3>Safety Notes</h3>
                    <p>All destinations on this route are CougarTravel-vetted for safety and respect toward women travelers. Still, travel with the usual street smarts: use hotel safes, keep copies of documents, stay aware in crowds, trust your instincts.</p>

                    <h3>Packing Tips</h3>
                    <ul>
                        <li>One carry-on suitcase (20–22 inches) or backpack</li>
                        <li>Comfortable walking shoes (these cities reward wandering)</li>
                        <li>Lightweight layers (seasons vary; weather changes)</li>
                        <li>A good book or journal</li>
                        <li>Minimal tech (yes, a phone; no, you don't need 12 apps)</li>
                    </ul>
                </section>

                <section class="route-section route-cta">
                    <h2>Ready to Start Planning?</h2>
                    <p>Explore the <a href="/destinations/">individual destination guides</a> for each stop on this route, or browse <a href="/routes/">other curated routes</a> that match your travel style.</p>
                    <p>This is your permission slip to book the ticket.</p>
                </section>

            </div>
        </article>

        <section class="related-routes" aria-labelledby="more-routes-heading">
            <div class="container">
                <h2 id="more-routes-heading">Explore More Routes</h2>
                <p><a href="/routes/">View all curated routes →</a></p>
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
        document.addEventListener('DOMContentLoaded', function() {{
            var toggle = document.querySelector('.nav-toggle');
            var menu = document.getElementById('main-nav');
            if (toggle && menu) {{
                toggle.addEventListener('click', function() {{
                    var expanded = toggle.getAttribute('aria-expanded') === 'true';
                    toggle.setAttribute('aria-expanded', String(!expanded));
                    menu.classList.toggle('nav-open');
                }});
            }}
        }});
    </script>
</body>
</html>
"""
    return html

def main():
    """Generate all route pages"""
    base_path = "/home/user/cougartravel/routes"

    print(f"Generating {len(ROUTES)} curated route pages...")

    for route in ROUTES:
        route_dir = os.path.join(base_path, route['slug'])
        os.makedirs(route_dir, exist_ok=True)

        html_content = generate_route_page(route)
        html_file = os.path.join(route_dir, "index.html")

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"✓ Created {route['name']}")

    print(f"\n✓ Successfully generated {len(ROUTES)} route pages!")

if __name__ == "__main__":
    main()
