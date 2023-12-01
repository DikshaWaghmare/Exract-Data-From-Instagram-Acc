import instaloader


L = instaloader.Instaloader()
# Login (type 'your_username' and 'your_password' with your credentials)
username = 'dikshaw44'
password = 'dikshaw44@'
L.context.login(username, password)


def get_profile_details(username):
    
    try:
        profile = instaloader.Profile.from_username(L.context, username)

        # Extract information
        followers = profile.followers
        posts = profile.mediacount
        following_count=profile.followees

        total_likes = 0
        total_comments = 0

        # Iterate through the posts to calculate total likes and comments
        for post in profile.get_posts():
            total_likes += post.likes
            total_comments += post.comments

        return {
            'Followers': followers,
            'Number of Posts': posts,
            'Total Likes': total_likes,
            'Total Comments': total_comments,
            'Following': following_count
        }

    except instaloader.exceptions.ProfileNotExistsException:
        return {'error': 'Profile does not exist.'}
    except Exception as e:
        return {'error': f'Something went wrong: {str(e)}'}

# Replace 'username' with the desired Instagram profile username
profile_username = 'smriti_mandhana'

# Get profile details including followers, posts, total likes, total comments, and following count
profile_details = get_profile_details(profile_username)
print("Username:", profile_username)
print(profile_details)

if 'error' not in profile_details:
    followers = profile_details['Followers']
    total_likes = profile_details['Total Likes']
    total_comments = profile_details['Total Comments']
    
    engagement_rate = ((total_likes + total_comments) / followers) * 100
    print(f"Engagement Rate: {engagement_rate:.2f}%")
elif profile_details.get('error') == 'Profile does not exist.':
    print(f"Profile '{profile_username}' does not exist.")
else:
    print(f"Error: {profile_details['error']}")
