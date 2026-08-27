"""Knowledge base for the Literary Companion chatbot.

Everything the bot knows about books, novels and poems lives here as plain
Python data so the app has zero external data dependencies at runtime.
"""

# ---------------------------------------------------------------------------
# Books and novels
# ---------------------------------------------------------------------------

BOOKS = [
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year": 1813,
        "genre": ["classic", "romance"],
        "summary": (
            "Elizabeth Bennet navigates class, family pressure and her own first "
            "impressions before falling for the proud Mr Darcy."
        ),
        "famous_line": "It is a truth universally acknowledged, that a single man in "
        "possession of a good fortune, must be in want of a wife.",
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "genre": ["dystopian", "classic", "science fiction"],
        "summary": (
            "Winston Smith rebels in small ways against a totalitarian state that "
            "rewrites history and polices thought itself."
        ),
        "famous_line": "War is peace. Freedom is slavery. Ignorance is strength.",
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "genre": ["classic", "literary fiction"],
        "summary": (
            "Scout Finch watches her father Atticus defend a Black man falsely "
            "accused in the segregated American South."
        ),
        "famous_line": "You never really understand a person until you consider "
        "things from his point of view.",
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "genre": ["classic", "literary fiction"],
        "summary": (
            "Jay Gatsby throws lavish parties chasing a lost love and a version of "
            "the American Dream that was never really available to him."
        ),
        "famous_line": "So we beat on, boats against the current, borne back "
        "ceaselessly into the past.",
    },
    {
        "title": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "year": 1866,
        "genre": ["classic", "psychological", "literary fiction"],
        "summary": (
            "A poor student murders a pawnbroker to test a theory about "
            "extraordinary men, then unravels under his own conscience."
        ),
        "famous_line": "Pain and suffering are always inevitable for a large "
        "intelligence and a deep heart.",
    },
    {
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel Garcia Marquez",
        "year": 1967,
        "genre": ["magical realism", "literary fiction"],
        "summary": (
            "Seven generations of the Buendia family rise and fall in the invented "
            "town of Macondo, where the magical is treated as ordinary."
        ),
        "famous_line": "Many years later, as he faced the firing squad, Colonel "
        "Aureliano Buendia was to remember that distant afternoon.",
    },
    {
        "title": "The God of Small Things",
        "author": "Arundhati Roy",
        "year": 1997,
        "genre": ["literary fiction", "indian literature"],
        "summary": (
            "Twins Rahel and Estha in Kerala live through a family tragedy shaped "
            "by caste, love laws and small forbidden acts."
        ),
        "famous_line": "It is curious how sometimes the memory of death lives on "
        "for so much longer than the memory of the life that it purloined.",
    },
    {
        "title": "Midnight's Children",
        "author": "Salman Rushdie",
        "year": 1981,
        "genre": ["magical realism", "indian literature"],
        "summary": (
            "Saleem Sinai, born at the exact moment of India's independence, finds "
            "his life handcuffed to the history of the nation."
        ),
        "famous_line": "Most of what matters in our lives takes place in our absence.",
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "year": 1988,
        "genre": ["philosophical", "adventure"],
        "summary": (
            "A shepherd boy travels from Spain to the Egyptian pyramids chasing a "
            "recurring dream of treasure, and learns to read the omens."
        ),
        "famous_line": "When you want something, all the universe conspires in "
        "helping you to achieve it.",
    },
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J. K. Rowling",
        "year": 1997,
        "genre": ["fantasy", "young adult"],
        "summary": (
            "An orphan discovers he is a wizard and begins his first year at "
            "Hogwarts School of Witchcraft and Wizardry."
        ),
        "famous_line": "It does not do to dwell on dreams and forget to live.",
    },
    {
        "title": "The Lord of the Rings",
        "author": "J. R. R. Tolkien",
        "year": 1954,
        "genre": ["fantasy", "adventure", "classic"],
        "summary": (
            "A hobbit carries a corrupting ring across Middle-earth to destroy it "
            "in the fire where it was made."
        ),
        "famous_line": "Not all those who wander are lost.",
    },
    {
        "title": "Frankenstein",
        "author": "Mary Shelley",
        "year": 1818,
        "genre": ["gothic", "science fiction", "classic"],
        "summary": (
            "Victor Frankenstein animates a creature from dead matter and then "
            "abandons it, with tragedy following both of them."
        ),
        "famous_line": "Beware; for I am fearless, and therefore powerful.",
    },
    {
        "title": "The Hound of the Baskervilles",
        "author": "Arthur Conan Doyle",
        "year": 1902,
        "genre": ["mystery", "detective", "classic"],
        "summary": (
            "Sherlock Holmes and Watson investigate a supposedly supernatural hound "
            "haunting a family on the Devon moors."
        ),
        "famous_line": "The world is full of obvious things which nobody by any "
        "chance ever observes.",
    },
    {
        "title": "Gone Girl",
        "author": "Gillian Flynn",
        "year": 2012,
        "genre": ["thriller", "mystery"],
        "summary": (
            "A wife vanishes on her fifth anniversary and her husband becomes the "
            "prime suspect in a story told by two unreliable narrators."
        ),
        "famous_line": "There's something disturbing about recalling a warm memory "
        "and feeling utterly cold.",
    },
    {
        "title": "The Kite Runner",
        "author": "Khaled Hosseini",
        "year": 2003,
        "genre": ["literary fiction", "historical"],
        "summary": (
            "Amir spends his life trying to atone for betraying his childhood "
            "friend Hassan in pre-Soviet Kabul."
        ),
        "famous_line": "For you, a thousand times over.",
    },
    {
        "title": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari",
        "year": 2011,
        "genre": ["non-fiction", "historical"],
        "summary": (
            "A sweeping account of how Homo sapiens went from an unremarkable ape "
            "to the dominant species, driven by shared fictions."
        ),
        "famous_line": "Large numbers of strangers can cooperate successfully by "
        "believing in common myths.",
    },
    {
        "title": "Wings of Fire",
        "author": "A. P. J. Abdul Kalam",
        "year": 1999,
        "genre": ["non-fiction", "indian literature"],
        "summary": (
            "The autobiography of India's missile man, from a newspaper-selling boy "
            "in Rameswaram to the country's space and defence programmes."
        ),
        "famous_line": "Dream is not that which you see while sleeping, it is "
        "something that does not let you sleep.",
    },
    {
        "title": "The Book Thief",
        "author": "Markus Zusak",
        "year": 2005,
        "genre": ["historical", "young adult"],
        "summary": (
            "Narrated by Death, a young girl in Nazi Germany steals books and reads "
            "them aloud in a bomb shelter."
        ),
        "famous_line": "I have hated words and I have loved them, and I hope I have "
        "made them right.",
    },
]

