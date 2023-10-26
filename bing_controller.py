import requests
import openai
import __main__

def requires_web_search(user_question: str) -> bool:
    prompt = (f"Given the user's question: \"{user_question}\", "
              f"does it suggest an explicit need for real-time or up-to-date information from a web search? "
              f"Please answer with \"Yes\" or \"No\".")

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",  # You can specify the 'gpt-3.5-turbo-instruct' model
        prompt=prompt,
        max_tokens=10
    )

    # Extract the content of the response and convert to lowercase
    answer = response.choices[0].text.strip().lower()

    # Check if the answer contains "yes" or "y" for affirmative responses
    if "yes" in answer or "y" in answer:
        return True

    # Check if the answer contains "no" or "n" for negative responses
    if "no" in answer or "n" in answer:
        return False

    # If the answer doesn't contain "yes", "y", "no", or "n", you can handle it as needed
    raise ValueError(f"Unexpected response from model: {answer}")



def get_bing_search_results(query, mkt="fr-FR", count=3):
    bing_subscription_key = __main__.bing_subscription_key
    params = {"q": query, "mkt": mkt, "count": count}
    headers = {"Ocp-Apim-Subscription-Key": bing_subscription_key}
    try:
        response = requests.get(
            "https://api.bing.microsoft.com/v7.0/search", headers=headers, params=params
        )
        response.raise_for_status()
        results = response.json()

        names, URLs, snippets = [], [], []

        if "webPages" in results and "value" in results["webPages"]:
            for item in results["webPages"]["value"]:
                names.append(item["name"])
                URLs.append(item["url"])
                snippets.append(item["snippet"])

        return names, URLs, snippets

    except Exception as ex:
        print(f"An error occurred: {str(ex)}")
        return None, None, None
    

