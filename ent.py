def facebookS(ListeEn, requests, BeautifulSoup, time):
    # Construire la requête de recherche Google pour Facebook
    search_query = f"{ListeEn} facebook "
    search_url = f"https://www.google.com/search?q={search_query}"

    # Définir les en-têtes pour simuler une requête du navigateur
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # Faire une requête GET vers Google avec la requête de recherche
    response = requests.get(search_url, headers=headers)

    # Analyser la réponse avec BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Initialiser la variable pour l'URL Facebook
    facebook_url = None

    # Parcourir les résultats de la recherche
    for result in soup.find_all("a", href=True):
        if "facebook.com" in result['href'] and "facebook.com/profile.php" not in result['href'] and "facebook.com/permalink" not in result['href']:
            # Si l'URL contient 'facebook.com' et n'est pas un profil ou un lien de publication
            facebook_url = result['href']
            break

    # Nettoyer et formater l'URL Facebook
    if facebook_url:
        facebook_url = facebook_url.replace(
            "/url?esrc=s&q=&rct=j&sa=U&url=", "")
        facebook_url = facebook_url.replace(
            "p/", "")
        tmp = facebook_url.split("%")
        facebook_url = tmp[0]
        tmp = facebook_url.split("&")
        facebook_url = tmp[0]

        # Afficher l'URL Facebook
        print(facebook_url)
        return facebook_url

    # Attendre 2 secondes si aucune URL n'est trouvée
    time.sleep(2)