# ---------------------------------------------------------------------------
# Poems
# ---------------------------------------------------------------------------

POEMS = [
    {
        "title": "The Road Not Taken",
        "poet": "Robert Frost",
        "year": 1916,
        "form": "narrative lyric, four quintains",
        "theme": "choice, individuality, and the stories we tell about our decisions",
        "extract": (
            "Two roads diverged in a yellow wood,\n"
            "And sorry I could not travel both\n"
            "And be one traveler, long I stood\n"
            "And looked down one as far as I could\n"
            "To where it bent in the undergrowth;"
        ),
    },
    {
        "title": "Stopping by Woods on a Snowy Evening",
        "poet": "Robert Frost",
        "year": 1922,
        "form": "four quatrains, chain rhyme",
        "theme": "the pull of rest and beauty against duty",
        "extract": (
            "The woods are lovely, dark and deep,\n"
            "But I have promises to keep,\n"
            "And miles to go before I sleep,\n"
            "And miles to go before I sleep."
        ),
    },
    {
        "title": "If-",
        "poet": "Rudyard Kipling",
        "year": 1910,
        "form": "four octaves of didactic verse",
        "theme": "stoicism, self-command and growing up",
        "extract": (
            "If you can keep your head when all about you\n"
            "Are losing theirs and blaming it on you,\n"
            "If you can trust yourself when all men doubt you,\n"
            "But make allowance for their doubting too;"
        ),
    },
    {
        "title": "Where the Mind is Without Fear",
        "poet": "Rabindranath Tagore",
        "year": 1910,
        "form": "free verse prayer from Gitanjali",
        "theme": "freedom, knowledge and a nation awakening",
        "extract": (
            "Where the mind is without fear and the head is held high;\n"
            "Where knowledge is free;\n"
            "Where the world has not been broken up into fragments\n"
            "By narrow domestic walls."
        ),
    },
    {
        "title": "Ozymandias",
        "poet": "Percy Bysshe Shelley",
        "year": 1818,
        "form": "sonnet",
        "theme": "the vanity of power and the erosion of empire by time",
        "extract": (
            "My name is Ozymandias, King of Kings;\n"
            "Look on my Works, ye Mighty, and despair!\n"
            "Nothing beside remains. Round the decay\n"
            "Of that colossal Wreck, boundless and bare\n"
            "The lone and level sands stretch far away."
        ),
    },
    {
        "title": "Sonnet 18 (Shall I compare thee to a summer's day?)",
        "poet": "William Shakespeare",
        "year": 1609,
        "form": "Shakespearean sonnet, iambic pentameter",
        "theme": "love outliving beauty through the permanence of verse",
        "extract": (
            "Shall I compare thee to a summer's day?\n"
            "Thou art more lovely and more temperate:\n"
            "Rough winds do shake the darling buds of May,\n"
            "And summer's lease hath all too short a date."
        ),
    },
    {
        "title": "Daffodils (I Wandered Lonely as a Cloud)",
        "poet": "William Wordsworth",
        "year": 1807,
        "form": "four sestets",
        "theme": "nature, memory and solitary joy",
        "extract": (
            "I wandered lonely as a cloud\n"
            "That floats on high o'er vales and hills,\n"
            "When all at once I saw a crowd,\n"
            "A host, of golden daffodils."
        ),
    },
    {
        "title": "Still I Rise",
        "poet": "Maya Angelou",
        "year": 1978,
        "form": "lyric with refrain",
        "theme": "resilience, dignity and defiance against oppression",
        "extract": (
            "You may write me down in history\n"
            "With your bitter, twisted lies,\n"
            "You may trod me in the very dirt\n"
            "But still, like dust, I'll rise."
        ),
    },
    {
        "title": "Hope is the thing with feathers",
        "poet": "Emily Dickinson",
        "year": 1861,
        "form": "three quatrains, slant rhyme",
        "theme": "hope as a small, tireless bird inside the soul",
        "extract": (
            "\"Hope\" is the thing with feathers -\n"
            "That perches in the soul -\n"
            "And sings the tune without the words -\n"
            "And never stops - at all -"
        ),
    },
    {
        "title": "The Raven",
        "poet": "Edgar Allan Poe",
        "year": 1845,
        "form": "trochaic octameter with internal rhyme",
        "theme": "grief, obsession and the refusal of consolation",
        "extract": (
            "Once upon a midnight dreary, while I pondered, weak and weary,\n"
            "Over many a quaint and curious volume of forgotten lore-\n"
            "Quoth the Raven \"Nevermore.\""
        ),
    },
]

