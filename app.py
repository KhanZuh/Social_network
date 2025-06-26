from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.user_repository import UserRepository
from lib.post_repository import PostRepository
from lib.user import User
from lib.post import Post



# Connect to the database
connection = DatabaseConnection()
connection.connect()

# For music_library project
# # Seed with some seed data
# connection.seed("seeds/music_library.sql")

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:
#     print(artist)

# For social_network project
connection.seed("seeds/social_network.sql")

# create repos for social_network project
user_repository = UserRepository(connection)
post_repository = PostRepository(connection)

print("=== Social Network Demo ===\n")


# USER STORY 1 & 2: Show that users have email addresses and usernames
print("📱 USER ACCOUNTS:")
print("Showing that users can have email addresses and usernames...\n")

# Get all users from database 
users = user_repository.all()
for user in users:
   # Show each user's details 
   print(f"User: {user.username}")
   print(f"Email: {user.email_address}")
   print(f"ID: {user.id}")
   print("---")

# USER STORY 3 & 4: Show posts are connected to users and have title + content
print("\n📝 POSTS WITH TITLES AND CONTENT:")
print("Showing posts that belong to users, with titles and content...\n")

# Get all posts 
posts = post_repository.all()
for post in posts:
   # Find which user wrote this post 
   post_author = user_repository.find(post.user_id)
   
   print(f"Post by: {post_author.username}")
   print(f"Title: {post.title}")
   print(f"Content: {post.content}")
   print(f"Views: {post.views}")
   print("---")

# USER STORY 5: Show that posts track how many people viewed them
print("\n👀 POST VIEW TRACKING:")
print("Demonstrating that posts count how many times they're viewed...\n")

# Picking the first post to demonstrate with 
demo_post_id = 1

# See how many views it has now 
post_before = post_repository.find(demo_post_id)
print(f"Post '{post_before.title}' currently has {post_before.views} views")

# Simulate someone viewing the post
print("Someone is viewing this post...")
post_repository.increment_views(demo_post_id)

# Check the view count again (see if our counter went up)
post_after = post_repository.find(demo_post_id)
print(f"Post '{post_after.title}' now has {post_after.views} views")
print(f"Views increased by: {post_after.views - post_before.views}")

# Ssimulate a few more people viewing it
print("\nSimulating 3 more people viewing the post...")
for i in range(3):
   post_repository.increment_views(demo_post_id)
   # Get updated post to show the view count climbing
   updated_post = post_repository.find(demo_post_id)
   print(f"  View #{i+2}: Post now has {updated_post.views} views")

print(f"\n🎉 Final view count: {post_repository.find(demo_post_id).views} views")

print("\n=== Demo Complete ===")
print("All user stories demonstrated successfully!")


