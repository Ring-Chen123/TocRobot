from transitions.extensions import GraphMachine
from utils import send_text_message

import requests
import re
import random
from bs4 import BeautifulSoup
from imgurpython import ImgurClient


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    #def is_going_to_state1(self, event):
    #    text = event.message.text
    #    return text.lower() == "go"
    #1
    def is_going_to_showfunction(self, event):
        text = event.message.text
        return text.lower() == "hi"
    #2 #8
    def is_going_to_moviestateask(self, event):
        text = event.message.text
        return text.lower() == "movie"
    #3  
    def is_going_to_atmovies(self, event):
        text = event.message.text
        return text.lower() == "information"
    #4
    def is_going_to_envy(self, event):
        text = event.message.text
        return text.lower() == "free movie"
    #5
    def is_going_to_back(self, event):
        text = event.message.text
        return text.lower() == "back"
    #6
    def is_going_to_upsetstateask(self, event):
        text = event.message.text
        return text.lower() == "help"
    #7
    def is_going_to_upsetstatesolve(self, event):
        text = event.message.text
        return text.lower() == "girlfriend"
    #9
    def is_going_to_present(self, event):
        text = event.message.text
        return text.lower() == "gift"
    #10
    def is_going_to_ini(self, event):
        text = event.message.text
        return text.lower() == "no"
	#11
    def is_going_to_newsstateask(self, event):
        text = event.message.text
        return text.lower() == "news"
	#12
    def is_going_to_tech(self, event):
        text = event.message.text
        return text.lower() == "tech"
	#13
    def is_going_to_technews(self, event):
        text = event.message.text
        return text.lower() == "1"
	#14
    def is_going_to_panx(self, event):
        text = event.message.text
        return text.lower() == "2"
	#15
    def is_going_to_gasprice(self, event):
        text = event.message.text
        return text.lower() == "gas"
	#16
    def is_going_to_upsetstatesolve2(self, event):
        text = event.message.text
        return text.lower() == "poor"
	#17
    def is_going_to_upset(self, event):
        text = event.message.text
        return text.lower() == "y"
	#Back To initial 2
    def reset(self, event):
        text = event.message.text
        return text.lower() == "reset"
#---------------------------------------------------------------------------------------
    #def on_enter_state1(self, event):
    #    print("I'm entering state1")

    #    reply_token = event.reply_token
    #    send_text_message(reply_token, "Trigger state1")
    #    self.go_back()

    #def on_exit_state1(self):
    #    print("Leaving state1")

	#1
    def on_enter_showfunction(self, event):
        print("I'm entering Show_function")
        reply_token = event.reply_token
        send_text_message(reply_token, "PLS type: \n <movie> for movie information \n <help> for asking help\n <news> for getting news")
        self.go_back()

    def on_exit_showfunction(self):
        print("Leaving Show_function")

    #2 #8
    def on_enter_moviestateask(self, event):
        print("I'm entering moviestateask")
        reply_token = event.reply_token
        send_text_message(reply_token, "PLS type: \n <information> for movie information \n <free movie> for free download resource\n <back> to back to initial state.")
        
        
    #3  
    def on_enter_atmovies(self, event):
        print("I'm entering Atmovies")
        reply_token = event.reply_token
        content = movie()
        print(content)
        send_text_message(reply_token, content + "State back to initial.\nPls type <hi> to learn more instructions.")
        #send_text_message(reply_token, "State back to initial.\nPls type <hi> to learn more instructions.")
        self.go_back()
 

    #4
    def on_enter_envy(self, event):
        print("I'm entering Envy")
        reply_token = event.reply_token
        content = eyny_movie()
        print(content)
        send_text_message(reply_token, content + "State back to initial.\nPls type <hi> to learn more instructions.")
        #send_text_message(reply_token, "State back to initial.\nPls type <hi> to learn more instructions.")
        self.go_back()
		
		
    #6
    def on_enter_upsetstateask(self, event):
        print("I'm entering upsetstateask")
        reply_token = event.reply_token
        send_text_message(reply_token, "PLS type: \n <girlfriend> if your girlfriend is upset.\n <poor> if you're really poor. \n <back> to back to initial state.")
    
	
	#7
    def on_enter_upsetstatesolve(self, event):
        print("I'm entering upsetstateask")
        reply_token = event.reply_token
        send_text_message(reply_token, "You can make her happy by : \n <movie> watching movie\n <gift> buy her gift \n <no> if you don't have a girlfriend, since you're loser.")
    
	
	#9
    def on_enter_present(self, event):
        print("I'm entering upsetstateask")
        reply_token = event.reply_token
        send_text_message(reply_token,"https://shopping.pchome.com.tw/ \n Pchome24hr到貨，效率高，是您解決問題的最快道路。" + "\n State back to initial.\nPls type <hi> to learn more instructions.")
        self.go_back()

    
	#11
    def on_enter_newsstateask(self, event):
        print("I'm entering newsstateask")
        reply_token = event.reply_token
        send_text_message(reply_token, "PLS type: \n <tech> for technology news \n <gas> for gas price")
        
        
	#12
    def on_enter_technewsstateask(self, event):
        print("I'm entering technewsstateask")
        reply_token = event.reply_token
        send_text_message(reply_token, "PLS type: \n <1> for source 1 \n <2> for source 2")


	#13
    def on_enter_technews(self, event):
        print("I'm entering technews")
        reply_token = event.reply_token
        content = technews()
        print(content)
        send_text_message(reply_token, content + "State back to initial.\nPls type <hi> to learn more instructions.")
        self.go_back()        
 

	#14
    def on_enter_panx(self, event):
        print("I'm entering panx")
        reply_token = event.reply_token
        content = panx()
        print(content)
        send_text_message(reply_token, content + "State back to initial.\nPls type <hi> to learn more instructions.")
        self.go_back()   

		
	#15
    def on_enter_gasprice(self, event):
        print("I'm entering gasprice")
        reply_token = event.reply_token
        content = gas_price()
        print(content)
        send_text_message(reply_token, content + "State back to initial.\nPls type <hi> to learn more instructions.")
        self.go_back()


	#16
    def on_enter_upsetstatesolve2(self, event):
        print("I'm entering upsetstateask2")
        reply_token = event.reply_token
        send_text_message(reply_token, "You may feel worse after you see this.\n If you do feel worse, I'll be happy to see that. \n If you're ready type <y>")
 

        
        

