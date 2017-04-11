# -*- coding: utf-8 -*-
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['http://www.zhihu.com/']
    # 获取关注列表
    follows_urls = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    # 选取的第一个用户
    start_user = 'excited-vczh'
    # 获取关注者信息
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    # 获取用户信息界面
    user_url = 'https://www.zhihu.com/api/v4/members/{include}?include={include}'
    # 获取用户相关信息
    user_query = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,avatar_hue,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'

    def start_requests(self):
        yield scrapy.Request(self.user_url.format(user=self.start_user, include=self.user_query, callback=self.parse_user))
        url = self.follows_urls.format(user=self.start_user, include=self.follows_query, offset=0, limit=20)
        yield scrapy.Request(url, callback=self.parse_follows)

    def parse_user(self, response):
        result = json.loads(response.text)
        item = UserItem()
        
    def parse_follows(self, response):
        print(response.text)
