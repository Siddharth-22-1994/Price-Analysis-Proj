from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
import pandas as pd
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def saerchformview(request):
    return render(request, 'searchform.html')


amazon = ''
def Flipkartsearchresults(request):
    name1 = request.POST['product']

    # global flipkart
    # name1 = name1.replace(" ", "+")  # iphone x  -> iphone+x
    # flipkart = f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
    # res = requests.get(flipkart)
    #
    # print("\nSearching in flipkart....")
    # soup = BeautifulSoup(res.text, 'html.parser')
    # flipkart_name = soup.select('._4rR01T')[0].getText().strip()  ### New Class For Product Name
    # flipkart_name = flipkart_name.upper()
    # if name1.upper() in flipkart_name:
    #     flipkart_price = soup.select('._1_WHN1')[0].getText().strip()  ### New Class For Product Price
    #     flipkart_name = soup.select('._4rR01T')[0].getText().strip()

    url2 = f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
    req = requests.get(url2)
    content = BeautifulSoup(req.content, 'html.parser')
    name = content.find_all('div', {'class': '_4rR01T'})
    price = content.find_all('div', {'class': '_1_WHN1'})
    print(name[1].text)
    print(price[1].text)
    flipkart_name = price[1].text
    flipkart_price = name[1].text

    return render(request, 'Flipkartproduct-result.html',{'flipkart_name': flipkart_name, 'flipkart_price': flipkart_price})

def ebaysearchresults(request):
    name1 = request.POST['product']

    # global ebay
    # name1 = name1.replace(" ", "+")
    # ebay = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={name1}&_sacat=0'
    # res = requests.get(f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={name1}&_sacat=0')
    # print("\nSearching in ebay.....")
    # soup = BeautifulSoup(res.text, 'html.parser')
    # length = soup.select('.s-item__price')
    # ebay_page_length = int(len(length))
    # for i in range(0, ebay_page_length):
    #     info = soup.select('.SECONDARY_INFO')[i].getText().strip()
    #     info = info.upper()
    #     if info == 'BRAND NEW':
    #         ebay_name = soup.select('.s-item__title')[i].getText().strip()
    #         name = name1.upper()
    #         ebay_name = ebay_name.upper()
    #         if name in ebay_name[:25]:
    #             ebay_price = soup.select('.s-item__price')[i].getText().strip()
    #             ebay_name = soup.select('.s-item__title')[i].getText().strip()
    #             print("Ebay:")
    #             print(ebay_name)
    #             ebay_price = ebay_price.replace("INR", "₹")
    #             ebay_price = ebay_price[0:14]
    #             return render(request, 'Flipkartproduct-result.html',
    #                           {'ebay_name': ebay_name, 'ebay_price': ebay_price})
    # return render(request, 'ebyesearchresults.html')
    # ebay
    url2 = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={name1}&_sacat=0'
    req = requests.get(url2)
    content = BeautifulSoup(req.content, 'html.parser')
    name = content.find_all('h3', {'class': 's-item__title'})
    price = content.find_all('span', {'class': 's-item__price'})
    print(name[0].text)
    print(price[0].text)
    ebayprice = price[0].text
    ebayname = name[0].text
    return render(request, 'ebyesearchresults.html',
                  {'ebay_name': ebayname, 'ebay_price': ebayprice})

def amazonproductresults(request):
# amazon
    name1 = request.POST['product']
    name2 = name1

    global amazon

    name1 = name1.replace(" ", "-")
    name2 = name1.replace(" ", "+")
    amazon = f'https://www.amazon.in/{name1}/s?k={name2}'
    res = requests.get(amazon)
    print("\nSearching in amazon:")
    soup = BeautifulSoup(res.text, 'html.parser')
    amazon_page = soup.select('.a-color-base.a-text-normal')
    amazon_page_length = int(len(amazon_page))
    for i in range(0, amazon_page_length):
        name = name1.upper()
        amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
        if name in amazon_name[0:20]:
            amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()
            return render(request, 'amazonsearchresults.html', {'amazonname': amazon_name,'amazonprice': amazon_price})


    return render(request, 'amazonsearchresults.html')

olx = ''
def olxpriceresuls(request):
    global olx
    name1 = request.POST['product']
    name1 = name1.replace(" ", "-")
    olx = f'https://www.olx.in/items/q-{name1}?isSearchCall=true'
    res = requests.get(olx)
    print("\nSearching in OLX......")
    soup = BeautifulSoup(res.text, 'html.parser')
    olx_name = soup.select('._2tW1I')
    olx_page_length = len(olx_name)
    for i in range(0, olx_page_length):
        olx_name = soup.select('._2tW1I')[i].getText().strip()
        name = name1.upper()
        olx_name = olx_name.upper()
        if name in olx_name:
            olx_price = soup.select('._89yzn')[i].getText().strip()
            olx_name = soup.select('._2tW1I')[i].getText().strip()
            olx_loc = soup.select('.tjgMj')[i].getText().strip()
            return render(request, 'olxpriceresults.html', {'olxname': olx_name, 'olxprice':olx_price})
    return render(request, 'olxpriceresults.html')