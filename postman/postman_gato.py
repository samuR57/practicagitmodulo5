import requests

url = "https://www.metmuseum.org/es/art/collection/search?q=gato"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'es-419,es;q=0.9',
  'cookie': 'NEXT_LOCALE=es; visid_incap_1661977=y4OfbiyxQ+OQjrN9XYFTpa9hc2YAAAAAQUIPAAAAAAAzS1U6cjW/fQMssLuEqtRo; visid_incap_1661922=mCUwcA/DRiyKcg0ymSrEEq9hc2YAAAAAQUIPAAAAAACmXbCe+WZZTSGN7skSsR3e; incap_ses_1693_1661922=EDZpZrawMSf+/rldmr5+F69hc2YAAAAAHd1Zykw9Cu2kOanGHza3mA==; incap_ses_1616_1661977=o/qGcr37JwZ6/Fx0hy9tFq9hc2YAAAAApFqtrgvtDyyW7WCiyOdSJA==; _gcl_au=1.1.1004737320.1718837681; _ga=GA1.2.93149416.1718837681; _gid=GA1.2.1735098232.1718837681; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.metmuseum.org/es/search-results?q=carola&searchFacet=Art%22%2C%22sref%22:%22%22%2C%22sts%22:1718837681953%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=eed5322c-6556-4c9e-ba8a-6df459aaccda%22%2C%22session_count%22:1%2C%22last_session_ts%22:1718837681953}; _tt_enable_cookie=1; _ttp=ToqH9HQkwiQnU431WsTNQexllyj; _fbp=fb.1.1718837682598.369171612971474693; __qca=P0-396634608-1718837681726; QuantumMetricSessionID=daf031b7ab6e7be0d98423ccdddd4f9e; QuantumMetricUserID=0f9bcba5c640cbcc70dac59a4ead2afc; _gat_UA-72292701-1=1; _ga_Y0W8DGNBTB=GS1.1.1718837681.1.1.1718837814.0.0.0',
  'next-router-prefetch': '1',
  'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22locale%22%2C%22es%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22(navigation)%22%2C%7B%22children%22%3A%5B%22search-results%22%2C%7B%22children%22%3A%5B%22__PAGE__%3F%7B%5C%22q%5C%22%3A%5C%22carola%5C%22%2C%5C%22searchFacet%5C%22%3A%5C%22Art%5C%22%7D%22%2C%7B%7D%2C%22%2Fes%2Fsearch-results%3Fq%3Dcarola%26searchFacet%3DArt%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
  'next-url': '/es/search-results',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/es/search-results?q=gat&searchFacet=Art',
  'rsc': '1',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