# ---------------------------------------------------------------------------
# General literary Q&A the retriever can match against
# ---------------------------------------------------------------------------

FAQS = [
    {
        "question": "What is the difference between a novel and a novella?",
        "answer": (
            "Length and scope. A novella usually runs 17,000-40,000 words and keeps "
            "to a single thread of action, while a novel runs longer and can carry "
            "subplots, several points of view and a wider cast. Animal Farm is a "
            "novella; War and Peace is emphatically a novel."
        ),
    },
    {
        "question": "What is a sonnet?",
        "answer": (
            "A fourteen-line poem in iambic pentameter. The Shakespearean form uses "
            "three quatrains and a closing couplet rhyming ABAB CDCD EFEF GG; the "
            "Petrarchan form splits into an octave and a sestet, with a turn - the "
            "volta - between them."
        ),
    },
    {
        "question": "What is a metaphor and how is it different from a simile?",
        "answer": (
            "A simile compares using 'like' or 'as' ('as busy as a bee'). A metaphor "
            "states the comparison outright ('he was a lion in the courtroom'). The "
            "metaphor is the bolder claim because it collapses the distance between "
            "the two things."
        ),
    },
    {
        "question": "What is magical realism?",
        "answer": (
            "A style where impossible events are narrated in the same flat, matter-"
            "of-fact tone as ordinary ones, so no one in the story treats them as "
            "strange. Gabriel Garcia Marquez and Salman Rushdie are the usual "
            "reference points."
        ),
    },
    {
        "question": "What is an unreliable narrator?",
        "answer": (
            "A narrator whose account you cannot fully trust, whether from bias, "
            "self-deception, immaturity or outright lying. Gone Girl and The Catcher "
            "in the Rye both build their effect on it."
        ),
    },
    {
        "question": "What is free verse in poetry?",
        "answer": (
            "Poetry without a fixed metre or rhyme scheme. It still uses rhythm, "
            "line breaks and sound, but it sets its own pattern instead of "
            "inheriting one. Walt Whitman and Rabindranath Tagore's Gitanjali are "
            "good examples."
        ),
    },
    {
        "question": "What do protagonist and antagonist mean?",
        "answer": (
            "The protagonist is the character whose goal drives the story; the "
            "antagonist is the force opposing that goal. The antagonist need not be "
            "a villain or even a person - it can be a society, a system or the "
            "protagonist's own nature."
        ),
    },
    {
        "question": "What is the theme of a story?",
        "answer": (
            "The underlying idea the story keeps returning to - justice, ambition, "
            "loss of innocence. Plot is what happens; theme is what the happening "
            "adds up to."
        ),
    },
    {
        "question": "Who won the Nobel Prize in Literature from India?",
        "answer": (
            "Rabindranath Tagore, in 1913, largely for Gitanjali - the first Nobel "
            "Literature laureate from Asia."
        ),
    },
    {
        "question": "What is the Booker Prize?",
        "answer": (
            "A major annual award for the best novel written in English and "
            "published in the UK or Ireland. Indian winners include Arundhati Roy "
            "for The God of Small Things and Salman Rushdie for Midnight's Children."
        ),
    },
    {
        "question": "How do I start reading more books?",
        "answer": (
            "Start with something short and fast-moving rather than a classic you "
            "think you should read. Twenty pages a day finishes roughly a book a "
            "month. Abandon anything that bores you by page fifty - reading is not "
            "an obligation."
        ),
    },
    {
        "question": "What is iambic pentameter?",
        "answer": (
            "Five iambs per line, an iamb being an unstressed syllable followed by a "
            "stressed one: da-DUM da-DUM da-DUM da-DUM da-DUM. It is the backbone "
            "of Shakespeare's plays and sonnets because it sits close to the rhythm "
            "of ordinary English speech."
        ),
    },
    {
        "question": "What is a dystopian novel?",
        "answer": (
            "A novel set in a society organised around control, scarcity or fear, "
            "usually presented by its rulers as a utopia. 1984, Brave New World and "
            "The Handmaid's Tale are the standard trio."
        ),
    },
    {
        "question": "What is the difference between fiction and non-fiction?",
        "answer": (
            "Fiction invents its people and events, even when it borrows real "
            "settings. Non-fiction claims to describe what actually happened - "
            "biography, history, essays, science writing. Sapiens is non-fiction; "
            "Midnight's Children is fiction built on real history."
        ),
    },
]

# Genre -> phrases used by the recommendation intent
GENRE_ALIASES = {
    "fantasy": ["fantasy", "magic", "wizard", "dragon", "middle earth"],
    "mystery": ["mystery", "detective", "crime", "whodunit", "sherlock"],
    "thriller": ["thriller", "suspense"],
    "romance": ["romance", "love story", "romantic"],
    "classic": ["classic", "classics", "timeless"],
    "science fiction": ["science fiction", "sci-fi", "scifi", "futuristic"],
    "dystopian": ["dystopian", "dystopia", "totalitarian"],
    "historical": ["historical", "history", "war novel"],
    "non-fiction": ["non-fiction", "nonfiction", "true story", "factual"],
    "young adult": ["young adult", "teen", "teenage"],
    "literary fiction": ["literary fiction", "literary"],
    "magical realism": ["magical realism", "magic realism"],
    "indian literature": ["indian", "india", "indian author"],
    "philosophical": ["philosophical", "philosophy", "self discovery"],
    "gothic": ["gothic", "horror", "spooky"],
    "adventure": ["adventure", "quest", "journey"],
}
