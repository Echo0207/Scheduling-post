import requests
import facebook

# 填入您的存取權杖
access_token = 'EABXB0gWIGF0BAEOnFo6ptymfqH448ZB3l5MU7hLA70eGXZC7DNdDI2r1t7MEdd4hHATNl0T91briV8Y6Yg5kh8qV9JTjK4d4dx4lbjZBeEy5YADm9hvjmm7vVm9hY2nxZB9ZBiYTbZCPnU6g0O1luHQx4T0ZBJ3QZCm4wUXPwvwFuXK1ZB1uXM72MhmWvuqR68soZD'

# 填入您的粉絲專頁ID
page_ids = ['376382859623485', '104343679256567', '103824709308769']

# 要發布的貼文內容
post_message = '''第一眼看到她就覺得她很適合
#歐美手刷染 #巴黎畫染
像去服飾店看到一件衣服
決定就是它了的感覺
髮型就是挖掘顧客本身的氣質

喜歡特別髮色的妳們可以來找我喲💕

線上預約連結
https://lin.ee/Kr6ZrtF
門店選擇❤️桃園民生店
設計師選擇❤️Elaine

請你一定要來到TiAM
Tiam Hair Salon 中壢延平店 👉🏻延平路456號
Tiam Hair Salon 中壢中平店👉🏻中平路155號
Tiam Hair Salon桃園民生店👉🏻 桃園區民生路57號2樓（7-11樓上）

#CP值最高髮廊
#中壢TiAM
#桃園TiAM'''
file_path = '/Users/echo/PycharmProjects/pythonProject/Elaine.mov'

for page_id in page_ids:
    # 上傳影片至Facebook
    video_endpoint = f'https://graph-video.facebook.com/{page_id}/videos'
    video_params = {
        'access_token': access_token,
    }
    video_files = {
        'source': open('/Users/echo/PycharmProjects/pythonProject/Elaine.mov', 'rb')
    }
    video_response = requests.post(video_endpoint, params=video_params, files=video_files)
    video_data = video_response.json()

    # 取得上傳影片的ID
    video_id = video_data['id']

    # 發布貼文
    post_endpoint = f'https://graph.facebook.com/{page_id}/feed'
    post_params = {
        'access_token': access_token,
        'message': post_message,
        'link': f'https://www.facebook.com/video.php?v={video_id}'
    }
    post_response = requests.post(post_endpoint, params=post_params)
    print(f"Posted on page {page_id}: {post_response.json()}")

    import json

    print(json.dumps(video_data, indent=4))
