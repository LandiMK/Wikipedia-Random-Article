
def search_wikipedia_article():
    '''Get and show Wikipedia random article, verifying if web page load well'''

    import requests
    from bs4 import BeautifulSoup
    import webbrowser

    # Wikipedia random article URL
    url = "https://en.wikipedia.org/wiki/Special:Random"

    # Get server response
    response = requests.get(url)


    def server_works(response):
        '''Verify if web page has been loaded well'''

        # Get web page status code
            # 200 OK
        server_load = response.status_code

        if server_load == 200:
            print(f"Web page has been loaded well!\nResponse: {server_load}\n")
        else:
            print(f"Could not load the web page...\nResponse: {server_load}")


    def wikipedia_random_article():
        '''Get random article for Wikipedia'''

        while True:

            url = "https://en.wikipedia.org/wiki/Special:Random"

            response = requests.get(url)
        
            soup = BeautifulSoup(response.content, "html.parser")

            # Get current article title
            article_title = soup.find("h1", {"class": "firstHeading"})

            user_input = input(f"{article_title.text}\nDo you want read this Wikipedia article? [Y/N]> ")

            if user_input.lower() == "y":

                article_url = f"https://en.wikipedia.org/wiki/{article_title.text}"

                # Open web browser with chosen article
                webbrowser.open(article_url)

                print("Enjoy your reading!")
                return
            
            elif user_input.lower() == "n":

                print("Searching another article...")
                wikipedia_random_article()
                return
            
            else:

                print("Invalid input. Please, try with Y or N.")
                continue
        
    return server_works(response), wikipedia_random_article()

search_wikipedia_article()