def pattern_mega(text):
    Free_site = ['mega', 'mg', 'mu', 'ＭＥＧＡ', 'ＭＥ', 'ＭＵ', 'ｍｅ', 'ｍｕ', 'ｍｅｇａ', 'GD', 'MG', 'google',]
	
    for pattern in Free_site:
        if re.search(pattern, text, re.IGNORECASE):
            return True

def eyny_movie():
    target_url = 'http://www.eyny.com/forum-205-1.html'
    print('Start parsing eynyMovie....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
	
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ''
    for titleURL in soup.select('.bm_c tbody .xst'):
        if pattern_mega(titleURL.text):
            title = titleURL.text
            if '11379780-1-3' in titleURL['href']:
                continue
            link = 'http://www.eyny.com/' + titleURL['href']
            data = '{}\n{}\n\n'.format(title, link)
            content += data
    return content

def movie():
    target_url = 'http://www.atmovies.com.tw/movie/next/0/'
    print('Start parsing movie ...')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
	
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ""
    print("entering For")
    for index, data in enumerate(soup.select('ul.filmListAll a')):
        if index == 16:
            return content
        if index%2 == 0:
            continue
        title = data.text.replace('\t', '').replace('\r', '')
        link = "http://www.atmovies.com.tw" + data['href']
        content += '{}\n{}\n'.format(title, link)
    print("endng For")
    return content

def technews():
    target_url = 'https://technews.tw/'
    print('Start parsing movie ...')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
	
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ""
    print("entering For")
    for index, data in enumerate(soup.select('article div h1.entry-title a')):
        if index == 10:
            return content
        title = data.text
        link = data['href']
        content += '{}\n{}\n\n'.format(title, link)
    print("endng For")
    return content
	
def panx():
    target_url = 'https://panx.asia/'
    print('Start parsing ptt hot....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
	
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ""
    for data in soup.select('div.container div.row div.desc_wrap h2 a'):
        title = data.text
        link = data['href']
        content += '{}\n{}\n\n'.format(title, link)
    return content

def gas_price():
    target_url = 'https://gas.goodlife.tw/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
	
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.select('#main')[0].text.replace('\n', '').split('(')[0]
    gas_price = soup.select('#gas-price')[0].text.replace('\n\n\n', '').replace(' ', '')
    cpc = soup.select('#cpc')[0].text.replace(' ', '')
    content = '{}\n{}{}'.format(title, gas_price, cpc)
    return content