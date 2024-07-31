import os

# Define directory structure and files
directories = ['css', 'js']
files = {
    'index.html': """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LeBonCoin Clone - Accueil</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <div class="header-container">
            <h1>leboncoin</h1>
            <div class="header-actions">
                <button class="post-ad"><a href="post_ad.html">Déposer une annonce</a></button>
                <input type="text" class="search-bar" placeholder="Rechercher sur leboncoin" onfocus="window.location.href='search.html'">
                <div class="notifications">
                    <div class="notification-icon" title="Mes recherches">
                        <img src="https://img.icons8.com/material-outlined/24/search.png" alt="Mes recherches" onclick="window.location.href='my_searches.html'">
                    </div>
                    <div class="notification-icon" title="Favoris">
                        <img src="https://img.icons8.com/material-outlined/24/like.png" alt="Favoris" onclick="window.location.href='favorites.html'">
                    </div>
                    <div class="notification-icon" title="Messages">
                        <img src="https://img.icons8.com/material-outlined/24/visible.png" alt="Messages" onclick="window.location.href='messages.html'">
                    </div>
                    <div class="notification-icon" title="Compte">
                        <img src="https://img.icons8.com/material-outlined/24/user.png" alt="Compte" onclick="window.location.href='account.html'">
                    </div>
                </div>
            </div>
        </div>
        <nav>
            <ul>
                <li><a href="index.html">Accueil</a></li>
                <li><a href="messages.html">Messages</a></li>
                <li><a href="account.html">Compte</a></li>
                <li><a href="post_ad.html">Déposer une annonce</a></li>
                <li><a href="search.html">Rechercher sur leboncoin</a></li>
                <li><a href="my_searches.html">Mes recherches</a></li>
                <li><a href="favorites.html">Favoris</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <div class="search-tags">
            <span>Immobilier</span> · 
            <span>Véhicules</span> · 
            <span>Locations de vacances</span> · 
            <span>Emploi</span> · 
            <span>Mode</span> · 
            <span>Maison & Jardin</span> · 
            <span>Famille</span> · 
            <span>Électronique</span> · 
            <span>Loisirs</span> · 
            <span>Autres</span>
        </div>
        <div class="promo-banner">
            <h2>C’est le moment de vendre ou d’acheter !</h2>
            <a href="post_ad.html">Déposez une annonce</a>
        </div>
        <section class="latest-ads">
            <h2>Annonces récentes</h2>
            <!-- List of ads will be here -->
        </section>
    </main>
    <footer>
        <p>&copy; 2024 LeBonCoin Clone</p>
    </footer>
    <script src="js/script.js"></script>
</body>
</html>
""",
    'account.html': """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LeBonCoin Clone - Mon Compte</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <div class="header-container">
            <h1>leboncoin</h1>
            <div class="header-actions">
                <button class="post-ad"><a href="post_ad.html">Déposer une annonce</a></button>
                <input type="text" class="search-bar" placeholder="Rechercher sur leboncoin" onfocus="window.location.href='search.html'">
                <div class="notifications">
                    <div class="notification-icon" title="Mes recherches">
                        <img src="https://img.icons8.com/material-outlined/24/search.png" alt="Mes recherches" onclick="window.location.href='my_searches.html'">
                    </div>
                    <div class="notification-icon" title="Favoris">
                        <img src="https://img.icons8.com/material-outlined/24/like.png" alt="Favoris" onclick="window.location.href='favorites.html'">
                    </div>
                    <div class="notification-icon" title="Messages">
                        <img src="https://img.icons8.com/material-outlined/24/visible.png" alt="Messages" onclick="window.location.href='messages.html'">
                    </div>
                    <div class="notification-icon" title="Compte">
                        <img src="https://img.icons8.com/material-outlined/24/user.png" alt="Compte" onclick="window.location.href='account.html'">
                    </div>
                </div>
            </div>
        </div>
        <nav>
            <ul>
                <li><a href="index.html">Accueil</a></li>
                <li><a href="messages.html">Messages</a></li>
                <li><a href="account.html">Compte</a></li>
                <li><a href="post_ad.html">Déposer une annonce</a></li>
                <li><a href="search.html">Rechercher sur leboncoin</a></li>
                <li><a href="my_searches.html">Mes recherches</a></li>
                <li><a href="favorites.html">Favoris</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h2>Mon Compte</h2>
        <p>Nom: John Doe</p>
        <p>Email: johndoe@example.com</p>
    </main>
    <footer>
        <p>&copy; 2024 LeBonCoin Clone</p>
    </footer>
    <script src="js/script.js"></script>
</body>
</html>
""",
    'post_ad.html': """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LeBonCoin Clone - Déposer une annonce</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <div class="header-container">
            <h1>leboncoin</h1>
            <div class="header-actions">
                <button class="post-ad"><a href="post_ad.html">Déposer une annonce</a></button>
                <input type="text" class="search-bar" placeholder="Rechercher sur leboncoin" onfocus="window.location.href='search.html'">
                <div class="notifications">
                    <div class="notification-icon" title="Mes recherches">
                        <img src="https://img.icons8.com/material-outlined/24/search.png" alt="Mes recherches" onclick="window.location.href='my_searches.html'">
                    </div>
                    <div class="notification-icon" title="Favoris">
                        <img src="https://img.icons8.com/material-outlined/24/like.png" alt="Favoris" onclick="window.location.href='favorites.html'">
                    </div>
                    <div class="notification-icon" title="Messages">
                        <img src="https://img.icons8.com/material-outlined/24/visible.png" alt="Messages" onclick="window.location.href='messages.html'">
                    </div>
                    <div class="notification-icon" title="Compte">
                        <img src="https://img.icons8.com/material-outlined/24/user.png" alt="Compte" onclick="window.location.href='account.html'">
                    </div>
                </div>
            </div>
        </div>
        <nav>
            <ul>
                <li><a href="index.html">Accueil</a></li>
                <li><a href="messages.html">Messages</a></li>
                <li><a href="account.html">Compte</a></li>
                <li><a href="post_ad.html">Déposer une annonce</a></li>
                <li><a href="search.html">Rechercher sur leboncoin</a></li>
                <li><a href="my_searches.html">Mes recherches</a></li>
                <li><a href="favorites.html">Favoris</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h2>Déposer une annonce</h2>
        <form>
            <label for="title">Titre :</label>
            <input type="text" id="title" name="title" required>
            <label for="description">Description :</label>
            <textarea id="description" name="description" rows="4" required></textarea>
            <label for="price">Prix :</label>
            <input type="number" id="price" name="price" required>
            <label for="category">Catégorie :</label>
            <select id="category" name="category">
                <option value="immobilier">Immobilier</option>
                <option value="vehicules">Véhicules</option>
                <option value="locations">Locations de vacances</option>
                <option value="emploi">Emploi</option>
                <option value="mode">Mode</option>
                <option value="maison-jardin">Maison & Jardin</option>
                <option value="famille">Famille</option>
                <option value="electronique">Électronique</option>
                <option value="loisirs">Loisirs</option>
                <option value="autres">Autres</option>
            </select>
            <label for="image">Image URL :</label>
            <input type="text" id="image" name="image" required>
            <button type="submit">Soumettre</button>
        </form>
    </main>
    <footer>
        <p>&copy; 2024 LeBonCoin Clone</p>
    </footer>
    <script src="js/script.js"></script>
</body>
</html>
""",
    'search.html': """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LeBonCoin Clone - Rechercher</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <div class="header-container">
            <h1>leboncoin</h1>
            <div class="header-actions">
                <button class="post-ad"><a href="post_ad.html">Déposer une annonce</a></button>
                <input type="text" class="search-bar" placeholder="Rechercher sur leboncoin" onfocus="window.location.href='search.html'">
                <div class="notifications">
                    <div class="notification-icon" title="Mes recherches">
                        <img src="https://img.icons8.com/material-outlined/24/search.png" alt="Mes recherches" onclick="window.location.href='my_searches.html'">
                    </div>
                    <div class="notification-icon" title="Favoris">
                        <img src="https://img.icons8.com/material-outlined/24/like.png" alt="Favoris" onclick="window.location.href='favorites.html'">
                    </div>
                    <div class="notification-icon" title="Messages">
                        <img src="https://img.icons8.com/material-outlined/24/visible.png" alt="Messages" onclick="window.location.href='messages.html'">
                    </div>
                    <div class="notification-icon" title="Compte">
                        <img src="https://img.icons8.com/material-outlined/24/user.png" alt="Compte" onclick="window.location.href='account.html'">
                    </div>
                </div>
            </div>
        </div>
        <nav>
            <ul>
                <li><a href="index.html">Accueil</a></li>
                <li><a href="messages.html">Messages</a></li>
                <li><a href="account.html">Compte</a></li>
                <li><a href="post_ad.html">Déposer une annonce</a></li>
                <li><a href="search.html">Rechercher sur leboncoin</a></li>
                <li><a href="my_searches.html">Mes recherches</a></li>
                <li><a href="favorites.html">Favoris</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h2>Recherche</h2>
        <form>
            <label for="search">Rechercher :</label>
            <input type="text" id="search" name="search" required>
            <button type="submit">Chercher</button>
        </form>
        <section class="search-results">
            <h3>Résultats de la recherche</h3>
            <!-- List of search results will be here -->
        </section>
    </main>
    <footer>
        <p>&copy; 2024 LeBonCoin Clone</p>
    </footer>
    <script src="js/script.js"></script>
</body>
</html>
""",
    'my_searches.html': """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LeBonCoin Clone - Mes recherches</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <div class="header-container">
            <h1>leboncoin</h1>
            <div class="header-actions">
                <button class="post-ad"><a href="post_ad.html">Déposer une annonce</a></button>
                <input type="text" class="search-bar" placeholder="Rechercher sur leboncoin" onfocus="window.location.href='search.html'">
                <div class="notifications">
                    <div class="notification-icon" title="Mes recherches">
                        <img src="https://img.icons8.com/material-outlined/24/search.png" alt="Mes recherches" onclick="window.location.href='my_searches.html'">
                    </div>
                    <div class="notification-icon" title="Favoris">
                        <img src="https://img.icons8.com/material-outlined/24/like.png" alt="Favoris" onclick="window.location.href='favorites.html'">
                    </div>
                    <div class="notification-icon" title="Messages">
                        <img src="https://img.icons8.com/material-outlined/24/visible.png" alt="Messages" onclick="window.location.href='messages.html'">
                    </div>
                    <div class="notification-icon" title="Compte">
                        <img src="https://img.icons8.com/material-outlined/24/user.png" alt="Compte" onclick="window.location.href='account.html'">
                    </div>
                </div>
            </div>
        </div>
        <nav>
            <ul>
                <li><a href="index.html">Accueil</a></li>
                <li><a href="messages.html">Messages</a></li>
                <li><a href="account.html">Compte</a></li>
                <li><a href="post_ad.html">Déposer une annonce</a></li>
                <li><a href="search.html">Rechercher sur leboncoin</a></li>
                <li><a href="my_searches.html">Mes recherches</a></li>
                <li><a href="favorites.html">Favoris</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h2>Mes Recherches</h2>
        <ul>
            <li>Recherche 1</li>
            <li>Recherche 2</li>
            <!-- Add more searches -->
        </ul>
    </main>
    <footer>
        <p>&copy; 2024 LeBonCoin Clone</p>
    </footer>
    <script src="js/script.js"></script>
</body>
</html>
""",
    'favorites.html': """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LeBonCoin Clone - Favoris</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <div class="header-container">
            <h1>leboncoin</h1>
            <div class="header-actions">
                <button class="post-ad"><a href="post_ad.html">Déposer une annonce</a></button>
                <input type="text" class="search-bar" placeholder="Rechercher sur leboncoin" onfocus="window.location.href='search.html'">
                <div class="notifications">
                    <div class="notification-icon" title="Mes recherches">
                        <img src="https://img.icons8.com/material-outlined/24/search.png" alt="Mes recherches" onclick="window.location.href='my_searches.html'">
                    </div>
                    <div class="notification-icon" title="Favoris">
                        <img src="https://img.icons8.com/material-outlined/24/like.png" alt="Favoris" onclick="window.location.href='favorites.html'">
                    </div>
                    <div class="notification-icon" title="Messages">
                        <img src="https://img.icons8.com/material-outlined/24/visible.png" alt="Messages" onclick="window.location.href='messages.html'">
                    </div>
                    <div class="notification-icon" title="Compte">
                        <img src="https://img.icons8.com/material-outlined/24/user.png" alt="Compte" onclick="window.location.href='account.html'">
                    </div>
                </div>
            </div>
        </div>
        <nav>
            <ul>
                <li><a href="index.html">Accueil</a></li>
                <li><a href="messages.html">Messages</a></li>
                <li><a href="account.html">Compte</a></li>
                <li><a href="post_ad.html">Déposer une annonce</a></li>
                <li><a href="search.html">Rechercher sur leboncoin</a></li>
                <li><a href="my_searches.html">Mes recherches</a></li>
                <li><a href="favorites.html">Favoris</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h2>Favoris</h2>
        <ul>
            <li>Article Favori 1</li>
            <li>Article Favori 2</li>
            <!-- Add more favorite articles -->
        </ul>
    </main>
    <footer>
        <p>&copy; 2024 LeBonCoin Clone</p>
    </footer>
    <script src="js/script.js"></script>
</body>
</html>
"""
}

# Create directories
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Create files with content
for filename, content in files.items():
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content.strip())
