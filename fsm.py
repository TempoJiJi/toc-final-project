from transitions.extensions import GraphMachine
import requests, json

class TocMachine(GraphMachine):
    currentState = 'user'
    first_visit = 0
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
    
    ##### Taiwan #####
    def is_going_to_taiwan(self, update):
        self.first_visit = 1
        text = update.message.text
        print('taiwan_function')
        return text.lower() == 'taiwan'

    # Taiwan trending #
    def is_going_to_taiwan_trending(self, update):
        text = update.message.text
        print('taiwan_trending_function: ')
        return text.lower() == 'trending'

    # Taiwan travel #
    def is_going_to_taiwan_travel(self, update):
        text = update.message.text
        print('taiwan_travel_function: ')
        return text.lower() == 'travel'

    # Taiwan news #
    def is_going_to_taiwan_news(self, update):
        text = update.message.text
        print('taiwan_news_function: ')
        return text.lower() == 'news'

    # Taiwan music #
    def is_going_to_taiwan_music(self, update):
        text = update.message.text
        print('taiwan_music_function: ')
        return text.lower() == 'music'

    # Taiwan entry #
    def on_enter_taiwan(self,update):
        update.message.reply_text("Please Choose a Channel:\ntrending\ntravel\nnews\nmusic\n")
        self.currentState = 'taiwan'
    
    def on_enter_taiwan_trending(self, update):
        update.message.reply_text("Here is the Top5 trending video on Youtube!")
        API_KEY = 'AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        region_code = 'TW'
        url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode='+region_code+'&maxResults=5&key=AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        youtube_url = "https://www.youtube.com/watch?v="
        r = requests.get(url.format(0, api_key=API_KEY))
        js = r.json()
        items = js["items"]
        for i in range(0,5):
            update.message.reply_text(youtube_url + items[i]["id"])
        self.finish(update)

    def on_enter_taiwan_travel(self, update):
        update.message.reply_text("Here is some travel video on Youtube!")
        API_KEY = 'AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        playlistID = 'PLi0ZZWlxtL4E_WBnbN2CbCPHMe_-ts9uO'
        url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='+playlistID+'&key=AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        youtube_url = "https://www.youtube.com/watch?v="
        r = requests.get(url.format(0, api_key=API_KEY))
        js = r.json()
        items = js["items"]
        for i in range(0,5):
            update.message.reply_text(youtube_url + items[i]["snippet"]["resourceId"]["videoId"])
        self.finish(update)

    def on_enter_taiwan_news(self, update):
        update.message.reply_text("Here is some travel video on Youtube!")
        API_KEY = 'AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        playlistID = 'PL084028CD47991AA6'
        url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='+playlistID+'&key=AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        youtube_url = "https://www.youtube.com/watch?v="
        r = requests.get(url.format(0, api_key=API_KEY))
        js = r.json()
        items = js["items"]
        for i in range(0,5):
            update.message.reply_text(youtube_url + items[i]["snippet"]["resourceId"]["videoId"])
        self.finish(update)

    def on_enter_taiwan_music(self, update):
        update.message.reply_text("Here is some music video on Youtube!")
        API_KEY = 'AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        playlistID = 'PLsyOSbh5bs16vubvKePAQ1x3PhKavfBIl'
        url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='+playlistID+'&key=AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        youtube_url = "https://www.youtube.com/watch?v="
        r = requests.get(url.format(0, api_key=API_KEY))
        js = r.json()
        items = js["items"]
        for i in range(0,5):
            update.message.reply_text(youtube_url + items[i]["snippet"]["resourceId"]["videoId"])
        self.finish(update)

    ##########################################################
    ##########################################################

    ##### America #####
    def is_going_to_america(self, update):
        self.first_visit = 1
        text = update.message.text
        print('america_function')
        return text.lower() == 'america'

    # america trending #
    def is_going_to_america_trending(self, update):
        text = update.message.text
        print('america_trending_function: ')
        return text.lower() == 'trending'

    # america travel #
    def is_going_to_america_travel(self, update):
        text = update.message.text
        print('america_travel_function: ')
        return text.lower() == 'travel'

    # america news #
    def is_going_to_america_news(self, update):
        text = update.message.text
        print('america_news_function: ')
        return text.lower() == 'news'

    # america music #
    def is_going_to_america_music(self, update):
        text = update.message.text
        print('america_music_function: ')
        return text.lower() == 'music'

    # america entry #
    def on_enter_america(self,update):
        update.message.reply_text("Please Choose a Channel:\ntrending\ntravel\nnews\nmusic\n")
        self.currentState = 'america'
    
    def on_enter_america_trending(self, update):
        update.message.reply_text("Here is the Top5 trending video on Youtube!")
        API_KEY = 'AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        region_code = 'US'
        url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode='+region_code+'&maxResults=5&key=AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        youtube_url = "https://www.youtube.com/watch?v="
        r = requests.get(url.format(0, api_key=API_KEY))
        js = r.json()
        items = js["items"]
        for i in range(0,5):
            update.message.reply_text(youtube_url + items[i]["id"])
        self.finish(update)

    def on_enter_america_travel(self, update):
        update.message.reply_text("Here is some travel video on Youtube!")
        API_KEY = 'AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        playlistID = 'PLdgCSoJzrmKHhvEWqmb3-1tUQmT8ZWBrv'
        url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='+playlistID+'&key=AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        youtube_url = "https://www.youtube.com/watch?v="
        r = requests.get(url.format(0, api_key=API_KEY))
        js = r.json()
        items = js["items"]
        for i in range(0,5):
            update.message.reply_text(youtube_url + items[i]["snippet"]["resourceId"]["videoId"])
        self.finish(update)

    def on_enter_america_news(self, update):
        update.message.reply_text("Here is some travel video on Youtube!")
        API_KEY = 'AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        playlistID = 'PLCUKIeZnrIUl1eYW3l1CzveYr4hP5E5kY'
        url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='+playlistID+'&key=AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        youtube_url = "https://www.youtube.com/watch?v="
        r = requests.get(url.format(0, api_key=API_KEY))
        js = r.json()
        items = js["items"]
        for i in range(0,5):
            update.message.reply_text(youtube_url + items[i]["snippet"]["resourceId"]["videoId"])
        self.finish(update)

    def on_enter_america_music(self, update):
        update.message.reply_text("Here is some music video on Youtube!")
        API_KEY = 'AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        playlistID = 'PLw-VjHDlEOgtCjYJB1r1EkZ-AKlYv6Ozj'
        url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='+playlistID+'&key=AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        youtube_url = "https://www.youtube.com/watch?v="
        r = requests.get(url.format(0, api_key=API_KEY))
        js = r.json()
        items = js["items"]
        for i in range(0,5):
            update.message.reply_text(youtube_url + items[i]["snippet"]["resourceId"]["videoId"])
        self.finish(update)

    ##########################################################
    ##########################################################

    ##### hongkong ######
    def is_going_to_hongkong(self, update):
        self.first_visit = 1
        text = update.message.text
        print('hongkong_function')
        return text.lower() == 'hongkong'

    # hongkong trending #
    def is_going_to_hongkong_trending(self, update):
        text = update.message.text
        print('hongkong_trending_function: ')
        return text.lower() == 'trending'

    # hongkong travel #
    def is_going_to_hongkong_travel(self, update):
        text = update.message.text
        print('hongkong_travel_function: ')
        return text.lower() == 'travel'

    # hongkong news #
    def is_going_to_hongkong_news(self, update):
        text = update.message.text
        print('hongkong_news_function: ')
        return text.lower() == 'news'

    # hongkong music #
    def is_going_to_hongkong_music(self, update):
        text = update.message.text
        print('hongkong_music_function: ')
        return text.lower() == 'music'

    # hongkong entry #
    def on_enter_hongkong(self,update):
        update.message.reply_text("Please Choose a Channel:\ntrending\ntravel\nnews\nmusic\n")
        self.currentState = 'hongkong'
    
    def on_enter_hongkong_trending(self, update):
        update.message.reply_text("Here is the Top5 trending video on Youtube!")
        API_KEY = 'AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        region_code = 'HK'
        url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode='+region_code+'&maxResults=5&key=AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        youtube_url = "https://www.youtube.com/watch?v="
        r = requests.get(url.format(0, api_key=API_KEY))
        js = r.json()
        items = js["items"]
        for i in range(0,5):
            update.message.reply_text(youtube_url + items[i]["id"])
        self.finish(update)

    def on_enter_hongkong_travel(self, update):
        update.message.reply_text("Here is some travel video on Youtube!")
        API_KEY = 'AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        playlistID = 'PLbwie-OwF9TbaX8xwPo8KB3NNyilRWvbU'
        url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='+playlistID+'&key=AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        youtube_url = "https://www.youtube.com/watch?v="
        r = requests.get(url.format(0, api_key=API_KEY))
        js = r.json()
        items = js["items"]
        for i in range(0,5):
            update.message.reply_text(youtube_url + items[i]["snippet"]["resourceId"]["videoId"])
        self.finish(update)

    def on_enter_hongkong_news(self, update):
        update.message.reply_text("Here is some travel video on Youtube!")
        API_KEY = 'AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        playlistID = 'PLuwJy35eAVaJS6yf7ne6m61lR5_-N1nrR'
        url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='+playlistID+'&key=AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        youtube_url = "https://www.youtube.com/watch?v="
        r = requests.get(url.format(0, api_key=API_KEY))
        js = r.json()
        items = js["items"]
        for i in range(0,5):
            update.message.reply_text(youtube_url + items[i]["snippet"]["resourceId"]["videoId"])
        self.finish(update)

    def on_enter_hongkong_music(self, update):
        update.message.reply_text("Here is some music video on Youtube!")
        API_KEY = 'AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        playlistID = 'PLsyOSbh5bs14TTmPFbNwXclmCR2-T0db7'
        url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='+playlistID+'&key=AIzaSyAPUnLBaQbsS6vJxWOCP-xJvTwbPwTqxmo'
        youtube_url = "https://www.youtube.com/watch?v="
        r = requests.get(url.format(0, api_key=API_KEY))
        js = r.json()
        items = js["items"]
        for i in range(0,5):
            update.message.reply_text(youtube_url + items[i]["snippet"]["resourceId"]["videoId"])
        self.finish(update)

    ##########################################################

    # Finish State #
    def on_enter_finish_state(self, update):
        self.currentState = 'user'
        self.first_visit = 0
        self.go_back(update)
