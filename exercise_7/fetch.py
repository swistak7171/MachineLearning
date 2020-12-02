import json
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = json.loads(response.text)
print(posts)

users_posts = {}
for post in posts:
    user_id = post['userId']
    if user_id in users_posts:
        users_posts[user_id] = users_posts[user_id] + 1
    else:
        users_posts[user_id] = 0

sorted_users_posts = sorted(
    users_posts.items(),
    key=lambda x: x[1],
    reverse=True
)

max_posts = sorted_users_posts[0][1]

users = []
for user_id, number_of_posts in sorted_users_posts:
    if number_of_posts == max_posts:
        users.append(str(user_id))

max_users = " & ".join(users)
print(max_users)

s = "s" if len(users) > 1 else ""
print(f"user{s} {max_users} wrote {max_posts} posts")


def keep(post):
    return str(post['userId'] in users)


with open('filtered_data_file.json', 'w') as writer:
    filtered_posts = list(filter(keep, posts))
    json.dump(filtered_posts, writer, indent=2)
