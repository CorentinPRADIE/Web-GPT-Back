import os

def setup_api_keys():
    bing_subscription_key = os.environ.get('BING_SEARCH_V7_SUBSCRIPTION_KEY')
    openai_api_key = os.environ.get('OPENAI_API_KEY')

    if bing_subscription_key is None:
        raise ValueError("Bing API key (BING_SEARCH_V7_SUBSCRIPTION_KEY) is not set in environment variables!")
    if openai_api_key is None:
        raise ValueError("OpenAI API key (OPENAI_API_KEY) is not set in environment variables!")
    return openai_api_key, bing_subscription_key